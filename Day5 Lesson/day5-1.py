
user_prompt = 'Type add, show, display, edit or exit: '

todos = []

while True:
    user_action = input(user_prompt)
    
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            
            # enumerate(list's variable name) in for loop to get the index number and item
            for index, item in enumerate(todos):
                item = item.title()
                print(index + 1, "." , item)
                
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            
            number = number - 1
            
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
            
            print(todos)
            
        case 'exit':
            break
        case _:
            print('Only type add, show or exit')

print('Bye Bye!')

# print x will return the object of enumerate
x = enumerate(['a', 'b', 'c'])
print(x)

# if you want to see the value of x, you can use list() to convert the object to list
print(list(x))

# for loop with enumerate work like this
for index, item in [(0, 'a'), (1, 'b'), (2, 'c')]:
    print(index, item)
    
# you can also use with strings