"""Заполнить справочники героев и предметов из OpenDota."""

import sqlite3
from pathlib import Path

import requests


API_URL = "https://api.opendota.com/api"
DB_PATH = Path(__file__).resolve().parent / "catalog.db"


def fetch_json(url):
    response = requests.get(url, timeout=20)
    response.raise_for_status()
    return response.json()


def main():
    heroes = fetch_json(f"{API_URL}/heroes")
    items = fetch_json(f"{API_URL}/constants/items")

    with sqlite3.connect(DB_PATH) as conn:
        for hero in heroes:
            roles = (hero.get("roles") or [])[:4]
            roles += [None] * (4 - len(roles))
            conn.execute(
                """
                INSERT OR REPLACE INTO heroes
                (id, localized_name, name, role_1, role_2, role_3, role_4)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    hero["id"],
                    hero["localized_name"],
                    hero["name"].removeprefix("npc_dota_hero_"),
                    *roles,
                ),
            )

        for name, item in items.items():
            if item.get("id") is None:
                continue
            conn.execute(
                """
                INSERT OR REPLACE INTO items (id, localized_name, name)
                VALUES (?, ?, ?)
                """,
                (item["id"], item.get("dname") or name, name),
            )

    print(f"Справочники обновлены: {len(heroes)} героев, {len(items)} предметов.")


if __name__ == "__main__":
    main()
