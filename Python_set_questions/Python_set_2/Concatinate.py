list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

new_list = []

for i in range(0,len(list1)):
    new_ele = f"{list1[i]}{list2[i]}"
    new_list.append(new_ele)
    
print(new_list)