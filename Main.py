import tkinter as tk
import csv
import sys
import os.path
from tkinter import messagebox
from Reservasi import Reservasi
from Jadwal import Jadwal

root = tk.Tk()
root.geometry("530x410")
root.title("DKP Sports Center")
root.config(bg='skyblue')
#Var
username = tk.StringVar()
password = tk.StringVar()
name = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()
#Functions
def setup():
	#Make textfiles
	file_exists = os.path.isfile("users.txt")
	if file_exists:
		pass
	else:
		file = open("users.txt", "w+")
		file.close()
	file_exists = os.path.isfile("appointments.txt")
	if file_exists:
		pass
	else:
		file = open("appointments.txt", "w+")
		file.close()
def raiseFrame(frame):
	frame.tkraise()
def moveToReg():
	raiseFrame(regFrame)
def moveToLogin():
	raiseFrame(start)
def moveToBook():
	raiseFrame(bookAppointment)
	# Calendar
def moveToUser():
	raiseFrame(userFrame)
def register():
	entries = []
	with open ("users.txt",'a',newline="") as userFile:
		writer = csv.writer(userFile)
		writeList = [name.get(),username.get(),password.get()]
		writer.writerow(writeList)
		userFile.close()
	#Clear entry boxes
	username.set("")
	password.set("")
	raiseFrame(start)
	
def makeAppointment(jadwalFrame):
	#Format date
	date = str(datePickercalendar.day_selected)+"/"+str(datePickercalendar.month_selected)+"/"+str(datePickercalendar.year_selected)
	#Format time
	minutesString=str(minutes.get())
	if minutes.get()==0:
		minutesString = "00"
	time = str(hours.get())+":"+minutesString
	with open ("appointments.txt",'a',newline="") as appFile:
		writer = csv.writer(appFile)
		writeList = [name.get(),date,time]
		writer.writerow(writeList)
		appFile.close()
	messagebox.showinfo("Success!","Appointment made!")
	jadwalFrame = tk.Frame(userFrame, borderwidth=5, bg="skyblue")
	jadwalFrame.grid(row=2, column=2, columnspan=5)
	viewCalendar = Jadwal(jadwalFrame, {name.get()})
	raiseFrame(userFrame)
	
def login():
	with open("users.txt",'r') as userFile:
		reader = csv.reader(userFile)
		for row in reader:
			#removes empty list 
			if len(row)>0:
				if username.get()==row[1] and password.get()==row[2]:
					print(row[0]+" has logged in!")
					# Calendar View
					global jadwalFrame
					jadwalFrame = tk.Frame(userFrame, borderwidth=5, bg="skyblue")
					jadwalFrame.grid(row=2, column=2, columnspan=5)
					viewCalendar = Jadwal(jadwalFrame, {row[0]})
					name.set(row[0])
					raiseFrame(userFrame)
					
def logOut():
	#Clear Entry boxes
	name.set("")
	username.set("")
	password.set("")
	raiseFrame(start)
#Call setup
setup()
#Define Frame
start = tk.Frame(root)
regFrame = tk.Frame(root)
userFrame = tk.Frame(root)
bookAppointment = tk.Frame(root)
frameList=[start,regFrame,userFrame, bookAppointment]
#Configure all (main) Frames
for frame in frameList:
	frame.grid(row=0,column=0, sticky='news')
	frame.configure(bg='skyblue')
	
#Labels
tk.Label(start,text="DKP Sports Center",font=("Courier", 30),bg='skyblue').grid(row=0,column=2,columnspan=5)
tk.Label(start,text=" ",font=("Courier", 30),bg='skyblue').grid(row=1,column=1)
tk.Label(start,text="Username: ",font=("Courier", 22),bg='skyblue').grid(row=2,column=1,columnspan=2)
tk.Label(start,text=" ",font=("Courier", 3),bg='skyblue').grid(row=3,column=1)
tk.Label(start,text="Password: ",font=("Courier", 22),bg='skyblue').grid(row=4,column=1,columnspan=2)
tk.Label(start,text=" ",font=("Courier", 20),bg='skyblue').grid(row=5,column=1)

