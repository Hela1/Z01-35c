from tkinter import *
import math
import ast
expression = ""
def input_number(number, equation):
   global expression
   if number == 'pow':
       try:
        result = eval(expression)
        expression = str(result) + "**"
        equation.set(expression)
       except:
        expression = ""
   elif number == 'mod':
       try:
        result = eval(expression)
        result = result%2
        expression = str(result)
        equation.set(expression)
       except:
        expression = ""
   elif number == 'log':
       try:
        result = eval(expression)
        result = math.log10(result)
        expression = str(result)
        equation.set(result)
       except:
        expression = ""
   elif number == 'abs':
       try:
        result = eval(expression)
        result = abs(result)
        equation.set(str(result))
        expression = str(result)
       except:
        expression = ""
   elif number == '1/x':
       try:
        result = eval(expression)
        result = 1/result
        equation.set(str(result))
        expression = str(result)
       except:
        expression = ""
   elif number == 'pow2':
       try:
        result = eval(expression)
        result = result**2
        equation.set(str(result))
        expression = str(result)
       except:
        expression = ""
   elif number == 'sq':
       try:
        result = eval(expression)
        result = math.sqrt(result)
        equation.set(str(result))
        expression = str(result)
       except:
        expression = ""
   else:
       expression = expression + str(number)
       equation.set(expression)


def clear_input_field(equation):
   global expression
   expression = ""
   equation.set("Enter the expression")


def evaluate(equation):
    global expression
    try:
        tree = ast.parse(expression, mode="eval")
        print(ast.dump(tree))
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        expression = ""


def main():
    window = Tk()
    window.title("Calculator")
    window.geometry("500x275")
    equation = StringVar()
    input_field = Entry(window, textvariable=equation)
    input_field.place(height=100)
    input_field.grid(columnspan=6, ipadx=50, ipady=5)
    equation.set("")
    _1 = Button(window, text='1', bd=0,
               command=lambda: input_number(1, equation), height=2, width=7)
    _1.grid(row=2, column=0)
    _2 = Button(window, text='2', bd=0,
               command=lambda: input_number(2, equation), height=2, width=7)
    _2.grid(row=2, column=1)
    _3 = Button(window, text='3', bd=0,
               command=lambda: input_number(3, equation), height=2, width=7)
    _3.grid(row=2, column=2)
    _4 = Button(window, text='4', bd=0,
               command=lambda: input_number(4, equation), height=2, width=7)
    _4.grid(row=3, column=0)
    _5 = Button(window, text='5', bd=0,
               command=lambda: input_number(5, equation), height=2, width=7)
    _5.grid(row=3, column=1)
    _6 = Button(window, text='6', bd=0,
               command=lambda: input_number(6, equation), height=2, width=7)
    _6.grid(row=3, column=2)
    _7 = Button(window, text='7', bd=0,
               command=lambda: input_number(7, equation), height=2, width=7)
    _7.grid(row=4, column=0)
    _8 = Button(window, text='8', bd=0,
               command=lambda: input_number(8, equation), height=2, width=7)
    _8.grid(row=4, column=1)
    _9 = Button(window, text='9', bd=0,
               command=lambda: input_number(9, equation), height=2, width=7)
    _9.grid(row=4, column=2)
    _0 = Button(window, text='0', bd=0,
               command=lambda: input_number(0, equation), height=2, width=7)
    _0.grid(row=5, column=0)
    plus = Button(window, text='+', bd=0,
                 command=lambda: input_number('+', equation), height=2, width=7)
    plus.grid(row=2, column=3)
    minus = Button(window, text='-', bd=0,
                  command=lambda: input_number('-', equation), height=2, width=7)
    minus.grid(row=3, column=3)
    multiply = Button(window, text='*', bd=0,
                     command=lambda:  input_number('*', equation), height=2, width=7)
    multiply.grid(row=4, column=3)
    divide = Button(window, text='/', bd=0,
                   command=lambda: input_number('/', equation), height=2, width=7)
    divide.grid(row=5, column=3)
    equal = Button(window, text='=', bd=0,
                  command=lambda: evaluate(equation), height=2, width=7)
    equal.grid(row=6, column=5)
    clear = Button(window, text='Clear', bd=0,
                  command=lambda: clear_input_field(equation), height=2, width=7)
    clear.grid(row=6, column=6)
    _LeftN = Button(window, text='(', bd=0,
                command=lambda: input_number('(', equation), height=2, width=7)
    _LeftN.grid(row=5, column=1)
    _RightN = Button(window, text=')', bd=0,
                command=lambda: input_number(')', equation), height=2, width=7)
    _RightN.grid(row=5, column=2)
    _abs = Button(window, text='|x|', bd=0,
                       command=lambda: input_number('abs', equation), height=2, width=7)
    _abs.grid(row=4, column=5)
    _pow = Button(window, text='x^y', bd=0,
                command=lambda: input_number('pow', equation), height=2, width=7)
    _pow.grid(row=5, column=5)
    _rev = Button(window, text='1/x', bd=0,
                  command=lambda: input_number('1/x', equation), height=2, width=7)
    _rev.grid(row=2, column=6)
    _log = Button(window, text='log(x)', bd=0,
                command=lambda: input_number('log', equation), height=2, width=7)
    _log.grid(row=3, column=6)
    _mod = Button(window, text='mod(x)', bd=0,
                command=lambda: input_number('mod', equation), height=2, width=7)
    _mod.grid(row=4, column=6)
    _pow2 = Button(window, text='x^2', bd=0,
                  command=lambda: input_number('pow2', equation), height=2, width=7)
    _pow2.grid(row=5, column=6)
    _sq = Button(window, text='sqrt(x)', bd=0,
                   command=lambda: input_number('sq', equation), height=2, width=7)
    _sq.grid(row=3, column=5)
    _dou = Button(window, text='.', bd=0,
                 command=lambda: input_number('.', equation), height=2, width=7)
    _dou.grid(row=2, column=5)
    window.mainloop()
    
if __name__ == '__main__':
    main()
