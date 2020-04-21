from hindi_pos_tagger.utils.rule_scrapper import Scrapper

obj = Scrapper()

def test_rule_file_exist():
    f = None
    with open('./resources/rule_table.csv') as outfile:
        f = outfile.read()
    assert f is not None

def test_rule_table_is_filled():
    assert obj.rule_table.shape[0] > 0
    assert obj.rule_table.shape[1] == 4
