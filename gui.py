from tkinter import *
from tkinter import ttk
import softwareadjuster

##########################################
##          SoftwareDB GUI              ##
##          Author: Jason Walsh         ##
##                                      ##
##########################################


def generate_report():
	softwareadjuster.main(str(landeskName_entry.get()),landeskOption,str(softwareDBName_entry.get()),softwareDBOption)
	
def set_radio(n0):
	if n0==0:
		set_globvar_landeskOption(0)
	if n0==1:
		set_globvar_landeskOption(1)
	if n0==2:
		set_globvar_landeskOption(2)
	if n0==3:
		set_globvar_softwareDBOption(3)
	if n0==4:
		set_globvar_softwareDBOption(4)
	if n0==5:
		set_globvar_softwareDBOption(5)
		
def set_globvar_landeskName(s0):
	global landeskName
	landeskName = s0

def set_globvar_landeskOption(n0):
	global landeskOption
	landeskOption = n0
	
def set_globvar_softwareDBName(s0):
	global softwareDBName
	softwareDBName = s0

def set_globvar_softwareDBOption(n0):
	global softwareDBOption
	softwareDBOption = n0
	
#MAIN_______________________
root = Tk()
root.title("Software Database Adjuster v1.2")

#setup vars
global landeskName
landeskName=''
global landeskOption
landeskOption= 0 #option 0-Explicit 1-Similar 2-Contains
global softwareDBName
softwareDBName=	''
global softwareDBOption
softwareDBOption=3 #option 0-Explicit 1-Similar 2-Contains

#setup GUI Grid
mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

#LANDesk section
landeskFields = ttk.Labelframe(mainframe,text="LANDesk Name",padding="5 5 5 5")
landeskFields.grid(column=0, row=0, sticky=(N, W, E, S))
landeskName_entry = ttk.Entry(landeskFields, width=50, textvariable=landeskName)
landeskName_entry.grid(column=0, row=1, columnspan=3,sticky=(W, E))
landeskOption_entry0 = ttk.Radiobutton(landeskFields,text='Exact', variable=landeskOption, value=0, command=lambda:set_radio(0))
landeskOption_entry0.grid(column=3, row=3, sticky=(W, E))
landeskOption_entry1 = ttk.Radiobutton(landeskFields,text='Similar', variable=landeskOption, value=1, command=lambda:set_radio(1))
landeskOption_entry1.grid(column=4, row=3, sticky=(W, E))
landeskOption_entry2 = ttk.Radiobutton(landeskFields,text='Contains', variable=landeskOption, value=2, command=lambda:set_radio(2))
landeskOption_entry2.grid(column=5, row=3, sticky=(W, E))


#SoftwareDB section
softwareDBFields = ttk.Labelframe(mainframe,text="SoftwareDB Name",padding="5 5 5 5")
softwareDBFields.grid(column=0, row=1, sticky=(N, W, E, S))
softwareDBName_entry = ttk.Entry(softwareDBFields, width=50, textvariable=softwareDBName)
softwareDBName_entry.grid(column=0, row=4, columnspan=3, sticky=(W, E))
softwareDBName = softwareDBName_entry
softwareDBOption_entry0 = ttk.Radiobutton(softwareDBFields,text='Exact', variable=softwareDBOption, value=3, command=lambda:set_radio(3))
softwareDBOption_entry0.grid(column=3, row=5, sticky=(W, E))
softwareDBOption_entry1 = ttk.Radiobutton(softwareDBFields,text='Similar', variable=softwareDBOption, value=4, command=lambda:set_radio(4))
softwareDBOption_entry1.grid(column=4, row=5, sticky=(W, E))
softwareDBOption_entry2 = ttk.Radiobutton(softwareDBFields,text='Contains', variable=softwareDBOption, value=5, command=lambda:set_radio(5))
softwareDBOption_entry2.grid(column=5, row=5, sticky=(W, E))

test_label = ttk.Label(softwareDBFields, width=50, textvariable=landeskName)
test_label.grid(column=0,row=6)

ttk.Button(mainframe, text="Generate Report", command=generate_report).grid(column=0, row=2, columnspan=3, rowspan=2, sticky=E)

root.bind('<Return>', generate_report)
root.iconbitmap('favicon.ico')
root.mainloop()