import streamlit as st

import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]

    if new_todo:
        todos.append(new_todo + "\n")
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""


st.title('Simple Todo App')
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

text_input = st.text_input(label="Add new todo", label_visibility="hidden",
                           placeholder="Add new todo...", on_change=add_todo, key="new_todo")
