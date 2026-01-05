class NumberCount:

    def solution(*args,**kwargs):

        op = kwargs.get("value")

        if op==10:

            return args.count(op)
        
num_count_instance = NumberCount()

print(NumberCount.solution(10,20,10,10,30,40,50,value = 10))

