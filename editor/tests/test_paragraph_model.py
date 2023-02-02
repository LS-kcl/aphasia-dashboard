from django.test import TestCase
from editor.models import Paragraph
from django.core.exceptions import ValidationError

class ParagraphModelTestCase(TestCase):
    """Unit tests for the Paragraph model"""
    def test_valid_paragraph(self):
        self._assert_paragraph_is_valid()

    def test_text_cannot_not_exceed_520_characters(self):
        self.paragraph.text = 'x' * 521
        self._assert_paragraph_is_invalid()

    def test_text_can_be_520_characters(self):
        self.paragraph.text = 'x' * 520
        self._assert_paragraph_is_valid()

    def test_text_cannot_not_be_blank(self):
        self.paragraph.text = ""
        self._assert_paragraph_is_invalid()

    """Auxillary methods"""
    def setUp(self):
        self.paragraph = Paragraph.objects.create(
            text="""Rem commodi ratione deleniti nemo 
                    dolore repellendus. Laudantium eaque ipsa 
                    repellat. Magni blanditiis recusandae qui 
                    sed est voluptates nihil."""
                )

    def _assert_paragraph_is_valid(self):
        try:
            self.paragraph.full_clean()
        except (ValidationError):
            self.fail("The paragraph should be valid")

    def _assert_paragraph_is_invalid(self):
        # This should raise an error
        with self.assertRaises(ValidationError):
            self.paragraph.full_clean()
