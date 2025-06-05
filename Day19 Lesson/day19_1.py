import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo App")
st.write("lorem ipsum dolor sit amet, consectetur adipiscing elit.")

for todo in todos:
    st.checkbox(todo)

st.text_input("Enter a new todo: ", placeholder="Type here...", key="new_todo")