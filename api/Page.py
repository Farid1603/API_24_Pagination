from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'p'
    page_size_query_param='s'
    max_page_size = 7
    last_page_strings= 'END'

# class MyPageNumberPagination1(PageNumberPagination):
#     page_size = 7

# class Mypagelayout(PageNumberPagination):
#     page_size = 3