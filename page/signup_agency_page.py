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
    
    
    def select_region_operation(self, region):
        """Select region from searchable dropdown."""
        
        # Click the combobox to open dropdown
        combobox = self.page.get_by_role("combobox").filter(has_text="Select Your Region of Operation")
        combobox.click()
        
        # Wait for dropdown to open
        self.page.wait_for_selector('button[role="combobox"][aria-expanded="true"]', timeout=5000)
        
        # Wait for search input to appear and be focused
        search_input = self.page.get_by_placeholder("Search...")  # or try get_by_placeholder if it has placeholder text
        search_input.wait_for(state="visible", timeout=5000)
        
        # Type the region name in the search box to filter options
        search_input.fill(region)
        
        # Wait a moment for filtering to happen
        self.page.wait_for_timeout(300)
        
        # Click the matching option
        self.page.get_by_role("option", name=region, exact=True).click()
        
        # Verify selection
        expect(combobox).to_contain_text(region)
        
    def next_step(self):
        self.page.locator('button[type="submit"]').click()