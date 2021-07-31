from tkinter import *
from PIL import Image,ImageTk
from datetime import datetime
import requests
import json
import socket
import bs4
from tkinter.messagebox import *
from sqlite3 import *
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt


def f1():
	adst.deiconify()
	root.withdraw()

#----------Validating for each input---------------- 
def validate(event,input):
    if (input == "Roll number"): 
        rno = entrno.get()  
        if (len(rno) < 1 or len(rno) > 2) or rno.isalpha(): 
            showwarning("Invalidate!") 
            entrno.focus_set() 
        else: 
            entname.focus_set() 
            entname.config(state='normal')

    elif (input == "Name"):
        if all(x.isalpha() or x.isspace() for x in entname.get()) and (len(entname.get()) > 1): 
            entmarks.focus_set() 
            entmarks.config(state='normal') 
        else: 
            showwarning("Invalidate!") 
            entname.focus_set()  

    elif (input == "Marks"):
        mark = entmarks.get()   
        if (len(mark)<0 or len(mark)>3) or mark.isalpha() or (int(mark)<0 or int(mark)>100):
            showwarning("Invalidate!") 
            entmarks.focus_set()
        else:
            pass
def f2():
	con=None
	try:
		con=connect("test.db")
		print("YES CONNECTED")
		rno1=int(entrno.get())
		name1=entname.get()
		marks1=int(entmarks.get())
		args=(rno1,name1,marks1)
		cursor=con.cursor()
		sql="insert into student1 values('%d','%s','%d')"
		cursor.execute(sql % args)
		con.commit()
		showinfo("Success")
	except Exception as e:
		showwarning("Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")

def f3():
	root.deiconify()

	adst.withdraw()
def f4():
	stdata.delete(1.0,END)
	vist.deiconify()
	root.withdraw()
	con=None
	try:
		con=connect("test.db")
		print("Connected")
		cursor=con.cursor()
		sql="select*from student1"
		cursor.execute(sql)
		data=cursor.fetchall()
		info=""
		for d in data:
			info=info+"ROLL NO : "+ str(d[0]) +str ("  ") +"NAME : " +str(d[1]) +str("  ") + "MARKS :" +str(d[2]) + "\n"
		stdata.insert(INSERT,info)
	except Exception as e:
		showerror("Issue ", e)
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
				
def f5():
	root.deiconify()
	vist.withdraw()
