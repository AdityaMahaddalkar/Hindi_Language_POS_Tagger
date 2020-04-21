## Hindi Parts of Speech Tagger

[![Build Status](https://travis-ci.com/AdityaMahaddalkar/Hindi_Language_POS_Tagger.svg?branch=master)](https://travis-ci.com/AdityaMahaddalkar/Hindi_Language_POS_Tagger)
---

A simple rule-based engine for highlighting Parts Of Speech (POS) tags of words in Hindi language.

- Rules are generated from resources/rule_table.csv which contains 1000 most frequent Hindi words and their POS tags
- Rules are incomplete, which means most words may be tagged as unknown
- The training code for generating resources/rule_table.csv is present in notebooks/"Generate Rule Table.ipynb" jupyter notebook

---

### TODO:

- Develop a CLI application for users to input their own stream of Hindi words (stdin or file)
- Increase the size and accuracy of rule table
- Dockerize the container for portability

### Notes

- Running the jupyter notebook requires dev requirements which are not specified in the requirements_dev.txt
- The notebook is added just for reference
