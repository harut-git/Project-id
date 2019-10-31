
class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_element_by_id(self, element_id):
        self.driver.find_element_by_id(element_id)