class webBrowser:
    number_of_web_browsers=0
    connected=True
    
    def __init__(self, page):
        self.history =[page]
        self.current_page=page
        self.is_incognito=False
        webBrowser.number_of_web_browsers += 1


firefox=webBrowser("google.com")
iceweasel=webBrowser("facebook.com")

print(webBrowser.number_of_web_browsers)
