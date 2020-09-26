/***************************************************
* Function Name : Fibonacci Sequence
* Description   : F(n) = 1, n = 0, 1
*                 F(n) = F(n - 1) + F(n - 2), n > 1
* Date          : 2020.09.26
* Author        : xbai
***************************************************/
#include <stdio.h>
/* Recursive method */
int Fibonacci_1(int n)
{
    if(n <= 1)
    {
        return 1;
    }
    else
    {
        return (Fibonacci_1(n - 1) + Fibonacci_1(n - 2));
    }
}

/* Iterative method */
int Fibonacci_2(int n)
{
    int i;
    int First_temp = 1;
    int Second_temp = 1;
    int Calc_item = First_temp + Second_temp;

    for(i = 3;i <= n;i ++)
    {
        First_temp = Second_temp;
        Second_temp = Calc_item;
        Calc_item = First_temp + Second_temp;
    }

    return Calc_item;
}

int main(void)
{
    int result_1;
    int result_2;

    result_1 = Fibonacci_1(6);
    result_2 = Fibonacci_2(6);

    return 0;
}