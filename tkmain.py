#!/bin/python
import tkinter as tk
from tkinter import *
from timetacking import time_functions, time_list


root = tk.Tk()
root.title("Time Tracking APP")
root.geometry("600x650+450+200")
root.resizable(width=False, height=False)
#root.attributes('-fullscreen', True)

"""Function to save to file"""


def save_file(name, string, function):
    file_save = open("Time worked", 'a')
    name = string, function, "\n"
    file_save.writelines(name)
    file_save.close()



"""Function to change state of buttons"""


def button_state(function1, function2):
    """Switch our state of buttons with each other"""
    function1["state"] = DISABLED
    function2["state"] = NORMAL




####//////////! Class function for labels !\\\\\\\\\\#####
class Label_options():
    """Class functions for the tkinter application GUI"""

    def banner():
        greet = "Welcome to my time tracking app!"
        label = tk.Label(space, text=greet, bg="grey", wraplength=208)
        label.place(x=182, y=20)

    def show_time_start():
        """Function to show start time"""
        x = time_functions.start_stop()
        y = time_functions.show_time()
        start = "Started working: " + y
        start_end_time_label.config(text=start, pady=10)

        """Saving to file new time string"""
        save_file("new_time", "", "")

        """Saving to file time started string"""
        save_file("start_time", "Started: ", x)

    def show_time_end():
        """Print stop time in app"""
        x = time_functions.start_stop()
        y = time_functions.show_time()
        z = str(time_functions.work_time())
        stop = "Stopped working: " + y
        total = "Time worked: " + z
        start_end_time_label["text"] = stop + "\n" + total

        """Saving to file time end string"""
        save_file("time_end", "Stopped: ", x)

        """Saving to file total time string"""
        save_file("total_time", "Total: ", z)
        time_list.clear()


    def show_time():
        """Function to show time"""
        clock_label["text"] = time_functions.show_time()
        show_clock.after(200, Label_options.show_time)

    # def copy_file():
    #    copy = open(,)



####//////////! Class to deal with button options !\\\\\\\\\\#####
class button_options():

    def time_logged():
        """Function to read log file and show in listbox"""
        file_read = open("Time worked", "r")
        lines = file_read.readlines()
        file_read.close()
        for iteam in lines:
            listbox.insert(END, iteam)

    def To_do_list():
        """Function to show To-Do list in listbox"""
        file_read = open("To-Do list", "r")
        lines = file_read.readlines()
        file_read.close()
        for iteam in lines:
            listbox.insert(END, iteam)


    def clear():
        """Function to clear the list box"""
        listbox.delete(0, END)

    def remove_iteam():
        """Function to remove item from list box"""
        listbox.delete(ACTIVE)

    def save_listbox(file_name):
        """Function to save listbox to file after edited"""
        save = open(file_name, "w")
        lines = listbox.get(0, END)
        save.writelines(lines)
        save.close

    def wipe(name):
        """Function to wipe a text file"""
        wipe_file = open(name, 'r+')
        wipe_file.truncate(0)

    def edit():
        """Edit selection in listbox by geting entry from user"""
        #for item in listbox.curselection():
            #text_frame.insert(END, item)
        text = listbox.curselection()
        test2 = listbox.clipboard_get(text)
        text_frame.insert(END, test2)
        #text_entry = text_frame.get()
        #for item in listbox.curselection():
        #    listbox.delete(item)
        #    listbox.insert(text, text_entry + "\n")
    
    def add_list():
        text_entry = text_frame.get()
        listbox.insert(0, text_entry + "\n")
    
    def button_gone(name):
        name.place_forget()
        



#####//////////! Class do deal with any pop up window functions !\\\\\\\\\\#####
class pop_ups():

    def open_popup():
        """Pop up window to confirm wiping log"""
        window = Toplevel(root)
        window.geometry("238x96")
        window.title("Wipe log")
        Label(window, text="Are you sure?",
              font=('ariel 16')).place(x=65, y=17)
        yes = tk.Button(
            window,
            text="Yes",
            fg="#F3E0AA",
            bg="#5239B6",
            font="ariel 16",
            command=lambda: [
                button_options.wipe("Time worked"),
                window.destroy()
            ]
        )
        yes.place(x=12, y=48, height=30, width=80)
        no = tk.Button(
            window,
            text="No",
            fg="#F3E0AA",
            bg="#5239B6",
            font="ariel 16",
            command=lambda: [
                window.destroy()
            ]
        )
        no.place(x=140, y=48, height=30, width=80)

    def Edit_popup():
        """Pop up window to edit log"""
        window = Toplevel(space)
        window.geometry("238x96")
        window.title("Wipe log")
        text_frame = tk.Entry(window, font="ariel 13", )
        text_frame.place(x=232, y=0, height=33, width=368)
        yes = tk.Button(
            window,
            text="Yes",
            fg="#F3E0AA",
            bg="#5239B6",
            font="ariel 16",
            command=lambda: [
                button_options.wipe("Time worked"),
                window.destroy()
            ]
        )
        yes.place(x=12, y=48, height=30, width=80)
        no = tk.Button(
            window,
            text="No",
            fg="#F3E0AA",
            bg="#5239B6",
            font="ariel 16",
            command=lambda: [
                window.destroy()
            ]
        )
        no.place(x=140, y=48, height=30, width=80)


#####//////////! Frames and Canvas for whole app !\\\\\\\\\\#####
#####//////////! Creating canvas to work on !\\\\\\\\\\###
space = tk.Canvas(root, height=650, width=600, bg="#5239B6")  # Create app
space.pack()


