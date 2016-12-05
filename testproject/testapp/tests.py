from django.test import TestCase
from django_dynamic_fixture import G
from testapp.models import Animal, Jungle, AnimalInJungle


class TestModel(TestCase):

    def test_delete(self):
        animal = G(Animal)
        jungle = G(Jungle, apex_predator=animal)
        animal_id = animal.id
        jungle_id = jungle.id
        animal.delete()

        deleted_animal = Animal.objects.filter(pk=animal_id).first()
        deleted_jungle = Animal.objects.filter(pk=jungle_id).first()
        self.assertTrue(deleted_animal.deleted)
        self.assertTrue(deleted_jungle.deleted)

        self.assertRaises(Exception, Animal.objects.get(pk=animal_id))
        self.assertRaises(Exception, Jungle.objects.get(pk=jungle_id))

    def test_final_delete(self):
        animal = G(Animal)
        jungle = G(Jungle, apex_predator=animal)
        animal_id = animal.id
        jungle_id = jungle.id
        animal.delete(final=True)

        self.assertEqual(Animal.objects.count(), 0)
        self.assertEqual(Jungle.objects.count(), 0)
