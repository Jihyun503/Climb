from django.urls import path
from visit.views import v1

visit = v1.UserVisitViewSet.as_view({"post": "create"})
visit_list = v1.VisitViewSet.as_view({"get": "list"})

urlpatterns = [
    path("", visit, name="visit"),
    path("list/", visit_list, name="visit_list"),
]
