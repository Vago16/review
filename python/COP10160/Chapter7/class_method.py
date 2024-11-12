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

>>> firefox = WebBrowser("www.org")
>>> firefox.geo_coordinates
{'lat': -4.764813, 'lng': 16.131331}

>>> WebBrowser.change_geo_coordinates({"lat": 31, "lng": 123})
>>> firefox.geo_coordinates
{'lat': 31, 'lng': 123}
>>> WebBrowser.change_geo_coordinates({"lat": 31, "lng": 190})
Invalid value for longitude. Should be within the range from -180 to 180 degrees.
>>> WebBrowser.change_geo_coordinates({"lat": -100, "lng": 123})
Invalid value for latitude. Should be within the range from -90 to 90 degrees.
>>>
'''
    number_of_web_browsers=0
    connected=True
    geo_coordinates = {"lat": -4.764813, "lng": 16.131331 }
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
#changes coordinates when called, takes the geo_coordinates parameter, which is a dict
#calling change_geo_coordinates on class will change geo_coordinates for all instances of the class
    @classmethod
    def change_geo_coordinates(cls, new_coordinates):
        if new_coordinates["lat"] > 90 or new_coordinates["lat"] < -90:
            print("Invalid value for latitude. Should be within the"
                  " range from -90 to 90 degrees.")
            return None
        if new_coordinates["lng"] > 180 or new_coordinates["lng"] < -180:
            print("Invalid value for longitude. Should be within the"
                  " range from -180 to 180 degrees.")
            return None
        cls.geo_coordinates = new_coordinates

chrome = WebBrowser.with_incognito("shady-website.com")
print(chrome.is_incognito)
print(chrome.current_page)
print(chrome.history)