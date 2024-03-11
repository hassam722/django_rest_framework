from django.shortcuts import render
from .models import CarList,ShowRoomList,Reviews
from .api_files.serializer import CarListSerializer,ShowRoomListSerializer,ReviewSerializer
from .api_files.permission import ReviewUserOrReadOnlyPermission

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,DjangoModelPermissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
# Create your views here.


# class Review_list_view(viewsets.ViewSet):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [ReviewUserOrReadOnlyPermission]
    

#     def list(self, request):
#         queryset = Reviews.objects.all()
#         serializer = ReviewSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Reviews.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = ReviewSerializer(user)
#         return Response(serializer.data)    

#     def update(self, request, pk=None):
#         queryset = Reviews.objects.all()
#         user = get_object_or_404(queryset,pk = pk)
#         serializer = ReviewSerializer(user,request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)


class Review_list_view(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]


    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
class Review_detail_view(RetrieveModelMixin,UpdateModelMixin,GenericAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [TokenAuthentication]

    # permission_classes = [DjangoModelPermissions]

    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.update(request, *args, **kwargs)




class ShowRoom_list_view(APIView):
    # permission_classes = [DjangoModelPermissions]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [SessionAuthentication]

    def get(self,request):
        showroomlist = ShowRoomList.objects.all()
        serializer = ShowRoomListSerializer(showroomlist, many=True,context  ={'request':request})
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ShowRoomListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    

class ShowRoomDetailView(APIView):
    def get(self,request,pk):
        try:
            showroom = ShowRoomList.objects.get(pk = pk)
        except ShowRoomList.DoesNotExist:
            return Response(status=404)
        serializer = ShowRoomListSerializer(showroom)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            showroom = ShowRoomList.objects.get(pk = pk)
        except ShowRoomList.DoesNotExist:
            return Response(status=404)
        serializer = ShowRoomListSerializer(showroom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



@api_view(['GET','POST'])
def carlist_view(request):
    if request.method=='GET':
        carlist = CarList.objects.all()
        serializer = CarListSerializer(carlist, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['GET','PUT','DELETE'])
def carlist_detail_view(request,pk):
    if request.method == 'GET':
        carlist = CarList.objects.get(pk=pk)
        serializer = CarListSerializer(carlist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        carlist = CarList.objects.get(pk=pk)
        serializer = CarListSerializer(carlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        carlist = CarList.objects.get(pk=pk)
        carlist.delete()
        return Response(status=204)