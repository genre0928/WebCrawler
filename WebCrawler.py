import pandas as pd
import re
import csv
import gspread
import requests
import time
import datetime
import json
from pprint import pprint
import urllib.request as req
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. 스크립트 시작할 때 시작시간 설정 및 오픈
startTime = time.time()
nowTime = datetime.datetime.now()

# 3. 운송장번호를 불러올 파일과 경로 설정
csv_file = open('기관 명단 '+ str(nowTime.month) + '.' + str(nowTime.day) + '.csv', 'w', newline="", encoding='utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['연번', '시설명', '우편번호', '주소', '지역', '운영주체', '전화', '팩스', '시설종류', '홈페이지', '설립일자', '이메일', '직원현황', '기관장', '이용인원'])
day_Today = str(nowTime.year) + "." + str(nowTime.month) + "." + str(nowTime.day) + "."
keywords = ['포항', '경주', '안동', '김천', '구미', '영주', '영천', '상주', '문경', '경산', '의성', '청송', '영양', '영덕', '청도', '고령', '성주', '칠곡', '예천', '봉화', '울진', '울릉']
for i in range(2, 1970) :
    res = requests.get(f'http://www.gbcsw.or.kr/content/05data/02_01_view.php?no={i}%d&prepage=%2Fcontent%2F05data%2F02_01.php%3F')
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find_all('td')
    name = content[0].get_text()
    addr = content[1].get_text()
    owner = content[2].get_text()
    number = content[3].get_text()
    fax = content[4].get_text()
    item = content[5].get_text()
    homepage = content[6].get_text()
    est = content[7].get_text()
    email = content[8].get_text()
    count = content[10].get_text()
    owner2 = content[11].get_text()
    count2 = content[13].get_text()
    for keyword in keywords :
        if keyword in addr :
            region = keyword
            break
        else :
            region = '지역'

    if name != '' :
        csv_writer.writerow([i-1, name, '우편번호', addr, region, owner, number, fax, item, homepage, est, email, count, owner2, count2])