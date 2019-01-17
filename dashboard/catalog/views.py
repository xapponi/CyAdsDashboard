from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import MySQLdb
import pandas as pd
from django.db.models import Sum
from datetime import datetime

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

        categories = pd.DataFrame(list(ProcessorCategory.objects.all().values()))
        categories = categories.to_dict('records')

        ratio = []
        category_names = []
        unique_ads= []
        total_ads = []
        for cat in categories:
            if 'external' not in cat['name']:
                if 'hows' not in cat['name']:
                    unique = ProcessorVideo.objects.filter(watched_as_ad__gt=0).filter(category_id=cat['id']).count()
                    total = ProcessorVideo.objects.filter(category_id=cat['id']).aggregate(Sum('watched_as_ad'))['watched_as_ad__sum']
                    category_names.append(cat['name'])
                    ratio.append(total/unique)
                    #category_counts.append(ProcessorVideo.objects.filter(watched_as_ad__gt=0).filter(category_id=cat['id']).count())
                    unique_ads.append(unique)
                    total_ads.append(total)


        total_category_data = {}
        for cat in categories:
            if 'external' not in cat['name']:
                if 'hows' not in cat['name']:
                    total_category_data[cat['id']] = 0







        data = {
            'unique_ads': unique_ads,
            'total_ads': total_ads,
            'ratio': ratio,
            'category_names': category_names,
        }

        return Response(data)

class ByDateData(APIView):
        authentication_classes = []
        permission_classes = []

        def get(self, request, format=None):

            return Response(data)
