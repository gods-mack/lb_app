from django.shortcuts import render
from django.views import View

from django.http import JsonResponse
from .models import UserPost
from django.views.decorators.csrf import csrf_exempt
import json 



# Create your views here.


def send_200(data):
    return JsonResponse(data, status=200)


class HomeView(View):
    def get(self, request):
        id  = request.GET.get('id')
        if id:
            post = UserPost.objects.get(id=id)
            resp = {
                'message': 'Post found',
                'post': post.serializer()
            }
            return send_200(resp)
        posts = UserPost.objects.all()

        resp = {
            'message': 'Hello World',
            'data': [post.serializer() for post in posts]
        }
        
        return send_200(resp)

    def post(self, request):
        data  = json.loads(request.body)
        post = UserPost.objects.create(
            media_url=data['media_url'],
            caption=data['caption']
        )
        resp = {
            'message': 'Post created successfully',
            'post': post.serializer()
        }

        return send_200(resp)


