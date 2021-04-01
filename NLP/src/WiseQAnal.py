#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseQAnal"
accessKey = "YOUR_ACCESS_KEY"
text = "가스파초는 어느 나라의 음식인가요?"
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text
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