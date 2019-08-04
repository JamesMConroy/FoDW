#!/usr/bin/env python3

import argparse

# This function checks to see if a word is a subsequence of a string sequence
# A string is a subsequence of another if all its chars appear in the same order in both
# This function works by comparing the first char in each string to the other
# If the chars are the same they are both removed from the strings and the strings
# are passed back to the function recursively
# The function terminates if the word is longer than the sequence, meaning it cant
# be a subsequence, or if the word length is = 0 meaning all of its characters
# have been matched in order in the sequence
# O(n) time
def check_for_subset (word, sequence):
    if len(word) > len(sequence):
        return False
    if len(word) == 0:
        return True

    if word[0] == sequence[0]:
        return check_for_subset (word[1:] , sequence[1:])
    if word[0] != sequence[0]:
        return check_for_subset (word , sequence[1:])

if __name__ == '__main__':

    # get command line input
    parser = argparse.ArgumentParser(description='ADD YOUR DESCRIPTION HERE')
    parser.add_argument('-w','--words', help='Word file name', required=True)
    parser.add_argument('-s','--string', help='String file name', required=True)
    args = parser.parse_args()

    words = []
    sequence = ""
    longest_sub_sequence = ""

    # convert word file into list words - O(n)
    with open (args.words, 'r') as word_file:
        for line in word_file:
            words.append(line)

    # convert string file into list of chars S - O(n)
    with open (args.string, 'r') as string_file:
        sequence = string_file.read()

    # sort D by length of words - O(n log n) according to python docs
    words.sort(key=len, reverse=True)

    # get length of S
    sequence_length = len(sequence)

    # Starting with the longest word in D check to see if it is a subsequence O(n)
    for word in words:
        word.rstrip()
        compare_seq = sequence
        if check_for_subset (word, compare_seq):
            longest_sub_sequence = word;
            break

    if len(longest_sub_sequence) > 0:
        print("The longest word in the sequence is: ", longest_sub_sequence)
    else:
        print("No provided word is a sub sequence")
