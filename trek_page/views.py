from django.shortcuts import render
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self, request):
        return render(request, 'trek_page/index.html')
    
    
def index(request):
    return render(request, 'trek_page/index.html')