---
tags: [synology, terminal, ssh, hibernation, debug]
sources: [terminal 3.md]
created: 2026-05-09
updated: 2026-05-09
---

# Terminal 3

**Source:** terminal 3.md
**Date ingested:** 2026-05-09
**Type:** log

## Summary

Лог терминала, в котором отражен процесс диагностики спящего режима на NAS [[synology-ds212j|Synology DS212j]] через SSH. Документ содержит детали SSH-подключения с подробным выводом, запуск и проверку процесса отладки `syno_hibernation_debug`, использование `/proc/diskstats` для мониторинга I/O счетчиков и процесс перезагрузки системы администратором.

## Key Claims

- Процесс диагностики включает ручной запуск процесса `syno_hibernation_debug` и последующий мониторинг его работы в фоне через `ps aux`.
- Для снятия показаний активности дисков в реальном времени используется `cat /proc/diskstats`.

## Entities Mentioned

- [[openssh|OpenSSH]] — Клиент для подключения по SSH.
- [[synology-ds212j|Synology DS212j]] — Тестируемый сервер.

## Concepts Covered

- [[ssh|SSH]] — Защищенный сетевой протокол.
- [[hibernation|Hibernation]] — Режим энергосбережения жестких дисков.
- [[disk-io|Disk I/O]] — Дисковые операции.
