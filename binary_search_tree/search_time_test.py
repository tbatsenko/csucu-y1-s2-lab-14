"""
File: search_time_test.py

This module measures search time of 1000 random words using:
- list
- binary tree
- balanced binary tree

Requires module linkedbst
"""

import timeit
import random
from linkedbst import LinkedBST


def get_dict(filename):
    """Reads the words from file and returns the list of them"""
    with open(filename) as f:
        dict_lst = []
        lines = f.readlines()
        c = 0
        for line in lines:
            dict_lst.append(line.strip())
    return dict_lst

def get_random_words(dict_lst):
    """Generate 1000 random words form list with all words"""
    random_words = []
    for i in range(1000):
        word = random.choice(dict_lst)
        random_words.append(word)
    return random_words

def construct_bst(dict_lst, balance=False):
    """Construct a binart tree based on lst"""
    tree = LinkedBST(dict_lst)
    if balance:
        tree.rebalance()
    return tree

def search_list(lst, words):
    """Search lst for words"""
    for i in range(len(words)):
        lst.index(words[i])


def search_bst(tree, words):
    """search binart search tree for words"""
    for i in range(len(words)):
        tree.find(words[i])


if __name__ == '__main__':
    dict_lst = get_dict("dict_lst.txt")

    random_words = get_random_words(dict_lst)

    tree = construct_bst(random_words)

    balanced_tree = construct_bst(random_words, balance=True)

    search_list(dict_lst, random_words)

    search_bst(tree, random_words)

    search_bst(balanced_tree, random_words)
    print("Time to search list: ", timeit.timeit(
                            "search_list(dict_lst, random_words)",
                            number=1,
                            # setup="from __main__ import search_list"),
                            globals=globals()))

    print("Time to search tree: ", timeit.timeit(
                            "search_bst(tree, random_words)",
                            number=1,
                            # setup="from __main__ import search_bst"),
                            globals=globals()))

    print("Time to search balanced tree: ", timeit.timeit(
                            "search_bst(balanced_tree, random_words)",
                            number=1,
                            # setup="from __main__ import search_bst"),
                            globals=globals()))
