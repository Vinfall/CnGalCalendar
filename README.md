# CnGal Calendar

[![Build][build]][build-ci] [![Test][test]][test-ci]

## 介绍

由 GitHub Action 自动更新的 [CnGal][cngal] 游戏发售日历。
你可以复制下面的订阅地址，并在任意支持 iCalendar 的日历应用中订阅。

```
https://github.com/Vinfall/CnGalCalendar/releases/download/continuous/cngal-calendar.ics
```

## 待办

- [x] 优化发售日处理，添加估算提示
- [ ] 通过 `/api/entries/GetPublishGamesTimeline` 或 `/api/entries/GetPublishGamesByTime` 生成已发售游戏日历（数据结构不一样，需要重构部分代码）
- [ ] 通过 `/api/entries/GetRoleBirthdaysByTime` 生成[角色生日日历][birthday]

## 致谢

- 项目受 [SteamWishlistCalendar][swc] (SWC) 启发，强烈建议用 SWC 替代 Steam 邮件通知
- 感谢 CnGal 官方提供的 API 文档，以及全体贡献者和编辑者

[build]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/release.yml/badge.svg
[build-ci]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/release.yml
[test]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/test.yml/badge.svg
[test-ci]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/test.yml
[cngal]: https://www.cngal.org
[swc]: https://github.com/icue/SteamWishlistCalendar
[birthday]: https://www.cngal.org/birthday
