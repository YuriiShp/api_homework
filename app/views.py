from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
from app.models import TV, Chair
from app.serializers import TVSerializer, ChairSerializer


class ArtCreateApiView(APIView):

    def post(self, request):
        if request.GET.get('model') == 'tv':
            serializer = TVSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
        elif request.GET.get('model') == 'chair':
            serializer = ChairSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()

        return Response(data=request.GET.get('model'), status=status.HTTP_400_BAD_REQUEST)

class ArtGetApiView(APIView):

    def get(self, request):
        response_data = []
        good_request = False

        if not request.GET.get('model') or not request.GET.get('pk'):
            response_data = [
                TVSerializer(TV.objects.all(), many=True).data,
                ChairSerializer(Chair.objects.all(), many=True).data
            ]

            good_request = True

        elif request.GET.get('model') == 'tv':
            if not request.GET.get('pk'):
                response_data = TVSerializer(TV.objects.all(), many=True).data
            else:
                response_data = TVSerializer(TV.objects.get(pk=request.GET.get('pk'))).data
            good_request = True

        elif request.GET.get('model') == 'chair':
            if not request.GET.get('pk'):
                response_data = ChairSerializer(Chair.objects.all(), many=True).data
            else:
                response_data = ChairSerializer(Chair.objects.get(pk=request.GET.get('pk'))).data
            good_request = True

        if good_request:
            return Response(response_data)

        return Response(data=request.GET, status=status.HTTP_400_BAD_REQUEST)
