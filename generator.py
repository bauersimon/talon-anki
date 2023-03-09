import csv
import random
from os import listdir, path, makedirs
from typing import List, Tuple
from sys import argv

import genanki


def read_csv(p: str) -> List[Tuple[str, str]]:
    with open(p) as f:
        reader = csv.reader(f, delimiter=',')
        return list(reader)


CARD = genanki.Model(
    123456789,
    'QA Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card',
            'qfmt': '{{Question}}',
            'afmt': '{{FrontSide}}<hr>{{Answer}}',
        },
    ])


def save_deck(items: List[Tuple[str, str]], p: str):
    deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        path.splitext(path.basename(p))[0])
    for i in items:
        deck.add_note(genanki.Note(
            model=CARD,
            fields=[i[0], i[1]]))
    genanki.Package(deck).write_to_file(p)


def batch(source: str, target: str):
    for f in listdir(source):
        d = read_csv(path.join(source, f))
        t = path.join(target, path.splitext(f)[0]+'.apkg')
        save_deck(d, t)
        print(f'saved {t}')


if __name__ == "__main__":
    if len(argv) == 1:
        makedirs(path.join('decks', 'apkg'), exist_ok=True)
        batch(path.join('decks', 'csv'), path.join('decks', 'apkg'))
    else:
        batch(argv[1], argv[2])
