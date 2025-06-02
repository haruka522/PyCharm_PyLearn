
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
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            # use int to convert the string to integer
            number = int(input('Number of the todo to edit: '))
            
            # cuz the index of the list starts from 0, we need to minus 1 from the number
            number = number - 1
            
            # use the index to update the value of the list
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
            
            print(todos)
            
        case 'exit':
            break
        case _:
            print('Only type add, show or exit')

print('Bye Bye!')