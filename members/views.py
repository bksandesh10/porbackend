from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FromSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Members


class FormRegistration(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self , request):
        qs_serializer = FromSerializer(
            data = {
                "name" : request.data.get('name'), 
                "email" : request.data.get('email'),
                "subject" : request.data.get('subject'),
                "message" : request.data.get('message')
            },

            context = {"request"  :request}
        )

        if qs_serializer.is_valid() :
            qs_serializer.save()
            return Response({
                "message"  : "data added successfully" ,
                "data" : qs_serializer.data
            },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "message" : qs_serializer.errors , "data" : None
                } ,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def get(self , request):
        qs = Members.objects.all()
        qs_serializer = FromSerializer(qs , many= True)
        return Response(
            qs_serializer.data , 
            status=status.HTTP_200_OK
        )
