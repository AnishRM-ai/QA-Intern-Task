class BasePage:
    def __init__(self, page):
        self.page = page
    
    def visit(self, url:str):
        self.page.goto(url)
    
    def wait_for_url(self, pattern:str):
        self.page.wait_for_url(pattern)
        
        
        