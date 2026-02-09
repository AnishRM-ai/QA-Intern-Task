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
        combobox = self.page.locator("button[role='combobox']")
        combobox.click()
        expect(combobox).to_have_attribute("aria-expanded", "true")

    # Get the radix dropdown id from aria-controls
        dropdown_id = combobox.get_attribute("aria-controls")

        # Scope everything to the actual dropdown portal
        dropdown = self.page.locator(f"#{dropdown_id}")

        search = dropdown.locator("input").first
        expect(search).to_be_visible()

        for countries in country:
            search.fill(countries)

            # Click the visible dropdown option 
            option = dropdown.locator("div", has_text=countries).first
            option.wait_for(state="visible")
            option.click()

            search.fill("")

            chip = (
            self.page.locator("div", has_text=countries)
            .filter(has_not=dropdown)
            .first
        )
            expect(chip).to_be_visible()
    
    
    def select_institute_type(self, institute):
        institute_checkbox = self.page.get_by_role("checkbox", name=institute)
        institute_checkbox.check()
        
        expect(institute_checkbox).to_be_checked()
        
    def upload_documents(self, file_path):
        if isinstance(file_path, str):
            file_path = [file_path]
            
        #file input
        file_input = self.page.locator("input[type='file']")
        
        for i, file_path in enumerate(file_path):
            file_input.nth(i).set_input_files(file_path)
            
            
    
    def add_documents(self, file_path):
        add_button = self.page.get_by_role("button", name="Add Documents")
        add_button.click()
        
        # Wait for new input to appear
        file_inputs = self.page.locator("input[type='file']")
        new_input = file_inputs.last

        new_input.set_input_files(file_path)
        
    def final_submit(self):
        self.page.locator("button[type='submit']").click()