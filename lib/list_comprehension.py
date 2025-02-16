#!/usr/bin/env python3

def return_evens(num_list):
    even_number =[num_list for num_list in num_list if num_list % 2 == 0]
    return even_number


print(return_evens([1,2,3,4,5,6,7,8]))
def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]