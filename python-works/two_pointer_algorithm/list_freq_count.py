arr = [10,20,60,10,20,40,20,10,80,60]

arr.sort()

frequency = []

left = 0

right = left+1

for num in range(len(arr)-1):

    if arr[right]-arr[left]==0 and arr[left] not in frequency:

        frequency.append(arr[left])

    left+=1

    right+=1

print(frequency)

