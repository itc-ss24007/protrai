#s24007
"""
dispImage.pyをアレンジして以下の機能を追加してください
ラベル「🎨画像表示アプリ バージョン2.0🎨」を最上部に表示
読み込んだ画像ファイルのパスをシェルに出力(ログ)
読み込んだ画像ファイルのパスをアプリに出力（UI）
↑きれいに見えるようウインドウサイズを調整
実行できたらコメントに学生番号、問題概要を記入してGitHubに提出

ClassroomにはGitHubにUPしたコードのURLを提出してください
"""
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
    
    imagepathlbl.config(text=path)#画像ファイルのパスをアプリに出力（UI）

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath) #画像ファイルのパスをシェルに出力(ログ)
        

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
