import pyaudio
import wave

from pydub import AudioSegment
from pydub.playback import play

# 録音データのパスを指定
input_path = ".\input.wav"

# wav形式で録音
def recsound(record_time):
    CHUNK = 2**10
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK
                    )
    
    print(str(record_time) + "秒間録音します。何か話しかけてください。")
    frames = []
    for i in range(0, int(RATE / CHUNK * record_time)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("録音が完了しました。")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open(input_path, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return input_path


# wavの音声を再生(path指定ではない(pathの指定でもいける？))
def playsound(output_wav):
    WIDTH = 2
    CHANNELS = 1
    RATE = 44100

    sound = AudioSegment(output_wav,
                        sample_width=WIDTH, 
                        channels=CHANNELS, 
                        frame_rate=RATE
                        )
    play(sound)
