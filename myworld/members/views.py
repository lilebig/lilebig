# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from rest_framework import generics

# from members import members
from .models import Members
from .serializers import SnippetSerializer

def index(request):
  # template = loader.get_template('myfirst.html')
  # meetups = False 
  return render(request, 'myfirst.html', {'test' : True})

class memberList(generics.ListCreateAPIView):
    queryset = Members.objects.all()
    serializer_class = SnippetSerializer
    print(queryset)


class memberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Members.objects.all()
    serializer_class = SnippetSerializer
