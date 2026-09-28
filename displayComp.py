import GenUtilities as gutl
from tkinter import *
def displayComp(title, ListDict):
    ## initialize parent window
    root = Tk()
    root.title(title)

    ## Position parent window using geometry() 
    window_width = 600 
    window_height = 400

    ## get monitor dimensions 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate center-right X and Y Pixel coordinates 
    center_x = int(screen_width/2)
    center_y = int(screen_height/4)

    ## Apply format 
    root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

    rowCount = 0 
    for key, value in ListDict.items():
        row  = gutl.getAsList(ListDict, key)  
        descValue = Label(root, text=row[0])
        value     = Label(root, text=row[1])
        descValue.grid(row=rowCount, padx=20, column=0,sticky=W)
        value.grid(row=rowCount, column=1,sticky=W)

        if len(row) == 3: 
            descValue2 = Label(root, text = row[2]) 
            descValue2.grid(row=rowCount, column =3, sticky=W)

        rowCount += 1

    root.mainloop()

    return 
