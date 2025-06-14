import FreeSimpleGUI as fsg
import functions
import time

label = fsg.Text("Type in a to-do")

# if we don't have a key for the input box, it will not be accessible in the event dictionary
input_box = fsg.InputText(size=(40, 1), tooltip="Enter todo", key='todo')

add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=functions.get_todos(), size=(40, 10), key='todos', enable_events=True)
edit_button = fsg.Button("Edit")

layout = [[label], [input_box, add_button], [ list_box , edit_button]]

window = fsg.Window('My To-Do App', layout,
                    font=('Helvetica', 15))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].strip()+"\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case fsg.WIN_CLOSED:
            break

window.close()
