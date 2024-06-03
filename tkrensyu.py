# GUIで動くアプリを作ってみるよ

import tkinter as tk # まずこの行を書く必要があるよ

root = tk.Tk() #初めのおまじない

root.geometry("600x400") #windowのサイズを決める
root.title("ハローアプリ")#windowのタイトルを決める

lbl = tk.Label(text="こんにちは世界")
lbl1=tk.Label(text="初めてのGUIアプリ")

lbl.pack() # lblを配置させる必要があるよ
lbl1.pack()

root.mainloop() # 終わりのおまじない
