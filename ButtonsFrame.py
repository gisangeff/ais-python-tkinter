from tkinter import Frame, Button
import InfoFrame, ContentFrame

def setButtonsFrame():
	buttonsFrame = Frame(width="230", height="35", bg="#cc9090")
	buttonsFrame.place(x=10, y=305)

	global btnSave, btnUpdate, btnDelete
	btnSave = Button(buttonsFrame, text="Save", width=11, relief="flat", command=ContentFrame.save)
	btnSave.place(x=8, y=3)

	btnUpdate = Button(buttonsFrame, text="Update", width=11, relief="flat", command=ContentFrame.update)
	btnUpdate.place(x=8, y=3)
	btnUpdate.lower()

	btnDelete = Button(buttonsFrame, text="Delete", width=11, relief="flat", state='disabled', command=ContentFrame.delete)
	btnDelete.place(x=117, y=3)

def showButtonSave(self):
	btnUpdate.lower()
	btnSave.lift()
	btnDelete.config(state='disabled')
	InfoFrame.clearValues()

def showButtonUpdate():
	btnSave.lower()
	btnUpdate.lift()
	btnDelete.config(state='normal')