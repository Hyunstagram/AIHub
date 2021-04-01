import cv2

import requests
import json
import base64

url="http://aiopen.etri.re.kr:8000/ObjectDetect"
accessKey = "YOUR_ACCESS_KEY"

videoFilePath = "./Visual_Intelligence/movies/demo_small.mp4"
video=cv2.VideoCapture(videoFilePath)
count=1

# 동영상 재생
while video.isOpened():
    run, frame = video.read()
    if not run:
        print("동영상 재생 종료")
        break
    #image = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
    cv2.imwrite("./opencv/frame/frame%d.jpg" % count, frame)
    imageFilePath = "./opencv/frame/frame%d.jpg" % count
    file = open(imageFilePath, "rb")
    imageContents = base64.b64encode(file.read()).decode("utf8")
    file.close() 

    json_data={
        "access_key": accessKey,
        "argument": {
            "file": imageContents,
            "type": 'jpg'
        }
    }
    
    response=requests.post(url,headers = {"Content-Type": "application/json; charset=UTF-8"},json = json_data)
    response_data = response.json()
    print(response_data["return_object"])
    
    for i in range(0,len(response_data["return_object"]["data"])):
        if response_data["return_object"]["data"][i]["class"] == "person":
            now_x=int(response_data["return_object"]["data"][i]["x"])
            now_y=int(response_data["return_object"]["data"][i]["y"])
            width=int(response_data["return_object"]["data"][i]["width"])
            height=int(response_data["return_object"]["data"][i]["height"])
            cv2.rectangle(frame, (now_x, now_y), (now_x + width, now_y + height), (255, 255, 255), 4)
            cv2.imshow("image", frame)
            cv2.waitKey(0)
        else:
            continue

    count+=1
    cv2.imshow('video', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()