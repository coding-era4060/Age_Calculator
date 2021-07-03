from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

age_calcy = Tk()
age_calcy.resizable(0, 0)
age_calcy.title('Age Calculator')

frame_1 = Frame(age_calcy)
frame_1.grid(row=0, column=0)

frame_2 = Frame(age_calcy)
frame_2.grid(row=1, column=0)

frame_3 = Frame(age_calcy)
frame_3.grid(row=2, column=0)

year_end = IntVar()
year_start = IntVar()

mon_end = StringVar()
mon_start = StringVar()

day_end = IntVar()
day_start = IntVar()


def calculate():
    date_start = day_start.get()
    month_start = mon_start.get()
    yrs_start = year_start.get()
    date_end = day_end.get()
    month_end = mon_end.get()
    yrs_end = year_end.get()

    no_of_month = 0
    print(date_start, date_end, len(month_start), len(
        month_end), yrs_start, yrs_end)
    if date_start != 0 and date_end != 0 and len(month_start) != 0 and len(
            month_end) != 0 and yrs_start != 0 and yrs_end != 0:
        if yrs_start < yrs_end:
            if month_start == 'Feb' and yrs_start % 4 == 0:
                no_of_days = 29 - date_start + date_end
            elif month_start == 'Feb' and yrs_start % 2 == 0:
                no_of_days = 28 - date_start + date_end
            elif month_start == 'Jan' or month_start == 'Mar' or month_start == 'May' or month_start == 'Jul' or month_start == 'Aug' or month_start == 'Oct' or month_start == 'Dec':
                no_of_days = 31 - date_start + date_end
            elif month_start == month_end and yrs_start == yrs_end:
                no_of_days = date_end - date_start
            else:
                no_of_days = 30 - date_start + date_end

            for index, month in enumerate(mon, 1):
                if month == month_start:
                    no_of_month = 12 - index
            for index, month in enumerate(mon, 1):
                if month == month_end:
                    no_of_month = no_of_month + (index - 1)

            no_of_year = yrs_end - yrs_start - 1
            while no_of_month >= 12 or no_of_days >= 30 or no_of_year < 0:
                if no_of_month >= 12:
                    no_of_year += 1
                    no_of_month -= 12
                if no_of_days >= 30:
                    no_of_days = no_of_days - 30
                    no_of_month += 1
                if no_of_year < 0:
                    no_of_month = 0
                    no_of_year = 0

            result_str = ' '
            if no_of_year != 0:
                result_str = result_str + str(no_of_year) + ' Year '
            if no_of_month != 0:
                result_str = result_str + str(no_of_month) + ' Month '
            if no_of_days != 0:
                result_str = result_str + str(no_of_days) + ' Days '

            result = Label(frame_3, text='Result :- ', font=('bold', 16))
            result.grid(row=0, column=0)

            show_result = Label(frame_3, pady=20, text=result_str, font=('bold', 16))
            show_result.grid(row=0, column=1)
        else:
            messagebox.showerror('ERROR', 'Year of end should bigger than year of start ')
    else:
        messagebox.showerror('ERROR', 'FIELD NOT BE BLANK')


date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        31]
mon = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
       'September', 'October', 'November', 'December']

year = []
for i in range(1920, 2021):
    year.append(i)

top_img = PhotoImage(file=os.path.abspath('age_calculator.png'))
top_img_lbl = ttk.Label(frame_1, image=top_img)
top_img_lbl.grid(row=0, column=0)

lbl_txt = Label(frame_2, text='Date Of Start', padx=15, pady=10, font=('bold', 16))
lbl_txt.grid(row=0, column=0)

date_combobox = ttk.Combobox(frame_2, font=('bold', 16), textvariable=day_start, state='readonly', height=7, width=6,
                             values=date)
date_combobox.grid(row=0, column=1)

mon_combobox = ttk.Combobox(frame_2, font=('bold', 16), textvariable=mon_start, height=7, state='readonly', width=8,
                            values=mon)
mon_combobox.grid(row=0, column=2)

year_lbl = Label(frame_2)
year_lbl.grid(row=0, column=3)

year_combobox = ttk.Combobox(frame_2, font=('bold', 16), textvariable=year_start, height=7, width=6, values=year)
year_combobox.grid(row=0, column=4)

lbl_txt = Label(frame_2, text='Date Of End', font=('bold', 16), padx=15, pady=10)
lbl_txt.grid(row=1, column=0)

date_combobox = ttk.Combobox(frame_2, font=('bold', 16), state='readonly', textvariable=day_end, height=7, width=6,
                             values=date)
date_combobox.grid(row=1, column=1)

mon_combobox = ttk.Combobox(frame_2, font=('bold', 16), state='readonly', textvariable=mon_end, width=8, height=7,
                            values=mon)
mon_combobox.grid(row=1, column=2)

year_combobox = ttk.Combobox(frame_2, font=('bold', 16), textvariable=year_end, width=6, height=7, values=year)
year_combobox.grid(row=1, column=4)

btn_img = PhotoImage(file=os.path.abspath('Continue Button.png'))
calculate_btn = Button(frame_2, image=btn_img, bg="peach puff", text="Calculate", compound=RIGHT, font=('bold', 22),
                       relief='groove', command=calculate)
calculate_btn.grid(row=2, column=2)

age_calcy.mainloop()
