from tkinter import *

window = Tk()  # Creating Window
window.geometry('354x460') # Defining Size
window.title('GUI CALCULATOR')
label = Label(window,text='CALCULATOR',bg='#2C3335',fg='#ffffff',font=('Monotype Corsiva',28,'bold'))
label.pack(side=TOP)
window.config(background = '#2C3335')

text = StringVar()  # Variable to store text.
operator = ''

def button_click(num):
    """
    Takes an operator as input
    attach that operator with text.
    """
    global operator
    operator += str(num)
    text.set(operator)

def equal_button():
    """
    Works on hitting equal button
    evaluate the string passed there
    """
    global operator
    add = str(eval(operator))
    text.set(add)
    operator = ''

def clear_button():
    """
    Works on hitting C Button
    sets the string 'text' as an empty string.
    """
    global operator
    text.set('')
    operator=''

"""
Section of formatting the Texts.
"""

boxtext = Entry(window, font=('Courier New',16,'bold'),textvar = text,width=25,bd=0,bg='#586776',fg='#ffffff')
boxtext.pack()

button_1 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(1),text='1',font=('Arial',16,'bold'))
button_1.place(x=10,y=100)

button_4 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(4),text='4',font=('Arial',16,'bold'))
button_4.place(x=10,y=170)

button_7 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(7),text='7',font=('Arial',16,'bold'))
button_7.place(x=10,y=240)

button_2 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(2),text='2',font=('Arial',16,'bold'))
button_2.place(x=75,y=100)

button_5 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(5),text='5',font=('Arial',16,'bold'))
button_5.place(x=75,y=170)

button_8 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(8),text='8',font=('Arial',16,'bold'))
button_8.place(x=75,y=240)

button_3 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(3),text='3',font=('Arial',16,'bold'))
button_3.place(x=140,y=100)

button_6 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(6),text='6',font=('Arial',16,'bold'))
button_6.place(x=140,y=170)

button_9 = Button(window,padx=17,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(9),text='9',font=('Arial',16,'bold'))
button_9.place(x=140,y=240)

button_0 = Button(window,padx=49,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click(0),text='0',font=('Arial',16,'bold'))
button_0.place(x=10,y=310)

button_dec = Button(window,padx=20,pady=14,bd=4,bg='#758AA2',fg='#ffffff',command=lambda:button_click('.'),text='.',font=('Arial',16,'bold'))
button_dec.place(x=140,y=310)

button_plus = Button(window,padx=17,pady=14,bd=4,bg='#2B2B52',fg='#ffffff',command=lambda:button_click('+'),text='+',font=('Arial',16,'bold'))
button_plus.place(x=205,y=100)

button_sub = Button(window,padx=19,pady=14,bd=4,bg='#2B2B52',fg='#ffffff',command=lambda:button_click('-'),text='-',font=('Arial',16,'bold'))
button_sub.place(x=205,y=170)

button_mul = Button(window,padx=18.5,pady=14,bd=4,bg='#2B2B52',fg='#ffffff',command=lambda:button_click('*'),text='*',font=('Arial',16,'bold'))
button_mul.place(x=205,y=240)

button_div = Button(window,padx=19.5,pady=14,bd=4,bg='#2B2B52',fg='#ffffff',command=lambda:button_click('/'),text='/',font=('Arial',16,'bold'))
button_div.place(x=205,y=310)

button_clear = Button(window,padx=21,pady=119,bd=4,bg='#2B2B52',fg='#ffffff',command=lambda:clear_button(),text='C',font=('Arial',16,'bold'))
button_clear.place(x=270,y=100)

button_equal = Button(window,padx=152,pady=14,bd=4,bg='#2B2B52',fg='#ffffff',command=lambda:equal_button(),text='=',font=('Arial',16,'bold'))
button_equal.place(x=10,y=380)

window.mainloop()