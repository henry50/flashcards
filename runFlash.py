import tkinter as tk
from tkinter.filedialog import askopenfile
import tkinter.messagebox

cardValues = ["a", 0]
#Binding functions
def nextCardEvt(event):
    nextCard()

#Main functions
def getQandA(ynFile, ynPath):
    global qaList
    qaList = []
    if ynFile == True:
        qaFilePath = tk.filedialog.askopenfilename(title = "Choose Flashcards", filetypes = (("Text Files","*.txt"),))
    elif ynFile == False:
        qaFilePath = ynPath
    qaFileRead = open(qaFilePath, "r")
    global qaFile
    qaFile = qaFileRead.readlines()
    processFile()

def processFile():
    for i in qaFile:
        qaSplit = i.split(";")
        qaList.append([])
        for j in qaSplit:
            qaList[qaFile.index(i)].append(j.strip())

    qaCopyList = qaList[:]
    
    global qaInfo
    global qaData
    qaInfo = qaCopyList[0]
    qaData = qaCopyList[1:]
    
def createGUI(initText):
    root = tk.Tk()
    qaTitleText = qaInfo[1] + " - Flashcards"
    root.title(qaTitleText)
    root.geometry("500x250")
    root.config(bg = "white")

    qFrame = tk.Frame(root, bg = "white")
    qFrame.pack(expand = True)
    global q
    q = tk.Label(qFrame, text=initText, bg = "white", font=("Courier New", "20"), wraplength = 400)
    q.pack(fill = "x")
    root.bind("<Return>", nextCardEvt)
    root.bind("<Button-1>", nextCardEvt)
    root.bind("<space>", nextCardEvt)
    root.bind("<Right>", nextCardEvt)
    root.mainloop()
def startFlash():
    qaDefTxt = qaInfo[1] + "\n" + qaInfo[0] + " questions"
    createGUI(qaDefTxt)
    
#True means display file dialog, false means don't
def runFlashCards(ynFile, ynPath):
    try:
        getQandA(ynFile, ynPath)
        startFlash()
    except IndexError:
        tk.messagebox.showerror("Invalid file", "The file you selected is not a Flashcard Data file")
    except:
        tk.messagebox.showerror("Error", "Error displaying flashcards")
        
def nextCard():
    if cardValues[1] < int(qaInfo[0]):
        if cardValues[0] == "a":
            q.config(text = qaData[cardValues[1]][1])
            cardValues[0] = "q"
        elif cardValues[0] == "q":
            q.config(text = qaData[cardValues[1]][2])
            cardValues[0] = "a"
            cardValues[1] += 1
    else:
        cardValues[1] = 0
        q.config(text = qaInfo[1] + "\n" + qaInfo[0] + " questions")

