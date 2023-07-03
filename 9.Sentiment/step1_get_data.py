import pandas as pd
import numpy as np
import os
import codecs
import re

#     파일명                함수/클래스


def step1_get_data():
    # 데이터 파일 위치
    path = "9.Sentiment/aclImdb/"
    # 긍정 부정 값
    labels = {"pos": 1, "neg": 0}
    df = pd.DataFrame()
    # 디렉토리 수 만큼 반복
    for s in ("test", "train"):
        for name in ("pos", "neg"):
            subpath = "%s/%s" % (s, name)
            # print(path + subpath)
            # 현재 디렉토리의 파일 목록
            file_list = os.listdir(path + subpath)
            # print(file_list)
            for file in file_list:
                # print(path + subpath + '/' + file)
                # print(os.path.join(path+subpath, file))
                file_name = os.path.join(path + subpath, file)
                with codecs.open(file_name, "r", "utf-8") as fp:
                    txt = fp.read()
                    # print(labels[name], txt)
                df = df.append([[txt, labels[name]]], ignore_index=True)
    df.columns = ["review", "sentiment"]
    np.random.seed(0)
    df = df.reindex(np.random.permutation(df.index))
    df.to_csv("9.Sentiment/aclImdb/movie_review.csv", index=False)


if __name__ == "__main__":
    step1_get_data()
