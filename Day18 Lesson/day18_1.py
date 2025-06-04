import FreeSimpleGUI as fsg
import functions
import time

label = fsg.Text("Type in a to-do")

# if we don't have a key for the input box, it will not be accessible in the event dictionary
input_box = fsg.InputText(size=(40, 1), tooltip="Enter todo", key='todo')

add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=functions.get_todos(), size=(40, 10), key='todos', enable_events=True)
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
quit_button = fsg.Button("Quit")

layout = [[label], [input_box, add_button], [list_box, edit_button, complete_button],[quit_button]]

window = fsg.Window('My To-Do App', layout,
                    font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)
    # print(values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].strip() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            input_box.update(value="")
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'].strip() + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            # you can replace functions.get_todos() with todos
            window['todos'].update(values=todos)
            input_box.update(value="")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            input_box.update(value="")
        case 'Quit':
            break
        case fsg.WIN_CLOSED:
            break

window.close()
