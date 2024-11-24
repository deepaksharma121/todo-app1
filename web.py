import streamlit as st
import functions

todos = functions.open_todos()

def add_todo():
    todo1 = st.session_state["new_todo"] + "\n"
    todos.append(todo1)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to list all the todo items.")

for index,todo in enumerate(todos):
    check_box = st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label="Enter a new Todo: ",
              placeholder="Add a new Todo",
              on_change=add_todo,
              key="new_todo")





