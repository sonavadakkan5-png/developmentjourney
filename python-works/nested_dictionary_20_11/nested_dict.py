# . Nested Dictionary
# Create a dictionary called classroom:
# classroom = {
# "student1": {"name": "John", "age": 15},
# "student2": {"name": "Mary", "age": 16}
# }
# Print the age of "Mary".


classroom = {
"student1": {"name": "John", "age": 15},
"student2": {"name": "Mary", "age": 16}
}

for i in classroom:

    n=i.get("name")

    a=i.get("age")

    print(n,a)