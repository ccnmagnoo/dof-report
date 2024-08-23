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
    
    