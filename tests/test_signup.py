import os
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from page.presignup_page import PreSignup
from page.signup_personal_page import SignUpPagePersonal
from page.signup_otp_page import VerifyOtp
from page.signup_agency_page import SignUpAgency
from page.signup_professinal_page import ProfessionalDetails
from page.signup_verification_page import VerificationPage
from utils.mailosaur_cllient import MailsaurHelper


def test_full_signup(page, mailosaur):
    """ This script automates the full signup flow with the correct credentials.
    """
    
    # IMPORTANT: Clean up old emails before starting
    print("Cleaning up old emails...")
    mailosaur.delete_all_messages()
    
    #Pre SignUp
    pre = PreSignup(page)
    pre.open()
    pre.acknowledge_and_continue()
    
    
    #Signup Personal Details
    email = "modern-settlers@pcqiozhk.mailosaur.net"
    
    personalDetails = SignUpPagePersonal(page)
    personalDetails.fill_personal_details(
        "Test00",
        "User",
        email,
        "9812072419",
        "SuperSecret1!",
        "SuperSecret1!"
    )
    
    print(f"Submitting personal details form...")
    personalDetails.next_step()
    
    print(f"Waiting for OTP email to {email}...")
    
    # Signup Otp verification
    # Wait for the code with optional subject filter
    code = mailosaur.wait_for_code(email, timeout=60000)
    
    print(f"✓ Got verification code: {code}")
    
    otp_verification = VerifyOtp(page)
    otp_verification.fill_code(code)
    
    otp_verification.confirm_continue()
    
    
    
    # Signup Agency section
    agency_details = SignUpAgency(page)
    agency_details.fill_agency(
        'CAN',
        'Manager',
        'chest-while@vgay1h0g.mailosaur.net',
        'www.youtube.com',
        'Kapan',
        'New Zealand'
    )
    agency_details.next_step()
    
    # Signup Professional Experience
    professional = ProfessionalDetails(page)
    professional.fill_prof_detail(
        "4 years",  # experience_level - adjust to match your app's options
        "21",         # number_of_student
        "USA",        # focus_area
        "90"          # success_metric
    )
    professional.next_step()
    
    # Signup Final Step Verification page
    final_step = VerificationPage(page)
    final_step.fill_verification_detail(
        "123123",
        "New Zealand",
        "Universities",
        "Counselor certificate"
    )
    
    # Fix file paths - use relative paths or ensure files exist
    test_dir = os.path.dirname(os.path.abspath(__file__))
    img1_path = os.path.join(test_dir, 'test_data', 'img00.jpg')
    img2_path = os.path.join(test_dir, 'test_data', 'img03.jpg')
    
    # Check if files exist
    if not os.path.exists(img1_path):
        print(f"⚠ Warning: {img1_path} does not exist")
    if not os.path.exists(img2_path):
        print(f"⚠ Warning: {img2_path} does not exist")
    
    final_step.upload_documents([img1_path, img2_path])
    final_step.add_documents([img2_path])
    final_step.final_submit()
    
    
    # Fix expected URL - use the correct domain
    expect(page).to_have_url("https://authorized-partner.vercel.app/admin/profile")
    
    print("✓ Test completed successfully!")