from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

# control the format of the response by using [Accept] header.
#   http http://127.0.0.1:8000/snippets/ Accept:application/json
#  => http http://127.0.0.1:8000/snippets.json  # JSON suffix
#   http http://127.0.0.1:8000/snippets/ Accept:text/html
#  => http http://127.0.0.1:8000/snippets.api  # Browsable API suffix
# control the format of the request by using [Content-Type] header.
#   http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"  # POST using form data
#   http --debug --json POST http://127.0.0.1:8000/snippets/ code="print(456)"  # POST using JSON
#   --debug can see the request type in request headers.
urlpatterns = format_suffix_patterns(urlpatterns)
