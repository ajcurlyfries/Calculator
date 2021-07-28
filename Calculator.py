#Lab 1
#File name: Calclator.py
#Author:Andora Zuniga
#Date: August 27th, 2019
#Purpose: prompt the user to select the mathematical operator, display what was selected and then prompt the user to enter the two integers.
#If the user enters a 0 for the second number when the division operator is selected, the application
#should warn that divide by zero is not allowed and exit

import sys
#welcome message
print('************Welcome to the Calculator Application************')

#ask user to pick operator and take input
print('\n\nWhat calculation do you want to perform?')
print('1. Addition (+)')
print('2. Subtraction (-)')
print('3. Multiplication (*)')
print('4. Division (/)')
print('5. Modulus (%)')

opChoice = int(input('\nEnter 1,2,3,4 or 5 indicating your selection: '))

#if 1 addition
if  opChoice == 1:
    print('\nAdditon was selected')
    int1 = int(input('\nEnter your first integer: '))
    int2 = int(input('\nEnter your second integer: '))
    int3 = int1 + int2
    print('\nThe sum of ', int1, ' and ', int2, ' is ', int3)
    print('Thank you for trying the program!')
    print('\n\n***********************************************')
#if 2 subtraction
if  opChoice == 2:
    print('\nSubtraction was selected')
    int1 = int(input('\nEnter your first integer: '))
    int2 = int(input('\nEnter your second integer: '))
    int3 = int1 - int2
    print('\nThe difference between ', int1, ' and ', int2, ' is ', int3)
    print('Thank you for trying the program!')
    print('\n\n***********************************************')
#if 3 multiplcation
if  opChoice == 3:
    print('\nMultiplication was selected')
    int1 = int(input('\nEnter your first integer: '))
    int2 = int(input('\nEnter your second integer: '))
    int3 = int1 * int2
    print('\nThe product of ', int1, ' and ', int2, ' is ', int3)
    print('Thank you for trying the program!')
    print('\n\n***********************************************')
#if 4 division
if  opChoice == 4:
    print('\nDivision was selected')
    int1 = int(input('\nEnter your first integer: '))
    int2 = int(input('\nEnter your second integer: '))
    if int2 == 0:
        print('Division by zero is not allowed')
        print('Thank you for trying the program!')
        print('\n\n***********************************************')
    if int2 != 0:
        int3 = int1 / int2
        print('\nThe division of ', int1, ' by ', int2, ' is ', int3)
        print('Thank you for trying the program!')
        print('\n\n***********************************************')

#if 5 modulus
if  opChoice == 5:
    print('Modulus was selected')
    int1 = int(input('\nEnter your first integer: '))
    int2 = int(input('\nEnter your second integer: '))
    int3 = int1 % int2
    print('\nThe remainder of ', int1, ' divided by ', int2, ' is ', int3)
    print('Thank you for trying the program!')
    print('\n\n***********************************************')

