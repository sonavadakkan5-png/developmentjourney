class Merged:

    def solution(self,intervals):

        intervals.sort(key = lambda i : i[0]) #[1,3],[2,6]

        output = [intervals[0]]#[1,3]

        for start,end in intervals[1:]:#[2,6]

            last =output [-1][1] #3

            if start <=last:#2<=3

                output [-1][1]=max(last,end)

            else:

                output.append([start,end])

        return output
    
instance = Merged()

print(instance.solution([[1,3],[2,6],[9,10]]))











