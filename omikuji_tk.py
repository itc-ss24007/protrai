# s24007
# windowsでおみくじプログラムをつくる
import tkinter as tk

import random
def draw_fortune():
    fortunes = [
        "大吉", "中吉", "小吉", "吉", "末吉", 
        "凶", "大凶", "なし", "再抽選"
    ]
    # ランダムにおみくじの結果を選択

    fortune_result = random.choice(fortunes)
    result_label.config(text=fortune_result)
# ウィンドウの作成
window = tk.Tk()
window.geometry("600x400")
window.title("おみくじ")

# おみくじの結果を表示するラベル
result_label = tk.Label(window, text="", font=("Helvetica", 24))
result_label.pack(pady=20)

# おみくじを引くボタン
draw_button = tk.Button(window, text="おみくじを引く", command=draw_fortune)
draw_button.pack(pady=10)


window.mainloop()
