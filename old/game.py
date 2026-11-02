"""Вывести случайную сборку из локальной базы."""

import sqlite3
from pathlib import Path

from random_quests import get_random_list


DB_PATH = Path(__file__).resolve().parent / "db" / "archive.db"


def main():
    if not DB_PATH.exists():
        raise SystemExit("База не найдена. Сначала запустите db/create_tables.py.")

    with sqlite3.connect(DB_PATH) as conn:
        ids = get_random_list(conn)
        if not ids:
            raise SystemExit("Нет заданий. Сначала запустите db/filling_db.py.")

        question = conn.execute(
            """
            SELECT match_id, hero_id, item_1, item_2, item_3,
                   item_4, item_5, item_6, item_neutral
            FROM quests WHERE id = ?
            """,
            (ids[0],),
        ).fetchone()

    print("Матч:", question[0])
    print("Герой (ID):", question[1])
    print("Предметы (ID):", question[2:8])
    print("Нейтральный предмет (ID):", question[8])


if __name__ == "__main__":
    main()
