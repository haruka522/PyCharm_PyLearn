
user_prompt = 'Type add, show, display, edit, complete or exit: '

todos = []

while True:
    user_action = input(user_prompt)
    
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show' | 'display':
            
            for index, item in enumerate(todos):
                item = item.title()
                
                # F String to get the style you want to show
                row = f"{index + 1} => {item}"
                print(row)
            
            # if index and item are not in the for loop, it will print the last value of the list
            print('maybe', index, item)
            print()
            print("The number of things to do: ", len(todos)) # len() to get the length of the list
            # or you can use (index + 1) but don't do it, just use len()
                
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

            # pop() to remove the item from the list by index number
            todos.pop(number - 1)
            
            # remove() need the value if the item you want to remove
            # todos.remove(item)

            for index, item in enumerate(todos):
                item = item.title()
                
                row = f"{index + 1} => {item}"
                print(row)
                
        case _:
            print('Only type add, show or exit')

print('Bye Bye!')