def f6():
	con=None
	try:
		con=connect("test.db")
		print("Connected")
		rno=int(checkrno.get())
		name=newname.get()
		marks=int(newmarks.get())
		args=(marks,name,rno)
		cursor=con.cursor()
		sql_query="update student1 set marks= '%d', name ='%s' where rno='%d' "
		cursor.execute(sql_query % args)
		if cursor.rowcount >=1:
			con.commit()
			showinfo("Record Updated")
	except Exception as e:
		showerror("Updation Issue -->",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
def f7():
	root.deiconify()
	upst.withdraw()
def f8():
	upst.deiconify()
	root.withdraw()
def f9():
	dest.deiconify()
	root.withdraw()
def f10():
	root.deiconify()
	dest.withdraw()
def f11():
	con=None
	try:
		con=connect("test.db")
		print("Connected")
		rno=int(checkrno2.get())
		args=(rno)
		cursor=con.cursor()
		sql="delete from student1 where rno ='%d' "
		cursor.execute(sql % args)
		if cursor.rowcount >=1:
			con.commit()
			showinfo("Deleted")
		else:
			showerror("Does Not Exist")
	except Exception as e:
		showerror("Issue " ,e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
def f12():
	root.deiconify()
	chst.withdraw()
def f13():
	chst.deiconify()
	root.withdraw()
	con=None
	names=[]
	marks=[]
	try:
		con=connect("test.db")
		print("Connected")
		cursor=con.cursor()
		sql="select*from student1"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			names.append(d[1])
			marks.append(int(d[2]))
		plt.bar(names,marks,color='red',width=0.25)
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.title("Batch Information")
		plt.grid()
		plt.show()
		
	except Exception as e:
		showerror("Issue ", e)
	finally:
		if con is not None:
			con.close()
			print("Disconnected")
				
	
#------------------Creates Main Window-------------------

root=Tk()
root.title("S.M.S")
root.geometry("800x600+300+200")

photo = PhotoImage(file = "C:\\Users\\madhu\\Desktop\\intern-ks\\tsecicon1.png")
root.iconphoto(False, photo)
root.resizable(False,False)

background_image=Image.open("C:\\Users\\madhu\\Desktop\\intern-ks\\img2.jpg")
background_photo=ImageTk.PhotoImage(background_image)
background_label=Label(root,image=background_photo)
background_label.place(relwidth=3.3,relheight=1)

#----------------------Added Buttons---------------------------------

btnadd=Button(root,text="ADD",font=("arial",16,"bold"),command=f1)
btnview=Button(root,text="VIEW",font=("arial",16,"bold"),command=f4)
btnupdate=Button(root,text="UPDATE",font=("arial",16,"bold"),command=f8)
btndelete=Button(root,text="DELETE",font=("arial",16,"bold"),command=f9)
btncharts=Button(root,text="CHARTS",font=("arial",16,"bold"),command=f13)
btnadd.pack(pady=15)
btnview.pack(pady=15)
btnupdate.pack(pady=15)
btndelete.pack(pady=15)
btncharts.pack(pady=15)


#------------------Location Info-----------------------------

lblloc=Label(root,text="Location:",font=("arial",12,"bold"))
lblloc.place(x=50,y=420)
res=requests.get('https://get.geojs.io/')
ip_request=requests.get('https://get.geojs.io/v1/ip.json')
ip_add=ip_request.json()['ip']
url='https://get.geojs.io/v1/ip/geo/'+ip_add+'.json'
geo_request=requests.get(url)
geo_data=geo_request.json()
printgeo=Label(root,text=geo_data['city']+" , " +geo_data['country'],font=("arial",12,"bold"))
printgeo.place(x=130,y=420)


#----------------Temp info------------------------

lbltemp=Label(root,text="Temp:: ",font=("arial",12,"bold"))
lbltemp.place(x=550,y=420)
city =geo_data['city']
a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
a2 = "&q=" + city 
a3 = "&appid=c6e315d09197cec231495138183954bd"
api_address =  a1 + a2  + a3 		
res1 = requests.get(api_address)
data=res1.json()
main=data['main']
temp1=main['temp']
temp2=data['main']['temp']
printtemp=Label(root,text= str(temp2) + "°C" ,font=("arial",12,"bold"))
printtemp.place(x=600,y=420)

#----------------TimeInfo------------------
time_label=Label(root,text="Time: ",font=("arial",10,"bold")) 
time_label.place(x=640,y=560)

time1 = ''
clock = Label(root, font=('arial', 10, 'bold'))
clock.place(x=680,y=560)
 
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)
    
tick()


#--------------QuoteOfTheDay-----------------

lblquote=Label(root,text="Quote Of The Day:", font=("arial",12,"bold"))
lblquote.place(x=50,y=465)

def getQotd():
	res = requests.get('https://quotes.rest/qod?language=en')
	data = res.json()
	print(data['contents']['quotes'][0])
	quote_dict = data['contents']['quotes'][0]
	print(quote_dict['quote'])
	final_quote = quote_dict['quote']
	final_quote = final_quote.replace('.','\n')
	final_quote = final_quote.replace(',','\n')
	return final_quote
           
lblgetQotd = Label(root, text=getQotd(),font=("arial", 12,"bold"))
lblgetQotd.place(x=200,y=465)


#------------------ADD STUDENT WINDOW --------------------

adst=Toplevel(root)
adst.title("ADD STUDENT DETAILS")
adst.geometry("500x500+400+200")
adst.configure(bg="sky blue")
adst.resizable(False,False)
adst.withdraw()

lblrno=Label(adst, text="Enter Roll Number",font=("arial",15,"bold"))
entrno=Entry(adst,bd=5,font=("arial",16,"bold"))
entrno.bind("<Return>", lambda event: validate(event, "Roll number")) 
entrno.bind("<Tab>", lambda event: validate(event, "Roll number")) 


lblname=Label(adst, text="Enter Name ",font=("arial",15,"bold"))
entname=Entry(adst,bd=5,font=("arial",16,"bold"),state='disabled')
entname.bind("<Return>", lambda event: validate(event, "Name")) 
entname.bind("<Tab>", lambda event: validate(event, "Name")) 

lblmarks=Label(adst, text="Enter Marks",font=("arial",15,"bold"))
entmarks=Entry(adst,bd=5,font=("arial",16,"bold"),state='disabled')
entmarks.bind("<Return>", lambda event: validate(event, "Marks")) 
entmarks.bind("<Tab>", lambda event: validate(event, "Marks")) 


btnsave=Button(adst,text="Save",font=("arial",12,"bold"),command=f2)
btnback=Button(adst,text="Back",font=("arial",12,"bold"),command=f3)

lblrno.pack(pady=7)
entrno.pack(pady=7)
lblname.pack(pady=7)
entname.pack(pady=7)
lblmarks.pack(pady=7)
entmarks.pack(pady=7)
btnsave.pack(pady=30)
btnback.pack(pady=7)


#----------------------VIEW WINDOW------------------------
vist=Toplevel(root)
vist.title("View Student")
vist.geometry("700x600+400+200")
vist.configure(bg="sky blue")
vist.resizable(False,False)
vist.withdraw()

stdata=ScrolledText(vist,width=50,height=30)
btnback1=Button(vist,text="Back",font=("arial",12,"bold"),command=f5)

stdata.pack(pady=10)
btnback1.pack(pady=10)


#--------------------UPDATE WINDOW-----------------------
upst=Toplevel(root)
upst.title("Update Student Details")
upst.geometry("700x600+400+200")
upst.configure(bg="sky blue")
upst.resizable(False,False)
upst.withdraw()

enterrno=Label(upst,text="Enter Roll No",font=("arial",15,"bold"))
checkrno=Entry(upst,bd=5,font=("arial",15,"bold"))

entername=Label(upst,text="Enter Name ",font=("arial",15,"bold"))
newname=Entry(upst,bd=5,font=("arial",15,"bold"))

entermarks=Label(upst,text="Enter Marks",font=("arial",15,"bold"))
newmarks=Entry(upst,bd=5,font=("arial",15,"bold"))

btnback2=Button(upst,text="Back",font=("arial",15,"bold"),command=f7)
btnsave2=Button(upst,text="Save",font=("arial",15,"bold"),command=f6)

enterrno.pack(pady=10)
checkrno.pack(pady=10)
entername.pack(pady=10)
newname.pack(pady=10)
entermarks.pack(pady=10)
newmarks.pack(pady=10)
btnback2.pack(pady=10)
btnsave2.pack(pady=10)



#----------------DELETE WINDOW------------------------
dest=Toplevel(root)
dest.title("Delete Student Details")
dest.geometry("700x600+400+200")
dest.configure(bg="sky blue")
dest.resizable(False,False)
dest.withdraw()

entrno2=Label(dest,text="Enter Roll Number" , font=("arial",15,"bold"))
checkrno2=Entry(dest,bd=5,font=("arial",15,"bold"))
btnback3=Button(dest,text="Back",font=("arial",15,"bold"),command=f10)
btnsave3=Button(dest,text="Save",font=("arial",15,"bold"),command=f11)

entrno2.pack(pady=10)
checkrno2.pack(pady=10)
btnback3.pack(pady=10)
btnsave3.pack(pady=10)



#--------------------CHART WINDOW-------------------------
chst=Toplevel(root)
chst.title("Student's Charts")
chst.geometry("700x600+400+200")
chst.configure(bg="sky blue")
chst.resizable(False,False)
chst.withdraw()
btnback3=Button(chst,text="Back",font=("arial",15,"bold"),command=f12)
btnback3.pack(pady=10)



root.mainloop()