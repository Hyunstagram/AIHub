#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/WiseWWN/WordRel"
accessKey = "YOUR_ACCESS_KEY"
firstWord = "사과"
firstSenseId = 'FIRST_SENSE_ID'
secondWord = "배"
secondSenseId = 'SECOND_SENSE_ID'
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        'first_word': firstWord,
        # 'first_sense_id': firstSenseId,
        'second_word': secondWord,
        # 'second_sense_id': secondSenseId
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