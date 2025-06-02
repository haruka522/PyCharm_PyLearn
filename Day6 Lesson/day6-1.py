
user_prompt = 'Type add, show, display, edit, complete or exit: '

while True:
    user_action = input(user_prompt)
    
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"
            
            # Need to read the file before 'w' overwrite, 'r' will read the file
            # open is builtin function of the file
            file = open('todos.txt', 'r')
            todos = file.readlines()
            
            # need to close the file after opening it
            file.close()
            
            todos.append(todo)
            
            # Storing the data in a file (this will create a new file in the root folder not in the Lesson folder) 
            # w will overwrite the file everytime it run
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'show' | 'display':
            
            file = open('todos.txt', 'r')
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