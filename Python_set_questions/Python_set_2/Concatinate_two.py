list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

new_list = []
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        new_ele = f"{list1[i]}{list2[j]}"
        new_list.append(new_ele)

print(new_list)