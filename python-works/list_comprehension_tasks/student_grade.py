# Convert a dictionary of student marks to grade using dict comprehension.
# Sample Input: {"Aju": 92, "Binu": 76, "Chandru": 64}
# Sample Output: {'Aju': 'A', 'Binu': 'B', 'Chandru': 'C'}


Sample_Input = {"Aju": 92, "Binu": 76, "Chandru": 64}

empty_dict ={

    name:  ("A" if  mark >90 else

            "B" if  mark >75 else

            "C" if mark >60 else "D")

    for name,mark in Sample_Input.items()
}

print(empty_dict)



