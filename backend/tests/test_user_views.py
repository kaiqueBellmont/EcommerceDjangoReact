from typing import Any

from .base_test import BaseTestSetup, User


class UserViewsFunctionsTest(BaseTestSetup):
    def setUp(self) -> Any:
        self.user = self.make_user(
            username='user for testing',
            password='user$%123',
            email='user@gmail.com'
        )
        return super().setUp()

    def test_register_user(self):
        self.user.save()
        assert isinstance(self.user, User)

    def test_retrieve_created_user(self):
        retrieved_user = User.objects.latest('id')
        assert retrieved_user.email == self.user.email

    def test_get_user_by_id(self):
        user = User.objects.get(pk=self.user.id)
        assert user == self.user

    def test_get_users(self):
        user2 = self.make_user(
            username='user2 for testing',
            password='user2$%123',
            email='user2@gmail.com'
        )
        users = User.objects.all()
        assert self.user, user2 in users

    def test_update_user_profile(self):
        updated_user = User.objects.get(pk=self.user.id)
        updated_user = self.user
        updated_user.email = 'userUPDATED@gmail.com'
        assert self.user.email == updated_user.email

    def test_delete_user(self):
        user = User.objects.latest('id')
        user.delete()
        users = User.objects.all()
        assert user not in users
