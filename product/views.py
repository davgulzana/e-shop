from rest_framework import permissions as p, viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, \
    CreateAPIView, UpdateAPIView, DestroyAPIView

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, CreateUpdateProductSerializer

# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# class ProductsList(APIView): #View
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)


# class ProductsList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ProductDetail(RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class CreateProduct(CreateAPIView):
#     queryset = Product.objects.all()
#     permission_classes = [p.IsAdminUser]
#     serializer_class = CreateUpdateProductSerializer
#
#
# class UpdateProduct(UpdateAPIView):
#     queryset = Product.objects.all()
#     permission_classes = [p.IsAdminUser]
#     serializer_class = CreateUpdateProductSerializer
#
#
# class DeleteProduct(DestroyAPIView):
#     queryset = Product.objects.all()
#     permission_classes = [p.IsAdminUser]


class CategoriesList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ProductSerializer
        return CreateUpdateProductSerializer

    def get_permissions(self):
        # if self.action == 'list' or self.action == 'retrieve':
        if self.action in ['list', 'retrieve']:
            permissions = []
        else:
            permissions = [p.IsAdminUser]
        return [permission() for permission in permissions]

