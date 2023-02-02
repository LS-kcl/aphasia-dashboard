from django.test import TestCase
from editor.models import Set
from django.core.exceptions import ValidationError

# Create your tests here.
class SetModelTestCase(TestCase):
    """Unit tests for the Set model"""
    def test_valid_set(self):
        self._assert_set_is_valid()

    def test_title_cannot_not_exceed_255_characters(self):
        self.set.title = 'x' * 256
        self._assert_set_is_invalid()

    def test_title_can_be_255_characters(self):
        self.set.title = 'x' * 255
        self._assert_set_is_valid()

    def test_title_cannot_not_be_blank(self):
        self.set.title = ""
        self._assert_set_is_invalid()

    """Auxillary methods"""
    def setUp(self):
        self.set = Set.objects.create(title="Sample text")

    def _assert_set_is_valid(self):
        try:
            self.set.full_clean()
        except (ValidationError):
            self.fail("The set should be valid")

    def _assert_set_is_invalid(self):
        # This should raise an error
        with self.assertRaises(ValidationError):
            self.set.full_clean()
