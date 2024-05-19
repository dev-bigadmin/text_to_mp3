# text_to_mp3

```bash
❯ mkdir workspace
❯ cd workspace
❯ git clone https://github.com/dev-bigadmin/text_to_mp3.git
'text_to_mp3'에 복제합니다...
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 0), reused 6 (delta 0), pack-reused 0
오브젝트를 받는 중: 100% (6/6), 완료.
❯ cd text_to_mp3
❯ python -m venv venv
❯ source venv/bin/activate
❯ pip install -r ./requirements.txt
Collecting certifi==2024.2.2 (from -r ./requirements.txt (line 1))
  Downloading certifi-2024.2.2-py3-none-any.whl (163 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.8/163.8 kB 1.7 MB/s eta 0:00:00
Collecting charset-normalizer==3.3.2 (from -r ./requirements.txt (line 2))
  Downloading charset_normalizer-3.3.2-cp311-cp311-macosx_11_0_arm64.whl (118 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 119.0/119.0 kB 7.3 MB/s eta 0:00:00
Collecting click==8.1.7 (from -r ./requirements.txt (line 3))
  Downloading click-8.1.7-py3-none-any.whl (97 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.9/97.9 kB 9.0 MB/s eta 0:00:00
Collecting gTTS==2.5.1 (from -r ./requirements.txt (line 4))
  Downloading gTTS-2.5.1-py3-none-any.whl (29 kB)
Collecting idna==3.7 (from -r ./requirements.txt (line 5))
  Downloading idna-3.7-py3-none-any.whl (66 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.8/66.8 kB 5.2 MB/s eta 0:00:00
Collecting pydub==0.25.1 (from -r ./requirements.txt (line 6))
  Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)
Collecting requests==2.31.0 (from -r ./requirements.txt (line 7))
  Using cached requests-2.31.0-py3-none-any.whl (62 kB)
Collecting simpleaudio==1.0.4 (from -r ./requirements.txt (line 8))
  Using cached simpleaudio-1.0.4-cp311-cp311-macosx_13_0_arm64.whl
Collecting urllib3==2.2.1 (from -r ./requirements.txt (line 9))
  Downloading urllib3-2.2.1-py3-none-any.whl (121 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.1/121.1 kB 7.2 MB/s eta 0:00:00
Installing collected packages: simpleaudio, pydub, urllib3, idna, click, charset-normalizer, certifi, requests, gTTS
Successfully installed certifi-2024.2.2 charset-normalizer-3.3.2 click-8.1.7 gTTS-2.5.1 idna-3.7 pydub-0.25.1 requests-2.31.0 simpleaudio-1.0.4 urllib3-2.2.1

[notice] A new release of pip is available: 23.1.2 -> 24.0
[notice] To update, run: pip install --upgrade pip
❯ python text-to-mp3.py
~/workspace/text_to_mp3 on main ··················· took 18s Py text_to_mp3 at 23:01:35
❯
```

---

아래 text 부분과 filename을 수정해서 사용하세요.  

```python
if __name__ == '__main__':
    text = 'All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness: 2 Timothy 3:16'
    filename = '2Timothy3-16.mp3'
    main(text, filename)
```


---

아래와 같이 에러가 발생할 경우는 `brew install ffmpeg` 명령으로 ffmpeg를 설치 해 주세요.  

```bash
Traceback (most recent call last):
  File "/Users/dk/Documents/workspace/gTTS/bibletomp3.py", line 17, in <module>
    speek("All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness")
  File "/Users/dk/Documents/workspace/gTTS/bibletomp3.py", line 13, in speek
    sound = AudioSegment.from_mp3(filename)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/dk/Documents/workspace/gTTS/venv/lib/python3.11/site-packages/pydub/audio_segment.py", line 796, in from_mp3
    return cls.from_file(file, 'mp3', parameters=parameters)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/dk/Documents/workspace/gTTS/venv/lib/python3.11/site-packages/pydub/audio_segment.py", line 728, in from_file
    info = mediainfo_json(orig_file, read_ahead_limit=read_ahead_limit)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/dk/Documents/workspace/gTTS/venv/lib/python3.11/site-packages/pydub/utils.py", line 274, in mediainfo_json
    res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/dk/.pyenv/versions/3.11.4/lib/python3.11/subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/Users/dk/.pyenv/versions/3.11.4/lib/python3.11/subprocess.py", line 1950, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'ffprobe'
```