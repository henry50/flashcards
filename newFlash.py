import tkinter as tk
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import os.path
#fcInfoFrm - .pack(expand = True)
def browseForPath():
    fcPathEnt.delete(0, tk.END)
    fcPathEnt.insert(0, tk.filedialog.askdirectory(title = "Choose save location", initialdir = ".."))

def nfRunFlash():
    import runFlash
    runFlash.runFlashCards(False,txtFilePath)
    
def handleButton(hbBtn):
    #Save current card
    getQVal = cnqTxtQ.get("1.0", "end-1c")
    getAVal = cnqTxtA.get("1.0", "end-1c")
    qList[cardInfo[1]] = [getQVal, getAVal]
    #Handle the button request
    if hbBtn == 0:
        cardInfo[0] += 1
        cardInfo[1] += 1
        cardInfo[2] += 1
        qList.insert(cardInfo[1],[])
        canNumber = str(cardInfo[0]) + "/" + str(cardInfo[2])
        createAddNum.config(text= canNumber)
        cnqTxtQ.delete(1.0, tk.END)
        cnqTxtA.delete(1.0, tk.END)
    elif hbBtn == 1:
        if cardInfo[0] == 1:
            False
        else:
            cardInfo[0] -= 1
            cardInfo[1] -= 1
            canNumber = str(cardInfo[0]) + "/" + str(cardInfo[2])
            createAddNum.config(text= canNumber)
            cnqTxtQ.delete(1.0, tk.END)
            cnqTxtA.delete(1.0, tk.END)
            cnqTxtQ.insert(1.0, qList[cardInfo[1]][0])
            cnqTxtA.insert(1.0, qList[cardInfo[1]][1])
    elif hbBtn == 2:
        cardInfo[0] += 1
        cardInfo[1] += 1
        canNumber = str(cardInfo[0]) + "/" + str(cardInfo[2])
        createAddNum.config(text= canNumber)
        cnqTxtQ.delete(1.0, tk.END)
        cnqTxtA.delete(1.0, tk.END)
        cnqTxtQ.insert(1.0, qList[cardInfo[1]][0])
        cnqTxtA.insert(1.0, qList[cardInfo[1]][1])
    elif hbBtn == 3:
        if cardInfo[0] != 1:
            qList.pop(cardInfo[1])
            cardInfo[0] -= 1
            cardInfo[1] -= 1
            cardInfo[2] -= 1
            canNumber = str(cardInfo[0]) + "/" + str(cardInfo[2])
            createAddNum.config(text= canNumber)
            cnqTxtQ.delete(1.0, tk.END)
            cnqTxtA.delete(1.0, tk.END)
            cnqTxtQ.insert(1.0, qList[cardInfo[1]][0])
            cnqTxtA.insert(1.0, qList[cardInfo[1]][1])
        else:
            cnqTxtQ.delete(1.0, tk.END)
            cnqTxtA.delete(1.0, tk.END)
    elif hbBtn == 4:
        finishCont = tk.messagebox.askokcancel("Are you finished?", "Do you want to finish?")
        if finishCont == True:
            iterNumber = 1
            txtFileName =  "".join(scTitle.split()).lower()
            global txtFilePath
            txtFilePath = os.path.join(scFileDir, txtFileName + ".txt")
            writeFile = open(txtFilePath, "w")
            infoLnJoin = [str(cardInfo[2]), scTitle]
            infoLn = ";".join(infoLnJoin) + "\n"
            writeFile.write(infoLn)
            for lines in qList:
                lines.insert(0,str(iterNumber))
                writeFile.write(";".join(lines)+"\n")
                iterNumber += 1
            createFrm.pack_forget()
            scsFrm = tk.Frame(root, bg = "white")
            scsFrm.pack(expand = True)
            scsLab = tk.Label(scsFrm, text = "Flashcards created successfully", font = ("Courier New", "20"), wraplength = 400, bg = "white")
            scsLab.pack()
            scsBtn = tk.Button(scsFrm, text = "Use flashcards", command = nfRunFlash, bg = "white",relief = "solid", font = ("Courier New", "10"))
            scsBtn.pack(pady = 10)
        else:
            False
    else:
        tk.messagebox.showerror("Internal error", "An internal error occured")
    #Check button enable/disable
    if cardInfo[2] != 1:
        createAddPrev.config(state="normal")
    else:
        createAddPrev.config(state="disabled")
    if cardInfo[2] != cardInfo[0]:
        createAddNext.config(state="normal")
    else:
        createAddNext.config(state="disabled")
    
