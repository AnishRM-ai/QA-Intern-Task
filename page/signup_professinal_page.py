from .basepage import BasePage

class ProfessionalDetails(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        #locators
        self.select = self.page.locator('select[aria-hidden="true"]')
        self.experience_combobox = self.page.get_by_role("combobox", name="Select Your Experience Level")
        
        
        
        
    def fill_prof_detail(self, experience_level, number_of_student, focus_area, success_metric):
        self.experience_combobox.click()
        self.page.get_by_role("option", name=experience_level).click()
        self.page.locator("input[type='number'][name='number_of_students_recruited_annually']").fill(str(number_of_student))
        self.page.get_by_label("Focus Area").fill(focus_area)
        self.page.locator("input[type='number'][name='success_metrics']").fill(str(success_metric))
        self.page.get_by_label("Career Counseling").click()
        
    
    def next_step(self):
        self.page.locator("button[type='submit']").click()