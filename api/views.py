from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from .models import Verb
from .serializers import VerbSerializer


# <------ Read/Search View ------->
class VerbSearchListAPIView(ListAPIView):
    """
    Api view to search and list verbs
    """
    queryset = Verb.objects.all()    
    serializer_class = VerbSerializer
    filter_backends = [SearchFilter]
    search_fields = ['present_simple']

# <------ Retrieve View ------->
class VerbRetrieveAPIView(RetrieveAPIView):
    """
    Api view to retrieve a specific verb
    """
    queryset = Verb.objects.all() 
    serializer_class = VerbSerializer 







