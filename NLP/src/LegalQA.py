#-*- coding:utf-8 -*-
import urllib3
import json

openApiURL = "http://aiopen.etri.re.kr:8000/LegalQA"
accessKey = "YOUR_ACCESS_KEY"
question = "대법원장의 임기는 몇년인가?"

requestJson = {
	"access_key": accessKey,
	"argument": {
		"question": question,
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