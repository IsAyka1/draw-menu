from django.test import TestCase

# Create your tests here.

from my_menu.models import Menu


class MenuTests(TestCase):
    """Contact model tests."""

    def test_str(self):
        contact = Menu(name='Elems')
        self.assertEquals(
            str(contact),
            'Elems',
        )
