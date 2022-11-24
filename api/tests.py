from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.reverse import reverse_lazy

from .models import Verb
from .serializers import VerbSerializer

# <----------- Endpoints Definitions ------------>
VERBS_URL = reverse_lazy('search')

def detail_url(verb_id):
    """Return verb datail endpoint"""
    return reverse_lazy('retrieve', args=[verb_id])

def search_url(keyword):
    """Return the search endpoint"""
    return f'{VERBS_URL}?search={keyword}'


# <----------- Model Test ------------>
class VerbModelTest(TestCase):
    """
    Testing the Verb model
    """
    def test_verb_string(self):
        """Testing the string representation of the Verb model"""
        verb = Verb.objects.create(classification='regular', present_simple='create', simple_past='created', past_participle='created')
        self.assertEqual(str(verb), verb.present_simple)


# <----------- API Test ------------>
class SearchListTest(TestCase):
    """
    Testing anyone can read the list of verbs or retrieve a specific verb
    """
    def setUp(self) -> None:
        """Setting a client to test the endpoints"""
        self.client = APIClient()

    def test_list_verb(self):
        """Getting the list of verbs"""
        verb1 = Verb.objects.create(classification='regular', present_simple='create', simple_past='created', past_participle='created')
        verb2 = Verb.objects.create(classification='regular', present_simple='list', simple_past='listed', past_participle='listed')

        response = self.client.get(VERBS_URL)

        verbs = Verb.objects.all().order_by('id')
        serializer = VerbSerializer(verbs, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_method_not_allowed(self):
        """A post request must raise an error"""
        payload = {
            'classification': 'regular', 
            'present_simple': 'create', 
            'simple_past': 'created', 
            'past_participle': 'created'
        }

        response = self.client.post(VERBS_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_search_verb_by_present_simple(self):
        """Search the verb passed as argument to the endpoint"""
        verb1 = Verb.objects.create(classification='regular', present_simple='create', simple_past='created', past_participle='created')
        verb2 = Verb.objects.create(classification='regular', present_simple='love', simple_past='loved', past_participle='loved')
        keyword = 'lov'
        response = self.client.get(search_url(keyword))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer1 = VerbSerializer(verb1)
        serializer2 = VerbSerializer(verb2)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0], serializer2.data)
        self.assertNotEqual(response.data[0], serializer1.data)
        


# <----------- API Test ------------>
class SingleObjectTest(TestCase):
    """
    Testing anyone can read the list of verbs or retrieve a specific verb
    """
    def setUp(self) -> None:
        """Setting a client to test the endpoints"""
        self.client = APIClient()

    def test_retrive_verb(self):
        """Retriving the verb details"""
        verb = Verb.objects.create(classification='regular', present_simple='create', simple_past='created', past_participle='created')
        
        response = self.client.get(detail_url(verb.id))

        serializer = VerbSerializer(verb)
        self.assertEqual(response.data, serializer.data)

    def test_put_method_not_allowed(self):
        """A put request must raise an error"""
        verb = Verb.objects.create(classification='regular', present_simple='create', simple_past='created', past_participle='created')
        payload = {
            'id': 1,
            'classification': 'irregular', 
            'present_simple': 'live', 
            'simple_past': 'lived', 
            'past_participle': 'lived'
        }

        response = self.client.post(detail_url(verb.id), payload)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch_method_not_allowed(self):
        """A patch request must raise an error"""
        verb = Verb.objects.create(classification='regular', present_simple='create', simple_past='created', past_participle='created')
        payload = {
            'id': 1,
            'classification': 'irregular', 
        }

        response = self.client.patch(detail_url(verb.id), payload)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_method_not_allowed(self):
        """A post delete must raise an error"""
        verb = Verb.objects.create(classification='regular', present_simple='create', simple_past='created', past_participle='created')
        payload = {
            'id': 1,
            'classification': 'irregular', 
        }

        response = self.client.patch(detail_url(verb.id), payload)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    




