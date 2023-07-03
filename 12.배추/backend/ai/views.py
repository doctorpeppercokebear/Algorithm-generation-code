from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response

import sklearn
import pickle
import numpy as np


@api_view(['GET'])
def ai(request):
    temperature = float(request.GET['temperature'])
    humidity = float(request.GET['humidity'])
    # wind_speed = float(request.GET['wind_speed'])

    # 평균 온도 습도를 가지고 학습된 모델
    with open('ai/bechu.pkl', 'rb') as fp:
        model = pickle.load(fp)
    predict = model.predict([[temperature, humidity]]) 

    return Response([{'ai': '모민규'},
                    # {'temperature' : temperature},
                    # {'wind_speed:': wind_speed},
                    {'predict' : predict[0]}])  # 키 : 밸류


