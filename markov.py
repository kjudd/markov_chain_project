#!/usr/bin/env python

import sys
from sys import argv
import random
import string

script, filename = argv


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    replaced = corpus.replace("\n", " ")
    split_txt = replaced.split(" ")

    markov_text = {}

    for i, word in enumerate(split_txt):

        if i < len(split_txt)-2:
            first_word = word
            second_word = split_txt[i+1]
            third_word = split_txt[i+2]
            current_tuple = (first_word, second_word)
            if current_tuple in markov_text:
                markov_text[current_tuple].append(third_word)

            else:
                markov_text[current_tuple] = [third_word]

    return_list = [0]*2
    return_list[0] = split_txt
    return_list[1] = markov_text
     

    #print markov_text
    return return_list


def make_text(chains, word_list):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #return "Here's some random text."

    random_num = random.randint(0, len(word_list)-2)

    first_word_in_starting_tuple = word_list[random_num]
    second_word_in_starting_tuple = word_list[random_num + 1]
    first_lookup = (first_word_in_starting_tuple, second_word_in_starting_tuple)
    first_value = chains[first_lookup][random.randint(0,len(chains[first_lookup])-1)]

    printout_list = [first_word_in_starting_tuple, second_word_in_starting_tuple, first_value]
     #[inital0, initial1, initial2, first,second,third,fourth,,,,,,,,,,,,,,]

    for i in range(0,50):
        lookup_tuple = (printout_list[i+1], printout_list[i+2])
        if lookup_tuple in chains:   
            initial = chains[lookup_tuple][random.randint(0,len(chains[lookup_tuple])-1)]
            printout_list.append(initial)
            #print i, "i"
            #print printout_list, "PRINTOUT LIST"
        else:
            random_num = random.randint(0, len(word_list)-2)
            first_word_in_backup_tuple = word_list[random_num]
            second_word_in_backup_tuple = word_list[random_num + 1]
            backup_lookup = (first_word_in_backup_tuple, second_word_in_backup_tuple)
            backup_value = chains[backup_lookup][random.randint(0,len(chains[backup_lookup])-1)]
            printout_list.append(first_word_in_backup_tuple)
            printout_list.append(second_word_in_backup_tuple)
            printout_list.append(backup_value)

    print printout_list
    print len(printout_list)

    return printout_list
    

def main():
    args = sys.argv


    text = open(filename)
    input_text = text.read()
    text.close()


    # Change this to read input_text from a file
    #input_text = "Some text"

    word_list_and_chain_dict = make_chains(input_text)

    word_list = word_list_and_chain_dict[0]
    chain_dict = word_list_and_chain_dict[1]

    random_text = make_text(chain_dict, word_list)

    string_random_text = string.join(random_text)

    print string_random_text


    
    #print word_list, "THIS IS WORD LIST"

if __name__ == "__main__":
    main()


#{(first word, second word): {(third word: percentage), (other word: percentage)}}
