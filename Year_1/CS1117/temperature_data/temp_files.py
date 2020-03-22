import os

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

os.chdir('/users/bscdsa2022/mc64/AK_temperature Orig')

try:
    os.mkdir('/users/bscdsa2022/mc64/temperature_data')

    for year in range(2000,2011):
        year = str(year)

        os.mkdir('/users/bscdsa2022/mc64/temperature_data/' + year)

        for m in months:
            os.mkdir('/users/bscdsa2022/mc64/temperature_data/' + year + '/' + m)
except:
    pass

for filename in os.listdir():
    if filename[:3] not in months:
        d_month = int(filename[-10])
        mon = months[d_month-1]
        os.rename(filename, mon + '_' + filename[-8:])

    os.rename('/users/bscdsa2022/mc64/AK_temperature Orig/' + filename, '/users/bscdsa2022/mc64/temperature_data/' + filename[-8:-4] + '/' + filename[:-9] + '/' + filename)


