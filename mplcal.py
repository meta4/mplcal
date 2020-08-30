import calendar
import matplotlib.pyplot as plt

calendar.setfirstweekday(6) # Sunday is 1st day in US
w_days = 'Sun Mon Tue Wed Thu Fri Sat'.split()
m_names = '''
January February March April
May June July August
September October November December'''.split()

class DayNotInMonthError(ValueError):
    pass

class MplCalendar(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.cal = calendar.monthcalendar(year, month)
        # A month of events are stored as a list of lists of list.
        # Nesting, from outer to inner, Week, Day, Event_str
        # Save the events data in the same format
        self.events = [[[] for day in week] for week in self.cal]

    def _monthday_to_index(self, day):
        '''The 2-d index of the day in the list of lists.

        If the day is not in the month raise a DayNotInMonthError,
        which is a subclass of ValueError.

        '''
        for week_n, week in enumerate(self.cal):
            try:
                i = week.index(day)
                return week_n, i
            except ValueError:
                pass
         # couldn't find the day
        raise DayNotInMonth("There aren't {} days in the month".format(day))

    def add_event(self, day, event_str):
        'Add an event string for the specified day'
        week, w_day = self._monthday_to_index(day)
        self.events[week][w_day].append(event_str)

    def _render(self, **kwargs):
        'create the calendar figure'
        plot_defaults = dict(
            sharex=True,
            sharey=True,
            figsize=(11, 8.5),
            dpi=80,
        )
        plot_defaults.update(kwargs)
        f, axs = plt.subplots(
            len(self.cal), 7,
            **plot_defaults
        )
        for week, ax_row in enumerate(axs):
            for week_day, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.cal[week][week_day] != 0:
                    ax.text(.02, .98,
                            str(self.cal[week][week_day]),
                            verticalalignment='top',
                            horizontalalignment='left')
                contents = "\n".join(self.events[week][week_day])
                ax.text(.03, .85, contents,
                        verticalalignment='top',
                        horizontalalignment='left',
                        fontsize=9)

        # use the titles of the first row as the weekdays
        for n, day in enumerate(w_days):
            axs[0][n].set_title(day)

        # Place subplots in a close grid
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        f.suptitle(m_names[self.month-1] + ' ' + str(self.year),
                   fontsize=20, fontweight='bold')

    def show(self, **kwargs):
        'display the calendar'
        self._render(**kwargs)
        plt.show()


    def save(self, filename, **kwargs):
        'save the calendar to the specified image file.'
        self._render(**kwargs)
        plt.savefig(filename)
