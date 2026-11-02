"""Собрать набор победных сборок из публичных матчей OpenDota."""

import sqlite3
import time
from pathlib import Path

import requests


API_URL = "https://api.opendota.com/api"
DB_PATH = Path(__file__).resolve().parent / "archive.db"


def fetch_json(session, url):
    response = session.get(url, timeout=20)
    response.raise_for_status()
    return response.json()


def main():
    stored = 0

    with requests.Session() as session:
        matches = fetch_json(session, f"{API_URL}/publicMatches")

        with sqlite3.connect(DB_PATH) as conn:
            for match in matches:
                if match.get("game_mode") != 22 or match.get("lobby_type") != 7:
                    continue

                match_id = match["match_id"]
                try:
                    details = fetch_json(session, f"{API_URL}/matches/{match_id}")
                except (requests.RequestException, ValueError) as error:
                    print(f"Пропущен матч {match_id}: {error}")
                    continue
                finally:
                    time.sleep(1.1)  # Не превышать бесплатный лимит запросов.

                for player in details.get("players") or []:
                    items = [player.get(f"item_{i}") or 0 for i in range(6)]
                    if (
                        player.get("win") != 1
                        or player.get("leaver_status", 0) != 0
                        or not player.get("hero_id")
                        or sum(bool(item) for item in items) < 3
                    ):
                        continue

                    cursor = conn.execute(
                        """
                        INSERT OR IGNORE INTO quests
                        (match_id, hero_id, item_1, item_2, item_3,
                         item_4, item_5, item_6, item_neutral)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            match_id,
                            player["hero_id"],
                            *items,
                            player.get("item_neutral") or 0,
                        ),
                    )
                    stored += cursor.rowcount

    print(f"Сохранено новых сборок: {stored}")


if __name__ == "__main__":
    main()
