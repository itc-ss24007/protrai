#s24007
"""
dispImage.pyをアレンジして以下の機能を追加してください
PIL.Image.open(path)で画像を読み込んだあと、
convert("L")メソッドでグレースケールに変換
rotate(90)メソッドで画像を９０度回転
transpose(PIL.Image.FLIP_LEFT_RIGHT)メソッドで水平方向に反転
resize((300, 300))メソッドで画像サイズを調整

"""
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    # 画像を読み込んでグレースケールに変換,画像を９０度回転,水平方向に反転
    newImage = PIL.Image.open(path).convert("L").\
               rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300, 300))
    
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
