import FreeSimpleGUI as fsg
import functions
import time

fsg.theme("DarkBrown2")

clock = fsg.Text('' , key='clock')
label = fsg.Text("Type in a to-do")

# if we don't have a key for the input box, it will not be accessible in the event dictionary
input_box = fsg.InputText(size=(40, 1), tooltip="Enter todo", key='todo')

add_button = fsg.Button("Add")

list_box = fsg.Listbox(values=[todo.strip("\n") for todo in functions.get_todos()], size=(40, 10), key='todos', enable_events=True)
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
quit_button = fsg.Button("Quit")

layout = [[clock],[label], [input_box, add_button], [list_box, edit_button, complete_button],[quit_button]]

window = fsg.Window('My To-Do App', layout,
                    font=('Helvetica', 15))

while True:
    event, values = window.read(timeout=1000)
    if event in (fsg.WIN_CLOSED, 'Quit'):
        break
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    print(event)
    print(values)
    # print(values['todos'])

    match event:
        case "Add":
            new_todo = values['todo'].strip() + "\n"
            if not new_todo:
                fsg.popup("Please enter a to-do.", font=('Helvetica', 15))
                continue
            todos = functions.get_todos()
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=[item.strip("\n") for item in todos])
            input_box.update(value="")
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip() + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit +'\n')
                todos[index] = new_todo
                functions.write_todos(todos)
                # you can replace functions.get_todos() with todos
                window['todos'].update(values=[item.strip("\n") for item in todos])
                input_box.update(value="")
            except IndexError:
                fsg.popup("No todo selected to edit.", font=('Helvetica', 15))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete + '\n')
                functions.write_todos(todos)
                window['todos'].update(values=[item.strip("\n") for item in todos])
                input_box.update(value="")
            except IndexError:
                fsg.popup("No todo selected to complete.", font=('Helvetica', 15))


window.close()
