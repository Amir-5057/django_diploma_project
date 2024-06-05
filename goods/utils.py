from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from goods.models import Products
def q_search(query):
    results = Products.objects.filter(name__icontains=query)  # Adjust the filter condition based on your model fields
    return results


