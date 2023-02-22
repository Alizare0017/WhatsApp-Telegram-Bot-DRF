from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import FactorSerializer
from users.serializer import UserSerializer
from users.models import User
from .models import Factor
from datetime import datetime, timedelta
import pytz
# Create your views here.

class SellView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.data['userID'])
        if user.exists():
            exp = timedelta(days=30) + datetime.now()
            dt = pytz.utc.localize(exp)
            exp_date = dt.astimezone(pytz.timezone('Asia/Tehran'))
            user.update(charge=user[0].charge+int(request.data['charge']),exp_date=exp_date)
            factor = Factor(user=user[0], charge=request.data['charge'],price=int(request.data['price']))
            factor.save()
            serializer = UserSerializer(user[0])
            
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'User not found'})
    
class FactorView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.data['userID'])
        if user.exists() :
            factor = Factor.objects.filter(user=user[0].pk)
            if factor.exists():
                serializer = FactorSerializer(factor, many=True)
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'no factor found'})
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'user not found'})