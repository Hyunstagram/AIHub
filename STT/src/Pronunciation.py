#-*- coding:utf-8 -*-
import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Pronunciation" # 영어
# openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/PronunciationKor" # 한국어
accessKey = "YOUR_ACCESS_KEY"
audioFilePath = "./STT/mp3/KOR_M.mp3"
languageCode = "korean"
script = "PRONUNCIATION_SCRIPT"
 
file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        # "script": script,
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