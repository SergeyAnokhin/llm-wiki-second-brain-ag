---
tags: [hardware, storage, power-management]
sources: [Управление hibernation debug.md]
created: 2026-05-09
updated: 2026-05-09
---

# Hibernation

Hibernation (Спящий режим) — механизм энергосбережения для жестких дисков, применяемый в том числе на устройствах [[nas|NAS]] от [[synology|Synology]]. 

Если жесткие диски не переходят в спящий режим, в [[dsm|DSM]] предусмотрен механизм отладки: специальный процесс (`syno_hibernation_debug`) начинает логировать всю дисковую активность и периоды бездействия. Управление этой отладкой осуществляется через правку конфигурации в [[synoinfo-conf|synoinfo.conf]].
