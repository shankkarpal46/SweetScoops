from django.test import TestCase
from .models import Icecream

# Create your tests here.
def add(a,b):
    return a+b

class IcecreamTest(TestCase):
    def setUp(self):
        self.icecream = Icecream.objects.create(icecream_name = "name for test",
                                                icecream_description = "description for test",
                                                icecream_price = "5000")
        
    def test_add_icecream(self):
        icecream = Icecream.objects.get(id=self.icecream.id)
        self.assertEqual(self.icecream,icecream)

    def test_all(self):
        icecream = Icecream.objects.all()
        ans = len(icecream) > 0
        self.assertTrue(ans)

            
    def test_add(self):
        expect = 11
        actual = add(5,6) #value should match.
        self.assertEqual(expect,actual)

    def test_update_product(self):
        icecream=Icecream.objects.get(id=self.icecream.id)
        self.assertEqual(self.icecream,icecream)

    def test_delete_icecream(self):
        icecream = Icecream.objects.get(id=self.icecream.id)
        self.assertEqual(self.icecream,icecream)

    



    