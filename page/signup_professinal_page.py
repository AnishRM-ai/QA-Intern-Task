from .basepage import BasePage
from playwright.sync_api import expect


class ProfessionalDetails(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Hidden native select
        self.experience_select = self.page.locator("select[aria-hidden='true']")

        # Visible combobox
        self.experience_combobox = self.page.get_by_role(
            "combobox",
            name="Select Your Experience Level"
        )

    def fill_prof_detail(
        self,
        experience_level,  
        number_of_student,
        focus_area,
        success_metric,
        services
    ):
        #  Select via native select
        self.experience_select.select_option(label=experience_level)

        # Continue form filling
        self.page.get_by_label("Number of Students Recruited Annually").fill(number_of_student)
        self.page.get_by_label("Focus Area").fill(focus_area)
        self.page.get_by_label("Success Metric").fill(success_metric)
        self.page.get_by_label(services).click()

    def next_step(self):
        self.page.locator("button[type='submit']").click()
