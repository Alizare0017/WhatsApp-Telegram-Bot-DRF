from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import User
import datetime
import pytz
# Create your views here.

class InfoView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.data.get('userID'))
        if user.exists():
            serializer = UserSerializer(user,many=True)
            user.update(userID=request.data['userID'],username=request.data['username'])
            return Response(status=status.HTTP_202_ACCEPTED, data=serializer.data)
        else :
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})


class ChangeView(APIView):

    def post(self,request):
        user = User.objects.filter(userID=request.query_params.get('userID'))
        if user.exists():    
            serializer = UserSerializer(user,many=True)
            date = user[0].changed_date
            print(date)
            date = str(date).replace('+00:00','')
            chaged_date = datetime.datetime.strptime(f"{date}","%Y-%m-%d %H:%M:%S.%f")
            exp = datetime.timedelta(days=7)
            exp_date = chaged_date + exp
            if datetime.datetime.now() < exp_date :
                if user[0].change_count < 3 :
                    print(exp_date , user[0].change_count)
                    user.update(change_count = user[0].change_count + 1)
                    return Response(status=status.HTTP_200_OK, data=serializer.data)
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'erorrs' : f'You cannot change your token until {exp_date}'})
            user.update(change_count = 0, changed_date=datetime.datetime.now(pytz.timezone('Asia/Tehran')))
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND, data={'errors' : 'user not found ! '})

