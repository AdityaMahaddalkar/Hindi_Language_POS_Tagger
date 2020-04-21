import pandas as pd

RULE_FILE = './resources/rule_table.csv'

class Scrapper:
    def __init__(self, rule_file=RULE_FILE):
        self.rule_file = rule_file
        self.rule_table = pd.read_csv(rule_file)

    def _word_exist(self, word):
        holder_dataframe = self.rule_table[self.rule_table['WORD'] == word]
        if holder_dataframe.shape[0] == 0:
            return False
        return True

    def get_pos_tag(self, word):
        if self._word_exist(word) == False:
            return 'Unk'
        print(type(self.rule_table[self.rule_table['WORD'] == word]['POS'].values[0]))
        return self.rule_table[self.rule_table['WORD'] == word]['POS'].values[0]
