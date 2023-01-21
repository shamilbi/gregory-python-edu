# coding: utf-8

from pathlib import Path
import secrets
import pickle
import pprint
from statistics import mean

PATH = Path('./scores.pickle')                  # pickle
PATH2 = Path(PATH.parent, PATH.name + '.txt')   # text
NAMES = 3
THEMES = 4
SCORES = 5
CHOICES = list(range(1, 6))

def dict_get(d: dict, key, type_c: type):
    'default value for dict'
    if key in d:
        v = d[key]
    else:
        v = d[key] = type_c()
    return v


def create_scores():
    'create random scores'
    d: dict[str, dict[str, list]] = {}
    for i in range(1, NAMES + 1):
        name = f'ФИО{i}'
        name_d: dict[str, list[int]] = dict_get(d, name, dict)
        for j in range(1, THEMES + 1):
            theme = f'Предмет{j}'
            theme_l = dict_get(name_d, theme, list)
            for _ in range(SCORES):
                score =  secrets.choice(CHOICES)
                theme_l.append(score)
    # save to pickle
    with open(PATH, 'wb') as fp:
        pickle.dump(d, fp)
    # save to text
    with open(PATH2, 'w', encoding='utf-8') as fp:
        pprint.pprint(d, fp)
    return d


def get_scores(name: str, theme: str):
    d = create_scores()
    if not name or name not in d:
        print(f'ФИО "{name}" не найдено')
        return
    d2 = d[name]
    if not theme or theme not in d2:
        print(f'Предмет "{theme}" не найден')
        return
    print(f'{name}, {theme}:')
    l = d2[theme]
    prompt = '1 - все оценки, 2 - средняя оценка >'
    i = input(prompt)
    if i == '1':
        pprint.pprint(l)
    else:
        print(mean(l))


def main():
    get_scores('ФИО2', 'Предмет3')


if __name__ == '__main__':
    main()