tk.Label(regFrame,text="Register",font=("Courier", 30),bg='skyblue').grid(row=0,column=2,columnspan=5)
tk.Label(regFrame,text=" ",font=("Courier", 20),bg='skyblue').grid(row=1,column=1)
tk.Label(regFrame,text="Name    : ",font=("Courier", 22),bg='skyblue').grid(row=2,column=1,columnspan=2)
tk.Label(regFrame,text=" ",font=("Courier", 3),bg='skyblue').grid(row=3,column=1)
tk.Label(regFrame,text="Username: ",font=("Courier", 22),bg='skyblue').grid(row=4,column=1,columnspan=2)
tk.Label(regFrame,text=" ",font=("Courier", 3),bg='skyblue').grid(row=5,column=1)
tk.Label(regFrame,text="Password: ",font=("Courier", 22),bg='skyblue').grid(row=6,column=1,columnspan=2)
tk.Label(regFrame,text=" ",font=("Courier", 20),bg='skyblue').grid(row=7,column=1)

tk.Label(userFrame,text="Booked List",font=("Courier", 30),bg='skyblue').grid(row=1,column=3)
tk.Label(userFrame,text=" ",font=("Courier", 20),bg='skyblue').grid(row=3,column=1)


tk.Label(bookAppointment,text="Book an Appointment",font=("Courier", 30),bg='skyblue').grid(row=1,column=1,columnspan=5)
tk.Label(bookAppointment,text="Select a Date: ",font=("Courier", 18),bg='skyblue').grid(row=2,column=1)
tk.Label(bookAppointment,text="Select a Time: ",font=("Courier", 18),bg='skyblue').grid(row=3,column=1,rowspan=2)

#Entry Boxes
tk.Entry(start,textvariable=username,font=("Courier", 22),bg='lightskyblue').grid(row=2,column=3,columnspan=2)
tk.Entry(start,textvariable=password,font=("Courier", 22),bg='lightskyblue').grid(row=4,column=3,columnspan=2)

tk.Entry(regFrame,textvariable=name,font=("Courier", 22),bg='lightskyblue').grid(row=2,column=3,columnspan=2)
tk.Entry(regFrame,textvariable=username,font=("Courier", 22),bg='lightskyblue').grid(row=4,column=3,columnspan=2)
tk.Entry(regFrame,textvariable=password,font=("Courier", 22),bg='lightskyblue').grid(row=6,column=3,columnspan=2)
#Buttons
tk.Button(start,font=("Courier", 18),bg='deepskyblue',text=" Login ",command=login).grid(row=6,column=4)
tk.Button(start,font=("Courier", 18),bg='deepskyblue',text="Register",command=moveToReg).grid(row=6,column=2)

tk.Button(regFrame,font=("Courier", 18),bg='deepskyblue',text="Register",command=register).grid(row=8,column=4)
tk.Button(regFrame,font=("Courier", 18),bg='deepskyblue',text="Back",command=moveToLogin).grid(row=8,column=2)

tk.Button(userFrame,font=("Courier", 18),bg='deepskyblue',text="Log Out",command=moveToLogin).grid(row=5,column=2)
tk.Button(userFrame,font=("Courier", 18),bg='deepskyblue',text="Book",command=moveToBook).grid(row=5,column=4)

tk.Button(bookAppointment,font=("Courier", 18),bg='deepskyblue',text="Make Appointment",command=lambda :makeAppointment(jadwalFrame)).grid(row=5,column=2)
tk.Button(bookAppointment,font=("Courier", 18),bg='deepskyblue',text="Back",command=moveToUser).grid(row=5,column=1)


#Time Selector
timeSelectFrame = tk.Frame(bookAppointment,borderwidth=5,bg="skyblue")
timeSelectFrame.grid(row=3,column=2)
tk.Spinbox(timeSelectFrame,from_=10, to=22,bg="skyblue",width=2,textvariable=hours).grid(row=1,column=1)
tk.Label(timeSelectFrame,text=":",bg="skyblue").grid(row=1,column=2)
tk.Spinbox(timeSelectFrame,width=2,textvariable=minutes,values=(0,30),bg="skyblue").grid(row=1,column=3)

reservasiFrame = tk.Frame(bookAppointment, borderwidth=5, bg="skyblue")
reservasiFrame.grid(row=2, column=2, columnspan=5)
datePickercalendar = Reservasi(reservasiFrame, {})
#Raise Initial Frame
raiseFrame(start)
root.mainloop()