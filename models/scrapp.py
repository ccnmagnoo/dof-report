from datetime import datetime
import requests


class Dof():
    """api http request handler"""
    _SOURCE = "https://www.diariooficial.interior.gob.cl/"
    
    def _url(self,date=datetime.now()):
        """compose url data request """
        date_api:str = date.strftime("%d-%m-%Y")
        compose:str = f'{self._SOURCE}?date={date_api}'
        return compose
    
    def request(self,date:datetime|None):
        """url request"""
        url = self._url(date)
        req = requests.get(url,timeout=1000)
        if req.status_code == 200:
            return req.content
        else:
         raise ValueError("wrong http request:",req.status_code)