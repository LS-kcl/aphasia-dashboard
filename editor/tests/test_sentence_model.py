from django.test import TestCase
from editor.models import Set, Sentence
from django.core.exceptions import ValidationError

# Create your tests here.
class SentenceModelTestCase(TestCase):
    """Unit tests for the Sentence model"""
    def test_valid_sentence(self):
        self._assert_sentence_is_valid()

    def test_text_cannot_not_exceed_520_characters(self):
        self.sentence.text = 'x' * 521
        self._assert_sentence_is_invalid()

    def test_text_can_be_520_characters(self):
        self.sentence.text = 'x' * 520
        self._assert_sentence_is_valid()

    def test_text_cannot_not_be_blank(self):
        self.sentence.text = ""
        self._assert_sentence_is_invalid()

    """Auxillary methods"""
    def setUp(self):
        set = Set.objects.create(title="Sample Title")
        self.sentence = Sentence.objects.create(text="Lorem Ipsum Dolores", parent_set=set)

    def _assert_sentence_is_valid(self):
        try:
            self.sentence.full_clean()
        except (ValidationError):
            self.fail("The sentence should be valid")

    def _assert_sentence_is_invalid(self):
        # This should raise an error
        with self.assertRaises(ValidationError):
            self.sentence.full_clean()
