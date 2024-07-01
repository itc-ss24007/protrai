# s24007

import tkinter as tk #tkinterをインポートしてtkと略して使う

root = tk.Tk()  #画面を作る
root.geometry("200x200") #画面の大きさを決める(xは半角英数字のエックス)

lbl = tk.Label(text="LABEL") #ラベルを作る
btn = tk.Button(text="PUSH") #　ボタンを作る

lbl.pack() #画面にラベルを配置する
btn.pack() #画面にボタンを配置する

tk.mainloop() #作ったWindowを表示する
