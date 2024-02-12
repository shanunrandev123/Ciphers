import pandas as pd
import numpy as np
import nltk
import matplotlib.pyplot as plt
import requests
import textwrap
import os
import random
import re
import string

letters1 = list(string.ascii_lowercase)
letters2 = list(string.ascii_lowercase)

true_mapping = {}
random.shuffle(letters2)

for k, v in zip(letters1, letters2):
  true_mapping[k] = v
  
  
M = np.ones((26,26))

pi = np.zeros(26)

#ord('a) = 97, ord('b') = 98, etc
def update_transition(ch1, ch2):
  i = ord(ch1) - 97
  j = ord(ch2) - 97
  M[i, j] += 1
  
  
  
def update_pi(ch):
  i = ord(ch) - 97
  pi[i] += 1
  

def get_word_prob(word):
  i = ord(word[0]) - 97
  logp = np.log(pi[i])

  for ch in word[1:]:
    j = ord(ch) - 97
    logp += np.log(M[i, j])
    i = j

  return logp


def get_sequence_prob(words):
  if type(words) == str:
    words = words.split()

  logp = 0
  for w in words:
    logp += get_word_prob(word)
  return logp





with open("C:/Users/Asus/Downloads/archive (4)/whale2.txt", 'r') as f:
  content = f.read()
  
# print(content)


regex = re.compile('[^a-zA-Z]')

for line in open('C:/Users/Asus/Downloads/archive (4)/whale2.txt'):
    line = line.rstrip()
    
    if line:
        line = regex.sub(' ', line)
        tokens = line.lower().split()
        
        for token in tokens:
            ch0 = token[0]
            update_pi(ch0)
            
            for ch1 in token[1:]:
                update_transition(ch0, ch1)
                ch0 = ch1

pi /= pi.sum()

M /= M.sum(axis = 1, keepdims = 1)




#Encoding function

def encode_message(msg):
    msg = msg.lowercase()
    
    #replace non alpha characters
    
    msg = regex.sub(' ', msg)
    
    #make the encoded message
    
    coded_msg = []
    
    for ch in msg:
        #no mapping for whitespace
        coded_ch = ch
        
        if ch in true_mapping:
            coded_ch = true_mapping[ch]
            
        coded_msg.append(coded_ch)
        
    return ''.join(coded_msg)


def decode_message(msg, word_map):
    decoded_msg = []
    for ch in msg:
        #for empty space
        decoded_ch = ch
        if ch in word_map:
            decoded_ch = word_map[ch]
        decoded_msg.append(decoded_ch)
    return ''.join(decoded_msg)


#Running an evolutionary algorithm to decode the message

# dna_pool = []

# for _ in range(20):
#     dna = list(string.ascii_lowercase)
#     random.shuffle(dna)
#     dna_pool.append(dna)
    
    
# def evolve_offspring(dna_pool, n_children):
#     offspring = []
    
#     for dna in dna_pool:
#         for _ in range(n_children):
#             copy = dna.copy()
            
    