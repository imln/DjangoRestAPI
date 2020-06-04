from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . serializers import EmployeeSerializer

class  empList(APIView):
	
	def get(self, request):
		emplist = Employee.objects.all()
		serial = EmployeeSerializer(emplist,many=True)
		return Response(serial.data)

	def post(self):
		pass
