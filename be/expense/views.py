from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseListView(APIView):

    def get(self, request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data, 
                        status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseDetailView(APIView):

    def get(self, request, id):
        try:
            expense = Expense.objects.get(id=id)
        except Expense.DoesNotExist:
            return Response({"error": f"Expense doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    
    def patch(self, request, id):
        try:
            expense = Expense.objects.get(id=id)
        except Expense.DoesNotExist:
            return Response({"error": f"Expense doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = ExpenseSerializer(instance=expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            expense = Expense.objects.get(id=id)
        except Expense.DoesNotExist:
            return Response({"error": f"Expense doesn't exist with id : {id}"}, 
                            status=status.HTTP_400_BAD_REQUEST)
        expense.delete()
        return Response({"message": f"Expense with id : {id} is deleted"}, 
                        status=status.HTTP_200_OK)
        