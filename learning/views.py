from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, mixins, generics

from .models import Newspaper
from .serializers import NewspaperSerializerOne


class NewspaperListOne(APIView):
    """
    List all newspaper, or create a new newspaper.
    """

    def get(self, request, format=None):
        newspaper = Newspaper.objects.all()
        serializer = NewspaperSerializerOne(newspaper, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NewspaperSerializerOne(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewspaperDetailOne(APIView):
    """
    Retrieve, update or delete a newspaper instance.
    """

    def get_object(self, pk):
        try:
            return Newspaper.objects.get(pk=pk)
        except Newspaper.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        newspaper = self.get_object(pk)
        serializer = NewspaperSerializerOne(newspaper)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        newspaper = self.get_object(pk)
        serializer = NewspaperSerializerOne(newspaper, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        newspaper = self.get_object(pk)
        newspaper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewspaperListTwo(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializerOne

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NewspaperDetailTwo(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializerOne

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class NewspaperListThree(generics.ListCreateAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializerOne


class NewspaperDetailThree(generics.RetrieveUpdateDestroyAPIView):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializerOne





