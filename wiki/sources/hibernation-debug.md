---
tags: [synology, nas, debug, hibernation]
sources: [Управление hibernation debug.md]
created: 2026-05-09
updated: 2026-05-09
---

# Hibernation Debug

**Source:** Управление hibernation debug.md
**Date ingested:** 2026-05-09
**Type:** manual

## Summary

Техническое руководство по диагностике спящего режима ([[hibernation|Hibernation]]) жестких дисков на NAS [[synology-ds212j|Synology DS212j]]. В документе описывается, как с помощью командной строки включать и выключать сбор логов активности, чтобы выявить процессы, не дающие устройству уснуть.

## Key Claims

- Для включения логирования необходимо изменить параметр `enable_hibernation_debug` в файле [[synoinfo-conf|synoinfo.conf]] с помощью утилиты [[synosetkeyvalue]].
- За сбор информации отвечает системный процесс `syno_hibernation_debug`.
- Логи сохраняются в директорию `/var/log/`, где `hibernation.log` содержит краткие записи с периодами бездействия (idle), а `hibernationFull.log` — детализированные операции.
- Изменения, внесенные через конфигурационный файл, переживают перезагрузку устройства, то есть процесс отладки запустится автоматически при следующем старте [[dsm|DSM]].

## Entities Mentioned

- [[synology-ds212j|Synology DS212j]] — Устройство, на котором производится отладка.
- [[synoinfo-conf|synoinfo.conf]] — Главный конфигурационный файл системы.
- [[synosetkeyvalue]] — Утилита для безопасного редактирования конфигурации.

## Concepts Covered

- [[hibernation|Hibernation]] — Режим энергосбережения для жестких дисков.
- [[dsm|DSM]] — Операционная система хранилища.
