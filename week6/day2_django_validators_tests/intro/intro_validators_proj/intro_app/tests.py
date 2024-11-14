from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Pokemon

class PokemonTest(TestCase):
    def test_01_create_pokemon_instance(self):
        new_pokemon = Pokemon(name='Squirtle', description='A turtle in poke.')
        try:
            new_pokemon.full_clean()
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            print(e.message_dict)
            self.fail()

    def test_02_create_pokemon_incorrect_name(self):
        new_pokemon = Pokemon(name='Squ1rtle', description='A turtle in poke.')

        try:
            new_pokemon.full_clean()
        except ValidationError as e:
            self.assertTrue("Improper name format." in e.message_dict['name']) #Must be same as the validator function message