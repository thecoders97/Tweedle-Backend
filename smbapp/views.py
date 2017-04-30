from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from .models import Book
from .serializers import BookSerializer
import json
import re
class BookList(APIView):

	def get(self,request):
		books = Book.objects.all()
		serializer = BookSerializer(books, many = True)	
		return Response(serializer.data)

	def post(self,request):	 
		serializer = BookSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def showform(request):
	return render(request,"postapi.html")

@csrf_exempt
def postapi(request):		
	if request.method == "POST": 
		a = json.loads((request.body.decode("utf-8")))
		b = (a["result"]["parameters"]["Book"])
		c = (a["result"]["parameters"]["City"])
		books = str(Book.objects.filter(book1 = b))
		words = books.split()
		locname = words[6] 
		libname = words[7]
		libname = libname.strip('>]>')
		print(locname)
		print(libname)
		finalstring = "The queried book is available in " + libname + " library at " + locname
		print(finalstring)
		return JsonResponse({	
		      "speech": finalstring,
		      "messages": [
		        {
		          "type": 0,
		          "speech": finalstring
		        }]})

		