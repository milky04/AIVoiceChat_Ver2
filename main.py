import LaunchApplication
import SoundRecAndPlay as sound
import ConvertVoiceToText
import GenerateText
import SpeechSynthesis
import os

def main():
    try:
        print("処理を開始します。終了する際はターミナルに「Ctrl+C」を入力してください。")
        # アプリケーションの起動
        process = LaunchApplication.launch(application, url)
        while True:
            # 録音データのパスと録音時間を指定して録音
            input_sound = sound.recsound(record_time)
            # input_soundに保存された録音データをConvertVoiceToTextでテキストに変換
            input_text = ConvertVoiceToText.convert_voice_to_text(input_sound)
            # 録音データ削除
            os.remove(input_sound)
            # input_textをGenerateTextに投げて生成された文章を受け取る
            result_text = GenerateText.generate_text(input_text)
            print("AI:" + result_text)
            # result_textをSpeechSynthesisに与えて音声合成のwavを生成
            response = SpeechSynthesis.speech_synthesis(result_text)
            # responseを再生
            sound.playsound(response)
    except KeyboardInterrupt:
        # プロセスを終了
        process.kill()
        print("処理を終了しました。")


# COEIROINKのパスとローカルAPIのURLを指定
application = r"COEIROINKのパスを記載"
url = "http://localhost:50031/"

# 録音時間を指定
record_time = 5

if __name__ == '__main__':
    main()
