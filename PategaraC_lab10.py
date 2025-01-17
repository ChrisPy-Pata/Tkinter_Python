import tkinter as tk # import tk module
from tkinter import messagebox #import messagebox
class Gui: #class Gui, to allow the usage of all the attributes in the class
	def __init__(self, master): # master = window or the root
		#option frame
		menu_frame = tk.Frame(master, bg="#ff8c00") #frame for the menu:Add Item, Remove, Print, Calculate, Cost, Exit

		#add item button
		self.add_item = tk.Button(menu_frame, text= "Add Item", font=("Bold", 15), fg= "black", bd=0, bg="#ff8c00", command=lambda: self.add_page())
		self.add_item.place(x=2, y=50)

		#remove item button
		self.remove_item = tk.Button(menu_frame, text= "Remove", font=("Bold", 15), fg= "black", bd=0, bg="#ff8c00", command=lambda: self.remove_page())
		self.remove_item.place(x=2, y=100)

		#print_all button
		self.print_item = tk.Button(menu_frame, text= "Print", font=("Bold", 15), fg= "black", bd=0, bg="#ff8c00", command=lambda: self.print_page())
		self.print_item.place(x=2, y=150)

		#Calculate button
		self.calculate_item = tk.Button(menu_frame, text= "Calculate", font=("Bold", 15), fg= "black", bd=0, bg="#ff8c00", command=lambda: self.calculate_page())
		self.calculate_item.place(x=2, y=200)

		#exit button
		self.exit_item = tk.Button(menu_frame, text= "Exit", font=("Bold", 15), fg= "black", bd=0, bg="#ff8c00", command=lambda: self.exit_page())
		self.exit_item.place(x=2, y=250)

		# pack the menu_frame
		menu_frame.pack(side=tk.LEFT)
		menu_frame.configure(width= 100, height=350)

		#main frame for each page of our menu
		self.main_frame = tk.Frame(master, background="black", highlightbackground= "gray", highlightthickness=2)
		self.main_frame.pack(side=tk.LEFT)
		self.main_frame.configure(width= 350, height=350)

		#Multiple lists used for: Item, Price, and Quantity 
		self.Itemlist= []
		self.Pricelist = []
		self.Quantitylist = []

	def get_values(self):  #get_values function
		try:  
			self.Itemlist.append(self.Item.get()) #add the inputted Item value entry to the Itemlist
			self.Pricelist.append(self.Price.get()) # add the inputted Price value entry to the Pricelist
			self.Quantitylist.append(self.Quantity.get()) #add the inputted Quantity value entry to the Quantitylist
		except: # if user inputs a invalid(wrong data type value) value,
			messagebox.showinfo("Number Error", "Invalid input!") # a message will popup saying "Invalid input!"
			count = 0 # count variable that has 0 as its value
			for i in self.Itemlist[:]: # for every item in the itemlist,
				if i in self.Item.get(): # we will delete the invalid inputted value to each of the lists of Item, Price, and Quantity
					self.Itemlist.remove(i)
					index = count  #get the index value of the incorrect inputted Item list by setting the value of index to the current number of count
					self.Pricelist.pop(index)
					self.Quantitylist.pop(index)
					break
				count += 1 #each lopp will add +1 to the value of the count variable
			return

	def remove_values(self): #remove_values function
		count = 0  #count variable that has 0 as its value
		for i in self.Itemlist[:]: #for every item in itemlist,
			if i.lower() in self.Remove.get().lower(): #if an item(lowecase in itemlist) is found in the value of remove.get(in lowercase),
				self.Itemlist.remove(i) #the item will be removed in the list
				self.index = count      #get the index value of the remove Item in the itemlist by setting the value of index to the current number of count
				self.Pricelist.pop(self.index) #remove an item in the pricelist that has the same index from the removed item in the itemlist
				self.Quantitylist.pop(self.index) #remove an item in the Quantitylist that has the same index from the removed item in the itemlist
				break #break
			count += 1 #each lopp will add +1 to the value of the count variable

	def print_list(self): #print_list function
		self.lbox = tk.Listbox(self.print_frame, width=10, height=15) #first listbox used to display every item in the Itemlist
		self.lbox.place(x=75, y=90) #listbox 1 coordinates of its position
		self.lbox2 = tk.Listbox(self.print_frame, width=10, height=15)#second listbox used to display every item in the Pricelist
		self.lbox2.place(x=140, y=90) #listbox 2 coordinates of its position
		self.lbox3 = tk.Listbox(self.print_frame, width=10, height=15)#third listbox used to display every item in the Quantitylist
		self.lbox3.place(x=205, y=90) #listbox 3 coordinates of its position
		
		for i in range(len(self.Itemlist)): #for item in the total index in the itemlist,
			self.lbox.insert("end", f'{self.Itemlist[i] : <20}') #insert each item from the Itemlist to the listbox1
			self.lbox2.insert("end",f'{self.Pricelist[i] : <20}') #insert each item from the Pricelist to the listbox2
			self.lbox3.insert("end",f'{self.Quantitylist[i] : <20}') #insert each item from the Quantitylist to the listbox3

	def calculate_list(self): #calculate function
		self.lbox = tk.Listbox(self.calculate_frame, width=10, height=10) #first listbox used to display every item in the Itemlist
		self.lbox.place(x=75, y=90) #listbox 1 coordinates of its position
		self.lbox2 = tk.Listbox(self.calculate_frame, width=10, height=10)#second listbox used to display every item in the Pricelist
		self.lbox2.place(x=140, y=90)#listbox 2 coordinates of its position
		self.lbox3 = tk.Listbox(self.calculate_frame, width=10, height=10)#third listbox used to display every item in the Quantitylist
		self.lbox3.place(x=205, y=90) #listbox 3 coordinates of its position

		for i in range(len(self.Itemlist)):  #for item in the total index in the itemlist,
			self.lbox.insert("end", f'{self.Itemlist[i] : <20}') #insert each item from the Itemlist to the listbox1
			self.lbox2.insert("end",f'{self.Pricelist[i] : <20}')#insert each item from the Pricelist to the listbox2
			self.lbox3.insert("end",f'{self.Quantitylist[i] : <20}')#insert each item from the Quantitylist to the listbox3

		
		grand_total = 0.0 # grand_total variable that has float value of 0.0
		for i in range(len(self.Itemlist)): #for every item in total number of index in Itemlist,
			index = self.Itemlist.index(self.Itemlist[i]) #get the index of every item in Itemlist and store it in the index variable
			unit_price = self.Pricelist[index] #unit_price variable, has a value from every index in Pricelist
			total_price = round(self.Quantitylist[i]*unit_price, 2)  #total price variable, product of every item in Quantitylist and Pricelist and round off to two decimals
			grand_total = grand_total + total_price # the sum of previous grand_total value + total_price

		result = tk.Listbox(self.calculate_frame, width = 45, height = 3, background="#ff8c00") #result variable, listbox used to display the value of grand_total
		result.place(x=40, y=275) #result listbox coordinates of its position

		result.insert("end", "TOTAL COST:" + "  " + str(grand_total)) #insert the string "TOTAL COST:" + the string value of Totality

	def close(self): #close function
		window.destroy() #window will be terminated
		exit() #program will exit

	def add_page(self): #add_page function
		self.delete_pages() #delete the previous data stored before generating new add_page
		add_frame = tk.Frame(self.main_frame, background="black") #frame used to display the multiple widgets in the add_page
		add_frame.configure(width= 350, height=350) #frame coordinates of its position


		self.Addlabel1 = tk.Label(add_frame, text="ADD AN ITEM", bg="black", fg="white", font="none 12 bold").place(x=125, y=10) #label that displays ADD AN ITEM
		self.Addlabel2 = tk.Label(add_frame, text="Give the following information:", bg="black", fg="white", font="none 12 bold").place(x=50, y=50) #label that displays Give the following information:
		self.Addlabel3 = tk.Label(add_frame, text="Name:", bg="black", fg="white", font="none 12 bold").place(x=50, y=100) # label that displays Name:
		self.Item = tk.StringVar() #store the entry String value from addentry1
		self.Addentry1 = tk.Entry(add_frame, textvariable=self.Item, width=10, bg="#ff8c00").place(x= 150, y= 105) # an entry used to input the Name of the product
		self.Addlabel4 = tk.Label(add_frame, text="Price:", bg="black", fg="white", font="none 12 bold").place(x=50, y=150) # label that displays Price:
		self.Price = tk.DoubleVar()  #store the entry Float value from addentry2
		self.Addentry2 = tk.Entry(add_frame, textvariable=self.Price, width=10, bg="#ff8c00").place(x= 150, y= 155) # an entry used to input the Price of the product
		self.Addlabel5 = tk.Label(add_frame, text="Quantity:", bg="black", fg="white", font="none 12 bold").place(x=50, y=200) # label that displays Quantity:
		self.Quantity = tk.IntVar()  #store the entry Integer value from addentry3
		self.Addentry3 = tk.Entry(add_frame, textvariable=self.Quantity, width=10, bg="#ff8c00").place(x= 150, y= 205) # an entry used to input the Quantity of the product
		self.Addbutton1 = tk.Button(add_frame, text="Add Grocery Item", command=lambda: self.get_values(), font="none 12 bold",  bg="white", bd=0).place(x=100, y=255) # Button that displays Add Grocery Item, and call the get_values function

		add_frame.pack() #pack the add_frame

	def remove_page(self): # remove_page function()
		self.delete_pages() #delete the previous data stored before generating new remove_page
		remove_frame = tk.Frame(self.main_frame, background="black") #frame used to display the multiple widgets in the remove_page
		remove_frame.configure(width= 350, height=350) #frame coordinates of its position

		self.Remlabel1 = tk.Label(remove_frame, text="REMOVE AN ITEM", bg="black", fg="white", font="none 12 bold").place(x=100, y=10) # label that displays REMOVE AN ITEM
		self.Remlabel2 = tk.Label(remove_frame, text="What would you like to remove?", bg="black", fg="white", font="none 12 bold").place(x=50, y=50) # label that displays What would you like to remove?
		self.Remlabel3 = tk.Label(remove_frame, text="Item Name:", bg="black", fg="white", font="none 12 bold").place(x=50, y=100) # label that displays Item Name:
		self.Remove = tk.StringVar() #store the entry String value from Rementry1
		self.Rementry1 = tk.Entry(remove_frame, textvariable=self.Remove, width=10, bg="#ff8c00").place(x= 150, y= 105) #an entry used to input the name of the item the user wants to remove
		self.Removebutton1 = tk.Button(remove_frame, text="Remove Grocery Item", command=lambda: self.remove_values(), font="none 12 bold",  bg="white", bd=0).place(x=100, y=150) # button that displays Remove Grocery Item, and call the remove_values function

		remove_frame.pack() # pack the remove_frame

	def print_page(self): # print_page function
		self.delete_pages() #delete the previous data stored before generating new print_page
		self.print_frame = tk.Frame(self.main_frame, background="black") #frame used to display the multiple widgets in print_page
		self.print_frame.configure(width= 350, height=350) #frame coordinates of its position

		self.Prilabel1 = tk.Label(self.print_frame, text="PRINT ENTIRE LIST", bg="black", fg="white", font="none 12 bold").place(x=100, y=10) #label that displays PRINT ENTIRE LIST
		self.Pributton1 = tk.Button(self.print_frame, text="Print Grocery Items", command=lambda: self.print_list(), font="none 12 bold",  bg="white", bd=0).place(x=100, y=50) # button that displays Print Grocery Items, and call the print_list function

		self.print_frame.pack() # pack the print_frame

	def calculate_page(self): #calculate_page function
		self.delete_pages() #delete the previous data stored before generating new calculate_page
		self.calculate_frame = tk.Frame(self.main_frame, background="black") #frame used to display the multiple widgets in calculate_page
		self.calculate_frame.configure(width= 350, height=350) #frame coordinates of its position

		self.Callabel1 = tk.Label(self.calculate_frame, text="CALCULATE COST", bg="black", fg="white", font="none 12 bold").place(x=100, y=10) # label that displays CALCULATE COST
		self.Calbutton1 = tk.Button(self.calculate_frame, text="Calculate total cost", command=lambda: self.calculate_list(), font="none 12 bold",  bg="white", bd=0).place(x=100, y=50) #button that displays Calculate total cost, and call the calculate_list function

		self.calculate_frame.pack() #pack the calculate_frame

	def exit_page(self): # exit_page function
		self.delete_pages() #delete the previous data stored before generating new exit_page
		exit_frame = tk.Frame(self.main_frame, background="black") #frame used to display the multiple widgets in exit_page
		exit_frame.configure(width= 350, height=350) #frame coordinates of its position

		self.extabel1 = tk.Label(exit_frame, text="Do you want to terminate the program?", bg="black", fg="white", font="none 12 bold").place(x=25, y=100) #  label that displays Do you want to terminate the program?
		self.extbutton1 = tk.Button(exit_frame, text="YES",command=lambda: self.close(), font="none 12 bold",  bg="white", bd=0).place(x=100, y=150) # button that displays YES, and call the close function
		self.extbutton2 = tk.Button(exit_frame, text="SURE",command=lambda: self.close(), font="none 12 bold",  bg="white", bd=0).place(x=200, y=150)# # button that displays SURE, and call the close function


		exit_frame.pack() #pack the exit_frame

	def delete_pages(self): #delete the previous data stored before generating new pages
		for frame in self.main_frame.winfo_children(): # for every frame in the main_frame
			frame.destroy() #destroy


#main window
window = tk.Tk() #main root
window.title("Grocery Shopping") #title of the tkinter GUI, Grocery Shopping
window.configure(background="black") #set the window background to black
window.geometry("450x350") #the size of the window/root
window.resizable(False,False) #window can't be resize (max/min)
g = Gui(window) #the class GUI will always pass the window
window.mainloop() #window.mainloop