#####//////////! Creating frames to post in !\\\\\\\\\\#####
###Frame 1 show time start and end###
time_start_end_frame = tk.Frame(space, bg="#3A3A3A")  # Create frame space in app
time_start_end_frame.place(height=70, width=210, x=11, y=40)

###Frame 2 show clock###
show_clock = tk.Frame(space, bg="#D9D9D9")  # Create frame space in app
show_clock.place(height=32, width=210, x=11, y=8)

###listbox to show information###
listbox = tk.Listbox(space, bg="#3A3A3A",  font=( "ariel 13"), fg="white", bd=0, borderwidth=0, border=0)
listbox.place(height=601, width=360, x=232, y=41)

###Frame 5 text frame###
text_frame = tk.Entry(space, font="ariel 13", bd=0)
text_frame.insert(END, "Text goes here!")
text_frame.place(x=232, y=8, height=33, width=360)




#####//////////! Labels for showing information !\\\\\\\\\\#####
###Label to show clock###
clock_label = tk.Label(
    show_clock,
    bg="#D9D9D9",
    font="ariel 16",
    fg="black"
)
clock_label.pack(pady=5)


###Add scroll bar to listbox###
scrollbar = Scrollbar(listbox)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

###Label to start, end, and total time###
start_end_time_label = tk.Label(
    time_start_end_frame,
    bg="#3A3A3A",
    wraplength=208,
    font=("Times", 16),
    fg="white"
)
start_end_time_label.pack()


#####\\\\\\\\\\! Stage 1 function buttons will never move !//////////#####

###Button 1 start time###


start_time = tk.Button(
    space,
    text="Start Time",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        Label_options.show_time_start(),
        button_state(start_time, stop_time),
    ]
)
start_time.place(height=30, width=100, x=56, y=141)

###Button 2 stop time###
stop_time = tk.Button(
    space,
    text="End Time",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        Label_options.show_time_end(),
        button_state(stop_time, start_time)
    ],
    state=DISABLED
)
stop_time.place(height=30, width=100, x=56, y=211)

###Button 3 show log files###
log_files = tk.Button(
    space,
    text="Time Log",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        button_options.button_gone(completed),
        button_options.button_gone(add_TODO),
        button_options.button_gone(remove2),
        button_options.button_gone(task_done),
        button_options.button_gone(completed1),
        button_options.button_gone(list_to_do),
        place5(), place6(), place7(), place12(), place13(),
        button_options.clear(),
        button_options.time_logged(),
        button_state(log_files, list_to_do),
    ]
)
log_files.place(height=30, width=100, x=56, y=281)

###Button 4 show To-Do list###
list_to_do = tk.Button(
    space,
    text="To-Do",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        button_options.button_gone(edit_log),
        button_options.button_gone(clear_log),
        button_options.button_gone(remove1),
        button_options.button_gone(completed1),
        button_options.clear(),
        button_options.To_do_list(),
        button_state(list_to_do, log_files),
        place8(), place9(), place10(), place11()
    ]
)
list_to_do.place(height=30, width=100, x=56, y=351)

def place14():
    list_to_do.place(height=30, width=100, x=56, y=351)

###Button 12 Edit###
completed1 = tk.Button(
    space,
    text="Completed",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
    ]
)
completed1.place(height=30, width=100, x=56, y=421)

#####\\\\\\\\\\! Stage 2 function buttons will be added when log files is used !//////////#####


###Button 5 Edit###
edit_log = tk.Button(
    space,
    text="Edit",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        button_options.edit(),
        button_options.save_listbox("Time worked")
    ]
)


def place5():
    edit_log.place(height=30, width=100, x=56, y=351)


###Button 6 remove from to-do list##
remove1 = tk.Button(
    space,
    text="Remove",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        button_options.remove_iteam(),
        button_options.save_listbox("Time worked")
    ]
)


def place6():
    remove1.place(height=30, width=100, x=56, y=410)


###Button 7 Clear listbox###
clear_log = tk.Button(
    space,
    text="Clear Log",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        pop_ups.open_popup()
    ]
)


def place7():
    clear_log.place(height=30, width=100, x=56, y=469)


list_to_do1 = tk.Button(
    space,
    text="To-Do",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        button_options.button_gone(edit_log),
        button_options.button_gone(clear_log),
        button_options.button_gone(remove1),
        button_options.button_gone(completed1),
        button_options.clear(),
        button_options.To_do_list(),
        button_state(list_to_do, log_files),
        place8(), place9(), place10(), place11(), place14()
    ]
)


def place12():
    list_to_do.place(height=30, width=100, x=56, y=528)


completed2 = tk.Button(
    space,
    text="Completed",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
    ]
)


def place13():
    completed2.place(height=30, width=100, x=56, y=587)


#####\\\\\\\\\\! Stage 3 function buttons will be added when To Do is used !//////////#####

###Button 8 Clear listbox###
add_TODO = tk.Button(
    space,
    text="Add",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        button_options.add_list(),
        button_options.save_listbox("To-Do list")
    ]
)


def place8():
    add_TODO.place(height=30, width=100, x=56, y=410)


###Button 9  Clear listbox###
remove2 = tk.Button(
    space,
    text="Remove",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
        button_options.remove_iteam(),
        button_options.save_listbox("To-Do list")
    ]
)


def place9():
    remove2.place(height=30, width=100, x=56, y=469)


task_done = tk.Button(
    space,
    text="Done",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [

    ]

)


def place10():
    task_done.place(height=30, width=100, x=56, y=528)


###Button 11 Edit###
completed = tk.Button(
    space,
    text="Completed",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 16",
    command=lambda: [
    ]
)


def place11():
    completed.place(height=30, width=100, x=56, y=587)




### Call Function to show time###
Label_options.show_time()


root.mainloop()
