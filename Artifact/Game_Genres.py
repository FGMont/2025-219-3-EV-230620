import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("lc-project-36865-firebase-adminsdk-fbsvc-6e6fe089a1.json")
import numpy as np

firebase_admin.initialize_app(cred, {'databaseURL': 'https://lc-project-36865-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference('/')

genre = db.reference('Games_per_Tags').get()



for each in genre:
    x = list(genre.keys())
    y = list(genre.values())
    
colors = ['#FF0000', '#0000FF', '#FFFF00', 
          '#ADFF2F', '#FFA500']
    
import matplotlib.pyplot as plt
print(x,y)

plt.pie(y, colors=colors, labels = x,autopct='%1.1f%%', pctdistance=0.85)

# draw circle
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
 
# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)
 
# Adding Title of chart
plt.title('Genre Popularity Chart')
 
# Displaying Chart
plt.show()
