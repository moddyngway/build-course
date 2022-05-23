import datetime
from collections import OrderedDict

from django.db.models import Min, Max, Sum, Avg
from django.db.models.functions import TruncMonth, TruncYear
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers

from core.models import Feedback
from projects.models import Check
from django.shortcuts import render
from django.http import HttpResponse
from .fusioncharts import FusionCharts
from dateutil.relativedelta import relativedelta


def chart(request):
    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Sum of checks"
    chartConfig["xAxisName"] = "Date"
    chartConfig["yAxisName"] = "Sum prices"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()

    d = Check.objects.annotate(month=TruncMonth('date')
                               ).values('month'
                                        ).annotate(c=Avg('price')
                                                   ).values('month', 'c')

    for di in d:
        chartData[di['month'].strftime('%b %Y')] = di['c']

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts.
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)

    column2D = FusionCharts("column2d", "ex1", "2500", "800", "chart-1", "json", dataSource)

    return render(request, 'dashboard.html', {'output': column2D.render(), 'chartTitle': 'Simple Chart Using Array'})
