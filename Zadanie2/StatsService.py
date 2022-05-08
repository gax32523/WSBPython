import requests

from MyModel import ResultModel, ResultTempModel


class StatTempService:
    @staticmethod
    def get_stats(year,  holiday):
        stats: ResultTempModel
        result = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/PL").json()
        for d in range(len(result)):
            if (result[d]['localName'] == holiday):
            #    print(result[d])
            #    print(f"https://www.metaweather.com/api/location/523920/{result[d]['date'][0:4]}/{result[d]['date'][5:7]}/{result[d]['date'][8:10]}/")
                res2 = requests.get(f"https://www.metaweather.com/api/location/523920/{result[d]['date'][0:4]}/{result[d]['date'][5:7]}/{result[d]['date'][8:10]}/").json()
                temper_min = int(res2[0]['min_temp'])
                temper_max = int(res2[0]['max_temp'])
                temper_mid = int(res2[0]['the_temp'])
                print(f'temp min: {temper_min}, temp max: {temper_max}, temp mid: {temper_mid}')
        #rs = ResultTempModel(holiday, year, temper_min, temper_max)
        rs = ResultTempModel(year,  temper_max)
        return rs


    @staticmethod
    def get_temperature(year_start,year_end,holiday):
        #tabresult = []
        tabresult={}
        stats: ResultTempModel

        for c in range(year_start,year_end+1):
            stats = StatTempService.get_stats(c,holiday)
            #tabresult.insert(stats.mystats['min_temp'])
            tabresult.update(stats.mystats)

            #tabresult.update({'year':stats.mystats['year'],'min_temp':stats.mystats['min_temp'],'min_temp':stats.mystats['max_temp']})

        print(tabresult)
        print(len(tabresult))
        return tabresult
