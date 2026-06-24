import streamlit as st
import csv


#==========================
#출처 https://github.com/deepankarvarma/To-Do-List-Using-Python
#기본적인 csv파일을 이용하는 부분 참고
#==========================
# Define the path to the CSV file
CSV_FILE = "tasks.csv"

# Define the main function
def main():
    # Set the title of the web app
    st.title("To-Do List")
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image:url("https://images.pexels.com/photos/3183187/pexels-photo-3183187.jpeg?cs=srgb&dl=pexels-fauxels-3183187.jpg&fm=jpg");
             background-attachment: fixed;
             background-size: cover
             
             color: white; #글자색을 흰색으로 변경
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

    # Load the tasks from the CSV file
    task_list = load_tasks()
#===========================
    # Add a form to input new tasks
    with st.form(key="todo_form",clear_on_submit=True):
        task_input = st.text_input("Enter a new task:")
        submit_button = st.form_submit_button(label = "Add")

    if submit_button:
        if task_input != "":
            # Add the new task to the list and save it to the CSV file
            task_list.append(task_input)
            save_tasks(task_list)
            st.success("할일이 추가되었습니다")

        elif task_input == "":
            st.warning("빈칸은 입력할 수 없습니다 다시 입력해주세요")

    task_list = display(task_list)

    # Add a button to clear the task list
    if st.button("Clear all tasks"):
        # Clear the task list and save the changes to the CSV file
        task_list.clear()
        save_tasks(task_list)
        st.success("모두 삭제되었습니다")  
        st.rerun()
#버튼을 눌러 정상적으로 작동했을때 출력하는 기능구현
#============================
def load_tasks():
    """
    Load the tasks from the CSV file.
    """
    try:
        with open(CSV_FILE, "r") as f:
            reader = csv.reader(f)
            task_list = [row[0] for row in reader]
    except FileNotFoundError:
        task_list = []
    return task_list

def display(task_list):
    # Display the current tasks
    if len(task_list) == 0:
        st.write("No tasks added yet.")
    else:
        st.write("Current tasks:")
        for i, task in enumerate(task_list):
            col1, col2 = st.columns([10, 1])
            with col1:
                st.write(f"{i + 1}. {task}")
            with col2:
                if st.button("X", key=f"delete_{i}"):
                    task_list.pop(i)
                    save_tasks(task_list)
                    st.rerun()

    return task_list
#리스트의 항목을 삭제하는 기능구현
#===========================
def save_tasks(task_list):
    """
    Save the tasks to the CSV file.
    """
    with open(CSV_FILE, "w", newline="") as f:
        f.truncate(0)
        writer = csv.writer(f)
        writer.writerows([[task] for task in task_list])

# Run the app
if __name__ == "__main__":
    main()