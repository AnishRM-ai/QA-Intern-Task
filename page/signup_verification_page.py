from .basepage import BasePage
from playwright.sync_api import expect
import os
class VerificationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
        
    def fill_verification_detail(self, registration_number, prefer_countries, preferred_institution_types, certification_detail):
        self.page.get_by_label("Business Registration Number").fill(registration_number)
        self.select_prefered_countries(prefer_countries)
        self.select_institute_type(preferred_institution_types)
        self.page.get_by_label("Certification Details (Optional)").fill(certification_detail)
        
        
        
    
    def select_prefered_countries(self, country):
        combobox = self.page.get_by_role("combobox")
        combobox.click()
        
        #select the specific region
        self.page.get_by_role("option", name=country, exact=True).click()
        expect(combobox).to_contain_text(country)
    
    
    def select_institute_type(self, institute):
        institute_checkbox = self.page.get_by_role("checkbox", name=institute)
        institute_checkbox.check()
        
        expect(institute_checkbox).to_be_checked()
        
    def upload_documents(self, file_path):
        if isinstance(file_path, str):
            #single file upload
            self.page.locator('input[type="file"]').set_input_files(file_path)
        else:
            #multiple files upload
            self.page.locator('input[type="file"]').set_input_files(file_path)
            
    # def verify_upload_success(self, file_paths):
    #     """ Method to verify upload was successful.
    #     """  
    #     if isinstance(file_paths, str):
    #         file_paths = [file_paths]
            
    #     for file_path in file_paths:
    #         filename = os.path.basename(file_path)
            
    
    def add_documents(self, file_path):
        add_button = self.page.locator("button[type='button']")
        add_button.click()
        
        self.upload_documents(file_path)
    
    def final_submit(self):
        self.page.locator("button[type='submit']").click()