from django.shortcuts import render
from .serializers import HouseDetailsSerializer
from .models import HouseDetails
from datetime import datetime
from rest_framework import generics
from django.http import JsonResponse

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = HouseDetails.objects.all()
    serializer_class = HouseDetailsSerializer

    def post(self, request):
        user_value= request.data['power_consumption']
        value=int(user_value)
        pre_define_value=15
        time = datetime.now()
        request_time = time.time()
        # time is in 24 hours so set the max. and min. on basic of it
        min = time.replace(hour=12, minute=0, second=0, microsecond=0)
        max = time.replace(hour=20, minute=0, second=0, microsecond=0)
        min_range = min.time()
        max_range = max.time()
        serializer = HouseDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        if min_range < request_time < max_range:
            if value > pre_define_value:
               return JsonResponse({
                 'status': 'True'
                 })
        else:
             return JsonResponse({
                'status': 'False'
            })
    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = HouseDetails.objects.all()
    serializer_class = HouseDetailsSerializer




