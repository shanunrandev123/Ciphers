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
    logp += get_word_prob(w)
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


original_message = "Now the Lord had prepared a great fish to swallow up Jonah There go the ships there is that Leviathan whom thou hast made to play therein In that day the Lord with his sore and great and strong sword shall punish Leviathan the piercing serpent even Leviathan that crooked serpent and he shall slay the dragon that is in the sea And what thing soever besides cometh within the chaos of this monster's mouth be it beast boat or stone down it goes all incontinently that foul great swallow of his and perisheth in the bottomless gulf of his paunch.The Indian Sea breedeth the most and the biggest fishes that are: among which the Whales and Whirlpooles called Balaene, take up as much in length as four acres or arpens of land.Scarcely had we proceeded two days on the sea, when about sunrise a great many Whales and other monsters of the sea, appeared. Among the former, one was of a most monstrous size.... This came towards us, open-mouthed raising the waves on all sides and beating the sea before him into a foam"


#Encoding function

def encode_message(msg):
    msg = msg.lower()
    
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
  

encoded_message = encode_message(original_message)

def decode_message(msg, word_map):
    decoded_msg = []
    for ch in msg:
        #for empty space
        decoded_ch = ch
        if ch in word_map:
            decoded_ch = word_map[ch]
        decoded_msg.append(decoded_ch)
    return ''.join(decoded_msg)
  
  
  
  
  
  


dna_pool = []

for _ in range(10):
    dna = list(string.ascii_lowercase)
    random.shuffle(dna)
    dna_pool.append(dna)
    
    
def evolve_offspring(dna_pool, n_children):
  offspring = []
  
  for dna in dna_pool:
    for _ in range(n_children):
      copy = dna.copy()
      j = np.random.randint(len(copy))
      k = np.random.randint(len(copy))
      
      
      #switch
      tmp = copy[j]
      copy[j] = copy[k]
      copy[k] = tmp
      offspring.append(copy)
      
  return offspring + dna_pool




num_iters = 20
scores = np.zeros(num_iters)
best_dna = None
best_map = None


best_score = float('-inf')

for i in range(num_iters):
  if i > 0:
    dna_pool = evolve_offspring(dna_pool, 3)
    

dna2score = {}
for dna in dna_pool:
  current_map = {}
  for k,v in zip(letters1, dna):
    current_map[k] = v
    
  decoded_message = decode_message(encoded_message, current_map)
  score = get_sequence_prob(decoded_message)
  dna2score[''.join(dna)] = score
  
  
  if score > best_score:
    best_dna = dna
    best_map = current_map
    best_score = score
    
    
scores[i] = np.mean(list(dna2score.values()))

sorted_dna = sorted(dna2score.items(), key = lambda x : x[1], reverse=True)
dna_pool = [list(k) for k,v in sorted_dna[:4]]

if i % 2 == 0:
  print("iter:", i, "score:", scores[i], "best so far", best_score)
  
  

decoded_message = decode_message(encoded_message, best_map)


print("Log likelihood of decoded message:", get_sequence_prob(decoded_message))

print("Log likelihood of True message:", get_sequence_prob(regex.sub(' ', original_message.lower())))



for true, v in true_mapping.items():
  pred = best_map[v]
  if true != pred:
    print("true: %s, pred: %s" % (true, pred))
    
    
  

    


    
            
    