import subprocess
from subprocess import PIPE
import sys
import requests

def launch(application_path, url):
    # アプリケーションをバックグラウンドで起動
    process = subprocess.Popen(application_path, stdout=subprocess.PIPE)

    # カウンタ初期値設定
    cnt = 1
    # カウンタ上限設定
    cnt_limit = 10
    print("アプリケーションにリクエストを送信し、起動確認をします。")
    # アプリケーションが起動するまでリクエストを送信し続けて起動確認
    while True:
        try:
            print("アプリケーションに" + str(cnt) + "回目のリクエストを送信します。")
            print("アプリケーションの起動確認中………")
            # POSTで指定URLにリクエストを送信して起動確認
            requests.post(url)
            print("起動しました")
            break
        except:
            cnt += 1
            if cnt > cnt_limit:
                print("リクエストの送信回数が" + str(cnt_limit) + "回を超えました。処理の実行を終了します。")
                # プロセスを終了
                process.kill()
                sys.exit()
            else:
                continue
            
    return process
