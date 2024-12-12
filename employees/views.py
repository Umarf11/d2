# from rest_framework.decorators import APIView
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from django.shortcuts import get_object_or_404


# Create your views here.

#-------------------------------------------------------------------ClassBaseFunction------------------------------------------------------------------------------

# class Employees(APIView):
#     def get(self, request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializer(employee, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeeDetail(APIView):
#     def object_get(self, pk):
#         try:        "id": 4,
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         employee = self.object_get(pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.object_get(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.object_get(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#----------------------------------------------------------------------------End-------------------------------------------------------------------------------

#----------------------------------------------------------------------------Mixins---------------------------------------------------------------------------------------
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer        "id": 4,

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.obj        "id": 4,ects.all()        "id": 4,
#     serializer_class = EmployeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self, request, pk):
#         return self.update(request, pk)        "id": 4,

#     def delete(self, request, pk):
#         return self.destroy(request, pk)    

#-----------------------------------------------------------------------End---------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------Generics----------------------------------------------------------------------------------------------------------------------------
#SEPERATE..........
# class Employees(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#COMBINE.........
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#SEPERATE..........
# class EmployeeDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#COMBINE.............
# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#--------------------------------------------------------------------------End-----------------------------------------------------------------------------------------


#---------------------------------------------------------------------------ViewSet----------------------------------------------------------------------------------------------
#VIEWSET
# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serialaizer = EmployeeSerializer(employee, data=request.data)
#         if serialaizer.is_valid():
#             serialaizer.save()
#             return Response(serialaizer.data, status=status.HTTP_200_OK)
#         return Response(serialaizer.errors)
    
#     def delete(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


#MODELVIEWSET
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#-----------------------------------------------------------------------------------------End---------------------------------------------------------------------------------------------
