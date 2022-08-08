from tkinter import *



def button_clicked():
    result = float(input.get()) * 1.609
    format_result = "{:.2f}".format(result)
    result_label.config(text=f"{format_result} km")






window = Tk()
window.title("Measurement Converter")
window.minsize(width=500, height=300)
window.config(pady=100)


#Label 1

my_title = Label(text="Welcome to measurement converter", font=("Arial", 20, "bold"))
my_title.pack()

#Label 2

mile_label = Label(text="Input the miles you want to convert to km", font=("Arial", 14, "normal"))
mile_label.pack()
mile_label.config(pady= 10)

#Entry

input = Entry(width=20)
input.pack()



button = Button(text= "Convert", font=("Arial", 14, "bold"), command=button_clicked)
button.pack()

result_label = Label(text="0", font=("Arial", 40, "bold"))
result_label.pack()
result_label.config(pady=10)









window.mainloop()