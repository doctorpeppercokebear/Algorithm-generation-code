import pandas as pd  # 회색으로 변하는건 사용하지 않아서 삭제해도 됨
import numpy as np
import re


def preprocessor(text):
    # HTML 태그 삭제
    text = re.sub("<[^>]*>", "", text)
    # 이모티콘 찾기 정규식
    emoticons = re.findall("(?::|;|=)(?:-)?(?:\)|\(|D|P)|\^.?\^", text)
    # 특수문자 제거
    # 소문자 변환
    # 이모티콘 제거
    text = re.sub("[\W]+", " ", text.lower() + " ".join(emoticons).replace("-", ""))
    return text


def step2_preprocessing():
    # print(preprocessor('<brrrr />ha<a>hah</a>ah :-( ;-) ADFSDFdfdfdfd'))
    df = pd.read_csv("9.Sentiment/aclImdb/movie_review.csv")
    # print(df.shape)
    df["review"] = df["review"].apply(preprocessor)
    df.to_csv("9.Sentiment/aclImdb/setp2_movie_review.csv", index=False)


if __name__ == "__main__":
    step2_preprocessing()
