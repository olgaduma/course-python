year = input ("Enter the year: ")
year = int(year)

if not (not (year % 4 == 0 and year % 100 != 0) and (year % 400)):
     print('YES')
else:
    print ('NO')