
user_prompt = 'Type add or show, or exit: '

todos = []

while True:
    user_action = input(user_prompt)
    
    # match case is used to match the value of user_action to the case
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break
        
        # _ is used to match any value that is not matched by the previous cases
        # literally you can use any value here
        case _:
            print('Only type add, show or exit')

print('Bye Bye!')