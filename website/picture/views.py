from django.http import HttpResponse

def index(request):
	return HttpResponse("THis is pictures homepage")