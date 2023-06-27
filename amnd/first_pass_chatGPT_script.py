#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  first_pass_chatGPT_script.py
#  
#  Copyright 2023 martin@theologenius <martin@theologenius.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
#
#
#def main(args):
#    return 0
#
#if __name__ == '__main__':
#    import sys
#    sys.exit(main(sys.argv))

#*********************************************************************

import csv
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

def get_root_word(word):
    lemmatizer = WordNetLemmatizer()
    word_pos = nltk.pos_tag([word])[0][1]
    pos_mapping = {
        'N': wordnet.NOUN,
        'V': wordnet.VERB,
        'R': wordnet.ADV,
        'J': wordnet.ADJ
    }
    pos = pos_mapping.get(word_pos[0].upper(), wordnet.NOUN)
    return lemmatizer.lemmatize(word, pos=pos)

def analyze_text_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        tokens = nltk.word_tokenize(text)
        word_counts = {}
        first_instances = {}
        content_words = []
        page_number = 1  # Initialize page number

        for i, token in enumerate(tokens):
            token = token.lower()
            if token.isalpha():
                if token not in word_counts:
                    word_counts[token] = 1
                    if token not in first_instances:
                        first_instances[token] = (get_root_word(token), page_number)  # Store lemmatized instance and page number
                else:
                    word_counts[token] += 1

                if nltk.pos_tag([token])[0][1][0] in ['N', 'V', 'R', 'J']:
                    content_words.append(token)

            if token == '<PAGEBREAK>':  # Check for page break marker
                page_number += 1

        root_words = [get_root_word(word) for word in content_words]

        # Match root words against CEFR list
        cefr_list = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']  # Example CEFR levels
        matched_words = [word for word in root_words if word in cefr_list]

        return first_instances, word_counts, matched_words

def write_output_to_csv(output_filename, first_instances, word_counts, matched_words):
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Lemmatized Instance', 'Page Number'])
        for word, (lemma, page) in first_instances.items():
            writer.writerow([word, lemma, page])

        writer.writerow([])  # Empty row

        writer.writerow(['Word', 'Count'])
        for word, count in word_counts.items():
            writer.writerow([word, count])

        writer.writerow([])  # Empty row

        writer.writerow(['Matched Words'])
        for word in matched_words:
            writer.writerow([word])

# Example usage
filename = 'example.txt'  # Replace with your text file
output_filename = 'output.csv'  # Replace with the desired output file name

first_instances, word_counts, matched_words = analyze_text_file(filename)
write_output_to_csv(output_filename, first_instances, word_counts, matched_words)

print("Analysis complete. Output file created: output.csv")

