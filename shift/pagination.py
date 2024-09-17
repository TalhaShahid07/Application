# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response

# class CustomPagination(PageNumberPagination):
#     page_size = 10  # Default page size
#     page_size_query_param = 'page_size'  # Allow users to customize page size
#     max_page_size = 100  # Max size allowed
#     def get_paginated_response(self, data):
#         return Response({
#             'count': self.page.paginator.count,
#             'previous': self.get_previous_link(),
#             'next': self.get_next_link(),
#             'results': data
#         })

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class ShiftPagination(PageNumberPagination):
    page_size = 10  # Number of results per page (adjust as needed)

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'results': data
        })