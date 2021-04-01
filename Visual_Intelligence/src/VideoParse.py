#-*- coding:utf-8 -*-
import urllib3
import json
import os

openApiURL = "http://aiopen.etri.re.kr:8000/VideoParse"
accessKey = "YOUR_ACCESS_KEY"
videoFilePath = "./Visual_Intelligence/movies/demo.mp4"

file = open(videoFilePath,'rb')
fileContent = file.read()
file.close();

requestJson_1 = {
	"access_key": accessKey,
	"argument": {}
}

http = urllib3.PoolManager()
response_1 = http.request(
	"POST",
	openApiURL,
	fields={
		'json': json.dumps(requestJson_1),
		'uploadfile': (os.path.basename(file.name), fileContent)
	}
)

response_data = json.loads(response_1.data)

openApiURL = "http://aiopen.etri.re.kr:8000/VideoParse/status"

requestJson_2 = {
	"request_id": "reserved field",
	"access_key": accessKey,
	"argument": {
		"file_id": response_data["return_object"]["file_id"]
	}
}

response_2 = http.request(
	"POST",
	openApiURL,
	fields={
		'json': json.dumps(requestJson_2),
		'uploadfile': (os.path.basename(file.name), fileContent)
	}
)

print("[responseCode] " + str(response_2.status))
print("[responBody]")
print(response_2.data)
print("[file_id]")
print(response_data["return_object"]["file_id"])