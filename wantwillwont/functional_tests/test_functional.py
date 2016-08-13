import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.utils.translation import activate
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from django.conf import settings


class HomePageTest(StaticLiveServerTestCase):
    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url('home'))
        self.assertIn('Want Will Won\'t', self.browser.title)

    def test_home_files(self):
        self.browser.get(self.live_server_url + '/robots.txt')
        self.assertNotIn('Not Found', self.browser.title)
        self.browser.get(self.live_server_url + '/humans.txt')
        self.assertNotIn('Not Found', self.browser.title)


class TestGoogleLogin(StaticLiveServerTestCase):
    fixtures = ['allauth_fixture']

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.browser = webdriver.Chrome()
        self.browser.wait = WebDriverWait(self.browser, 3)
        self.browser.implicitly_wait(3)
        activate('en')

    def tearDown(self):
        self.browser.quit()
        self.display.stop()

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located((By.ID, element_id)))

    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable((By.ID, element_id)))

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)
    
    def user_login(self):
        import json
        with open(os.path.join(settings.BASE_DIR, 'fixtures') + '/google_user.json') as f:
            credentials = json.loads(f.read())
        if self.get_button_by_id('next'):
            self.get_element_by_id('Email').send_keys(credentials['Email'])
            self.get_button_by_id('next').click()
        if self.get_button_by_id('signIn'):
            self.get_element_by_id('Passwd').send_keys(credentials['Passwd'])
            self.get_button_by_id('signIn').click()


    def test_google_login(self):
        self.browser.get(self.get_full_url('home'))
        google_login = self.get_element_by_id('google_login')
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('logout')
        self.assertEqual(google_login.get_attribute('href'), self.live_server_url + '/accounts/google/login/')
        google_login.click()
        self.user_login()
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('google_login')
        # Otherwise Google's "Have offline access" prompt ruins it: http://stackoverflow.com/questions/28052155/always-have-offline-access-google-oauth-2
        if 'localhost' not in self.live_server_url:
            google_logout = self.get_element_by_id('logout')
            google_logout.click()
            google_login = self.get_element_by_id('google_login')
