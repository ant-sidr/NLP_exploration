TRASH_SYMBOLS = ["\n"]

ENG_STOP_WORDS = [
    'is', 'a', 'who', 'will', 'be'
]

RUS_STOP_WORDS = [
    'из', 'на', 'все', 'мы', 'и', 'так'
]

RUS_UNION_WORDS = [
    'только'
]

STOP_WORDS = {
    'ENG': ENG_STOP_WORDS,
    'RUS': RUS_STOP_WORDS + RUS_UNION_WORDS
}

SUPPORTED_LANGUAGES = list(STOP_WORDS.keys())

LANGUAGES_STRING = ', '.join(SUPPORTED_LANGUAGES)
