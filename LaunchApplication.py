import subprocess
from subprocess import PIPE
import sys

# def launch(application_path, request):
#     # アプリケーションをバックグラウンドで起動
#     pro = subprocess.Popen(application_path, stdout=subprocess.PIPE)

#     # カウンタ初期値設定
#     cnt = 1
#     # カウンタ上限設定
#     cnt_limit = 10
#     print("アプリケーションにリクエストを送信し、起動確認をします。")
#     print("アプリケーションに" + str(cnt) + "回目のリクエストを送信します。")
#     # アプリケーションが起動するまでリクエストを送信し続けて起動確認
#     while True:
#         try:
#             print("アプリケーションの起動確認中………")
#             request
#             print("起動しました")
#             break
#         except:
#             cnt += 1
#             if cnt > cnt_limit:
#                 print("リクエストの送信回数が" + str(cnt_limit) + "回を超えました。処理の実行を終了します。")
#                 pro.kill() # プロセスを終了
#                 sys.exit()
#             else:
#                 print("アプリケーションに" + str(cnt) + "回目のリクエストを送信します。")
#                 continue
#         # finally:
#         #     print("done")

#     print("done")


# import SpeechSynthesis
# import SoundRecAndPlay as sound

# application = r"COEIROINKのパスを記載"
# request = SpeechSynthesis.speech_synthesis("起動しました")
# launch(application, request)





def launch(application_path):
    pro = subprocess.Popen(application_path, stdout=subprocess.PIPE)
    return pro

application = r"COEIROINKのパスを記載"
pro = launch(application)


import SpeechSynthesis
import SoundRecAndPlay as sound


cnt = 1
cnt_limit = 10
print("アプリケーションにリクエストを送信し、起動確認をします。")
print("アプリケーションに" + str(cnt) + "回目のリクエストを送信します。")

while True:
    try:
        print("アプリケーションの起動確認中………")
        res = SpeechSynthesis.speech_synthesis("起動しました")
        sound.playsound(res)
        print("起動しました")
        break
    except:
        cnt += 1
        if cnt > cnt_limit:
            print("リクエストの送信回数が" + str(cnt_limit) + "回を超えました。処理の実行を終了します。")
            pro.kill() # プロセスを終了
            sys.exit()
        else:
            print("アプリケーションに" + str(cnt) + "回目のリクエストを送信します。")
            continue
    # finally:
    #     print("done")

print("done")
