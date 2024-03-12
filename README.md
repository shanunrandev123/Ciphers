# Substitution Ciphers

                                                             
They are one of the oldest and simplest methods of encryption. They involve replacing plain text letters or characters with others in a fixed pattern to create a cipher text.
They represent probably the most widely used encryption system in antiquity.

Overview : Sender sends a message to the reciever -> An intruder intercepts the message but is encrypted -> The reciever decrypts the message. Both sender/reciever can encrypt/decrypt a message using a dictionary(that maps plain text to cipher text)

## Higher Level Picture

![image](https://github.com/shanunrandev123/Ciphers/assets/49170258/f27d7791-2ec4-49ae-b0a0-7439bc085231)

##Intuition -> Build a model that assigns high probability to real words/ sentences and low probability to unreal words/ sentences

![image](https://github.com/shanunrandev123/Ciphers/assets/49170258/1bf4d927-9205-40b9-9aaf-03c6992eff34)

for example :

LangModel("I Love NLP") -> High probability number (real words and sentence)

LangModel("UBNHGTY") -> Low probability number(unreal words and sentence)

so, if we decrypt the message correctly, the model should return a high probability and if the decryption is done incorrectly the model should return a low probability.

# Basic approach in Language Modelling
## N - Grams and markov modelling

-> N grams is a sequence of N tokens. For this project tokens refer to indivisual letters. We usually work with small values of N
   N = 1 : Unigram
   N = 2 : Bigram
   N = 3 : Trigram

###Markov Assumption : In the current state x(t) depends only on the previous state x(t - 1) and not on x(t - 2), x(t - 3) and so on.

P(X(T) | X(T - 1), X(t - 2), X(t - 3)) = P(X(t) | X(t - 1))


## Practical Issue
Probabilities are small, assume they are around 0.15 on average(overestimate)

What will happen if we have a 100 character long sentence? - Probability = 10 ^ -100. Probabilities will get so small that they will get rounded to zero 

To solve this problem we employ ## Log-Likelihood

# How to use the language model?

## Naive approach - 

1.Get all the possible decryption maps and initialise a minimum log likelihood value and best message as None.
2. Then we loop through each map and decode the encrypted message and calculate the log likelihood, if the calculated log likelihood is greater than the initialised log likelihood value we update the value and in this way we can find the best log likelihood message.

## This approach is quite infeasible and it will take billions of years to compute this.


## To solve this issue we employ Genetic Algorithms






