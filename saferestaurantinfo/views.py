from django.shortcuts import render
from django.views.generic.base import TemplateView, View
import pymysql
import json
from datetime import date, timedelta
from django.http import HttpResponse, JsonResponse

# Create your views here.
class HomeView(TemplateView):
    template_name = 'saferestaurantinfo/index.html'

class RestaurantListView(TemplateView):
    template_name = 'saferestaurantinfo/saferestaurantlist.html'

class SafeRestaurantInfo(View):
    def get(self, request, region):
        connection_info = { 'host': 'localhost', 'user': 'root', 'password': 'Kweondh123!', 'db': 'saferestaurant', 'charset': 'utf8' }
        conn = pymysql.connect(**connection_info)
        cursor = conn.cursor()

        sql = 'SELECT * from safe_restaurant'
        cursor.execute(sql)
        conn.commit()
        datas=[]
        modified_data=[]
        datas = cursor.fetchall()

        for row in datas:
            if (row[2]+' '+row[3]).startswith(region):
                values = (row[0],row[2]+' '+row[3],row[4],row[6].isoformat(),row[7]+' '+row[8],row[9],row[11])
                modified_data.append(values)
        
        json_data=json.dumps(modified_data, ensure_ascii=False)

        return HttpResponse(json_data, content_type="application/json;charset=utf-8")