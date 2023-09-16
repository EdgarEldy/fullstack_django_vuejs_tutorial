from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math


# vous pouvez remplacer page_size, max_page_size à partir des paramètres de requête d'url \
# pour le rendre plus dynamique

class CustomPagination(PageNumberPagination):
    # page_size = 5  # default page size
    # max_page_size = 1000 # default max page size
    # si vous souhaitez des éléments dynamiques par page à partir de la demande, vous devez l'ajouter
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        # si vous voulez afficher la taille de la page dans la réponse, ajoutez simplement ces 2 lignes
        if self.request.query_params.get('page_size'):
            self.page_size = int(self.request.query_params.get('page_size'))

        # vous pouvez compter la page totale de la demande par total et page_size
        total_page = math.ceil(self.page.paginator.count / self.page_size)

        # revoyer la response
        return Response({
            'count': self.page.paginator.count,
            'current_rows': len(data),
            'page_max': total_page,
            'page_size': self.page_size,
            'page_current': self.page.number,
            'previous': self.get_previous_link(),
            'next': self.get_next_link(),
            'results': data
        })
