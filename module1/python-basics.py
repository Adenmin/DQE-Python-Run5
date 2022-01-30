from random import randint

# Create an empty list.
randomlist = []

# List length.
n = 100

# In for loop in range(0,100) append to empty list random int in range (0,1000).
for i in range(n):
    randomlist.append(randint(0, 1000))

# Sort list from min to max by bubble sorting.
for i in range(n):
    for j in range(n - 1 - i):
        if randomlist[j] > randomlist[j + 1]:
            randomlist[j], randomlist[j + 1] = randomlist[j + 1], randomlist[j]

# Create empty lists for even and odd numbers.
evens = []
odds = []

# Fill lists by cases.
for number in randomlist:
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

# Calculate average of even numbers
try:
    avg_evens = sum(evens) / len(evens)
    print("Average of evens: " + str(avg_evens))
except ZeroDivisionError:
    print("List doesn't contain even values.")

# Calculate average of odd numbers.
try:
    avg_odds = sum(odds) / len(odds)
    print("Average of odds: " + str(avg_odds))
except ZeroDivisionError:
    print("List doesn't contain odd values.")
