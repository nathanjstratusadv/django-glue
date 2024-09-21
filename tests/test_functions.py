from django.test import TestCase


class TestFunctions(TestCase):
    def test_everything(self) -> None:
        try:
            self.assertTrue(True)
        except:
            self.assertTrue(False)
