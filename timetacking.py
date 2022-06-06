import datetime
from datetime import datetime
import time

time_list = []  # list for time punches


class time_functions():

    """All functions for keeping time"""
    def start_stop():
        """start and stop time function appended to list removing milliseconds"""
        x = datetime.now().replace(microsecond=0)
        """Clean good looking time format for show"""
        y = datetime.now().strftime("%a, %b %d, %Y %I:%M:%S %p")
        time_list.append(x)
        return y

    def work_time():
        """Get total time worked function by adding first and second indexed time in list"""
        total_time = time_list[1] - time_list[0]
        return(total_time)

    def show_time():
        new_time = time.strftime("%I:%M:%S %p")
        return  new_time



