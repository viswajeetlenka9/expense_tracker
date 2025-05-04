from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Income
from .serializers import IncomeSerializer


class IncomeListView(APIView):

    def get(self, request):
        incomes = Income.objects.all()
        serializer = IncomeSerializer(incomes, many=True)
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncomeDetailView(APIView):

    def get(self, request, id):
        try:
            income = Income.objects.get(id=id)
        except Income.DoesNotExist:
            return Response({"error": f"Income doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = IncomeSerializer(income)
        return Response(serializer.data)
    
    def patch(self, request, id):
        try:
            income = Income.objects.get(id=id)
        except Income.DoesNotExist:
            return Response({"error": f"Income doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = IncomeSerializer(instance=income, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            income = Income.objects.get(id=id)
        except Income.DoesNotExist:
            return Response({"error": f"Income doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        income.delete()
        return Response({"message": f"Income with id : {id} is deleted"}, 
                        status=status.HTTP_200_OK)
        