#!/usr/bin/env python3
'''
Query for content from a book of the bible.
'''
import argparse
import query_utils

def query_for_all_chapters(book_name:str=None):
    '''
    '''
    book_text = ''
    prev_text = None
    for chapter_number in range(1, 200):
        chapter_text = query_utils.get_esv_text(
            query_utils.create_passage_query(
                        book=book_name,
                        chapter=str(chapter_number),
                        verse='1-100'
                        )
                    )

        is_new = str(chapter_text) != str(prev_text)
        if is_new:
            book_text += f' {chapter_number}::' + chapter_text
            prev_text = chapter_text
        else:
            break

    return book_text

def main(args):
    '''
    locigal entry point
    '''
    query_utils.process_secrets(args.secrets_file)

    book_name = args.book_name
    book_text = query_for_all_chapters(book_name)
    with open(book_name.replace(' ', '_') + '.txt', 'w') as outfile:
        outfile.write(book_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('secrets_file', type=str, help='a string indicating the secrets file')
    parser.add_argument('book_name', type=str, help='A book of the bible')
    args = parser.parse_args()

    main(args)