import re
import random
import argparse
import query_utils

def get_passage(book:str=None, chapter:str=None, verses:str=None):
    """
    """
    return query_utils.create_passage_query(book=book, chapter=chapter, verse=verses)


def parse_reference_into_tuple(reference:str=None):
    """
    """
    strarray1 = reference.split('.')
    strarray2 = reference.split(':')
    if (len(strarray1) != 2 and len(strarray2) != 2):
        print(f'Input Error: could not parse {reference}. Please use ch:vrs or ch.vrs format.')
        return None, None
    if (len(strarray1)==2):
        return strarray1[0], strarray1[1]
    return strarray2[0], strarray2[1]


def main(args):
    '''
    locigal entry point
    '''
    query_utils.process_secrets(args.secrets_file)
    chapter, verses = parse_reference_into_tuple(reference=str(args.reference))
    if chapter is None and verses is None:
        return
    text, validated_reference = query_utils.get_esv_text(
        get_passage(book=args.book_name, chapter=chapter, verses=verses))
    print(f'{text} - {validated_reference}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('secrets_file', type=str, help='a string indicating the secrets file')
    parser.add_argument('book_name', type=str, help='A book of the bible in double quotes: "psalms"')
    parser.add_argument('reference', type=str, help='The chapter:verse reference in double quotes: "1:1-3" or "1.1-3"')
    args = parser.parse_args()

    main(args)