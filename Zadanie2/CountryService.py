
import requests


class CountryService:
    @staticmethod
    def get_countries():
        tabresult=[]
        result = requests.get(f"https://api.covid19api.com/countries").json()

        #print(result)
        for c in result:
            tabresult.append(c['Country'])
        tabresult.sort()

        return tabresult

class HolidaysList:
    @staticmethod
    def get_holidays():
        tableresult=["Nowy Rok","Wielkanoc","Święto Pracy","Boże Ciało"]
        return tableresult

class YearsList:
    @staticmethod
    def get_years():
        tableyears=[]
        for i in range(2014, 2022):
            tableyears.append(i)
        return tableyears