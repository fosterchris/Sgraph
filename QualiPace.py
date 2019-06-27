from TableScraper import ScrapeTableByRowCount

def get_laptime_safe(track_name, year):
    try:
        url = 'https://www.statsf1.com/en/{year}/{track}/qualification.aspx'.format(track=track_name, year=year)
        data = ScrapeTableByRowCount(url, 8)

        if data != []:
            print(data[1][4])
            return data[1][4]
    except:
        return
#Script which takes all (current) circuit P1 qualifying times from the last 68 years
#countries as defined on the statsf1 site which we scrape
START_YEAR=1950
END_YEAR=2019

countries = [
    "australie",
    "bahrein",
    "chine",
    "azerbaidjan",
    "espagne",
    "monaco",
    "canada",
    "france",
    "autriche",
    "grande-bretagne",
    "allemagne",
    "hongrie",
    "belgique",
    "italie",
    "singapour",
    "russie",
    "japon",
    "mexique",
    "etats-unis",
    "bresil",
    "abou-dhabi"
]
#x will run first
#urls = ['https://www.statsf1.com/en/{year}/{track}/qualification.aspx'.format(track=x, year=y) for x in countries for y in range(START_YEAR,END_YEAR)]

urls = ['https://www.statsf1.com/en/{year}/{track}/qualification.aspx'.format(track='canada', year=y) for y in range(START_YEAR,END_YEAR)]

array = []
for year in range(1990, 2000):
    array.append(get_laptime_safe('canada', year))

print(array)