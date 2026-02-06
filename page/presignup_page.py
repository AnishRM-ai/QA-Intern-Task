from .basepage import BasePage
from playwright.sync_api import expect

class PreSignup(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
    
    def open(self):
        self.visit("https://authorized-partner.vercel.app/register")
        
    def acknowledge_and_continue(self):
        self.page.get_by_role("checkbox").check()
        self.page.get_by_role("button", name="Continue").click()
        
        
    
    