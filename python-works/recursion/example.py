def display_msg(limit):

    if limit == 0:

        return
    
    print("hello December!")

    return display_msg(limit-1)

display_msg(3)


def display_number(limit):

    if limit==0:

        return 
    
    print(limit)
    
    return display_number(limit-1)

display_number(5)


def display_num(limit):

    if limit==1:

        return 1 

    return limit+display_num(limit-1)  # 5 + display_num( 4)

print(display_num(5))






# display_num(5)

# 5+display_num(4)= 5+10 => 15

# 4+ display_num(3)=4+6 =>10

# 3+ display_num(2) = 3+3 = >6

# 2 + display_num(1) = 2+1 = > 3



def factorial(n):

    if n == 1:

        return 1
    
    return n*factorial(n-1) 

print(factorial(5))
    


"""




factorial(5)


5*fact_num(4)=5*24=120
4*fact_num(3)=4*6=24
3*fact_num(2)=3*2=6
2*fact_num(1)=2*1 =2
1*fact_num(0)=1
"""



def sum_digit(num):

    if num ==0:

        return 0
    
    return num%10 + sum_digit(num//10)

print(sum_digit(512))



def product(num):

    if num==0:

        return 1
    
    return num%10 * product(num//10)

print(product(52))



def reverse_num(num):

    if num==0:

        return ""

    return str(num%10) + str(reverse_num(num//10))

print(reverse_num(123))






    