def showCreationFrame():
    global qList, cardInfo, createFrm
    #List of question in format [["question", "answer"],["question", "answer"]]
    qList = [[]]
    #Card number, list index, total cards
    #Only change total cards in add and delete
    cardInfo = [1,0,1]
    #Main question frame
    createFrm = tk.Frame(root, bg = "white")
    createFrm.pack(expand = True)
    
    createTitleLab = tk.Label(createFrm, text = "Create new flashcards", font = ("Courier New", "20"), bg = "white")
    createTitleLab.pack(pady = 10, anchor = "w")

    #Create question entry area
    cnqFrm = tk.Frame(createFrm, bg = "white")
    cnqFrm.pack()

    #Question entry
    cnqLabQ = tk.Label(cnqFrm, text = "Question", bg = "white", font = ("Courier New", "12"))
    cnqLabQ.grid(column = 0, row = 0)
    #Frame for question Text
    cnqTxtQFrm = tk.Frame(cnqFrm, height = 70, width = 150, bg = "white")
    cnqTxtQFrm.grid(column = 0, row = 1, padx = 10)
    cnqTxtQFrm.pack_propagate(False)
    #Question Text
    global cnqTxtQ
    cnqTxtQ = tk.Text(cnqTxtQFrm, relief = "solid", wrap=tk.WORD)
    cnqTxtQ.pack()

    #Answer entry
    cnqLabA = tk.Label(cnqFrm, text = "Answer", bg = "white", font = ("Courier New", "12"))
    cnqLabA.grid(column = 1, row = 0)
    #Frame for answer text
    cnqTxtAFrm = tk.Frame(cnqFrm, height = 70, width = 150, bg = "white")
    cnqTxtAFrm.grid(column = 1, row = 1, padx = 20)
    cnqTxtAFrm.pack_propagate(False)
    #Answer Text
    global cnqTxtA
    cnqTxtA = tk.Text(cnqTxtAFrm, relief = "solid", wrap=tk.WORD)
    cnqTxtA.pack()

    #Controls
    createQFrm = tk.Frame(createFrm, bg = "white")
    createQFrm.pack(pady = 10)
    createCreateBtn = tk.Button(createQFrm, text = "+", bg = "white", relief = "solid", command = lambda: handleButton(0), font = ("Courier New", "10"))
    createCreateBtn.grid(column = 0, row = 0, padx = 10)
    global createAddPrev
    createAddPrev = tk.Button(createQFrm, text = "<", bg = "white", relief = "solid", command = lambda: handleButton(1), state = "disabled", font = ("Courier New", "10"))
    createAddPrev.grid(column = 1, row = 0)
    global createAddNum
    createAddNum = tk.Label(createQFrm, text = "1/1", bg = "white", font = ("Courier New", "10"))
    createAddNum.grid(column = 2, row = 0)
    global createAddNext
    createAddNext = tk.Button(createQFrm, text = ">", bg = "white", relief = "solid", command = lambda: handleButton(2), state = "disabled", font = ("Courier New", "10"))
    createAddNext.grid(column = 3, row = 0)
    createAddBtn = tk.Button(createQFrm, text = "Delete", bg = "white", relief = "solid", command = lambda: handleButton(3), font = ("Courier New", "10"))
    createAddBtn.grid(column = 4, row = 0, pady = 10, padx = 20)
    createFinishBtn = tk.Button(createQFrm, text = "Finish", bg = "white", relief = "solid", command = lambda: handleButton(4), font = ("Courier New", "10"))
    createFinishBtn.grid(column = 5, row = 0)
    
    
def startCreation():
    global scTitle, scFileDir
    if len(fcTitleEnt.get()) != 0 and len(fcPathEnt.get()) and os.path.exists(fcPathEnt.get()):
        scTitle = fcTitleEnt.get()
        scFileDir = fcPathEnt.get()
        fcInfoFrm.pack_forget()
        showCreationFrame()
    else:
        tk.messagebox.showerror("Error", "Fill in all fields")

def createGUI():
    global fcInfoFrm, fcTitleEnt, fcPathEnt, root
    root = tk.Tk()
    root.title("Flashcard creator")
    root.geometry("500x250")
    root.config(bg = "white")
    root.lift()
    
    fcInfoFrm = tk.Frame(root, bg = "white")
    fcInfoFrm.pack(expand = True)

    fcCreateLab = tk.Label(fcInfoFrm, text = "Create new flashcards", font = ("Courier New", "20"), bg = "white")
    fcCreateLab.pack(pady = 10, anchor = "w")

    fcTitleLab = tk.Label(fcInfoFrm, text="Title", bg = "white", font = ("Courier New", "10"))
    fcTitleLab.pack(anchor = "w")
    fcTitleEnt = tk.Entry(fcInfoFrm, width = 40, relief = "solid", font = ("Courier New", "10"))
    fcTitleEnt.pack(pady = (0,10), anchor = "w")

    fcPathFrm = tk.Frame(fcInfoFrm, bg = "white")
    fcPathFrm.pack(anchor = "w")
    fcPathLab = tk.Label(fcPathFrm, text="Save location", bg = "white", highlightthickness=0, font = ("Courier New", "10"))
    fcPathLab.grid(row = 0, column = 0, sticky = "w")
    fcPathEnt = tk.Entry(fcPathFrm, width = 40, relief = "solid", font = ("Courier New", "10"))
    fcPathEnt.grid(row = 1, column = 0, pady = (0, 10))
    fcPathBtn = tk.Button(fcPathFrm, text = "Browse...", command = browseForPath, relief = "solid", bg = "white", font = ("Courier New", "8"))
    fcPathBtn.grid(row = 1, column = 1, pady = (0,10), padx = (10,0))

    fcNextBtn = tk.Button(fcInfoFrm, text = "Next >", command = startCreation, font = ("Courier New", "8"), relief = "solid", bg = "white")
    fcNextBtn.pack(pady = 10, anchor = "w")
    root.mainloop()

def newFlashCards():
    createGUI()
