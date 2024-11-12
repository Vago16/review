class WebBrowser:
    '''
    >>> chrome = WebBrowser("example.net")
>>> chrome.navigate("example2.net")
>>> chrome.navigate("example3.net")
>>> chrome.history
['example.net', 'example2.net', 'example3.net']
>>> chrome.current_page
'example3.net'
>>> chrome.clear_history()
>>> chrome.history
['example3.net']
>>>
'''
    number_of_web_browsers=0
    connected=True
#initializes a browser
    def __init__(self, page):
        self.history =[page]
        self.current_page=page
        self.is_incognito=False
        WebBrowser.number_of_web_browsers += 1
#a call to navigate() will set browser's current page to new_page and then add to history
#if not in incognito mode
    def navigate(self,new_page):
        self.current_page=new_page
        if not self.is_incognito:
            self.history.append(new_page)
#a call to clear_history() method will delete the browser's history
    def clear_history(self):
        self.history[:-1]=[]
#initializes a browser in incognito mode, cls refers to class
    @classmethod
    def with_incognito(cls,page):
        instance=cls(page)
        instance.is_incognito=True
        instance.history=[]
        return instance

chrome = WebBrowser.with_incognito("shady-website.com")
print(chrome.is_incognito)
print(chrome.current_page)
print(chrome.history)