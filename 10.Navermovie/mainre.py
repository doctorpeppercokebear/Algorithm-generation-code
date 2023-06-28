import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
import re
import numpy as np
from sklearn.model_selection import train_test_split

def step1_get_data():
    # 영화 코드 목록 만들기
    site1 = 'https://pedia.watcha.com/ko-KR/?domain=movie'
    # # root > div > div.css-1xm32e0 > section > div > section > div:nth-child(1) > div.css-1qq59e8 > div > div.css-9dnzub > div > div > ul
    # # //*[@id="root"]/div/div[1]/section/div/section/div[1]/div[2]/div/div[1]/div/div/ul
    # # css-a19lp3-VisualUl
    res1 = requests.get(site1)
    code_movie_list = list()
    name_movie_list = list()
    if res1.status_code == requests.codes.ok:    
        bs1 = BeautifulSoup(res1.text, 'html.parser')
        ul = bs1.find_all(class_ = re.compile('-VisualUl'))[2]
        # print(ul)
        lis = ul.find_all('li')
        # li_a = lis[0].find('a')
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
        res2 = requests.get(site2)
        if res2.status_code == requests.codes.ok:
            bs2 = BeautifulSoup(res2.text, 'html.parser') # 속도가 빠른 것은 'lxml' 
            # -CommentLists
            div1 = bs2.find(class_ = re.compile('-CommentLists')) # 클래스 속성이 -CommetLists인 것만 가져오기 
            # css-bawlbm
            # ul = div1.find('ul')
            div2s = div1.find_all(class_ = 'css-bawlbm') # -CommetLists에서 클래스 속성이 css-bawlbm인 것만 가져오기
            for div2 in div2s:
                div3 = div2.find_all('div') # 태그로 찾을 때
                # print('리뷰 : ', div3[5].get_text()) # 별점
                # print('별점 : ', div3[6].get_text()) # 커멘트 
                # print('좋아요 : ',div3[8].find('em').get_text()) # 좋아요 
                star =  div3[5].get_text()
                review = div3[6].get_text()
                reviw = review.replace(',', '')
                # good = div3[8].find('em').get_text()
                df = df.append([[name, code, star, review]], ignore_index=True)

        # 저장
        if check_save == False: # 첫 번째 저장
            df.columns = ['name', 'code', 'star', 'review']
            df.to_csv('10.Navermovie/movie_data.csv', encoding='utf-8', index=False)
            check_save = True    
        else: # 두 번째 이후 저장
            df.to_csv('10.Navermovie/movie_data.csv', encoding='utf-8', index=False,
                    mode='a', header=False)
        count += 1
        print('진행중 :', count) 

#별점 처리 함수
def star_preprocessing(text):
    value = float(text)
    if value > 2.5:
        return 1
    else:
        return '0'
def review_preprocessing(text):
    if text.startswith('관람객'):
        new_str = text[:3]
        return new_str
    else:
        return text

def step2_preprocessing():
    df = pd.read_csv('10.Navermovie/naver_star.csv', encoding='utf-8')
    # 랜덤하게 섞기
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    #전처리
    df['star'] = df['star'].apply(star_preprocessing)
    review_list = df['review'].tolist()
    star_list = df['star'].tolist()
    X_train, X_test, y_train, y_test = train_test_split(review_list, star_list, test_size=0.2, random_state=0)
    # print(len(X_train), len(X_test), len(y_train), len(y_test))

    # 학습, 테스트 데이타 저장
    dic_train = {'review': X_train, 'star': y_train}
    df_train = pd.DataFrame(dic_train)
    dic_test = {'review': X_test, 'star': y_test}
    df_test = pd.DataFrame(dic_test)
    df_train.to_csv('naver_train.csv', encoding='utf-8-sig', index=False)
    df_test.to_csv('naver_test.csv', encoding='utf-8-sig', index=False)


if __name__ == '__main__':
    # step1_get_data()
    step2_preprocessing()