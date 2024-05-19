import os

# gTTS (Google Text-to-Speech) 라이브러리는 텍스트를 음성으로 변환하는 데 사용됩니다.
from gtts import gTTS

# pydub 라이브러리는 오디오 파일을 처리하는 데 사용됩니다. 이 경우 mp3 파일을 불러오는 데 사용됩니다.
from pydub import AudioSegment

# pydub.playback 모듈은 오디오 파일을 재생하는 기능을 제공합니다.
from pydub.playback import play


def text_to_mp3(text, filename='voice.mp3'):
    """
    text_to_mp3 함수는 텍스트를 음성으로 변환하여 mp3 파일로 저장하고, 그 파일을 재생하는 기능을 합니다.
    """

    tts = gTTS(text, lang='en') # gTTS 객체를 생성하여 주어진 텍스트를 영어 음성으로 변환합니다.
    tts.save(filename) # 변환된 음성을 mp3 파일로 저장합니다.

    sound = AudioSegment.from_mp3(filename) # 저장된 mp3 파일을 AudioSegment 객체로 불러옵니다.
    play(sound) # 불러온 오디오 파일을 재생합니다.
    # os.remove(filename)


def main(text, filename):
    # 원하는 로직을 추가하세요.
    text_to_mp3(text, filename)


if __name__ == '__main__':
    text = 'All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness: 2 Timothy 3:16'
    filename = '2Timothy3-16.mp3'
    main(text, filename)
