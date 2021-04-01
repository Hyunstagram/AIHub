#-*- coding:utf-8 -*-
import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
accessKey = "YOUR_ACCESS_KEY"
imageFilePath = "./Visual_Intelligence/images/object_detect_cat.jpg"
type = "jpg"
 
file = open(imageFilePath, "rb")
imageContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "type": type,
        "file": imageContents
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
print(response.data)