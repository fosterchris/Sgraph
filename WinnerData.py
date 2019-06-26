from TableScraper import ScrapeTableByRowCount
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import numpy as np
import string
from helpers.helpers import Helpers

def ConvertYMDtoYears(value):

    value = value.replace('y', '')
    value = value.replace('m', '')
    value = value.replace('d', '')
    value = value.split(' ')

    fraction_age = int(value[0])+ float(value[1])/12.0 + float(value[2])/365.0
    return fraction_age

data = ScrapeTableByRowCount("https://www.statsf1.com/en/statistiques/pilote/champion/age.aspx", 4)
npX = np.array(data)
byYear = npX[np.argsort(npX[:,1])]

years = Helpers.convert_array_strings_to_ints(byYear[:,1])
ages = np.array([ConvertYMDtoYears(y) for y in byYear[:,3]])

rolling_ages = []
for i in range(0, len(ages)-5):
    rpa = (ages[i] + ages[i+1] + ages[i+2] + ages[i+3] + ages[i+4]) / 5.0
    rolling_ages.append(rpa)

rolling_years = years[5:]

years_smooth = np.linspace(rolling_years.min(), rolling_years.max(), 400)
age_smooth = spline(rolling_years, rolling_ages, years_smooth)

#plt.plot(rolling_years, rolling_ages, marker=">")
plt.plot(years_smooth, age_smooth, 'red')
plt.xlabel('Year')
plt.ylabel('Age of winner')
plt.show()