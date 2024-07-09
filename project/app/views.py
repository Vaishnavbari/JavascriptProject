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
        project = Project.objects.filter(name=projectName)
        if not project:
           return JsonResponse({"status":"error", "message":"project not found"})
        module = request.POST.getlist("module[]")
        hours = request.POST.getlist("hours[]")

        for data in range(len(module)):
           if not module[data]:
              return JsonResponse({"status":"error", "message":"module name is required"})
           if not hours[data]:
              return JsonResponse({"status":"error", "message":"hours is required"})
           hour = int(hours[data]) if hours[data] else 0
           if hour < 0:
              return JsonResponse({"status":"error", "message":"hours cannot be negative"})
           Module.objects.create(project=project.first(), name=module[data], hours=hours[data])
        return  JsonResponse({"status":"success", "message":"Data saved successfully"})
    
class LoadModuleView(View):

    def get(self, request):
       return render(request, 'app/module.html')
    
# class