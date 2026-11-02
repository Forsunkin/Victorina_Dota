"""Выбрать ID заданий в случайном порядке без повторений."""

import random


def get_random_list(connection):
    ids = [row[0] for row in connection.execute("SELECT id FROM quests")]
    random.shuffle(ids)
    return ids
