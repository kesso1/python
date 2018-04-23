#!/usr/bin/env python
"""Build an index for word to list of occurrences."""

import argparse
import re
import collections


def load_stop_words(file_name):
    """Load stop words from file into a set. One word per line."""
    with open(file_name) as file:
        return {w.strip() for w in file}


def build_word_index(file_name, stop_words):
    """Create index that maps lower-case word to a list of its occurrence.
       Each occurrence is a tuple (line number and the start column) of the
       word.

       :param file_name text file to open for read
       :param stop_words set containing stop words
       :return dictionary map from word to occurrence
       """
    index = collections.defaultdict(list)
    word_regex = re.compile(r'\w+')

    with open(file_name) as file:
        for line_number, line_text in enumerate(file, 1):
            for match in word_regex.finditer(line_text):
                word = str.lower(match.group())
                column_number = match.start() + 1
                # YOUR CODE HERE
                # Skip word if it is in stop_words set,
                # otherwise, add occurrence to the index
                # The occurrence is a tuple (line number, column number).
    return index


def print_index_top_k_frequent(k, index):
    """
    Print the index for the k most frequently occurring words.

    :param k: k most-frequent words to print
    :param index: word-to-array of occurrence dictionary
    :return None
    """
    # YOUR CODE HERE


def print_top_k_frequent_words(k, index):
    """
    Print the k most frequently occurring words along with their frequency.
    :param k: k most-frequent words
    :param index: word-to-array of occurrence dictionary
    :return: None
    """
    # YOUR CODE HERE


def main():
    """Parses command line, optionally reads in stop words from file,
       builds index and prints it."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='create word index.')
    parser.add_argument('textfile', metavar='file', type=str,
                        help='text file to index')
    parser.add_argument('-w', '--stopwords', metavar='f', type=str,
                        help='text file that contains stop words')
    parser.add_argument('-s', '--short', action='store_true',
                        help='print only word and number of occurrences')
    parser.add_argument('-t', '--top', metavar='k', type=int, default=None,
                        help='number of k-top elements to return')
    args = parser.parse_args()

    stop_words = {} if not args.stopwords else load_stop_words(args.stopwords)
    index = build_word_index(args.textfile, stop_words)
    if args.short:
        print_top_k_frequent_words(args.top, index)
    else:
        print_index_top_k_frequent(args.top, index)


if __name__ == '__main__':
    main()
