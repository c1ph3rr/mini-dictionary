import json
from tkinter import *

data = json.load(open('data.json'))

def dictionary():
    word = input1.get()
    if word in data:
        res = data[word]
        if type(res) == list:
            for i in res:
                answer.config(text=i)
        else:
            answer.config(text=res)

    else:
        answer.config(text='Word doesn\'t exist')

root = Tk()
root.title('Mini Dictionary')
root.geometry('400x300')
root.resizable(width=FALSE, height=FALSE)

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label1 = Label(topFrame, text='Enter the word: ')
label1.pack()

input1 = Entry(topFrame)
input1.pack()

button1 = Button(topFrame, text='Search', command=dictionary)
button1.pack()

button2 = Button(bottomFrame, text='Quit',fg='red', command=quit)
button2.pack()

answer = Label(bottomFrame, text='')
answer.pack()

root.mainloop()