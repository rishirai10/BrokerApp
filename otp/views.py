from django.shortcuts import render
from django.http import JsonResponse
from login.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.
@csrf_exempt
def send_otp(request):
	
	if request.methord=='POST':
	   response_json={}
	   try:		
		name=str(request.POST.get("name"))
		firm_name = str(request.POST.get("firm_name"))
		mobile=str(request.POST.get("mobile"))
		city=str(request.POST.get("city"))
		otp=random.randint(10000,99999)

		#opt sending

		try:
			otp_row=otp_info.objects.get(mobile = int(mobile))
			setattr(otp_info,'flag',False)
			setattr(otp_info,'otp',int(otp))
			otp_info.save()
			user_row=login_user.objects.get(mobile=int(mobile))
			setattr(user_row,'name',name)
			setattr(user_row,'frim_name',frim_name)
			setattr(user_row,'city',city)
			user_row.save()
		except:
			otp_info.objects.create(mobile=int(mobile),otp=int(otp))
			login_user.objects.create(name=name,
				frim_name=firm_name,
				city=city,
				mobile=int(mobile))
			print "new user created"
			response_json['success']=True
			response_json['message']="Otp Sent Successfully"
	   except:
		response_json['success']=False
		response_json['message']="Otp is not sent"
	   print str(response_json)
	   return JsonResponse(response_json)	   


			







			
