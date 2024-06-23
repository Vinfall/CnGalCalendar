#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Documentation
# CnGal: https://api.cngal.org/swagger/index.html
# ICS: https://icspy.readthedocs.io/en/stable/api.html#event
# Dateparser: https://dateparser.readthedocs.io/en/latest/settings.html#handling-incomplete-dates

import os
import sys
import dateparser
from datetime import datetime
from datetime import timedelta
import requests
import json
import csv
import re
from ics import Calendar, Event

# Output files
_OUTPUT_FOLDER = "output/"
_CSV_FILE = "cngal-release.txt"
_JSON_FILE = "cngal-release.json"
_ICS_FILE = "cngal-calendar.ics"

# Date format
# Mid year
_MID_YEAR = "-09-15"
_YEAR_ONLY_REGEX = "^(\\d{4})$"
_YYYYMM_ONLY_REGEX = "^(\\d{4}-\\d{2})$"

_TO_REPLACE = (
    # Regular time string
    # Time span first
    ("q1-q2", "4月"),
    ("q2-q3", "7月"),
    ("q3-q4", "10月"),
    # Keyword second
    ("spring|春(季|节)?", "3月"),
    ("summer|夏(季)?", "6月"),
    ("fall|秋(季)?", "9月"),
    ("winter|冬(季)?", "12月"),
    ("q1(季度)?", "2月"),
    ("q2(季度)?", "5月"),
    ("q3(季度)?", "8月"),
    ("q4(季度)?", "11月"),
    # Alias third
    ("第一季度", "2月"),
    ("第二季度", "5月"),
    ("第三季度", "8月"),
    ("第四季度", "11月"),
    ("年初", "年1月"),
    ("年[底内]", "年12月"),
    ("上旬", "10日"),
    ("中旬", "20日"),
    ("下旬", "28日"),
    ("月[底内]", "月"),
    # Annotation last
    ("号", "日"),
    # ("年", "."),
    # ("月", "."),
    # ("日", "."),
    # Block word list
    ("^预[计定期]", ""),
    ("发[售布].*?$", ""),
    ("[Ww]ishlist.*?$", ""),
    ("TB[AD]|tb[ad]", ""),
    (" ", ""),
)
# Convert time string like `2024年8月` to partial/full YYYY-MM-DD
_TO_REPLACE_ISO = (
    (r"(\d+)年(\d{1,2})月(\d{1,2})日", r"\1-\2-\3"),  # 年月日
    (r"(\d+)年(\d{1,2})月", r"\1-\2"),  # 年月
    (r"(\d+)年", r"\1"),  # 年
)

# Exclude outdated ID, not meant to be misused as personal blocklist
_INDEX_FILTER = [2962]

# Cli testing one-liner:
# curl -X 'GET' 'https://api.cngal.org/api/home/ListUpcomingGames'  -H 'accept: application/json'


def get_list():
    api_url = "https://api.cngal.org"
    api_upcoming = "/api/home/ListUpcomingGames"
    headers = {"Content-Type": "application/json"}
    url = api_url + api_upcoming

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Post request successful")
        return response.json()
    else:
        print("Post request failed")
        print(response)
        sys.exit()


