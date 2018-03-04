import random

highest = 1000000

times = set() 

right_answer = random.randint(1, highest)
guess_answer = -1
guess_high = highest
guess_low = 0 
answers = []

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
