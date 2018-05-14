from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Chatter")

mainFrame = ttk.Frame(root, width = 800, height = 600)
mainFrame.grid(column=0, row=0)

demoChatter = "Cthon98: hey, if you type in your pw, it will show as stars\n\
Cthon98: ********* see!\n\
AzureDiamond: hunter2\n\
AzureDiamond: doesnt look like stars to me\n\
Cthon98> <AzureDiamond: *******\n\
Cthon98: thats what I see\n\
AzureDiamond: oh, really?\n\
Cthon98: Absolutely\n\
AzureDiamond: you can go hunter2 my hunter2-ing hunter2\n\
AzureDiamond: haha, does that look funny to you?\n\
Cthon98: lol, yes. See, when YOU type hunter2, it shows to us as *******\n\
AzureDiamond: thats neat, I didnt know IRC did that\n\
Cthon98: yep, no matter how many times you type hunter2, it will show to us as *******\n\
AzureDiamond: awesome!\n\
AzureDiamond: wait, how do you know my pw?\n\
Cthon98: er, I just copy pasted YOUR ******'s and it appears to YOU as hunter2 cause its your pw\n\
AzureDiamond: oh, ok."

textBox = Text(mainFrame, width = 80, height = 20)
textBox.grid(column=0, row=0)
textBox.insert(0.0, demoChatter)

scrollbar = ttk.Scrollbar(mainFrame, orient=VERTICAL, command=textBox.yview)
scrollbar.grid(column=1, row=0, sticky = (N, S))

textBox['yscrollcommand'] = scrollbar.set

name_list = ['AzureDiamond', 'Cthon98']
names = StringVar(value = name_list)

listBox = Listbox(mainFrame, listvariable = names)
listBox.grid(column=2, row=0, sticky = (N, S))

message = StringVar()
messageEntry = ttk.Entry(mainFrame, textvariable = message)
messageEntry.grid(column=0, row=2, sticky = (E, W))

sendButton = ttk.Button(mainFrame, text = 'Send')
sendButton.grid(column=1, row=2, columnspan=2, sticky = W)

root.mainloop()