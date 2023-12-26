# time_speaker
설정한 키워드를 음성으로 인식하면 현재 시간을 스피커로 출력하는 프로그램입니다./This program outputs the current time through the speaker when the set keyword is recognized by voice.

# How_It_Works
speech_recognition 라이브러리로 음성을 녹음해서 audio 변수로 저장한 뒤, Google Speech_to_Text API를 사용하여 audio를 텍스트로 변환한 후 키워드 포함 여부를 판독한다. 키워드가 포함될 시 datetime 라이브러리로 현재 시간을 불러들이고 pyttsx3 라이브러리로 현재시간을 스피커로 출력하는 원리이다./ Record the voice with the speech_recognition library and save it as an audio variable, then convert the audio to text using the Google Speech_to_Text API and read whether it contains keywords. The principle is that when a keyword is included, the current time is loaded into the datetime library and the current time is output to the speaker using the pyttsx3 library.

# How_to_Use
1. Google Cloud Flatform에 접속하여 Speech_to_Text API의 API 키를 발급받으세요./Access Google Cloud Flatform to obtain an API key for the Speech_to_Text API.
2. ver~.py 파일에서 path/to/your/credentials.json 부분을 본인의 API키로 대체하세요./In the ver~.py file, replace path/to/your/credentials.json with your API key.
3. 필요하다면 ver~.py 파일에서 키워드를 변경하세요./Change keywords in the ver~.py file if necessary.

# Tips
한국어, 영어 버전이 존재합니다. 각각 verKor.py, verEng.py 파일입니다./Korean and English versions exist. These are verKor.py and verEng.py files, respectively.
사용량이 많아지면 본인의 API키로 요금이 청구된다는 점을 주의하세요./Please note that as your usage increases, you will be billed using your API key.
