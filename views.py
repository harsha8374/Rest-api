from rest_framework import viewsets
from .models import PersonalDetail
from .serializers import PersonalDetailSerializer

class PersonalDetailViewSet(viewsets.ModelViewSet):
    queryset = PersonalDetail.objects.all()
    serializer_class = PersonalDetailSerializer
