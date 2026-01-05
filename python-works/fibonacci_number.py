class Fibonacci:

    def solution(self, limit):

        p = 0

        c = 1

        print(p)

        print(c)

        for _ in range(1,limit-1):

            n = p + c

            print(n)

            p = c

            c = n


isinstance = Fibonacci()

isinstance.solution(4)
  
