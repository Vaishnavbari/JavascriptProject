from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views import View
from .models import Project, Module

# Create your views here.

class HomeView(View):

    def get(self, request):
        return render(request, 'app/index.html')
    
    def post(self, request):
       
       if request.method == "POST":
        projectName = request.POST.get("project")
        if not projectName:
            return JsonResponse({"status":"error", "message":"Project name is required"})
        
        module = request.POST.getlist("module[]")
        hours = request.POST.getlist("hours[]")

        for index in range(len(module)):
           if not module[index]:
              return JsonResponse({"status":"error", "message":"module name is required"})
           if not hours[index]:
              return JsonResponse({"status":"error", "message":"hours is required"})
           hour = int(hours[index]) if hours[index] else 0
           if hour < 0:
              return JsonResponse({"status":"error", "message":"hours cannot be negative"})
           
        project, is_created = Project.objects.get_or_create(name=projectName)
        

        for index in range(len(module)):
           Module.objects.create(project=project, name=module[index], hours=hours[index])

        return  JsonResponse({"status":"success", "message":"Data saved successfully"})
    
class LoadModuleView(View):

    def get(self, request):
       return render(request, 'app/module.html')
    