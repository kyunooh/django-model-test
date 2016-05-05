from django.test.testcases import LiveServerTestCase
from selenium import webdriver


class TravisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def test_title_is_selenium_test(self):
        self.browser.get(self.live_server_url)
        self.assertEquals("selenium test", self.browser.title)
