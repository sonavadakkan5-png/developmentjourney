class Fibonacci:

    def solution(self,number):

        is_fib = False

        empty = []

        p = 0

        c = 1

        empty.append(p)

        empty.append(c)

        for i in range(1,number+1):

            n = p+c 

            p= c

            c=n

            empty.append(n)

            if number in empty:

                is_fib = True

        return is_fib
    
isinstance = Fibonacci()

print(isinstance.solution(15))
























