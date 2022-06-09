#!/bin/python
from cProfile import label
from cgitb import text
from glob import glob
from pickle import GLOBAL
import tkinter as tk
from tkinter import *
from turtle import done
from timetacking import time_functions, time_list


root = tk.Tk()
root.title("Time Tracking APP")
root.geometry("600x650+450+200")
root.resizable(width=False, height=False)

###Function to save to file###

def save_file(name, string, function):
    file_save = open("Time worked", 'a')
    name = string, function, "\n"
    file_save.writelines(name)
    file_save.close()



###Function to change state of buttons###

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

    def select_edit():
        """Select from listbox for edit"""
        text_frame.delete(0, END)
        text = listbox.get(ANCHOR)
        text_frame.insert(END, text)

    def add_todo():
        """Add edited selection to listbox for save"""
        text_entry = text_frame.get()
        listbox.insert(ACTIVE, text_entry)
        listbox.delete(ACTIVE)
  
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
        window.resizable(width=False, height=False)
        window.title("Wipe log")
        window.config(bg="#3A3A3A")
        test1 = Label(window, text="This will wipe the log file!" + "\n" + "Are you sure?", font="16", fg="white", bg="#3A3A3A").place(x=33, y=9)
        yes = tk.Button(
            window,
            text="Yes",
            fg="white",
            bg="#5239B6",
            bd=0,
            font="16",
            command=lambda: [
                button_options.wipe("Time worked"),
                window.destroy()
            ]
        )
        yes.place(x=19.5, y=60, height=30, width=80)
        no = tk.Button(
            window,
            text="No",
            fg="white",
            bd=0,
            bg="#5239B6",
            font="16",
            command=lambda: [
                window.destroy()
            ]
        )
        no.place(x=138.5, y=60, height=30, width=80)



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
    font="ariel 18",
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


#####\\\\\\\\\\! Stage 1 function buttons !//////////#####

###Button 1 start time###
start_time = tk.Button(
    space,
    text="Start",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        Label_options.show_time_start(),
        button_state(start_time, stop_time),
    ]
)
start_time.place(height=40, width=105, x=56, y=141)

def start_time_place1():
    start_time.place(height=40, width=105, x=56, y=141)

def start_time_place2():
    start_time.place(height=40, width=105, x=11, y=120)

###Button 2 stop time###
stop_time = tk.Button(
    space,
    text="Stop",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        Label_options.show_time_end(),
        button_state(stop_time, start_time)
    ],
    state=DISABLED
)
stop_time.place(height=40, width=105, x=56, y=211)

def stop_time_place1():
    stop_time.place(height=40, width=105, x=56, y=211)

def stop_time_place2():
    stop_time.place(height=40, width=105, x=116, y=120)

###Button 3 show time log###
log_files = tk.Button(
    space,
    text="Time Log",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        start_time_place2(), 
        stop_time_place2(),
        log_files_place1(),
        to_do_place1(),
        completed_place1(),
        edit_log_place1(),
        remove_time_log_place1(),
        clear_log_place1(), 
        main_menu_place(),
        submit_palce(),
        button_options.clear(),
        button_options.time_logged(),
        button_state(log_files, list_to_do),
    ]
)
log_files.place(height=40, width=120, x=56, y=281)

def log_files_place():
    log_files.place(height=40, width=120, x=56, y=281)

def log_files_place1():
    log_files.place(height=40, width=120, x=55, y=187)

###Button 4 show To-Do list###
list_to_do = tk.Button(
    space,
    text="To-Do",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        button_options.clear(),
        button_options.To_do_list(),
        button_state(list_to_do, log_files),
    ]
)

list_to_do.place(height=40, width=120, x=56, y=351)

def to_do_place():
    list_to_do.place(height=40, width=120, x=56, y=351)

def to_do_place1():
    list_to_do.place(height=40, width=120, x=55, y=455)


def to_do_place2():
    list_to_do.place(height=40, width=120, x=56, y=528)



###Button 5 show Completed list###
completed = tk.Button(
    space,
    text="Completed",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [ 
    ]
)
completed.place(height=40, width=120, x=56, y=421)

def completed_place():
    completed.place(height=40, width=120, x=56, y=421)

def completed_place1():
    completed.place(height=40, width=120, x=55, y=522)

def completed_place2():
    completed.place(height=40, width=120, x=56, y=587)



#####\\\\\\\\\\! Stage 2 function buttons will be added when log files is used !//////////#####


###Button 6 select time log to edit###
edit_log = tk.Button(
    space,
    text="Edit",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        button_options.select_edit(),
    ]
)

def edit_log_place1():
    edit_log.place(height=40, width=105, x=11, y=254)

###Button 7 submit edited time log to listbox for save###
submit = tk.Button(
    space,
    text="Submit",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        button_options.add_todo(),
        button_options.save_listbox("Time worked")
    ]
)


def submit_palce():
    submit.place(height=40, width=105, x=117, y=254)


###Button 6 remove from to-do list##
remove_time_log = tk.Button(
    space,
    text="Remove",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        button_options.remove_iteam(),
        button_options.save_listbox("Time worked")
    ]
)


def remove_time_log_place1():
    remove_time_log.place(height=40, width=120, x=55, y=321)


###Button 7 Clear listbox###
clear_log = tk.Button(
    space,
    text="Clear Log",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        pop_ups.open_popup()
    ]
)


def clear_log_place1():
    clear_log.place(height=40, width=120, x=55, y=388)


###Button 12 Edit###
main_menu = tk.Button(
    space,
    text="Main Menu",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        start_time_place1(),
        stop_time_place1(),
        log_files_place(),
        to_do_place(),
        completed_place(),
        button_options.button_gone(edit_log),
        button_options.button_gone(remove_time_log),
        button_options.button_gone(clear_log),
        button_options.button_gone(main_menu),
        button_options.button_gone(submit)
    ]
)
def main_menu_place():
    main_menu.place(height=40, width=120, x=55, y=589)



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
    font="ariel 18",
    command=lambda: [
        button_options.add_list(),
        button_options.save_listbox("To-Do list")
    ]
)


def add_TODO_place1():
    add_TODO.place(height=40, width=120, x=56, y=410)


###Button 9  Clear listbox###
remove_ToDo_list = tk.Button(
    space,
    text="Remove",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [
        button_options.remove_iteam(),
        button_options.save_listbox("To-Do list")
    ]
)


def remove_ToDo_list_place1():
    remove_ToDo_list.place(height=40, width=120, x=56, y=469)


task_done = tk.Button(
    space,
    text="Done",
    padx=10,
    pady=5,
    fg="#F3E0AA",
    bg="#5239B6",
    bd=0,
    font="ariel 18",
    command=lambda: [

    ]

)


def task_done_place1():
    task_done.place(height=40, width=120, x=56, y=528)



### Call Function to show time###
Label_options.show_time()


root.mainloop()
