import sklearn.datasets

digits = sklearn.datasets.load_digits()

print("データの個数=",len(digits.images))
print("画像データ=",digits.images[1796])
print("何の数字か=",digits.target[1796])
