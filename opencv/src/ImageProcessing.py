#-*- coding:utf-8 -*-
import cv2

import urllib3
import json
import base64

openApiURL = "http://aiopen.etri.re.kr:8000/FaceDeID"
accessKey = "YOUR_ACCESS_KEY"
imageFilePath = "./Visual_Intelligence/images/demoImg.jpg"
type = "1";     # 얼굴 비식별화 기능 "1"로 설정

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

response_data = json.loads(response.data)
image = cv2.imread(imageFilePath, cv2.IMREAD_UNCHANGED)

for i in range(0,len(response_data["return_object"]["faces"])):
    now_x = int(response_data["return_object"]["faces"][i]["x"])
    now_y = int(response_data["return_object"]["faces"][i]["y"])
    width = int(response_data["return_object"]["faces"][i]["width"])
    height = int(response_data["return_object"]["faces"][i]["height"])
    text = str(now_x) + ", " + str(now_y)

    cv2.rectangle(image, (now_x, now_y), (now_x + width, now_y + height), (255, 255, 255), 4)
    cv2.putText(image, text, (now_x, now_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    image_crop = image[now_y : now_y + height, now_x : now_x + width]
    cv2.imwrite('./img/crop.jpg', image_crop)
    
cv2.imshow("image", image)
cv2.waitKey(0)



