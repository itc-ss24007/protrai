# turtle3.py
# カラフルな星を描く
from turtle import *  #タートルグラフィックを使う準備
shape("turtle") #カメの登場
col=["orange","limegreen","gold","plum","tomato"]
for i in range(5):
    color(col[i])
    forward(100) #　真っ直ぐ１００進むこと
    left(144)
    
done() #　おしまい
