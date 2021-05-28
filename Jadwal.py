import calendar
import datetime
import sys
import csv
import tkinter as tk


class Jadwal:

	def __init__(self, parent, values):
		self.values = values
		self.parent = parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY)
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		self.wid = []
		self.day_selected = 1
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = ''
		self.COLOR_OF_CALENDAR_ARROWS = "skyblue"
		self.COLOR_OF_CALENDAR_LABEL = "skyblue"
		self.COLOR_OF_DAY_BUTTONS = "skyblue"
		self.COLOR_OF_APP_DAY_BUTTONS = "red"
		
		self.setup(self.year, self.month)
	
	# Resets the buttons
	def clear(self):
		for w in self.wid[:]:
			w.grid_forget()
			self.wid.remove(w)
	
	# Previous month/year
	def go_prev(self):
		if self.month > 1:
			self.month -= 1
		else:
			self.month = 12
			self.year -= 1
		# self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)
	
	# Next month/year 
	def go_next(self):
		if self.month < 12:
			self.month += 1
		else:
			self.month = 1
			self.year += 1
		
		# self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)
	
	# Called on date button press
	def selection(self, day, name):
		pass
	
	def setup(self, y, m):
		# Calendar
		left = tk.Button(self.parent, text='<', command=self.go_prev,bg=self.COLOR_OF_CALENDAR_ARROWS)
		self.wid.append(left)
		left.grid(row=0, column=1)
		
		header = tk.Label(self.parent, height=2,bg=self.COLOR_OF_CALENDAR_LABEL, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
		self.wid.append(header)
		header.grid(row=0, column=2, columnspan=3)
		
		right = tk.Button(self.parent, text='>', command=self.go_next,bg=self.COLOR_OF_CALENDAR_ARROWS)
		self.wid.append(right)
		right.grid(row=0, column=5)
		
		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		for num, name in enumerate(days):
			t = tk.Label(self.parent, text=name[:3],bg=self.COLOR_OF_CALENDAR_LABEL)
			self.wid.append(t)
			t.grid(row=1, column=num)
		#Read Appointments
		appointments=[]
		bookedDays=[]
		with open("appointments.txt", 'r') as appFile:
			reader = csv.reader(appFile)
			for row in reader:
				# removes empty list
				if len(row) > 0:
					#Check appointments 
					if row[0] in self.values:
						#Uraikan date
						dayInt,monthInt,yearInt = row[1].split("/")
						appointments.append((int(dayInt),int(monthInt),int(yearInt)))
		
		print("appointments:"+str(appointments))
		for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
			for d, day in enumerate(week):
				if day:
					# determine color current calendar
					color = self.COLOR_OF_APP_DAY_BUTTONS if (day, m, y) in appointments else self.COLOR_OF_DAY_BUTTONS
					btn = tk.Button(self.parent, text=day, bg=color,
											command=lambda day=day: self.selection(day, calendar.day_name[(day) % 7]))
					self.wid.append(btn)
					btn.grid(row=w, column=d, sticky='news')
			
			
		
	# Quit calendar
	def kill_and_save(self):
		self.parent.destroy()