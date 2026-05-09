---
tags: [synology, terminal, debug, cloudsync, hibernation]
sources: [terminal 2.md]
created: 2026-05-09
updated: 2026-05-09
---

# Terminal 2

**Source:** terminal 2.md
**Date ingested:** 2026-05-09
**Type:** log

## Summary

Лог терминала диагностики гибернации на NAS [[synology-ds212j|Synology DS212j]]. Администратор отключает журналирование SMB-сессий, управляет процессом отладки `syno_hibernation_debug` и анализирует `/proc/diskstats`. Также системный лог `/var/log/messages` выявляет критические ошибки работы приложения [[cloudsync|CloudSync]] с недействительными токенами авторизации для [[dropbox|Dropbox]] и [[onedrive|OneDrive]], что вызывает постоянную дисковую активность и в итоге приводит к остановке и удалению проблемного пакета.

## Key Claims

- Отключение `smbxferlog` немного снижает дисковую активность.
- Ошибки `invalid_request` и `invalid_grant` для `refresh_token` облачных сервисов (Dropbox, OneDrive) приводят к постоянным сбоям службы `CloudSync`, что создает лишнюю нагрузку на диски и не позволяет системе уснуть.
- Удаление/остановка сбойных пакетов (таких как `SynoFinder` и `CloudSync`) — один из шагов диагностики проблем со сном ([[hibernation|Hibernation]]).

## Entities Mentioned

- [[cloudsync|CloudSync]] — Приложение Synology для синхронизации с облаком.
- [[dropbox|Dropbox]] — Облачное хранилище данных.
- [[onedrive|OneDrive]] — Облачное хранилище Microsoft.
- [[synofinder|SynoFinder]] — Средство поиска на NAS.

## Concepts Covered

- [[hibernation|Hibernation]] — Спящий режим дисков.
- [[disk-io|Disk I/O]] — Дисковые операции ввода/вывода.
