from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response


# Create and List Notes
class NoteCreateAPIView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        # Get query parameters from request
        title_substring = request.query_params.get("title", None)

        if title_substring:
            queryset = self.queryset.filter(title__icontains=title_substring)
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Retrieve and Update a Note
class NoteRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
