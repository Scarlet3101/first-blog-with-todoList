from django.shortcuts import render, get_object_or_404
from .models import Event
from django.http import HttpResponse,JsonResponse
from django.core import serializers
# Create your views here.
def home(request):
    events = Event.objects
    return render(request,'events/home.html', {'events': events})

# def specific_post_in_home(request,post_id):
#     event = get_object_or_404(Event,pk = post_id)
#     return render(request,'events/specific_post_in_home.html',{'event':event})


def specific_post_in_home(request,post_id):
    try:
        event = Event.objects.get(pk= post_id)
        return render(request,'events/specific_post_in_home.html',{'event':event})
    except:
        return render(request,'events/404_page.html')




def return_json(request):
    json = Event.objects.all()
    json_obj = serializers.serialize('python',json)
    return JsonResponse(json_obj,safe = False)
    # print(json)
    # return HttpResponse("Ok")
