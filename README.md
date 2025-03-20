# CnGal Calendar

[![Build][build]][build-ci] [![Test][test]][test-ci]

## 介绍

这是一个创建 [CnGal][cngal] 游戏发售日历的小工具，由 GitHub Actions 定期更新。你可以[点击这里][release]获取订阅地址，并在任意支持 iCalendar 的日历应用中订阅。

## 目的

CnGal 没有提供最近发售游戏的 RSS，这是个人使用的替代方案（虽然协议从 RSS 修改为 ICS），同时当作博客文章 [iCalendar (ICS) 的养成方式][ics] 的拓展。

## 待办

- [x] 优化发售日处理，添加估算提示
- [ ] 通过 `/api/entries/GetPublishGamesTimeline` 或 `/api/entries/GetPublishGamesByTime` 生成已发售游戏日历（数据结构不一样，需要重构部分代码）
- [ ] 通过 `/api/entries/GetRoleBirthdaysByTime` 生成[角色生日日历][birthday]

## 致谢

- 项目受 [SteamWishlistCalendar][swc] 启发，强烈建议用 SWC 替代 Steam 邮件通知
- 感谢 CnGal 官方提供的 API 文档，以及全体贡献者和编辑者

[build]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/gen.yml/badge.svg
[build-ci]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/gen.yml
[test]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/test.yml/badge.svg
[test-ci]: https://github.com/Vinfall/CnGalCalendar/actions/workflows/test.yml
[cngal]: https://www.cngal.org
[release]: https://github.com/Vinfall/CnGalCalendar/releases/download/continuous/cngal-calendar.ics
[ics]: https://blog.vinfall.com/posts/2023/12/ics/
[swc]: https://github.com/icue/SteamWishlistCalendar
[birthday]: https://www.cngal.org/birthday
