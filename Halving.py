import random

highest = 1000000

times = set() 

for time in range (1, 1000):

   answer = random.randint(1, highest)
   asnwer = -1
   asnwerh = highest
   asnwerl = 0
   asnwers = [] 

   while asnwer!= answer:
      asnwer = asnwerl + int((asnwerh - asnwerl)/2) 
      print(asnwer) 
      asnwers.append(asnwer)
      if asnwer < answer:
          print("up") 
          asnwerl = asnwer
      elif asnwer > answer:
          print("down") 
          asnwerh = asnwer
   else:
      print("Waude! %d arvausta." % len(asnwers)) 
      times.add(len(asnwers)) 

print(times)
