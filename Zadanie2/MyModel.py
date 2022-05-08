
class ResultModel:
    def __init__(self,country,confirmed,deaths,date,active):
        self.country = country

        self.mystats={
            "confirmed":confirmed,
            "deaths":deaths,
            "date":date,
            "active":active
        }


    #return object represantation
    def __repr__(self):
        return f"{self.country}:{self.mystats}"

class ResultTempModel:
    def __init__(self,  year , max_temp ):
        self.mystats={
        year:max_temp}

    def __repr__(self):
        return f"{self.year}:{self.max_temp}"
