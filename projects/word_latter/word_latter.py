# Given two words (beginWord and endWord), and a dictionary's word list, return the
# shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a
# transformed word.

# Note:
# Return None if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.


# Breakdown
# Shortest - BFS
# One letter at a time - edges
# Word list/words - Vertexes
# Return none - path not found
# BeginWord and EndWord - Starting and ending vertices
# No duplicates
# Same length - don't ahve to do anything with different length words
# ^^ Connected componets
# Transofrmation sequence - path


# If we organize the word list in a graph
# with words as vertexes and edges between
# two words that are 1 letter different,
# then
# if we do a BFS from BeginWord to EndWord
# the resulting path will be
# transformation sequence

from util import Queue
from graph import Graph
import sys

word_graph = Graph()
f = open("words.txt", "r")
starting_word = sys.argv[1]
goal_word = sys.argv[2]
