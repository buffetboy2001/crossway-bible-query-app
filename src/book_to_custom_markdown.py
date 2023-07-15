#!/usr/bin/env python3
'''
Query for content from a book of the bible. Write the text using the custom markdown format used by swils.markdown-scripture vscode extension.

Ex: ./book_to_custom_markdown.py ./secret.json job
'''
import argparse
import query_utils

def query_for_all_chapters(book_name:str=None) -> dict:
    '''
    Returns the text of each chapter in a dict. Key is chapter number.
    '''
    params = {
            'q': None,
            'indent-poetry': False,
            'include-headings': False,
            'include-footnotes': False,
            'include-verse-numbers': True,
            'include-short-copyright': False,
            'include-passage-references': False}
    chapters = {} # chapter_num: chapter_text
    prev_text = None
    for chapter_number in range(1, 200):
        chapter_text, reference = query_utils.get_esv_text(
            passage = query_utils.create_passage_query(
                        book=book_name,
                        chapter=str(chapter_number),
                        verse='1-200'
                        ),
            params=params)
        print(f'Chapter {chapter_number}')

        is_new = str(chapter_text) != str(prev_text)
        if is_new:
            chapters.update({chapter_number:chapter_text})
            prev_text = chapter_text
        else:
            break

    return chapters

def main(args):
    '''
    locigal entry point
    '''
    query_utils.process_secrets(args.secrets_file)

    book_name = args.book_name
    chapters = query_for_all_chapters(book_name)
    with open(book_name.replace(' ', '_') + '.md', 'w') as outfile:
        for chapter_number, chapter_text in chapters.items():
            outfile.write(f'\n## Chapter {chapter_number} <!-- scripture:{chapter_number} -->\n')
            outfile.write(chapter_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('secrets_file', type=str, help='a string indicating the secrets file')
    parser.add_argument('book_name', type=str, help='A book of the bible')
    args = parser.parse_args()

    main(args)