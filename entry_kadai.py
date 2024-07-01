#s24007
#エントリーウィジェットで受け付けた金額を税込み価格として出力するプログラムを作成してください

import tkinter as tk

def dispLabel():
    #entryメソッドを使用して入力を受け付けた変数aに格納
    a = int(entry.get())
    #print(f"aは{type(a)}")
    lbl.config(text=f"税込み価格は{a*1.1}")

root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200")

lbl=tk.Label(text="ラベル",font=("Helvetica",20))
entry=tk.Entry(font=("Helvetica",20))
btn=tk.Button(text="ボタン",font=("Helvetica",20),command=dispLabel)

lbl.pack()
entry.pack()
btn.pack()

tk.mainloop()


