#많이 쓰면 돈 내야함!!
import os
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import sys

# Google Cloud Speech-to-Text API
#path/to/your/credentials.json 부분을 API키로 대체하세요. API 키는 Google Cloud 플랫폼에서 생성 가능합니다.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json" 
r = sr.Recognizer()

# 음성 출력 엔진 초기화
engine = pyttsx3.init()

while True:
    #마이크가 계속 켜져있는 상황 방지.
    with sr.Microphone() as source:
        print("말씀하세요...")
        #음성을 녹음해서 audio로 저장 source를 통해 이미 열려있는 마이크 사용
        audio = r.listen(source)   
        try:
            text = r.recognize_google(audio, language="ko-KR")
            print("인식된 텍스트:", text)
            #아래 키워드를 변경하거나 추가할 수 있습니다.시간 인식 기능이며 기본값은 "몇시야", "시간 좀 알려 줘"입니다.
            if "몇 시야" in text.lower() or "시간 좀 알려 줘" in text.lower():
                current_time = datetime.now().strftime("%H:%M %p")
                print("현재 시간:", current_time)
                #음성 생성
                engine.say("현재 시간은 " + current_time + "입니다") 
                #음성 재생
                engine.runAndWait()  
                #아래 키워드를 변경하거나 추가할 수 있습니다.프로그램 종료의 기능을 하며 기본값은 "꺼져", "종료"입니다.
            elif "꺼져" in text.lower() or "종료" in text.lower():
                print("프로그램을 종료합니다")
                engine.say("프로그램을 종료합니다")
                engine.runAndWait()
                sys.exit()
                
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError as e:
            print(f"Google API에 요청할 수 없습니다: {e}")