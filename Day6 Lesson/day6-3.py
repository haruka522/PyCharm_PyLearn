
user_prompt = 'Type add, show, display, edit, complete or exit: '

while True:
    user_action = input(user_prompt)
    
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"
            
            # file = open(r"I:\Python Learning\Day6 Lesson\todos.txt", 'r')  ----- this is the absolute path
            # need to add r in front of the file path, if not some backslash function run
            
            # the file path change if we store todos.txt file in a different folder
            file = open('Day6 Lesson/todos.txt', 'r')  # this is relative path
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open('Day6 Lesson/todos.txt', 'w')
            file.writelines(todos)
            file.close()
            
        case 'show' | 'display':
             
            file = open('Day6 Lesson/todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # print(todos)  //uncomment this line to see the list of todos, there is \n i every item
            
            for index, item in enumerate(todos):
                # item.strip('\n') is to remove the \n from the end of the item
                item = item.title().strip('\n')
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