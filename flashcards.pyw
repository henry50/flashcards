#Flashcard creator
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog

def newFlash(event):
    import newFlash
    newFlash.newFlashCards()

def editFlash(event):
    tkinter.messagebox.showinfo("Edit Flashcards", "Edit Flashcards")
    """
    import editFlash
    editFlash.(function name)
    """
def runFlash(event):
    import runFlash
    runFlash.runFlashCards(True,True)

root = tk.Tk()
root.title("Flashcard creator")
root.geometry("500x250")
root.config(bg = "white")

btnFrm =tk.Frame(root, bg = "white")
btnFrm.pack(expand = True)


titleLab = tk.Label(btnFrm, text="Flashcard maker", font = ("Courier New", "20"), bg = "white")
titleLab.pack(pady = 10, padx = 10)

makeFCBtn = tk.Label(btnFrm, text="Make new flashcards", font = ("Courier New", "15"), bg = "white")
makeFCBtn.pack(pady = 10, fill = "x")

editCurrentBtn = tk.Label(btnFrm, text="Edit existing flashdards", font = ("Courier New", "15"), bg = "white")
editCurrentBtn.pack(pady = 10, fill = "x")

useFCBtn = tk.Label(btnFrm, text="Use flashcards", font = ("Courier New", "15"), bg = "white")
useFCBtn.pack(pady = 10, fill = "x")

#Button bindings
makeFCBtn.bind("<Button-1>", newFlash)
editCurrentBtn.bind("<Button-1>", editFlash)
useFCBtn.bind("<Button-1>", runFlash)

root.mainloop()
