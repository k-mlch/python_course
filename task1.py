from random import randint

#new empty list
numbers = []

#loop that 100 times will append a random value from 0 to 1000 to the empty list that was created earlier
for i in range(100):
    numbers.append(randint(0, 1000))

print("List of random numbers: ", numbers)

#bubble sort of the list
for i in range(len(numbers) - 1):  #loop that controls the number of passes
    for j in range(len(numbers) - 1 - i):  #loop that compares element with all other unsorted elements
        if numbers[j] > numbers[j + 1]:  #if current number is greater than the next we swap place of the elements
            temp = numbers[j] #put element that is greater into temp variable
            numbers[j] = numbers[j + 1] #on the place of greater element we put smaller one
            numbers[j + 1] = temp #on place of the smaller one we put our greater element

print("List of sorted numbers: ", numbers)

#lists for odd and even numbers
odd_numbers = []
even_numbers = []

#append even & odd numbers to the correct list variable
for num in numbers:
    if num % 2 == 0:  #checking if the number is even & append it into proper list
        even_numbers.append(num)
    else:  #all others are considered as odd numbers
        odd_numbers.append(num)

print("List of odd numbers: ", odd_numbers)
print("List of even numbers: ", even_numbers)


#find average of odd numbers
if len(odd_numbers) > 0:  #verify that we have at least one odd number to avoid division by zero
    average_odd = sum(odd_numbers) / len(odd_numbers) #divide sum of numbers into their number
else:
    average_odd = 0

print("Average for odd numbers: ", average_odd)

#find average of even numbers
if len(even_numbers) > 0:  #verify that we have at least one odd number to avoid division by zero
    average_even = sum(even_numbers) / len(even_numbers) #divide sum of numbers into their number
else:
    average_even = 0

print("Average for even numbers: ", average_even)