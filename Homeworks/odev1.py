import random # we need to use this module to generate random numbers #
def isPrime(num): # we will define a new function which takes a number as a parameter called "num"
  if num <= 1: #checking if number is lesser or equal to 1;
    return False # returning false since  1 and 0 are not prime numbers
  elif num == 2: # checking if num equals to 2
    return True # returns true since it is Prime
  for i in range(2, num): # For every iteration of loop; i increases by 1 while it is between 2 and given number
    if num%i == 0: # Mods num. and current iteraion "i" and checks if its result equals to 0 (remainder)
      return False # Returns false since the condition is not met  
  return True # returns True since none of the conditions which made the num. non-Prime were met
rndPrimelist = [] # creates an empty list to assign random prime numbers
for i in range(101):# for loop between 0-100
  if isPrime(i): # checking if the number is Prime by using isPrime() function
    rndPrimelist.append(i) #using append method to add i to given list
#rndPrimelist = [x for x in range (101) if isPrime(x)]# or we can use list comprehensions
matrix = [] # creates an empty list 
for i in range(3): # creates a for loop between 0 to 3
  matrix.append([]) # appending an empty list to matrix[]
  for j in range(3): # creates another for loop inside its parent loop
    rnd = random.choice(rndPrimelist)# picks and assigns a random number for every iteration of i from rndPrimelist[]
    matrix[i].append(rnd) # appends the random numbers which were picked and assigned in previous line to the matrix[i] which we created as an empty list in outer loop(current iteration of i)
    rndPrimelist.remove(rnd) # removes the picked number from pre-created rndPrimeList[] to prevent duplication

for x in matrix:# creates a for-each loop for every item of matrix[] which is a list
  for y in x: # creates an inner for-each loop for elements of outer for loop row for each iteration
    print(y, end = " ") # adding spaces instead of \n to make it look PRETTIER
  print("\n") # adding new lines on the  end of  every iteration of the outer loop
