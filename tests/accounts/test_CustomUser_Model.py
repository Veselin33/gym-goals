from django.core.exceptions import ValidationError
from django.test import TestCase

from accounts.models import CustomUser


class TestCustomUserModel(TestCase):

    def test__invalid_email__raises_validation_error(self):
        user = CustomUser(
            username = 'TestUsername',
            email = 'test-invalid.com',
            password = '123test456',
        )

        with self.assertRaises(ValidationError):
            user.full_clean()



