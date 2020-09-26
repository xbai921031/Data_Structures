"""
* Function Name : Fibonacci Sequence
* Description   : F(n) = 1, n = 0, 1
*                 F(n) = F(n - 1) + F(n - 2), n > 1
* Date          : 2020.09.26
* Author        : xbai
"""

""" Recursive method """
def Fibonacci_1(n):
    counter = int(n)
    if counter < 0:
        print("Put a wrong number !")
    if counter <= 1:
        result = 1
    else:
       result = Fibonacci_1(counter - 1) + Fibonacci_1(counter - 2)
    return result



""" Iterative method """
def Fibonacci_2(n):
    First_temp = 1;
    Second_temp = 1;
    result = First_temp + Second_temp
    counter = int(n)

    if counter < 0:
        print("Put a wrong number !")
    if counter <= 1:
       result = 1
    else:
        while counter >= 3:
            First_temp = Second_temp
            Second_temp = result
            result = First_temp + Second_temp
            counter = counter - 1
    return result

""" Compare two methods' result """
def Fibonacci12_Cmp():
    input_number = int(input("Please input a number : "))
    """ If input is not 'q', keep calculating. """
    result_1 = Fibonacci_1(input_number)
    result_2 = Fibonacci_2(input_number)

    if result_1 == result_2:
        print("Your code is running correctly in both method !\nand result is : %d"%(result_1))
    else:
        print("Your algorithm is not correct, please check !")


cmd = " "
while cmd != 'n':
    cmd = input("Do you want to calculate the fibonacci sequense? y/n : ")
    if cmd == 'y':
        Fibonacci12_Cmp()
