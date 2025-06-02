waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row) 

help(list.sort)

waiting_list.sort(reverse=True)
print(waiting_list)

# most string methods return new values instead of modifying the original string
# but list methods modify the original list value and return None