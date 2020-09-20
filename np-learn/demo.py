import requests
import json

domain_url = 'https://www.trainline.fr'
url = "https://www.trainline.fr/api/v5_1/search"
payload = {"search": {"departure_date": "2019-09-14T16:00:00UTC", "return_date": "2019-09-15T16:00:00UTC",
                      "passengers": [
                          {"id": "833914d4-f9a7-4c16-99a9-122e87ede397", "label": "adult", "age": 26, "cards": [],
                           "cui": None}],
                      "systems": ["sncf", "db", "idtgv", "ouigo", "trenitalia", "ntv", "hkx", "renfe", "cff",
                                  "benerail", "ocebo", "westbahn", "leoexpress", "locomore", "busbud", "flixbus",
                                  "distribusion", "cityairporttrain", "obb", "timetable"], "exchangeable_part": None,
                      "source": None, "is_previous_available": False, "is_next_available": False,
                      "departure_station_id": "4916", "via_station_id": None, "arrival_station_id": "83",
                      "exchangeable_pnr_id": None}}

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8',
    'referer': 'https://www.trainline.fr/',
    'Host': 'www.trainline.fr',
    'x-not-a-bot': 'i-am-human',
    'x-user-agent': 'CaptainTrain/1568362833(web) (Ember 3.5.1)'}

cookies = {
    'ak_bmsc': '4769664A0B546B236EC5C6947392904D17D4367C130D000010B47C5D35C75245~plPNsc8rWKko4y8ICgZTDjWlqQWH3V/kwMmTtlYk4YpYDfBN6I7EY65TRulYPRweoSEnBN1/9I71JBU7BpbLZEA0KPGHo6ycnx7Zr1LB5VMYApx31dHEG7mFbpGI4WH+j2mVegT6EmlmBxYXYCXHddp05vl7hEaeY3xAvsIS52661izmtCTA7aQmJrNfrfJ2SJy4MPU1OaKMlmcDoBXWimUesJvH/RPMDNGpHMHqkTnWs=',
    'bm_sv': '83728B3CD6D78B04C18E9DADBE7BAF9B~KRWUu2Qz2YNUcuzRoh8M9+AbdYHVxNXBMv/rJeRgsSRDsDsaloKvDWeEJSigFl+pcAUPnh5LVqLeE6M1l9GZWqkVMqqSuhVjTaGSaI8oDVDO+0lchT1SE73AjgK4V/EsM9TZw6DDPm7mgHmPGA7jmbXBG1UVSK+9J7RJsd1UAyQ='}
if __name__ == '__main__':
    s = requests.session()
    #  r = requests.session.get(domain_url, allow_redirects=True)
    # print(r.text)
    r = s.post(url, data=json.dumps(payload), headers=header)
    print(r.text)
