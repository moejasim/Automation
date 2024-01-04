from BrainBucketTests.webelements.UIElement import UIElement as Element
from selenium.webdriver.support.select import Select


class Dropdown(Element):
    def __init__(self, browser, by, locator):
        super().__init__(browser, by, locator)

    def select_by_text(self, option):
        """
        Selects the option in dropdown by visible text
        :param option: option to select
        """
        Select(self.get_element()).select_by_visible_text(option)

    def select_by_value(self, value):

        Select(self.get_element()).select_by_value(value)

    def select_by_index(self, index):

        Select(self.get_element()).select_by_index(index)

    def deselect_by_text(self, option):

        select = Select(self.get_element())
        select.deselect_by_visible_text(option)

    def deselect_by_value(self, value):

        select = Select(self.get_element())
        select.deselect_by_value(value)

    def deselect_by_index(self, index):

        select = Select(self.get_element())
        select.deselect_by_index(index)