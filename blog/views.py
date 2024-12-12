from blog.models import Blog, Comment
from blog.serializers import BlogSerializer, CommentSerializer
from rest_framework import mixins, generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.

#========================================================NESTED SERIALIZATION==================================================================================================================================

#By using mixins
# class BlogView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#         queryset = Blog.objects.all()
#         serializer_class = BlogSerializer

#         def get(self, request):
#             return self.list(request)

#         def post(self, request):
#             return self.create(request)


# class CommentView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#         queryset = Comment.objects.all()
#         serializer_class = CommentSerializer

#         def get(self, request):
#             return self.list(request)

#         def post(self, request):
#             return self.create(request)
#--------------------------------------------------------------------

#Using Generics
# class BlogView(generics.ListCreateAPIView):
#         queryset = Blog.objects.all()
#         serializer_class = BlogSerializer


# class CommentView(generics.ListCreateAPIView):
#         queryset = Comment.objects.all()
#         serializer_class = CommentSerializer
#----------------------------------------------------------------------


#By usng ViewSet
# class BlogView(viewsets.ViewSet):
#     def list(self, request,):
#         queryset = Blog.objects.all()
#         serializer_class = BlogSerializer(queryset, many=True)
#         return Response(serializer_class.data)

#     def create(self, request):
#         serializer_class = BlogSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors)

#     def retrieve(self, request, pk=None):
#         queryset = get_object_or_404(Blog, pk=pk)
#         serializer_class = BlogSerializer(queryset)
#         return Response(serializer_class.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         queryset = get_object_or_404(Blog, pk=pk)
#         serializer_class = BlogSerializer(queryset, data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_200_OK)
#         return Response(serializer_class.errors)
    
#     def delete(self, request, pk=None):
#         queryset = get_object_or_404(Blog, pk=pk)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

# class CommentView(viewsets.ViewSet):
#     def list(self, request,):
#         queryset = Comment.objects.all()
#         serializer_class = CommentSerializer(queryset, many=True)
#         return Response(serializer_class.data)

#     def create(self, request):
#         serializer_class = CommentSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors)

#     def retrieve(self, request, pk=None):
#         queryset = get_object_or_404(Blog, pk=pk)
#         serializer_class = CommentSerializer(queryset)
#         return Response(serializer_class.data, status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         queryset = get_object_or_404(Blog, pk=pk)
#         serializer_class = CommentSerializer(queryset, data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_200_OK)
#         return Response(serializer_class.errors)
    
#     def delete(self, request, pk=None):
#         queryset = get_object_or_404(Blog, pk=pk)
#         queryset.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#----------------------------------------------------------------------------------------------------------------------------------

# By Using ModelViewSet
class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
#-----------------------------------------------------------------------------------------------------------------------------------
