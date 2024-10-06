from tkinter import *
import math

first_no=second_no=operator=None

def get_digit(digit):
    current=result_label['text']
    new =current + str(digit)
    result_label.config(text=new)

#Function to clear the screen
def clear():
    result_label.config(text='')

#function for backspace
def backspace():
    current = result_label['text']
    result_label.config(text=current[:-1])

def get_operator(op):
    global first_no,operator

    first_no= float(result_label['text'])
    operator= op
    result_label.config(text='')

def get_result():
    global first_no,operator,operator
    second_no= float(result_label['text'])

    if operator=='+':
        result_label.config(text=str(first_no+second_no))
    elif operator=='-':
        result_label.config(text=str(first_no-second_no))
    elif operator=='X':
        result_label.config(text=str(first_no*second_no))
    elif operator=='^':
        result_label.config(text=str(first_no ** second_no))
    elif operator=='%':
        result_label.config(text=str((first_no*second_no)/100))
    else:
        if second_no==0:
            result_label.config(text='Not divisible')
        else:
            result_label.config(text=str(round(first_no/second_no,3)))
    

def get_trigonometry(func):
    num = float(result_label['text'])
    rad = math.radians(num)  # convert to radians for trig functions
    if func == 'sin':
        result_label.config(text=str(round(math.sin(rad), 3)))
    elif func == 'cos':
        result_label.config(text=str(round(math.cos(rad), 3)))
    elif func == 'tan':
        result_label.config(text=str(round(math.tan(rad), 3)))


def get_sqrt():
    num = float(result_label['text'])
    result_label.config(text=str(round(math.sqrt(num), 3)))

def add_decimal():
    current = result_label['text']
    if '.' not in current:
        result_label.config(text=current + '.')



root= Tk()
root.title('Calculator')
root.geometry('300x500')
root.resizable(0,0)
root.configure(background='black')

result_label= Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))

#Button 7
btn7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14,'bold'))

#Button 8
btn8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14,'bold'))

#Button 9
btn9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14,'bold'))

#AC button
btn_clr=Button(root,text='AC',bg='#ff0000',fg='white',width=5,height=2,command=lambda :clear())
btn_clr.grid(row=1,column=3)
btn_clr.config(font=('verdana',14,'bold'))

#Button 4
btn4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14,'bold'))

#Button 5
btn5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14,'bold'))

#Button 6
btn6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14,'bold'))

#one clear
btn_one_remove=Button(root,text='<--',bg='#ff5733',fg='white',width=5,height=2, command=backspace)
btn_one_remove.grid(row=2,column=3)
btn_one_remove.config(font=('verdana',14,'bold'))

#Button 1
btn1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14,'bold'))

#Button 2
btn2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14,'bold'))

#Button 3
btn3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14,'bold'))

#Plus button
btn_plus=Button(root,text='+',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_operator('+') )
btn_plus.grid(row=3,column=3)
btn_plus.config(font=('verdana',14,'bold'))

#Button 0
btn0=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14,'bold'))

#Decimal point
btn_point=Button(root,text='.',bg='#00a65a',fg='white',width=5,height=2,command=add_decimal)
btn_point.grid(row=4,column=0)
btn_point.config(font=('verdana',14,'bold'))

#Button Equal to =
btn_equal=Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',14,'bold'))

#Minus button
btn_minus=Button(root,text='-',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btn_minus.grid(row=4,column=3)
btn_minus.config(font=('verdana',14,'bold'))

#Sin function button
btn_sin=Button(root,text='sin',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_trigonometry('sin'))
btn_sin.grid(row=5,column=0)
btn_sin.config(font=('verdana',14,'bold'))

#cos funtion button
btn_cos=Button(root,text='cos',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_trigonometry('cos'))
btn_cos.grid(row=5,column=1)
btn_cos.config(font=('verdana',14,'bold'))

#tan function button
btn_tan=Button(root,text='tan',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_trigonometry('tan'))
btn_tan.grid(row=5,column=2)
btn_tan.config(font=('verdana',14,'bold'))

#Multiply Button
btn_mul=Button(root,text='X',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_operator('X'))
btn_mul.grid(row=5,column=3)
btn_mul.config(font=('verdana',14,'bold'))

#Percentage button
btn_per=Button(root,text='%',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_operator('%'))
btn_per.grid(row=6,column=0)
btn_per.config(font=('verdana',14,'bold'))

#under root button
btn_sqrt=Button(root,text='√',bg='#d48c06',fg='white',width=5,height=2,command=get_sqrt)
btn_sqrt.grid(row=6,column=1)
btn_sqrt.config(font=('verdana',14,'bold'))

#Power button
btn_pow=Button(root,text='^',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_operator('^'))
btn_pow.grid(row=6,column=2)
btn_pow.config(font=('verdana',14,'bold'))

#Division button
btn_div=Button(root,text='/',bg='#d48c06',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=6,column=3)
btn_div.config(font=('verdana',14,'bold'))



root.mainloop()