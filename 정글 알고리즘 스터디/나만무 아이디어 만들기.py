import random
print(random.randint(0,10))
from itertools import product
# 누가
who = ['취준생','재택근무자','남자','여자','부모','손이 불편한 장애자','편집자','개발자','20~30대','40~50대']
# 어디서
space = ['집안','사무실','방안','대중교통 안','개인적인 공간','공공장소','백화점']
# 무엇을
what = ['밥먹기','공부하기','컴퓨터하기','실시간 그림그리기','책감상','영상편집하기','잠들기 도전','음악듣기','티비보기','세탁하기','옷입기','요리','설겆이','코딩','보고서 만들기','발표자료 만들기','미팅','게임','채팅','영화감상','일','스트리밍보기','웹툰보기','쇼핑','부동산구매','주식','아이돌보기']
# 어떻게
how = ['화상통화', '블루투스', 'wifi', '동시편집', 'VR', 'AR', 'AI', '무선으로', '동시에',
        '캔버스 API', '코드에디터', '결제 API', '채팅 API', '지도 API', '검색 API', '날씨 API', '정보제공 API', '번역 API']
# 왜 ?
why = ['간편함을','신속함을','정확성 향상을','소속감 향상','편안함을 느끼기','사회성 향상','쇠외감을 느끼지 않기','부자가 되기','취업하기','재미를']

#~한다.
do = ['만든','웹으로 만든','모바일로 만든','편집툴로 한','손으로 그린','도구를 가지고 한']



for i in range(10):
    print(who[random.randint(0,len(who)-1)],'가',space[random.randint(0,len(space)-1)],'에서',what[random.randint(0,len(what)-1)],'를(을)',
          how[random.randint(0, len(how)-1)], '를(을) 이용해서', why[random.randint(0, len(why)-1)],'위해서', do[random.randint(0, len(do)-1)],'다')

# print(list(product(*items)))

