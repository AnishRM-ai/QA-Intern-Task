import os
import re
from datetime import datetime, timezone
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria

class MailsaurHelper:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        self.server_id = os.getenv("SERVER_ID")
        self.client = MailosaurClient(self.api_key)

    def wait_for_code(self, email_add, timeout=60000):
        """Wait for verification email and extract OTP code.
        
        Args:
            email_add: Email address to wait for
            timeout: Timeout in milliseconds (default 60000 = 60 seconds)
        
        Returns:
            str: The 6-digit verification code
        """
        criteria = SearchCriteria()
        criteria.sent_to = email_add
        
        # Only get emails received after NOW to avoid old emails
        received_after = datetime.now(timezone.utc)
        
        print(f"Waiting for email to: {email_add}")
        
        try:
            full_message = self.client.messages.get(
                self.server_id,
                criteria,
                timeout=timeout,
                received_after=received_after
            )
        except Exception as e:
            raise Exception(f"No emails found for {email_add} within {timeout}ms: {str(e)}")
        
        print(f"✓ Email received: {full_message.subject}")
        
        # Get HTML body
        body = full_message.html.body if full_message.html else full_message.text.body
        
        # Extract OTP from centered paragraph with letter-spacing
        # Pattern matches: <p style="...letter-spacing: 2px...">448455</p>
        match = re.search(r'<p[^>]*letter-spacing[^>]*>\s*(\d{6})\s*</p>', body, re.IGNORECASE)
        
        if not match:
            raise Exception("No 6-digit verification code found in email!")
        
        code = match.group(1)
        print(f"✓ Extracted code: {code}")
        
        # Clean up: delete the email
        try:
            self.client.messages.delete(full_message.id)
        except:
            pass
        
        return code
    
    def delete_all_messages(self):
        """Delete all messages in the server (useful for cleanup before tests)."""
        try:
            self.client.messages.delete_all(self.server_id)
            print("✓ All messages deleted")
        except Exception as e:
            print(f"⚠ Could not delete messages: {e}")