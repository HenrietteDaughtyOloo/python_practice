#Write a Python function to calculate the area of a circle given its radius.
def area_circle(r):
    area = 3.14*r**2
    return area 
#Write a Python function to calculate the sum of two numbers and return the result.
def sum (a,b):
    the_sum = a + b
    return the_sum
#Write a Python function to find the maximum element in a list.
def maximum (w):
    x= sorted(w)
    return x[-1]
#Write a Python function that returns the Nth Fibonacci number.
def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
    
#Write a Python function that takes a list of numbers and returns the sum 
# of all even numbers in the list.
def even_numbers(numbers):
    sum = 0
    for nums in numbers:
     if nums%2 == 0:
        sum += nums
    return sum
#Write a Python function that takes two strings and returns True if they are palindromes, False otherwise.
def anagram(a,b):
    if a[::-1]==b:
        print("True")
    else:
        print("False")

#Write a Python function that takes a string and returns the reverse of the string.
def reverse(a):
    reversed = a[::-1]
    return reversed

#Write a Python function that takes a list of strings and returns the longest string in the list.
def longest(a_list):
    max_val = -1
    for a in a_list:
        if len(a) > max_val:
            max_val = len(a)
            word = a
    return word  

#Write a Python function that takes a list of integers and returns the second
#  largest number in the list.
def second_largest(int_list):
    sorted_list= sorted(int_list)
    return sorted_list[-2]
#Write a Python function that takes a string and returns True if the string is a palindrome, 
# False otherwise.
def palindrome (string):
    if string[::-1]==string:
        return ("True")
    else:
        return ("False")

#Write a function print_square that takes a number as an argument and prints its square.
def squared(*number):
    # square = number**2
  #  print(square)
    y=[]
    for num in number:
        x=num**2
        y.append(x)
    return y


# Write a Python function that takes two strings and returns True if they are anagrams, False otherwise.
def anagram(a,b):
    word = a.lower()
    word2 = b.lower()
    if len(word)==len(word2):
        sorted_word = sorted(word)
        sorted_word2 = sorted(word2)
        if sorted_word ==sorted_word2:
            return ("True")
    else:
        return ("False")

def remove_second_last(a):
    a.remove(a[-2])
    return a
#write a python function that has a list of days: 
# [Monday, Tuesday, friday, monday] and counts the number of occurences of Monday.
def number_of_occurences(list_of_days):
    return list_of_days.count('Monday')

#Write a function that accepts an unsorted list of integers and 
# finds the smalllest number in the list
def find_smallest(unsorted_list):
    unsorted_list.sort()
    return unsorted_list[0]

def divisible_by_seven():
    empty = []
    for i in range(100,200):
        if i % 7 ==0:
            empty.append(i)
    print(empty)
            # return empty

#Write a program that takes in a list of numbers returns sum of even numbers nd 
#product of odd numbers using the if else statement.
def even_and_odd_numbers(numbers_list):
    sum = 0
    product = 1
    for i in numbers_list:
        if i%2 == 0:
            sum += i
        else:
            product*=i
    print("Sum of even numbers is",sum,)
    print("The product is ",product)
def check_against_ten(number1,number2):
    sum = number1+number2
    if sum<10:
        print("Sum is Less than ten")
    elif sum==10:
        print('Sum is equal to ten')
    elif sum>10:
        print('greater than ten')