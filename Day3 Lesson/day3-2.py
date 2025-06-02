
user_prompt = 'Type add, show, display or exit: '

todos = []

while True:
    user_action = input(user_prompt)
    
    # to remove space after or before the value of user_action
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
            
        # use case to check if the value of user_action is show or display
        case 'show' | 'display':
            
            #use for loop to print out the values in the list of todos
            for item in todos:
                item = item.title()
                print(item)
                
        case 'exit':
            break
        case _:
            print('Only type add, show or exit')

print('Bye Bye!')