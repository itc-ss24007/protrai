# turtle4.py
# カラフルな花を描く
from turtle import *  #タートルグラフィックを使う準備
shape("turtle") #カメの登場
col=["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
   # forward(100) #　真っ直ぐ１００進むこと
    circle(100)  # 半径１００の円を描くこと
    left(72) # ひだりに72度曲がること
    
done() #　おしまい
