#s24007
"""

"""
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    # 画像を読み込んでモザイクに変換
    newImage = PIL.Image.open(path).convert("L").\
               resize((32,32)).resize((300, 300))
    
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

    imagepathlbl.config(text=path)    
    #lbl2 = tk.Label(text=path,font=("Helvetica",16))
    #lbl2.pack()

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        #fpathをprint()でシェルに出力
        print(fpath)
        

root = tk.Tk()
root.geometry("400x450")

lbl = tk.Label(text="🎨画像表示アプリ バージョン2.0🎨")
imagepathlbl=tk.Label(text="")
btn = tk.Button(text="ファイルを開く",command = openFile)

imageLabel = tk.Label()
lbl.pack()
btn.pack()
imageLabel.pack()
imagepathlbl.pack()

tk.mainloop()
