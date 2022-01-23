#!/usr/bin/env python3
'''
From: https://api.esv.org/docs/samples/
'''
import re
import random
import argparse
import query_utils

CHAPTER_LENGTHS = [
    33, 22, 35, 27, 23, 35, 27, 36, 18, 32,
    31, 28, 25, 35, 33, 33, 28, 24, 29, 30,
    31, 29, 35, 34, 28, 28, 27, 28, 27, 33,
    31
]


def get_random_proverbs_passage():
    chapter = random.randrange(1, len(CHAPTER_LENGTHS))
    verse = random.randint(1, CHAPTER_LENGTHS[chapter])

    return query_utils.create_passage_query(book="Proverbs", chapter=chapter, verse=verse)


# def render_esv_text(data):
#     text = re.sub('\s+', ' ', data['passages'][0]).strip()

#     return '%s – %s' % (text, data['canonical'])

def main(args):
    '''
    locigal entry point
    '''
    query_utils.process_secrets(args.secrets_file)
    print(query_utils.get_esv_text(get_random_proverbs_passage()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('secrets_file', type=str, help='a string indicating the secrets file')
    args = parser.parse_args()

    main(args)