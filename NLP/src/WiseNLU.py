#-*- coding:utf-8 -*-
import urllib3
import json
 
# 언어 분석 기술 문어/구어 중 한가지만 선택해 사용
# 언어 분석 기술(문어)
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU" 
# 언어 분석 기술(구어)
# openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU_spoken"
accessKey = "YOUR_ACCESS_KEY"
analysisCode = "morp"
"""
형태소 분석 (문어/구어) : "morp",
어휘의미 분석 (동음이의어 분석)(문어) : "wsd"
어휘의미 분석 (다의어 분석)(문어) : "wsd_poly"
개체명 인식 (문어/구어) : "ner"
의존 구문 분석 (문어) : "dparse"
의미역 인식 (문어) : "srl"
"""
 
# 언어 분석 기술(문어)
text = "윤동주(尹東柱, 1917년 12월 30일 ~ 1945년 2월 16일)는 한국의 독립운동가, 시인, 작가이다."
"""
"중국 만저우 지방 지린 성 연변 용정에서 출생하여 명동학교에서 수학하였고, 숭실중학교와 연희전문학교를 졸업하였다. 숭실중학교 때 처음 시를 발표하였고, 1939년 연희전문 2학년 재학 중 소년(少年) 지에 시를 발표하며 정식으로 문단에 데뷔했다."
"일본 유학 후 도시샤 대학 재학 중 , 1943년 항일운동을 했다는 혐의로 일본 경찰에 체포되어 후쿠오카 형무소(福岡刑務所)에 투옥, 100여 편의 시를 남기고 27세의 나이에 옥중에서 요절하였다. 사인이 일본의 생체실험이라는 견해가 있고 그의 사후 일본군에 의한 마루타, 생체실험설이 제기되었으나 불확실하다. 사후에 그의 시집 《하늘과 바람과 별과 시》가 출간되었다."
"일제 강점기 후반의 양심적 지식인으로 인정받았으며, 그의 시는 일제와 조선총독부에 대한 비판과 자아성찰 등을 소재로 하였다. 그의 친구이자 사촌인 송몽규 역시 독립운동에 가담하려다가 체포되어 일제의 생체 실험으로 의문의 죽음을 맞는다. 1990년대 후반 이후 그의 창씨개명 '히라누마'가 알려져 논란이 일기도 했다. 본명 외에 윤동주(尹童柱), 윤주(尹柱)라는 필명도 사용하였다."
"""
# 언어 분석 기술(구어)
# text += "네 안녕하세요 홍길동 교숩니다"+;
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "text": text,
        "analysis_code": analysisCode
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