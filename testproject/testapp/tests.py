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

    
    def test_full_restore(self):
        animal = G(Animal)
        jungle = G(Jungle, apex_predator=animal)
        animal_id = animal.id
        jungle_id = jungle.id
        animal.delete()

        restore_animal_response = Animal.objects.filter(pk=animal_id).first().full_restore()
        should_restore_objects_count = 2
        should_restore_objects_count_type = {'jungle':1, 'animal':1}
        self.assertEqual(should_restore_objects_count, restore_animal_response[0])
        self.assertEqual(should_restore_objects_count_type.keys(), restore_animal_response[1].keys())
        self.assertEqual(list(should_restore_objects_count_type.values()), list(restore_animal_response[1].values()))
