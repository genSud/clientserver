#!/usr/bin/python
#coding: utf8
import socket
def infixToPostfix(exp):
    stack = []    
    res = []   # <--- тут будет хранится postfix выражение
    #убираем возможные пробелы в строке
    exp = exp.replace(" ", "")
    #инициализируем переменные для цикла
    end = False
    i = 0
    while not end:
        #последовательно берем каждый элемент строки
        c = exp[i]
        x = None
        #если попадается цифра, обрабатываем весь блок
        while c >= '0' and c <='9':
            if x:
                #если много цифр -> получаем число
                x = x*10 + int(c)
            else:
                #если первая цифра, то читаем ее пока числом
                x = int(c)
            i = i + 1
            c = exp[i]
        #если была найдена цифра, то добавляем ее в результат
        if x:
            res.append(x)
         #если попалась скобка, значит нужно добавить в 
         #результат символ операции, который хранится
         #в стеке
        if c == ')':
            res.append(stack.pop())
        if c in ['+','-','/','*']:
            #если попался символ операции в строке,
            #то добавить его в стек   
            stack.append(c)
        i = i + 1
        if i >= len(exp):
            #все элементы строки обработаны -> выход
            end = True
    return res
def summ(a,b):
     return a+b
def sub(a,b):
     return b-a
def mul(a,b):
      return a*b
def div(a,b):
     return b/a
def calcExpression(exp):
    stack = []      
    exp = infixToPostfix(exp)
    #объявляем словарь с функциями
    funcs = {'+':summ,'-':sub,'*':mul,'/':div}
    i = 0
    x = 0
    end = False    
    while not end:
        c = exp[i]
        x = 0
        if c in ['+','-','/','*']:
            #достать два последних числа из стека
            a = stack.pop()
            b = stack.pop()
            #выполнить операцию по ключу С
            x = funcs[c](a,b) 
        else:
            x = float(c)      
        #добавить в стек прочитанное число,
        #или результат операции
        stack.append(x) 
        i = i + 1
        if i >= len(exp):
            end = True
    return x
def main():
    sock = socket.socket()
    sock.bind(('', 1111))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
           break
        x=calcExpression(data)
        conn.send(str(x))
    
if __name__ == "__main__":
    main()
