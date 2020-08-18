import pandas as pd

#df = pd.read_excel("Sample for Excel Data Translation.xlsx","Sheet1",index_col=None)
#df.to_csv('output.csv',header=False,index=False)

df=pd.read_csv('output.csv')
#print(df.head())

#print(df.drop(df.index[[0,1]]))
#df=pd.read_csv('output.csv',header=None)
#print(df.head())
#df.apply(lambda x:x in[0,2])
df.drop([0,1],inplace=True)
df.drop(['Unnamed: 3','Unnamed: 4','Unnamed: 5','Unnamed: 7','Unnamed: 8','Unnamed: 9','Unnamed: 10','Unnamed: 11','Unnamed: 12','Desired Output'], axis=1,inplace=True)
df.rename(columns={"Sample Input": "Team", "Unnamed: 1": "Opponent","Unnamed: 2":"Result"},inplace=True)
df.reset_index(drop=True)

#df.to_csv('out.csv',index=False)
#desired_output = df.groupby(['Team','Opponent'])
desired_output = pd.pivot(df,index='Team',columns='Opponent',values='Result')
#print(desired_output)
# writer = pd.ExcelWriter('desired.xlsx')
#
# for  in desired_output.index:
#     temp_df = desired_output.xs(Team)
#     temp_df.to_excel(writer)
#
# writer.save()

desired_output.to_excel('desired1.xlsx')
