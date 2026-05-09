---
tags: [proxmox, nfs, smb, backup, hibernation]
sources: [NFS solution.md]
created: 2026-05-09
updated: 2026-05-09
---

# NFS Solution

**Source:** NFS solution.md
**Date ingested:** 2026-05-09
**Type:** manual / guide

## Summary

Руководство по оптимизации сетевого взаимодействия между [[proxmox|Proxmox]] и NAS [[synology-ds212j|Synology DS212j]] для корректной работы режима гибернации ([[hibernation|Hibernation]]). Описывается переход с [[smb-cifs|SMB/CIFS]] на [[nfs|NFS]] для минимизации нагрузки на диски, так как NFS не сохраняет состояние сессии (stateless). Также приведена схема использования [[wake-on-lan|Wake-on-LAN]] для автоматического пробуждения NAS перед бэкапом.

## Key Claims

- Использование [[nfs|NFS]] предпочтительнее [[smb-cifs|SMB/CIFS]] для режима сна, так как протокол NFS не держит постоянную сессию и не пишет данные аутентификации на диск.
- Оптимальная схема резервного копирования включает скрипты `pre-backup` (для отправки WOL-пакета) и `post-backup` (для размонтирования ресурса).
- Описаны конкретные шаги настройки NFS на Synology и монтирования хранилища в Proxmox.

## Entities Mentioned

- [[proxmox|Proxmox]] — Платформа виртуализации.
- [[synology-ds212j|Synology DS212j]] — Сетевое хранилище.

## Concepts Covered

- [[hibernation|Hibernation]] — Режим сна.
- [[nfs|NFS]] — Сетевой файловый протокол, не имеющий состояния сессии.
- [[smb-cifs|SMB/CIFS]] — Сетевой файловый протокол с постоянной сессией.
- [[wake-on-lan|Wake-on-LAN]] — Технология пробуждения устройства по сети.
