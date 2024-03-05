from django.urls import path
from .views import NoteCreateAPIView, NoteRetrieveUpdateAPIView

urlpatterns = [
    path("notes/", NoteCreateAPIView.as_view(), name="note-list-create"),
    path(
        "notes/<int:pk>/",
        NoteRetrieveUpdateAPIView.as_view(),
        name="note-retrieve-update",
    ),
]
