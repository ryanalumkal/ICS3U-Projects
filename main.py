# https://www.geeksforgeeks.org/how-to-create-a-frame-inside-a-frame-tkinter/
# https://www.pythontutorial.net/tkinter/tkinter-frame/
# Temp Colour Scheme: https://coolors.co/dcdcdd-c5c3c6-46494c-4c5c68-1985a1

import tkinter as tk

##### FUNCTIONS #####

### Hide Widgets ###
def hide_widgets(*widgets):
	for widget in widgets:
		widget.grid_forget()


### Splash Page ###
def splash_page():
	title_text = tk.Label(main_frame, text="I LOOOOOOVE TKINTER! SUCH A AWESOME PROGRAM HOLY BatChest!", bg="#C5C3C6")
	title_text.grid(row=0, column=0, columnspan=2)
	
	next_page_button = tk.Button(main_frame, text="Click here for next page bozo :yawn:", command=lambda:[hide_widgets(next_page_button, title_text), pg_ques1()])
	next_page_button.grid(row=1, column=0, rowspan=3, columnspan=2)

### Question 1: Display ###
def pg_ques1():
	
	q1_text = tk.Label(main_frame, text="What year of university are you currently in?")
	q1_text.grid(row=0, column=0, columnspan=2)
	
	year_1 = tk.Button(main_frame, text="ModCheck option1", command=lambda:[hide_widgets(q1_text, year_1,year_2, year_3, year_4), pg_ques2()])
	year_1.grid(row=1, column=0)
	
	year_2 = tk.Button(main_frame, text="ModCheck option2", command=lambda:[hide_widgets(q1_text, year_1,year_2, year_3, year_4), pg_ques2()])
	year_2.grid(row=1, column=1)
	
	year_3 = tk.Button(main_frame, text="ModCheck option3", command=lambda:[hide_widgets(q1_text, year_1, year_2, year_3, year_4), pg_ques2()])
	year_3.grid(row=2, column=0)
	
	year_4 = tk.Button(main_frame, text="ModCheck option4", command=lambda:[hide_widgets(q1_text,year_1, year_2, year_3, year_4), pg_ques2()])
	year_4.grid(row=2, column=1)

### Question 2 ###
def pg_ques2():
  test = tk.Label(main_frame, text = "hello")
  test.grid(row=1, column=1)

##### MAIN PROGRAM #####

### Window setup ###
win = tk.Tk()
win.title("Housing Thingy")
win.minsize("600", "400")
win.maxsize("600", "400")

### Creating frames ###
main_frame = tk.Frame(win, bg="white", width="600", height="400")
main_frame.pack()

main_frame.rowconfigure(0, weight=4)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.columnconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)

top_section = tk.Frame(main_frame, bg="#4C5C68", width="600", height="200")
top_section.grid(row=0, column=0, columnspan=3)
bottom_section = tk.Frame(main_frame, bg="#C5C3C6", width="600", height="200")
bottom_section.grid(row=1, column=0, rowspan=3, columnspan=3)

### Display Splash Page ###
splash_page()

### Loop ###
win.mainloop()