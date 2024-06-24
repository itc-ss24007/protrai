# s24007
# 時計アプリ
# 時計アプリをモジュール名time_kadai.pyで作成します

import datetime
import tkinter as tk# GUIでアプリを作ることができるモジュール

# 時間を処理する部分を関数で実装
def update_time():
    now = datetime.datetime.now()
    current_time=now.strftime("%Y年%m月%d日 %H時%M分%S秒")
    lbl.config(text= current_time) #ラベルに現在の時刻を挿入する
    root.after(1000,update_time)　#毎after1000ms自分をもう一回呼び出す1000ミリ秒(millsecond)が1秒に相当する、

# TkinterのWindowを作成
root = tk.Tk() #初めのおまじない(魔法)

root.title("現在の時刻")
#
lbl=tk.Label()
lbl.config(text="",font=("Helvetica",20))#ラベルに文字を挿入する
lbl.pack()

# 関数の呼び出し
update_time()

root.mainloop()
