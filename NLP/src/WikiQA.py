#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WikiQA"
accessKey = "YOUR_ACCESS_KEY"
question = "김구가 누구야?"
type = "irqa"
"""
irqa: 언어분석 기반과 기계독해 기반의 질의응답을 통합한 질의응답 방식
kbqa: 지식베이스 기반의 질의응답 방식
hybridqa: irqa와 kbqa를 통합한 질의응답 방식
"""
 
requestJson = {
"access_key": accessKey,
"argument": {
    "question": question,
    "type": type
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