from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from rest_framework import serializers
from rest_framework import status
# Create your views here.

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


@api_view(['GET'])
def getAllArticles(request):
    allpost = Article.objects.filter(active = True).all().order_by("-datecreated")
    converted_data = articleSerializer(allpost, many=True)
    return Response(converted_data.data)

@api_view(['GET'])
def getArticle(request, id):
    post = Article.objects.filter(id=id).first()
    converted_data =articleSerializer(post)
    return Response(converted_data.data)


@api_view(['POST'])
def createarticle(request):
    
    serializer = articleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)