from .basepage import BasePage
from playwright.sync_api import expect


class VerifyOtp(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    
    def fill_code(self, code):
        otp_field = self.page.locator("input[data-input-otp='true']")
        otp_field.fill(code)
        #Verify the otp field has been filled.
        expect(otp_field).to_have_value(code)
        
    def confirm_continue(self):
        self.page.locator("button[type='submit']").click()
        