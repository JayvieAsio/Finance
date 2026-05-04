from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

@api_view(['GET', 'POST'])
def transactions(request):
    if request.method == 'GET':
        items = Transaction.objects.all()
        serializer = TransactionSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)