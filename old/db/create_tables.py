"""Создать локальные SQLite-базы старого прототипа."""

import sqlite3
from pathlib import Path


DB_DIR = Path(__file__).resolve().parent


def main():
    with sqlite3.connect(DB_DIR / "catalog.db") as conn:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                localized_name TEXT NOT NULL,
                name TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS heroes (
                id INTEGER PRIMARY KEY,
                localized_name TEXT NOT NULL,
                name TEXT NOT NULL,
                role_1 TEXT,
                role_2 TEXT,
                role_3 TEXT,
                role_4 TEXT
            );
            """
        )

    with sqlite3.connect(DB_DIR / "archive.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS quests (
                id INTEGER PRIMARY KEY,
                match_id INTEGER NOT NULL,
                hero_id INTEGER NOT NULL,
                item_1 INTEGER,
                item_2 INTEGER,
                item_3 INTEGER,
                item_4 INTEGER,
                item_5 INTEGER,
                item_6 INTEGER,
                item_neutral INTEGER,
                UNIQUE (match_id, hero_id)
            )
            """
        )


if __name__ == "__main__":
    main()
