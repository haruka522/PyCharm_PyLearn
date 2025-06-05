import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    new_todo = st.session_state["new_todo"].strip() + "\n"
    print(new_todo)
    if new_todo:
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo App")
st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a new todo: ", placeholder="Type here...", key="new_todo", on_change=add_todo)

st.session_state