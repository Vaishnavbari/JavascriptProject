from django.shortcuts import render
from django.views import View

# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'app/index.html')
    
class LoadModuleView(View):

    def get(self, request, count):
        return render(request, 'app/module.html', {'count': count})
    
# class