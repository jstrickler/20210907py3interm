#!/usr/bin/env python
import os
from calendar import HTMLCalendar
import webbrowser

hcal = HTMLCalendar()  # <1>
formatted_month = hcal.formatmonth(2021, 9)  # <2>

html_file_name = 'sample_calendar.html'

with open(html_file_name, 'w') as calendar_out:
    calendar_out.write(formatted_month)  # <3>
    webbrowser.open("file://" + os.path.realpath(html_file_name))  # <4>
