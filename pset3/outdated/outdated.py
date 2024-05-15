months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input('Date: ')
    if '/' in date:
        f = 'integer'
        m, d, y = date.split('/')
        if m.isdigit() and d.isdigit() and y.isdigit() and 0 < int(m) <= 12 and 0 < int(d) <= 31:
            break
    elif ',' in date:
        f = 'str'
        mo, da, ye = date.split()
        da = da.strip(',')
        if (mo in months) and da.isdigit() and ye.isdigit() and 0 < int(da) <= 31:
            break
if f == 'integer':
    print(y + '-' + f"{int(m):02}" + '-' + f"{int(d):02}")
if f == 'str':
    ind = months.index(mo) + 1
    print(ye + '-' + f"{ind:02}" + '-' + f"{int(da):02}")