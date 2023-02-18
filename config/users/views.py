from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from .models import users
# Create your views here.

class InfoView(APIView):

    def get(self,request):
        user = users.objects.filter(user_id=request.query_params.get('user_id'))
        if user.exists():
            serializer = UserSerializer(user,many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error' : 'user not found'})

    def post(self,request):
        user = users.objects.filter(user_id=request.query_params.get('user_id'))
        if user.exists():
            user.update(user_id=request.data['user_id'])
            return Response(status=status.HTTP_202_ACCEPTED)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data={'error':serializer.errors})


class ChangeView(APIView):

    def post(self,request):
        user = users.objects.filter(user_id=request.query_params.get('user_id'))
        user.update(plan=request.query_params.get('charge'))
        return Response(status=status.HTTP_200_OK, data={'info':f'{user[0].plan}'})