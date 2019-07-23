from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import District
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import DistrictListSerializer, DistrictCreateSerializer
from accounts.permissions import AdminPermissions
from rest_framework import permissions

class DistrictListView(ListAPIView):

    queryset = District.objects.all()
    serializer_class = DistrictListSerializer
    permission_classes = [permissions.IsAuthenticated]

class DistrictCreateView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, AdminPermissions)

    def post(self, request):
        district_data = DistrictCreateSerializer(data=request.data)
        if district_data.is_valid():
            district_data.save(created_by=request.user)
            return Response(district_data.data, status=status.HTTP_201_CREATED)
        return Response(district_data.errors, status=status.HTTP_400_BAD_REQUEST)