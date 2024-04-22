import calendar
from tkinter import simpledialog
import datetime

import matplotlib.pyplot as plt
import tkinter as tk
from Table_Events import EventsController



w_days = 'Sun Mon Tue Wed Thu Fri Sat'.split()
m_names = 'January February March April May June July August September October November December'.split()
# Setting Sunday as first day of the week
calendar.setfirstweekday(6)


# Calendar class is used to generate and display monthly calendars with events
class Calendar:
    def __init__(self, year, month):
        self._year = year
        self._month = month
        self.cal = calendar.monthcalendar(year, month)
        self.eventsController = EventsController()

        self.events = [[[] for day in week] for week in self.cal]

    # Function finds the index of a specific day in a month or raises an error if day doesn't exist
    def dayIndex(self, day):
        # index of the day in the list of lists
        for week_n, week in enumerate(self.cal):
            try:
                i = week.index(day)
                return week_n, i
            except ValueError:
                pass
        raise ValueError(f"There are not {day} days in the month")

    # Function formats and generates calendar
    def show(self):
        # Creates a grid w/ number of weeks in the month and 7 columns
        # Values:f - figure name, axs - array of subplots
        f, axs = plt.subplots(len(self.cal), 7, sharex=True, sharey=True)
        # Iterates through each week(ax_row) and each week_day(ax)
        for week, ax_row in enumerate(axs):
            for week_day, ax in enumerate(ax_row):
                # Removes ticks for x-axis and y-axis
                ax.set_xticks([])
                ax.set_yticks([])
                if self.cal[week][week_day] != 0:
                    # Add the number value of the day to the subplot
                    ax.text(.02, .98,
                            str(self.cal[week][week_day]),
                            verticalalignment='top',
                            horizontalalignment='left')
                    # Adds any events to calendar
                    contents = "\n".join(self.events[week][week_day])
                    ax.text(.03, .80, contents,
                            verticalalignment='top',
                            horizontalalignment='left',
                            fontsize=9)

        # Using the titles of the weekdays(w_days) as first row
        for n, day in enumerate(w_days):
            axs[0][n].set_title(day)

        # Adjusting spacing between subplots
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)

        # Adds the month and year titles
        f.suptitle(m_names[self._month - 1] + ' ' + str(self._year),
                   fontsize=20, fontweight='bold')

        #currentEvents = self.eventsController.getMonthEvents(self._month, self._year)
        #self.addMultipleEvents(currentEvents)

        home_button = tk.Button(master=f.canvas.toolbar, text="addEvent", command=self.promptEvent)
        home_button.pack(side=tk.LEFT, padx=10)

        plt.show()


    # Function takes a string(event) and ensure that the date exist and adds to calendar
    def addEvent(self, day, event):
        week, w_day = self.dayIndex(day)
        self.events[week][w_day].append(event)
        plt.close()
        self.show()

    def addMultipleEvents(self, eventList):
        self.events = [[[] for day in week] for week in self.cal]

        for event in eventList:
            name = event[0]
            date = event[1]
            day = date.split('/')[1]
            if day.startswith('0'):
                day = day[1]
            week, w_day = self.dayIndex(int(day))
            self.events[week][w_day].append(name)


    def promptEvent(self):
        name = simpledialog.askstring("Input", "Enter Event Name: ")
        date = simpledialog.askstring("Input", "Enter in Format(MM/DD/YYYY) ")
        self.eventsController.addEventQuery(name, date, 1)
        currentDate = datetime.datetime.now()
        month_events = self.eventsController.getMonthEvents(currentDate.month, currentDate.year)
        self.addMultipleEvents(month_events)
        plt.close()
        self.show()


    def forward_call(self, *args, **kwargs):
        print("forward call")

    def backward_call(self, *args, **kwargs):
        print("backward call")