# Process & Write results to JSON & CSV
def process_json(results):
    base_url = "https://www.cngal.org/"
    processed_results = []
    for result in results:
        # Extract index from url
        url = base_url + result["url"]
        index = re.search(r"index/(\d+)", url).group(1)

        # Skip deprecated index
        if int(index) in _INDEX_FILTER:
            continue

        # Build new json
        processed_result = {
            "url": url,
            "index": index,
            "title": result["name"],
            "released": result["publishTime"],
            "raw_date": result["publishTime"],
            "intro": result["briefIntroduction"],
        }
        # Make ambiguous release date like `预计2024年发售` and `2022年底` machine-readable
        for pair in _TO_REPLACE:
            processed_result["released"] = re.sub(
                pair[0], pair[1], processed_result["released"].lower()
            )
        for pair in _TO_REPLACE_ISO:
            processed_result["released"] = re.sub(
                pair[0], pair[1], processed_result["released"]
            )
        # Format date string to ISO date
        if processed_result["released"] != "":
            date_parts = processed_result["released"].split("-")
            if len(date_parts) == 2:
                processed_result["released"] = f"{date_parts[0]}-{date_parts[1]:0>2}"
            elif len(date_parts) == 3:
                processed_result["released"] = (
                    f"{date_parts[0]}-{date_parts[1]:0>2}-{date_parts[2]:0>2}"
                )
        else:
            break

        # Ignore release without valid date
        if processed_result["released"]:
            processed_results.append(processed_result)

    # Save raw results to JSON file
    with open(
        f"{_OUTPUT_FOLDER + _JSON_FILE}",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(processed_results, file, ensure_ascii=False, indent=2)

    # Save compact results to CSV file
    with open(
        _OUTPUT_FOLDER + _CSV_FILE, mode="w", newline="", encoding="utf-8"
    ) as csv_file:
        fields_to_save = ["index", "title", "raw_date"]
        # Use semi-column seperator to avoid mismatches
        writer = csv.DictWriter(csv_file, fieldnames=fields_to_save, delimiter=";")

        writer.writeheader()
        for result in processed_results:
            # Compact fields
            selected_data = {field: result[field] for field in fields_to_save}
            writer.writerow(selected_data)

    return processed_results


# Function borrowed from SteamWishlistCalendar
# https://github.com/icue/SteamWishlistCalendar/blob/b5995dd44e8a0e682e80962277bc905eed744768/swc.py#L33-L51
def last_day_of_next_month(dt):
    """
    Returns the datetime of the last day of the next month.

    Args:
    dt: A datetime.datetime object.

    Returns:
    A datetime.datetime object.
    """

    year = dt.year
    next_next_month = dt.month + 2
    if next_next_month > 12:
        next_next_month -= 12
        year = dt.year + 1

    # Subtracting 1 day from the first day of the next next month, to get the last day of next month.
    return datetime(year, next_next_month, 1) - timedelta(days=1)


# Make calendar
def make_calendar(processed_results):
    cal = Calendar(creator="CnGalCalendar")
    now = datetime.now()

    for result in processed_results:
        description_suffix = ""
        description = result["url"] + "\n" + result["intro"]
        index = result["index"]
        title = result["title"]
        release_date = result["released"]

        # Parse date to better fit into reality
        # Match release date like `2026`
        year_only_match = re.match(_YEAR_ONLY_REGEX, release_date)
        if year_only_match:
            year = year_only_match.group(1)
            # If Sep 15 of this year passed, use the end of year
            mid_release_date = datetime.strptime(year + _MID_YEAR, "%Y-%m-%d").date()
            release_date = year + (
                _MID_YEAR if mid_release_date > now.date() else "-12-31"
            )
            description_suffix = f'\n发售日估算自 "{result["raw_date"]}"'
        # Complete remaining release date like `2024-03`
        yyyymm_only_match = re.match(_YYYYMM_ONLY_REGEX, release_date)
        if yyyymm_only_match:
            release_date = dateparser.parse(
                release_date,
                settings={
                    # Set time zone to UTC+8
                    "TIMEZONE": "Asia/Shanghai",
                    "PREFER_DAY_OF_MONTH": "last",
                    "PREFER_DATES_FROM": "future",
                },
            )
            while release_date.date() < now.date():
                # If the estimated release date has already passed, pick the earliest upcoming last-of-a-month date
                release_date = last_day_of_next_month(release_date)
                # Only show estimation message in above cases
                description_suffix = f'\n发售日估算自 "{result["raw_date"]}"'

        # Ensure release_date is a datetime object
        if isinstance(release_date, str):
            release_date = datetime.strptime(release_date, "%Y-%m-%d")

        # TODO: include more info
        event = Event(
            uid=index,
            summary=title,
            description=description + description_suffix,
            begin=release_date,
            last_modified=now,
            dtstamp=now,
            categories=["cngal"],
        )
        event.make_all_day()
        cal.events.append(event)

    with open(_OUTPUT_FOLDER + _ICS_FILE, "w", encoding="utf-8") as f:
        f.write(cal.serialize())


os.makedirs(_OUTPUT_FOLDER, exist_ok=True)
j = get_list()
results = process_json(j)
make_calendar(results)
