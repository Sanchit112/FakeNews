import pandas as pd
#df1 = pd.read_csv("faketweetsfinal.csv")
#df2 = pd.read_csv("realtweetsfinal.csv")
#pd.DataFrame(df1["username"].unique().tolist()).to_csv('fake.csv')
#pd.DataFrame(df2["username"].unique().tolist()).to_csv('real.csv')

'''import requests
import time
import twint

df = pd.read_csv("fake.csv")
for i in df["0"]:
    try:
        c = twint.Config()
        c.Username = str(i)
        c.Custom["id"] = ["name","followers", "following"]
        c.Output = "userfake.csv"
        c.Store_csv = True
        twint.run.Lookup(c)
    except Exception as e:
        print(e)
        print(i)

df = pd.read_csv("real.csv")
for i in df["0"]:
    try:
        c = twint.Config()
        c.Username = str(i)
        c.Custom["id"] = ["name","followers", "following"]
        c.Output = "userreal.csv"
        c.Store_csv = True
        twint.run.Lookup(c)
    except Exception as e:
        print(e)
        print(i)
'''
'''
df1 = pd.read_csv("userfake.csv")
df2 = pd.read_csv("userreal.csv")
df11 = df1[['username', 'bio', 'location', 'join_date', 'join_time', 'tweets', 'following', 'followers', 'likes', 'media','verified']]
df22 = df2[['username', 'bio', 'location', 'join_date', 'join_time', 'tweets', 'following', 'followers', 'likes', 'media', 'verified']]
df11.to_csv("fakemerge.csv")
df22.to_csv("realmerge.csv")
'''

df1 = pd.read_csv("userfake.csv")
df2 = pd.read_csv("userreal.csv")
df11 = pd.read_csv("faketweetsfinal.csv")
df22 = pd.read_csv("realtweetsfinal.csv")

fake = pd.merge(left=df11, right=df1, left_on='username', right_on='username')
real = pd.merge(left=df22, right=df2, left_on='username', right_on='username')
fake.to_csv("fake11.csv")
real.to_csv("real11.csv")


