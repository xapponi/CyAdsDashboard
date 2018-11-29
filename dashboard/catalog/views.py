from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import MySQLdb
import pandas as pd
from django.db.models import Sum

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
        categories = pd.DataFrame(list(ProcessorCategory.objects.all().values()))
        categories = categories.to_dict('records')

        category_counts = []
        category_names = []
        watched_as_ad = []
        watched_as_video = []
        for cat in categories:
            if 'external' not in cat['name']:
                if 'hows' not in cat['name']:
                    unique = ProcessorVideo.objects.filter(watched_as_ad__gt=0).filter(category_id=cat['id']).count()
                    total = ProcessorVideo.objects.filter(category_id=cat['id']).aggregate(Sum('watched_as_ad'))['watched_as_ad__sum']
                    category_names.append(cat['name'])
                    category_counts.append(unique/total)
                    #category_counts.append(ProcessorVideo.objects.filter(watched_as_ad__gt=0).filter(category_id=cat['id']).count())
                    watched_as_ad.append(unique)
                    watched_as_video.append(total)
                    #> Book.objects.annotate(num_authors=Count('authors')).filter(num_authors__gt=1)
                    #watched_as_video.append(ProcessorVideo.objects.filter(watched_as_video__gt=0).filter(category_id=cat['id']).count())

        # conn_cyads = MySQLdb.connect(host='db.misc.iastate.edu', user='xander', passwd='iam@cyadsDb123', database='cyads_processor')
        # cursor_cyads = conn_cyads.cursor()
        # sql_query =   '''
        #         SELECT
        #
        #             v.url AS url,
        #         --    b.state_name AS state,
        #         --    b.batch_id AS batch_id,
        #             DATE(FROM_UNIXTIME(batch.start_timestamp)) AS batch_startime,
        #             -- MIN(DATE(FROM_UNIXTIME(request_timestamp))) AS first_encounter,
        #             -- MAX(DATE(FROM_UNIXTIME(request_timestamp))) AS last_encounter,
        #             COUNT(ad_video_id) AS times_encountered
        #         --    cat.name AS category_name,
        #         --    cat.cat_id AS category_id,
        #         --    v.title AS title,
        #         --    v.description AS description,
        #         --    chan.channel_id AS channel_id,
        #         --    chan.name AS channel_name
        #         FROM
        #             processor_ad_found_watchlog AS watchlog
        #                 INNER JOIN
        #             processor_batch batch ON watchlog.batch_id = batch.id
        #         --        INNER JOIN
        #         --    processor_locations batch_state_mapping ON batch.location_id = batch_state_mapping.id
        #                 INNER JOIN
        #             batch_state_mapping b ON watchlog.batch_id = b.batch_id
        #                 INNER JOIN
        #             processor_videos v ON watchlog.ad_video_id = v.id
        #                 LEFT JOIN
        #             processor_categories cat ON v.category_id = cat.id
        #         --        LEFT JOIN
        #         --    processor_channels chan ON v.channel_id = chan.id
        #         WHERE
        #             v.watched_as_ad > 0 AND cat.cat_id = 25
        #
        #         GROUP BY  batch_startime, url
        #
        #         ORDER BY batch_startime ASC
        #         '''
        # byDateDF = pd.read_sql_query(sql_query, con=conn_cyads)
        # byDateDf = byDateDF.groupby()
        data = {
            'watched_as_ad': watched_as_ad,
            'watched_as_video': watched_as_video,
            'unique_videos': category_counts,
            'category_names': category_names,
        }
        # video_data = {
        #     'numVideos': ProcessorVideo.objects.all().count(),
        #     'numCategories': ProcessorCategories.objects.all().count(),
        #     'categories': category_counts
        #     'videos': videos.head().to_dict('records'),
        #
        #     }
        #videos = serializers.serialize('json', ProcessorVideo.objects.all(), fields=('title', 'category'))
        return Response(data)

class ByDateData(APIView):
        authentication_classes = []
        permission_classes = []

        def get(self, request, format=None):

            return Response(data)
