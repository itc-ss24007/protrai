# s24007

import tkinter as tk #tkinterをインポートしてtkと略して使う

def dispLabel():
    lbl.config(text="こんにちは")

root = tk.Tk()  #画面を作る
root.geometry("400x200") #画面の大きさを決める(xは半角英数字のエックス)

lbl = tk.Label(text="LABEL",font=("Helvetica",20)) #ラベルを作る
btn = tk.Button(text="PUSH",command=dispLabel,font=("Helvetica",20)) #　ボタンを作る

lbl.pack() #画面にラベルを配置する
btn.pack() #画面にボタンを配置する

lbl2=tk.Label(text="label2").pack()
btn2=tk.Button(text="button2").pack()

tk.mainloop() #作ったWindowを表示する
