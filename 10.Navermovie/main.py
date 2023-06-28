import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import re

def step1_get_data():
    #영화 코드 목록 만들기
    site1 = 'https://pedia.watcha.com/ko-KR/?domain=movie'
    # #root > div > div.css-1xm32e0 > section > div > section > div:nth-child(6) > div.css-5rbrg6 > div > div.css-9dnzub > div > div > ul > li:nth-child(1) > a > div.css-ixy093 > div.css-5yuqaa
    #  css--visualu1
    res1 = requests.get(site1)
    code_movie_list = list()
    name_movie_list = list()
    if res1.status_code == requests.codes.ok:
        bs1 = BeautifulSoup(res1.text, 'html.parser')
        ul = bs1.find_all(class_ = re.compile('-VisualUl'))[2]
        # print(ul)
        lis = ul.find_all('li')
        # li_a = lis[0].find_all('a')
        # print(li_a.get('href').split('/')[-1], li_a.get('title'))
        # print(li_a)
        for li in lis:
            # print(li.find('a').get('href').split('/')[-1])
            # print(li.find('a').get('title'))

            code_movie_list.append(li.find('a').get('href').split('/')[-1])
            name_movie_list.append(li.find('a').get('title'))

            
# 영화 코드별 리뷰 가져오기
    temp = zip(code_movie_list, name_movie_list)
    df = pd.DataFrame()
    # 최초 저장 여부 상태 값 Flase면 처음 저장 / True면 두 번째 저장
    check_save = False
    count = 0 
    for code, name in temp:
        sleep(0.5)
        site2 = 'https://pedia.watcha.com/ko-KR/contents/%s/comments' % code
        print(site2)
        res2 =  requests.get(site2)
        
        if res2.status_code == requests.codes.ok:
            bs2 = BeautifulSoup(res2.text, 'html.parser')
        #     #-CommentLists
            div1 = bs2.find(class_ = re.compile('-CommentLists'))
            # ul = div1.find('ul')
            div2s = div1.find_all(class_='css-bawlbm')
            for div2 in div2s:
                div3 = div2.find_all('div')
                # print('별점: ', div3[5].get_text())
                # print('리뷰: ', div3[6].get_text())
                # print('좋아요: ', div3[8].find('em').get_text())
                star = div3[5].get_text()
                review = div3[6].get_text()
                # good = div3[8].find('em').get_text()
                df = df.append([[name,code,star,review]], ignore_index=True)

            # 저장
            if check_save == False:   # 첫번 째 저장
                df.columns = ['name', 'code', 'star', 'review']
                df.to_csv('movie_data.csv', encoding='utf-8', index=False)
                check_save = True
            else:  # 두번째 이후 저장
                df.to_csv('movie_data.csv', encoding='utf-8', index=False,
                            mode = 'a', header=False)
            count += 1
            print('진행중: ', count)
                
if __name__ == '__main__':
    step1_get_data()