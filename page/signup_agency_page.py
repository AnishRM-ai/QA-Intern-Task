from .basepage import BasePage
from playwright.sync_api import expect

class SignUpAgency(BasePage):
    def __init__(self, page):
        super().__init__(page)
        
    def fill_agency(self, agencyname, role, email, website, address, region_operation):
        self.page.get_by_label("Name").fill(agencyname)
        self.page.get_by_label("Role in Agency").fill(role)
        self.page.get_by_label("Email Address").fill(email)
        self.page.get_by_label("Website").fill(website)
        self.page.get_by_placeholder("Enter Your Agency Address").fill(address) 
        
        # Handle combobox
        self.select_region_operation(region_operation)
    
    
    def select_region_operation(self, regions):
        combobox = self.page.locator("button[role='combobox']")
        combobox.click()
        expect(combobox).to_have_attribute("aria-expanded", "true")

        #Get the dropdown id from aria-controls
        dropdown_id = combobox.get_attribute("aria-controls")

        dropdown = self.page.locator(f"#{dropdown_id}")

        search = dropdown.locator("input").first
        expect(search).to_be_visible()

        for region in regions:
            search.fill(region)

            # Click the visible dropdown option.
            option = dropdown.locator("div", has_text=region).first
            option.wait_for(state="visible")
            option.click()

            search.fill("")

            chip = (
            self.page.locator("div", has_text=region)
            .filter(has_not=dropdown)
            .first
        )
            expect(chip).to_be_visible()

            
            
        
        
    def next_step(self):
        self.page.locator('button[type="submit"]').click()