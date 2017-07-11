from django.test import TestCase
from django.urls import reverse


class LoginViewTest(TestCase):
    def test_uses_login_template(self):
        url = reverse('member:login')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'member/login.html')