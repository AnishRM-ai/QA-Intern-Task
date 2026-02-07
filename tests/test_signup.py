from playwright.sync_api import sync_playwright
from page.presignup_page import PreSignup
from page.signup_personal_page import SignUpPagePersonal
def test_presignup():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        pre = PreSignup(page)
        
        
        pre.open()
        pre.acknowledge_and_continue()
        
        personal = SignUpPagePersonal(page)
        personal.fill_personal_details("Ram", "Hero", "ram@gmail.com", "9876234312", "GothicAss1!", "GothicAss1!")
        personal.next_step()
        
        page.wait_for_url("**/register?step=setup")
        assert "/register?step=setup" in page.url
   
        browser.close()
        