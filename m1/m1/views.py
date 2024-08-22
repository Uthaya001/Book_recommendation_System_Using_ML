from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse




class modelPredict(APIView):
    
    
    def post(self, request):
        value = request.data.get('value')
        print(value)
        resp = model.test(value=value)
        return Response(resp)
     