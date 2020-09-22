"""Main module."""
import os

from hindi_pos_tagger.utils.rule_scrapper import Scrapper


class Main:
    def __init__(self):
        self.scrapper = Scrapper()

    def process_word(self, word):
        try:
            return self.scrapper.get_pos_tag(word)
        except Exception as e:
            print(f'Occurred Exception {e} in Main.process_word function')
            return e

    def process_document(self, document_path):

        assert os.path.exists(document_path) == True

        try:
            with open(document_path, encoding="utf-8") as document:
                file = document.readlines()

            for i, line in enumerate(file):
                tokens = line.split()
                for token in tokens:
                    pos_tag = self.scrapper.get_pos_tag(token)
                    if pos_tag != 'Unk':
                        print(
                            f'({token}, {self.scrapper.get_pos_tag(token)})', end='\t')
            return True
        except Exception as e:
            print(f'Occurred Exception {e} in Main.process_document function')
            return e
