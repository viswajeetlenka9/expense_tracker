from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

class CategoryListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CategoryDetailView(APIView):

    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"error": f"Category doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def patch(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"error": f"Category doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"error": f"Category doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        category.delete()
        return Response({"message": f"Category with id : {id} is deleted"}, 
                        status=status.HTTP_200_OK)
        