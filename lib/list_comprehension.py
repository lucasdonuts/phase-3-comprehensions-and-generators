#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [s + "!" for s in sentence_list]

print(return_evens([0, 1, 3, 5, 7, 8, 9]))
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
# function return_evens() returns empty list when num_list has no evens F
# function return_evens() returns evens from num_list F
# function make_exclamation() returns empty list when sentence_list is empty F
# function make_exclamation() returns list of sentences with exclamation marks F