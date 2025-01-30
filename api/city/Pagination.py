from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CityPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = None
    max_page_size = 10