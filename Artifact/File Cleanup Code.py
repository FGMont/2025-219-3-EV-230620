import pandas as pd

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from collections import defaultdict

'''
Getting necessary colums from the original csv file and putting them under a new variable.
'''
df = pd.read_csv(r"games.csv", usecols = ['AppID','Name','Release date','Full audio languages','Tags'],encoding='utf-8',index_col=False)


df.dropna(inplace = True)




df['Release year'] = pd.to_datetime(df['Release date'], format= 'mixed').dt.year
 
counts_per_year = df.groupby('Release year')['AppID'].count().to_dict() #to be sent to firebase. Will be used for timeline
 
game_names_per_year = df.groupby('Release year')['Name'].apply(list).to_dict()  #to be sent to firebase. Used for filterage and search
 
def convert_to_array(string : str):
    return [x.strip() for x in string.replace('[','').replace(']','').replace("'",'').replace('\\n','').replace('\\r','').replace('b/b','').replace('$','').replace('#','').replace('.','').strip().split(',')]



# Tags dictionary

df['Tags'] = df['Tags'].transform(convert_to_array)
           
tag_dict = defaultdict(list)


for name, tags in zip(df["Name"], df["Tags"]):
    for tag in tags:
        tag_dict[tag].append(name)

# print(type(tag_dict))
games_per_tags = dict(tag_dict)
# print(type(games_per_tags))



##########
 
         
cred = credentials.Certificate("C:\\Users\\19FMonteiro.ACC\\OneDrive - Longford and Westmeath Education and Training Board\\2025 Computer Science Python projects\\Computer Science JS Project\\lc-project-36865-firebase-adminsdk-fbsvc-6e6fe089a1.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://lc-project-36865-default-rtdb.europe-west1.firebasedatabase.app/'})






ref = db.reference('/Games_per_year') #Filtering games per year UPLOADED / DISPLAYING
ref.set(game_names_per_year)


ref = db.reference('/Games_per_Tags') #Doughnut chart UPLOADED / DISPLAYING
ref.set({})

for key in games_per_tags:
    counter=0
    ref = db.reference('/Games_per_Tags/')
    ref.update({key:len(games_per_tags[key])})

#picking out top 10 games in every tag
    
top_tags = games_per_tags.copy()
top_tag_list = []
top_tag_dict = []

for key in top_tags:
    
    length = len(games_per_tags[key])
    each_tag_list = games_per_tags[key]
    
    if length > 10:
        
        each_tag_list = each_tag_list[:10]
        top_tag_list.append(each_tag_list)
    
    else:
        
        top_tag_list.append(each_tag_list)
 
top_tag_dict = dict(zip(top_tags.keys(),top_tag_list))

ref = db.reference('/Top_Games_per_Tags') #for Reccomendations
ref.set(top_tag_dict)
    
 
ref = db.reference('/Counts_per_year') #Timeline COMPLETED AND UPLOADED
ref.set(counts_per_year)


