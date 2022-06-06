#task = []
import pickle
from pickle import *

tasks = [
]

class to_do():


    def task_text():
        """Add new task as dictionary to the task list."""
        new_task = {'name':input("What task would you like to add: "), 'completed': False}
        tasks.append(new_task)
        #new_task = "Name" + str(input("What task would you like to add: "))  +" " + "Completed" + " " + str(False) + "\n"
        with open('list', 'wb') as f:
            pickle.dump(tasks, f)
        #save_file = open("ShowList", "a")
        #save_file.writelines(str(tasks))
        #save_file.close()


    def show():
        #file_read = open("ShowList", "r")
        #lines = file_read.read()
        #file_read.close
        #return lines
        with open('list', 'rb') as f:
            add_list = pickle.load(f)
        return add_list


    def remove_task():
        """Select tasks in list by index number and remove task."""
        del tasks[int(input('Task number to remove: '))]


    def completed_task():
        """Select tasks in list by index number then select key completed and change the value to true."""
        tasks[int(input('Task number you would like to complete: '))]['completed'] = True


    def unmark_task():
        """Select tasks in list by index number then select key completed and change the value to false."""
        tasks[int(input('Task number you would like to complete: '))]['completed'] = False

    def time_logged():
        """Function to read log file and show in listbox"""
        file_read = open("To-Do", "r")
        #lines = file_read.read()
        lines = file_read.readlines()
        file_read.close()
        #for iteam in lines:
        #listbox.insert(END, iteam)
        print(lines)


#tryThis = show()

#x = to_do.show()

#print(x[0]['name'])

#to_do.task_text()

#x = to_do.show()

#print(x)

#print(tasks)



