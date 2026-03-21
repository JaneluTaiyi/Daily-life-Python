
# present the deck of cards by numbers
list1 = list (range(1,33))
print("The deck is:", list1)

# split the deck into the first and the second half
mid = len(list1)//2
print("The length of half of the deck is", mid)

# store the two halves into new lists
list2 = list1[:mid]
list3 = list1[mid:]
print("The first half of the original deck is:", list2)
print("The second half of the original deck is:", list3)

# reorgnize the deck method #1
list4 = []
for i in range(len(list2)):
    list4.append(list2[i])
    list4.append(list3[i])
print("The deck after one shuffle is:", list4)

# reorgnize the deck method #2
list5 = [item for pair in zip(list2, list3) for item in pair]
print("The deck after one shuffle is:(method 2)", list5)

# reorgnize the deck method #3
list6 = [item for pair in zip(list1[:16], list1[16:]) for item in pair]
print("The deck after one shuffle is:(method 3)", list6)

# shuffle the deck 6 times
i = list (range(1,7))
print ("i = ", i)

# shuffle the deck 5 times and check it up 
# (supposed to be the same as the original deck)
for i in range(1,6): list1 = [item for pair in zip (list1[:16], list1[16:]) 
    for item in pair];

print(f"The deck after {i} times of shuffle: {list1}")

for i in range(1,7): list1 = [item for pair in zip (list1[:16], list1[16:]) 
    for item in pair];

print(f"The deck after {i} times of shuffle: {list1}")
