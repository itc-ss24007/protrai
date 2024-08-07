# s24007
# Flaskの練習

# 事前にflaskモジュールをインストールすると使える
# render_templateはhtmlファイルを扱う際必要
from flask import Flask,render_template

# Flaskライブラリをインスタンス化し、app変数に割り当て
# その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

# ルートurlに対するリクエストを処理する関数を定義するデコレーター
# 引数にルート'/'を指定するとアクセスした際index()関数が呼び出される
@app.route('/')
def index():
    #templates/index.html をあらかじめ作成しておく
    return render_template('index.html')

@app.route('/himitsu')
def himitsu():
    #templates/himitsu.html をあらかじめ作成しておく
    #return render_template('himitsu.html')
    return """
           <h1>秘密のページ</h1>
           <a href="/">ホームページに戻る</a>
           """

if __name__=='__main__':
    # それぞれのユニークなipアドレスでアクセスするように設定
    app.run(host='0.0.0.0',port=5000,debug=True)

# python flask_rensyu2.pyで実行し
#　ブラウザから表示させて
