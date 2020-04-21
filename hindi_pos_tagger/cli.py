"""Console script for hindi_pos_tagger."""
import argparse
import sys

from hindi_pos_tagger.hindi_pos_tagger import Main

parser = argparse.ArgumentParser()
parser.add_argument('choice', type=str, help='Enter choice of stream (word or document)', choices=['word', 'document'])
parser.add_argument('--word', '-w', type=str, help='If choice is word, enter the Hindi word to be tagged')
parser.add_argument('--path', '-p', type=str, help='If choice is document, add path of document to be parsed and the words to be tagged')

args = parser.parse_args()

main_object = Main()

def main():

    if args.choice == 'word' and args.word is not None:
        pos_tag = main_object.process_word(args.word)
        print(f'POS tag for {args.word} is {pos_tag}')
    elif args.choice == 'document' and args.path is not None:
        document_path = args.path
        error = main_object.process_document(document_path=document_path)
        if error is not None:
            print(f'Please select relevant document')
    else:
        print('Incorrect usage')
        parser.print_help()



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
