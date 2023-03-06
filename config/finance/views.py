from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import FactorSerializer
from users.serializer import UserSerializer
from users.models import User
from .models import Factor
from helpers.generator import Token_Generator
from django.utils import timezone
from datetime import timedelta
# Create your views here.

class SellView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.headers.get('Userid'))
        if user.exists():
            exp = timedelta(days=30) + timezone.now()
            user.update(charge=user[0].charge+int(request.query_params['charge']),exp_date=exp,last_charge_date=timezone.now(),
                        is_active=True, token=Token_Generator())
            factor = Factor(user=user[0], charge=request.query_params['charge'],price=int(request.query_params['price']))
            factor.save()
            serializer = UserSerializer(user[0])
            
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'User not found'})

  
class FactorView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.headers.get('Userid'))
        if user.exists() :
            factor = Factor.objects.filter(user=user[0].pk)
            if factor.exists():
                serializer = FactorSerializer(factor, many=True)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'no factor found'})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'user not found'})