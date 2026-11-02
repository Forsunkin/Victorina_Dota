# Старый прототип (2022)

Консольные эксперименты с матчами Dota 2, OpenDota и SQLite. Оставлены как архив, не используются в новой версии игры.

Для локального запуска из каталога `old/`:

```bash
pip install requests
python db/create_tables.py
python db/fill_heroes_table.py
python db/filling_db.py
python game.py
```

Скрипты обращаются к OpenDota; для повторного сбора данных нужен интернет. Базы SQLite создаются локально и не публикуются в Git.
