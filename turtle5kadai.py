# turtle5.py
# 六角形を描く
from turtle import *  #タートルグラフィックを使う準備
shape("turtle") #カメの登場
col=["orange","limegreen","gold","plum","tomato","red"]
for i in range(6):
    color(col[i])
    forward(100) #　真っ直ぐ１００進むこと
   # circle(80)  # 半径１００の円を描くこと
    left(60) # ひだりに60度曲がること
    
done() #　おしまい
