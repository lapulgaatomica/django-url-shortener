import re
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .views import HomePageView, CreateUrlView

class HomepageTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Home page')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'visit')

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class CreateUrlTest(TestCase):
    def setUp(self):
        url = reverse('create_url')
        self.response = self.client.get(url)

    def test_create_url_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_create_url_template(self):
        self.assertTemplateUsed(self.response, 'createurl.html')

    def test_create_url_page_contains_correct_html(self):
        self.assertContains(self.response, 'Shorten Url')

    def test_create_url_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Short form')

    def test_create_url_resolves(self):
        view = resolve('/shorten-url/')
        self.assertEqual(
            view.func.__name__,
            CreateUrlView.as_view().__name__
        )

class SaveAndVisitUrlTest(TestCase):
    def setUp(self):
        self.first_response = self.client.post(reverse('save_url'), {
            'url': 'google.com'
        })
        first_response_content = str(self.first_response.content)
        first_response_visit_link = re.findall('visit/\w+', first_response_content)[0]
        self.uuid = first_response_visit_link.lstrip('visit/')
        self.response = self.client.get('/visit/'+self.uuid)

    def test_create_url_view_after_url_is_submitted(self):
        self.assertEqual(self.first_response.status_code, 200)

    def test_save_url_template(self):
        self.assertTemplateUsed(self.first_response, 'home.html')

    def test_save_url_page_contains_correct_html(self):
        self.assertContains(self.first_response, 'visit')

    def test_redirect(self):
        self.assertRedirects(self.response, 'https://google.com', fetch_redirect_response=False)
