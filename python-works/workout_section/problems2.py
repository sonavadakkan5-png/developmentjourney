nums = [4, 2, 7, 1]

new =[]

for i in range(len(nums)):

    for j in range(i+1,len(nums)):

        print(nums[i],nums[j])

        if (nums[i]>nums[j]):

            new.append(max(nums[i],nums[j]))

print(new)

           

        

