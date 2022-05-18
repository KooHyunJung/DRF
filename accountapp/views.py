from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from accountapp.models import Book
from accountapp.serializers import BookSerializer
from rest_framework.generics import get_object_or_404
# DRF mixins
from rest_framework import generics
from rest_framework import mixins


# DRF FBV 방식
@api_view()
def hello_world_drf(request):
    return Response({'msg': 'hello_world!!!'})


# DRF CBV 방식
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


# DRF mixins
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookAPIMixins(mixins.RetrieveModelMixin , generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # 책 1권 수정 메소드
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # 책 1권 delete 메소드
    def delete(self, request, *args, **kwargs):
        return self.destory(request, *args, **kwargs)
