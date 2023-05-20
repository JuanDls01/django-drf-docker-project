import math
from rest_framework import pagination, response as res


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"
    page_query_param = "page"

    def get_paginated_response(self, data):
        previous_page_number = (
            self.page.previous_page_number() if self.page.has_previous() else None
        )
        next_page_number = (
            self.page.next_page_number() if self.page.has_next() else None
        )
        num_pages = (
            math.ceil(self.page.paginator.count / self.get_page_size(self.request))
            if math.ceil(self.page.paginator.count / self.get_page_size(self.request))
            >= 1
            else 1
        )
        return res.Response(
            {
                "data": data,
                "pagination": {
                    "num_pages": num_pages,
                    "page": self.page.number,
                    "next_page": next_page_number,
                    "previous_page": previous_page_number,
                },
            }
        )
