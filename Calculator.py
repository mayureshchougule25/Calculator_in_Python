from tkinter import *

def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

def equalpress():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set("Error")
		expression = ""

def clear():
	global expression
	expression = ""
	equation.set("")

if __name__ == "__main__":
	gui = Tk()
	gui.title("Simple Calculator")

	expression = ""
	equation = StringVar()

	expression_field = Entry(gui, textvariable=equation, font=("Helvetica", 20))
	expression_field.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

	buttons = [
		'7', '8', '9', '/',
		'4', '5', '6', '*',
		'1', '2', '3', '-',
		'0', '.', '=', '+'
	]

	row_val = 1
	col_val = 0

	for button in buttons:
		Button(gui, text=button, fg='white', bg='gray', font=("Helvetica", 15),
			   command=lambda btn=button: press(btn) if btn != '=' else equalpress(),
			   height=2, width=8 if button == '=' else 4).grid(row=row_val, column=col_val, padx=5, pady=5)
		col_val += 1
		if col_val > 3:
			col_val = 0
			row_val += 1

	Button(gui, text="C", fg='white', bg='red', font=("Helvetica", 15),
		   command=clear, height=2, width=8).grid(row=row_val, column=col_val, padx=5, pady=5)

	gui.mainloop()
