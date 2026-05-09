---
tags: [synology, config, dsm]
sources: [cat etc synoinfo.conf.md]
created: 2026-05-09
updated: 2026-05-09
---

# Synoinfo Conf

**Source:** cat etc synoinfo.conf.md
**Date ingested:** 2026-05-09
**Type:** log / config

## Summary

Дамп конфигурационного файла `/etc/synoinfo.conf` сетевого хранилища [[synology-ds212j|Synology DS212j]]. Документ служит центральным узлом для определения системных параметров и доступных функций устройства. 

## Key Claims

- Файл содержит технические ограничения устройства (максимальное количество учетных записей, дисков, общих папок).
- В файле зафиксированы региональные настройки (часовой пояс, язык).
- Описывает состояние системных служб (NFS, SSH, FTP и другие).
- Содержит параметры энергосбережения и планировщика задач.

## Entities Mentioned

- [[synoinfo-conf|synoinfo.conf]] — Главный конфигурационный файл DSM.
- [[synology-ds212j|Synology DS212j]] — Устройство, конфигурация которого приведена.

## Concepts Covered

- [[dsm|DSM]] — Операционная система, использующая данный конфиг.
- [[nas|NAS]] — Тип устройства.
