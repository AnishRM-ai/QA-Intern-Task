from .basepage import BasePage

class SignUpPagePersonal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    def fill_personal_details(self,firstname, lastname, email, phoneNumber, password, confirmPassword):
        self.page.locator("input[name='firstName']").fill(firstname)
        self.page.locator("input[name='lastName']").fill(lastname)
        self.page.locator("input[name='email']").fill(email)
        self.page.locator("input[name='phoneNumber']").fill(phoneNumber)
        self.page.locator("input[name='password']").fill(password)
        self.page.locator("input[name='confirmPassword']").fill(confirmPassword)
        
    
    def next(self):
        self.page.locator("button[type='submit']").click()