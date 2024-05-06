from django.shortcuts import render
from django.http import JsonResponse
from time import time
from django.views.generic import View

class AjaxHandlerView(View):
    def get(request):
        text = request.GET.get('button_text')
        if request.is_ajax():
            t = time()
            return JsonResponse({'seconds': t}, status= 200)
        """print()
        print(text)
        print()
        data = {'message': 'Hello, World!'}"""
        return render(request, 'ajax/ajax.html')

