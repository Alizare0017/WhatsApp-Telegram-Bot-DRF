from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User
from helpers.generator import Token_Generator
from django.utils import timezone
import datetime

# Create your views here.

class InfoView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.headers.get('Userid'))
        if user.exists():
            serializer = UserSerializer(user,many=True)
            user.update(userID=request.headers.get('Userid'),username=request.query_params.get('username'))
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        else :
            data = {'userID':request.headers.get('Userid'),'username':request.query_params['username']}
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})


class ChangeView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.headers.get('Userid'))
        if user.exists():
            if user[0].is_active == False :
                return Response(status=status.HTTP_403_FORBIDDEN, data={'error' : 'Your account is not premium !'})
            if user[0].exp_date <= timezone.now():
                user.update(is_active=False)
                return Response(status=status.HTTP_403_FORBIDDEN, data={'error':'Account Expired !','Expire date':user[0].exp_date})
            serializer = UserSerializer(user,many=True)
            date = user[0].changed_date
            exp = datetime.timedelta(days=7)
            exp_date = date + exp
            if timezone.now() <= exp_date :
                if user[0].change_count < 3 :
                    user.update(change_count = user[0].change_count + 1, token = Token_Generator())
                    return Response(status=status.HTTP_200_OK, data=serializer.data)
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'erorr' : f'You cannot change your token until {exp_date}'})
            if timezone.now() > exp_date :
                user.update(change_count = 1, changed_date=timezone.now(), token=Token_Generator())
                return Response(status=status.HTTP_200_OK, data=serializer.data)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={'error':'Internal error'})
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error' : 'user not found ! '})

