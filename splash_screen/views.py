from django.shortcuts import render
from django.http import JsonResponse 
from .models import *
# Create your views here.

def splash_scr_response(request):
	
	if request.method == 'GET':

		try:
			response_json={}
			version_row=version_data.objects.get(compulsory_update=True)
			version=version_row.version
			response_json["success"]=True
			response_json["version"]=version
			response_json["compulsory_update"]=compulsory_update
			response_json["message"]="version_data found"
			
		except Exception,e:                                              #bug here
			response_json["success"]=False     
			response_json["message"]="error"

		print str(response_json)
		return JsonResponse(response_json)

