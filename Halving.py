import random

highest = 1000000 # maximum value of random number.

"""
We set here some variables:
- right answer we try to guess.
- three variables related to guessing process, including the current guess.
- all guesses made so far.
"""

right_answer = random.randint(1, highest)
guess_answer = -1
guess_high = highest
guess_low = 0 
answers = []

"""
Algorithm:
- set guess in the middle of low to high guess range.
- depending the comparison to right answer (higher or lower) we adjust boundaries.
- while loop goes to last else on match and tells the amount of guesses used.
"""

while guess_answer != right_answer:
   guess_answer = guess_low + int((guess_high - guess_low)/2) 
   print(guess_answer) 
   answers.append(guess_answer)
   if guess_answer < right_answer:
      print("up") 
      guess_low = guess_answer 
   elif guess_answer > right_answer:
      print("down") 
      guess_high = guess_answer
else:
   print("Cool! %d tries only." % len(answers))
