"""Main module."""
import os

from hindi_pos_tagger.utils.rule_scrapper import Scrapper

class Main:
    def __init__(self):
        self.scrapper = Scrapper()

    def process_word(self, word):
        try:
            print(f'Processing {word} ...')
            print(f'POS tag: {self.scrapper.get_pos_tag(word)}')
            return self.scrapper.get_pos_tag(word)
        except Exception as e:
            print(f'Occurred Exception {e} in Main.process_word function')
            return e

    def process_document(self, document_path):

        assert os.path.exists(document_path) == True

        print(f'Processing document {document_path}')
        try:
            with open(document_path) as document:
                file = document.readlines()

            for i, line in enumerate(file):
                print('-'*100)
                print(f'Processing line no.{i}')
                tokens = line.split()
                for token in tokens:
                    print(self.scrapper.get_pos_tag(token), end=' ')
                print()

            return True
        except Exception as e:
            print(f'Occurred Exception {e} in Main.process_document function')
            return e
