sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

new_dictionary = {}
# Keys to extract
keys = ["name", "salary"]

for i in keys:
    new_dictionary[i]=sample_dict[i]

print(new_dictionary)