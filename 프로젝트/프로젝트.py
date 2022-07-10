from urllib.request import urlopen #url오픈 모듈 (크롤링 할 웹사이트 오픈 위함)
from bs4 import BeautifulSoup #BeautifulSoup 모듈 (크롤링 위함)
import time #시간 모듈 (현재 시간 불러오기 위함)
import csv #csv 파일 만들기 위한 모듈

#크롤링 함수
def web_crawler():
    url = input('웹사이트 주소: ') #크롤링 할 사이트를 사용자로부터 입력 받음
    start = time.strftime #크롤링 시작 시간 저장
    filename = time.strftime('%Y%m%d%H%M') #시작 시간을 후에 저장할 csv파일명으로 저장

    a = urlopen(url) #변수 a에 입력받은 주소 할당
    soup = BeautifulSoup(a, 'html.parser') #BeautifulSoup이용하여 웹 크롤링

    #차종 이름
    name = soup.find_all('span','box') #차종 이름에 해당하는 부분 모두 찾기
    n = [] #차종 이름 리스트
    for i in name:   
        text = i.text #텍스트 추출
        n.append(text) #이름에 해당하는 텍스트만 리스트 n에 저장
        
    #출시 가격
    price = soup.find_all('li','price new') #출시 가격에 해당하는 부분 모두 찾기
    p = [] #출시 가격 리스트
    for j in price:    
        text = j.text #텍스트 추출
        text = text.replace(' ','')
        text = text.replace('\n','')
        text = text.replace('출시','') #필요 없는 부분 삭제
        p.append(text) #가격에 해당하는 텍스트만 리스트 p에 저장
        
    #연비와 연료
    full = soup.find_all('li','mileage') #연비와 연료를 포함하는 부분(같이 가지고 있음) 모두 찾기 

    m_f = [] #mileage(연비)와 fuel(연료) 리스트

    for i in full:
        text = i.text #텍스트 추출
        text = text.replace('\n','')
        text = text.replace(' ','')
        text = text.replace('\r','')
        text = text.replace('연비','') #필요 없는 부분 삭제
        text = text.split('연료') #'연료'를 기준으로 앞이 연비, 뒤가 연료이므로 나누어 줌
        m_f.append(text) #해당 부분 리스트 m_f에 저장

    for i in range(len(m_f)):
        m_f[i].insert(0,p[i]) #m_f각각에 가격(각각) 추가

    for i in range(len(m_f)):
        m_f[i].insert(0,n[i]) #m_f각각에 이름(각각) 추가

    final_list = m_f #최종 리스트  
    final_list.insert(0,['차종','출시 가격','연비','연료']) #파일에서 항목 이름 알기 위해 추가

    f = open(f'{filename}.csv', 'w') #csv파일 생성(쓰기모드)

    csv_w = csv.writer(f) #csv 기록기 

    for i in final_list:
        csv_w.writerow(i) #최종 리스트의 데이터를 행으로 추가

    f.close() #파일 닫기
    finish = time.strftime #크롤링 끝난 시간 저장
    print("'%s.csv' 파일에 크롤링 결과가 저장되었습니다."%(filename))
    print('소요 시간: %d초'%(int(finish('%M%S'))-int(start('%M%S'))))
    print('시작시간: %s년 %s월 %s일 %s시 %s분 %s초'%(start('%Y'),start('%m'),start('%d'),start('%H'), start('%M'), start('%S')))
    print('완료시간: %s년 %s월 %s일 %s시 %s분 %s초'%(finish('%Y'),finish('%m'),finish('%d'),finish('%H'), finish('%M'), finish('%S')))

#다시 할 것인지 결정하는 함수
def conti():
    cont = input('계속하시겠습니까? (네/아니오)')
    while not (cont == '네' or cont == '아니오'):
        cont = input('계속하시겠습니까? (네/아니오)')
    return cont == '네'

#메인 함수
def main():
    cont = True #초기 설정: True
    while cont: #True이면 계속함
        web_crawler() #웹크롤링 함수 실시
        cont = conti() #conti 함수 T/F여부

main()
print('안녕히 가십시오')
