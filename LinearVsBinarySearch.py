# Importing needed libraries
import random
import matplotlib.pyplot as plt

# Function to create a random array given the number of elements and range of the numbers
def randomList(numElements, numRange):
    # Creating an empty list
    list = []
    # Creating a temporary random integer
    temp = random.randint(1, numRange)
    # Looping the number of elements passed in to create add a random integer
    for i in range(numElements):
        # Creating while loop to loop through all elements all ready in the list
        while temp in list:
            # Assigning the temp variable to a new random number integer if the temp integer is already in the list
            temp = random.randint(1, numRange)
        # Adding the temp integer to the list
        list.append(temp)
    # Returning the random and distinct list of integers
    return list

# Function to create a sorted random array given the number of elements and range of the numbers
def randomListSorted(numElements, numRange):
    # Creating an empty list
    list = []
    # Creating a temporary random integer
    temp = random.randint(1, numRange)
    # Looping the number of elements passed in to create add a random integer
    for i in range(numElements):
        # Creating while loop to loop through all elements all ready in the list
        while temp in list:
            # Assigning the temp variable to a new random number integer if the temp integer is already in the list
            temp = random.randint(1, numRange)
        # Adding the temp integer to the list
        list.append(temp)
    # Sorting the completed random list
    list.sort()
    # Returning the sorted, random and distinct list of integers
    return list

# Function to generate a random number given range of the numbers in the array
def randomInt(numRange):
    # Generating a random integer given the range
    randomNum = random.randint(1, (numRange + 2))
    # Returning the random integer
    return randomNum

# Implementing the linear search algorithm passing in an integer to found and an array to check
def linearSearch(find, search):
    # Creating a counter to loop through the list and store the number of comparisons
    counter = 0
    # Creating a while loop to search through all elements of the list
    while counter < len(search):
        # Checking if the integer to be found is equal to the indexed element of the list
        if find == search[counter]:
            # Returning the counter plus one to indicate the number of comparisons
            return counter + 1
        # Incrementing the counter if the integer is not found
        counter += 1
    # If the element is not found, returning the length of the list to indicate the comparisons made
    return 0

# Creating the binary search function passing in an integer to be found and a sorted array to be checked
def binarySearch(find, search):
    # Creating the counter to loop though the array and keep track of comparisons
    counter = 0
    # Creating initial left variable to indicate the leftmost part of the list
    left = 0
    # Creating the right variable to indicate the rightmost part of the list
    right = len(search) - 1
    # Creating while loop to compare the values
    while left < right:
        # Creating middle variable to be inbetween the left and right variables
        middle = int((left + right) / 2)
        # Checking if the integer to be found is equal to the middle element of the list
        if find == search[middle]:
            # Returning counter plus one to represent the comparisons made
            return counter + 1
        # Checking if the element to be found is greater than the middle element of the list
        elif find > search[middle]:
            # Altering the left variable of condition is met
            left = middle + 1
        else:
            # Setting right variable equal to the middle variable if the previous two conditions didn't pass
            right = middle
        # Incrementing the counter
        counter += 1
    # Returning the counter to represent the number comparisons made if the element is not found
    return 0

# Creating linear search test function to find the average count
def linearTest(n):
    # Creating count varaible
    count = 0
    # Creating loop to run 100 times
    for i in range(100):
        # Summing up the count for every iteration of the for loop
        count += linearSearch(randomInt(n), randomList(n, n))
    # Calculating the average the count
    average = (count / 100)
    # Returning the average
    return average

def binaryTest(n):
    # Creating count varaible
    count = 0
    # Creating loop to run 100 times
    for i in range(100):
        # Summing up the count for every iteration of the for loop
        count += binarySearch(randomInt(n), randomListSorted(n, n))
    # Calculating the average the count
    average = (count / 100)
    # Returning the average
    return average

# Creating a list with the X-Values to be plotted for the Linear Test and O(n)
xPointsL = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Creating the Y-Values for O(n)
yPointsLBigO = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Creating a list with the Y-Values to be plotted for the Linear Test
yPointsL = [linearTest(10), linearTest(10), linearTest(30), linearTest(40), linearTest(50),
           linearTest(60), linearTest(70), linearTest(80), linearTest(90), linearTest(100)]
#Plotting the Linear Search Algorithm results for the Linear Test
plt.title("Behavior of Linear Search Algorithm")
plt.xlabel("Value of N")
plt.ylabel("Average of Linear Search for N")
plt.plot(xPointsL, yPointsLBigO, label = "f(n) = n")
plt.plot(xPointsL, yPointsL, marker = "o", label = "Linear Test Results")
plt.legend()
plt.show()

# Creating a list with the X-Values to be plotted for the Binary Test
xPointsB = [4, 8, 10, 16, 32, 64, 128, 256, 512, 1024]
# Creating the Y-Values for O(log2n)
yPointsBBigO = [2, 3, 3.3219280949, 4, 5, 6, 7, 8, 9, 10]
# Creating a list with the Y-Values to be plotted for the Binary Test
yPointsB = [binaryTest(4), binaryTest(8), binaryTest(10), binaryTest(16), binaryTest(32),
            binaryTest(64), binaryTest(128), binaryTest(256), binaryTest(512), binaryTest(1024)]
# Plotting the Binary Search Algorithm Results
plt.title("Behavior of Binary Search Algorithm")
plt.xlabel("Value of N")
plt.ylabel("Average of Binary Search for N")
plt.plot(xPointsB, yPointsBBigO, label = "f(n) = log2(n)")
plt.plot(xPointsB, yPointsB, marker = "o", label = "Binary Test Results")
plt.legend()
plt.show()