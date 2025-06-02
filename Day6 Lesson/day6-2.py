
user_prompt = 'Type add, show, display, edit, complete or exit: '

while True:
    user_action = input(user_prompt)
    
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('todos.txt', 'w')
            # file.write will write the file with a single string
            # file.writelines will write the file with a list
            file.writelines(todos)
            file.close()
            
        case 'show' | 'display':
             
            file = open('todos.txt', 'r')
            # file.read will read the file and store the data as a single string
            # file.readlines will read the file and store the data as a list
            todos = file.readlines()
            file.close()
            
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index + 1} => {item}"
                print(row)
            
            print('maybe', index, item)
            print()
            print("The number of things to do: ", len(todos))
                
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number = number - 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
            print(todos)
            
        case 'exit':
            break
        
        case 'complete':
            number = int(input('Number of the todo to complete: '))
            todos.pop(number - 1)
            
            for index, item in enumerate(todos):
                item = item.title()
                row = f"{index + 1} => {item}"
                print(row)
                
        case _:
            print('Only type add, show or exit')

print('Bye Bye!')