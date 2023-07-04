from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle
import sklearn

def ai(request):
    return render(request, 'ai.html')

@api_view(['GET'])
def ai_rest(request):
    temperature = request.GET.get('temperature')
    humidity = request.GET.get('humidity')
    # return Response({'message': temperature + ':' + humidity})
    with open('ai/bechu.pkl', 'rb') as fp:
        model = pickle.load(fp)
    # if temperature is not None & humidity is not None:
    #     prediction = model.predict([[float(temperature), float(humidity)]])
    # print('temperature==========>', type(temperature))
    # print('humidity==========>', type(humidity))
    predict = [0]
    if (temperature is not None) & (humidity is not None):
        predict = model.predict([[float(temperature), float(humidity)]])
    return Response({'predict': + predict[0]})

# Create your views here.
