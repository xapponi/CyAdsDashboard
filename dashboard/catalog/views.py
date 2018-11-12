from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import pandas as pd

# Create your views here.
from catalog.models import *
def index(request):

    context = {
        'hello': 'Hello World!',
    }

    return render(request, 'index.html', context=context)

def chart(request):
    return render(request, 'charts.html')

class CategoryData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        #videos = pd.DataFrame(list(ProcessorVideo.objects.all().values()))
        categories = pd.DataFrame(list(ProcessorCategories.objects.all().values()))
        categories = categories.to_dict('records')

        category_counts = []
        for cat in categories:
            if 'external' not in cat['name']:
                category_counts.append({'category_name': cat['name'],
                                        'category_count': ProcessorVideo.objects.filter(category_id=cat['id']).count()})

        # video_data = {
        #     'numVideos': ProcessorVideo.objects.all().count(),
        #     'numCategories': ProcessorCategories.objects.all().count(),
        #     'categories': category_counts
        #     'videos': videos.head().to_dict('records'),
        #
        #     }
        #videos = serializers.serialize('json', ProcessorVideo.objects.all(), fields=('title', 'category'))
        return Response({'categories_counts': category_counts})
