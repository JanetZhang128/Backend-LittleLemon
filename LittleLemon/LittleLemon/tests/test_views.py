from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json 
from django.urls import reverse

# test for MenuView 
class MenuItemsViewTest(TestCase):
    def setup(self):
        Menu.objects.create(title="meatball", price=100, inventory=101)
        Menu.objects.create(title="salomsoup", price=150, inventory=102)
    
    def test_getall(self):
        data = Menu.objects.all()
        serialized_data = MenuSerializer(data, many= True)
        serialized_data = json.loads(json.dumps(serialized_data.data))

        response = self.client.get(reverse('menu'))
        response = str(response.content, 'UTF-8')
        response = json.loads(response)

        self.assertEqual(response,serialized_data)


