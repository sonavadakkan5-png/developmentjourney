def min_two(n1,n2):

    return n1 if n1<n2 else n2

print(min_two(10,2))


def max_two(n1,n2):

    return n1 if n1>n2 else n2

print(max_two(10,20))



def is_odd(n):

    return True if n%2!=0 else False
print(is_odd(5))


def last_digit_max(n1,n2):

    return n1 if n1%10>n2%10 else n2

print(last_digit_max(10,11))



def is_leap_year(year):

    return True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False

print(is_leap_year(1900))   
 



def bmi(height_in_cm,weight_in_kg):

    height_in_meter=height_in_cm/100

    return weight_in_kg/height_in_meter**2

print (round(bmi(156,56)))









    



