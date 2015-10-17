from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def draw_point(lats, lons):
    m = Basemap(resolution='i')
    m.drawcoastlines()
    m.drawcountries()
    x, y = m(lons, lats)
    m.scatter(x, y, s=0.3, color='#ff0000', marker='.')
    plt.show()

def read_data():
    lats=[]
    lons=[]
    with open('data.txt') as dt:
        for row in dt.readlines():
            lats.append(row.split()[1])
            lons.append(row.split()[2])
    return lats, lons

lats, lons = read_data()
draw_point(lats, lons)
