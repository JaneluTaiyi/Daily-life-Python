import random

def calculation (n):
  
  female_share_allhousehold = 0 # name the accumulated female share per household as "female_share_allhousehold"
  
  for _ in range (n):
    children = [] # name the gander combination in a household in list "children"
    while True:
      child = random.choice([0,1]) # assume: female child -1, non-female child -0
      children.append(child) # store all events (1 or 0) of the household to 'children'
      if child == 1:  # when the child born is female
        break         # stop producing more child in the household
      
    female_share_inthishousehold = 1 / len(children) # 'len(children)' is the amount of kids this household has
    female_share_allhousehold += female_share_inthishousehold # name the accumulated female share per household as "female_share_allhousehold"
    average_share = female_share_allhousehold *(1/n) 
  return average_share
  
n=5000 # considering the total 5000 households -'n'
result = calculation(n) * 100 # the unit of result is 100%
print(f"Average share of female children per household: {result:.4f}%")