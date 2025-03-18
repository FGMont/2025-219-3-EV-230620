import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("lc-project-36865-firebase-adminsdk-fbsvc-6e6fe089a1.json")


firebase_admin.initialize_app(cred, {'databaseURL': 'https://lc-project-36865-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/')

year = db.reference('Counts_per_year').get()




for each in year:
    x = list(year.keys())
    y = list(year.values())

#plotting line graph
import matplotlib.pyplot as plt
print(x,y)

plt.plot(x,y)

plt.ylabel('Number of Games Published')
plt.xlabel('Year')

plt.show()

'''
Make it so the user can alternate 
eg. top 5, top 10, top 14, top 20, top 25, top 30... top 50 being the highest possible selection
'''
