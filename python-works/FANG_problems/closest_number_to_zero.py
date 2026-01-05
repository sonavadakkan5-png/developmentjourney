class Closeset:

    def solution(self,arr):

        closest_num = arr[0]

        for num in arr:

            if abs(num) < abs(closest_num):

                closest_num = num

        if closest_num <0 and abs(closest_num) in arr:

            return abs(closest_num)
        
        else:

            return closest_num
        
closest_instance = Closeset()

print(closest_instance.solution([2,3,-1]))








#         return closest_number
    
# clst_instance = ClosestNumberToZero()

# clst_instance.solution([-2,2,-1,4,5])

# positive = []

# negative =[]

# numbers = [-1,1,2,-2,4,6]

# # print(sorted(numbers))

# for i in numbers:

#     if i >0:

#         positive.append(i)

#     else:

#         negative.append(i)



# print(positive[0])

# print(negative[0])

# if positive[0]>negative[0]:

#     print(positive[0])

# else:

#     print(negative[0])



# closet_no = 0

# numbers = [ 1,-2,3,-2]

# for i in numbers:

#     if closet_no+1 ==i:

#         a=i

#     elif closet_no-1==i:

#         b=i

# if a and b:

#     print(a if a>b else b)


# elif a:

#     print(a)

# elif b:

#     print(b)




# num = [1, -2, 3, 4, 5]

# result = []

# for i in num:

#     result.append(abs(i))

# print(min(result))


class Close:

    def solution(self,arr): #[1,-2,-1,3]

        result = arr[0] #1

        for num in arr:#1

            if abs(num)<abs(result):

                result = num

        if result<0 and abs(result) in arr:

            return abs(result)
        
        else:

            return result
        
instance = Close()

print(instance.solution([1,-1,3]))





