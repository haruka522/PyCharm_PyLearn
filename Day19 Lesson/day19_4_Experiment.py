import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    raw_input = st.session_state["new_todo"].strip()
    print(raw_input)
    if raw_input:
        new_todo = raw_input + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""

st.set_page_config(page_title="My Todo App", layout="wide")

st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your <strong>productivity</strong>.", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    # &nbsp; is a non-breaking space, cuz using a normal space would break the layout of checkboxes in streamlit
    checkbox = st.checkbox(f"{index+1}.&nbsp;{todo}", key=todo)
    if checkbox:
        print(index)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        # if there is no st.rerun(), we'll need to manually refresh the page to see the result
        st.rerun()

st.text_input(label="Enter a new todo: ", placeholder="Type here...", key="new_todo", on_change=add_todo)

print(st.session_state)

# print statements are just to check if the code is working properly