import tkinter as tk

root = tk.Tk()
root.title("Calculator Window!")
root.minsize(350, 320)

root.columnconfigure(0, weight =1)
root.columnconfigure(1, weight =1)

for r in range(6):
    root.rowconfigure(r, weight = 1)

#User interface elements
label = tk.Label(root, text = "<Simple Calculator>",font = ("Arial", 12))
label.grid(row = 0, column = 0, columnspan = 2, pady = 15, sticky = 'ew')

label1 = tk.Label(root, text = "First Number: ", font = ("Arial", 11),anchor = "w")
label1.grid(row = 1, column = 0, sticky = "ew", padx = 15, pady = 5)
entry1 = tk.Entry(root, font = ("Arial",11), justify = "left", bd = 2)
entry1.grid(row = 1, column = 1, sticky = 'ew', padx = 15, pady = 5)
entry1.focus()

label2 = tk.Label(root, text = "Second Number: ", font = ("Arial", 11), anchor = "w")
label2.grid(row = 2, column = 0, sticky = "ew", padx = 15, pady = 5)
entry2 = tk.Entry(root, font = ("Arial", 11), bd = 2)
entry2.grid(row = 2, column = 1, sticky = 'ew', padx = 15, pady = 5)

operatelabel = tk.Label(root, text = "Operation: ", font = ("Arial",11), anchor = "w")
operatelabel.grid(row = 3, column = 0, sticky = "ew", padx = 15, pady = 5)

button_frame = tk.Frame(root)
button_frame.grid(row = 3, column=1, sticky = "ew", padx = 15, pady = 5)

for i in range(4):
    button_frame.columnconfigure(i, weight = 1)

#Calculator logic
def calculate(operation):
    result_label.config(bg = root.cget("bg"), anchor = "center")
    try:
        val1 = entry1.get().strip()
        val2 = entry2.get().strip()

        if not val1 or not val2:
            result_label.config(text= "Error: Fields cannot be empty.", fg = "red")
            return
        
        num1 = float(val1)
        num2 = float(val2)

        if operation == "+":
            res = num1 + num2
        elif operation == "-":
            res = num1 - num2
        elif operation == "*":
            res = num1 * num2
        elif operation == "/":
            if num2 == 0:
                result_label.config(text = "Division by Zero is not possible!", fg = "red", )
                return
            res = num1 / num2

        #Floating point precision
        res = round(res, 10)

        if res % 1 == 0:
            res = int(res)

        result_label.config(text= f"Result: {res}", fg = "blue")
    except ValueError:
        result_label.config(text = "Error: Invalid numbers",fg = "red" )

#Buttons for operation
add = tk.Button(button_frame, text = "+", font = ("Arial", 12, "bold"), width = 2, command = lambda: calculate("+"))
add.grid(row = 0, column = 0, padx = 2, sticky = 'ew')

sub = tk.Button(button_frame, text = "-", font = ("Arial", 12, "bold"), width = 2, command = lambda: calculate("-"))
sub.grid(row = 0, column = 1, padx = 2, sticky = 'ew')

mul = tk.Button(button_frame, text = "*", font = ("Arial", 12, "bold"), width = 2, command = lambda: calculate("*"))
mul.grid(row = 0, column = 2, padx = 2, sticky = 'ew')

div = tk.Button(button_frame, text = "/", font = ("Arial", 12, "bold"), width = 2, command = lambda: calculate("/"))
div.grid(row = 0, column = 3, padx = 2, sticky = 'ew')

#result label
result_label = tk.Label(root, text = "Result:", font = ("Arial", 11, "bold"), fg = 'blue', wraplength = 340, justify = "center")
result_label.grid(row = 4, column = 0, columnspan = 2, pady = 15, sticky = 'ew')

#Clear button
def clear():
    entry1.delete(0,tk.END)
    entry2.delete(0,tk.END)
    result_label.config(text = "Result:", fg = "blue", bg = root.cget("bg"))
    entry1.focus()

clrbtn = tk.Button(root, text = "Clear", command = clear, bg = "#c677f7")
clrbtn.grid(row = 5, column = 0, padx = 15, pady = 10, sticky = 'ew')

#Exit button
exitbtn = tk.Button(root, text = "Exit", command = root.destroy, bg = "#ffcccb")
exitbtn.grid(row = 5, column = 1, padx = 15, pady = 10, sticky = 'ew')

root.mainloop()