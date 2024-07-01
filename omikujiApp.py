# s24007
# 

import tkinter as tk #tkinterをインポートしてtkと略して使う
import random

def dispLabel():
    kuji=["大吉","中吉","小吉","凶","大凶"]
    result=random.choice(kuji)
    lbl.config(text=result)

root = tk.Tk()  #画面を作る
root.geometry("400x200") #画面の大きさを決める(xは半角英数字のエックス)

lbl = tk.Label(text="goodluck",font=("Helvetica",20)) #ラベルを作る
btn = tk.Button(text="抽選",command=dispLabel,font=("Helvetica",20)) #　ボタンを作る

lbl.pack() #画面にラベルを配置する
btn.pack() #画面にボタンを配置する

tk.mainloop() #作ったWindowを表示する
