#printing datetime
import datetime
a = datetime.datetime.now()
print(a)

#printing date time 
import datetime
a = datetime.datetime.now()
print(a)
print(a.year)
print(a.strftime("%A"))
print(a.strftime("%d"))

#creating date objects(three parameters requires to create a )

import datetime
a = datetime.datetime(2021,6,21)
print(a)

#using strf method specifying the format of the returned string
import datetime
a = datetime.datetime(2021,6,21)
print(a)
print(a.strftime("%d"))
print(a.strftime("%b"))