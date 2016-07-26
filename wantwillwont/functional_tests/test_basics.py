from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from pyvirtualdisplay import Display
from selenium import webdriver


class HomePageTest(StaticLiveServerTestCase):
    def setUp(self):
        self.display = Display(visible=0, size=(1920, 1080))
        self.display.start()
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

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