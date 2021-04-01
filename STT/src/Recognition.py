#-*- coding:utf-8 -*-
import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "YOUR_ACCESS_KEY"
audioFilePath = "./STT/mp3/KOR_M.mp3"
languageCode = "korean"
"""
korean : 한국어 음성인식 코드
english: 영어 음성인식 코드
japanese: 일본어 음성인식 코드
chinese: 중국어 음성인식 코드
spanish: 스페인어 음성인식 코드
french: 프랑스어 음성인식 코드
german: 독일어 음성인식 코드
russian: 러시아어 음성인식 코드
vietnam: 베트남어 음성인식 코드
arabic: 아랍어 음성인식 코드
"""
 
file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        "audio": audioContents
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))