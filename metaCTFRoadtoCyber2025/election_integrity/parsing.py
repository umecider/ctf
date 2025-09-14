import pandas as pd
#import numpy as np #not needed, force of habit :p


df = pd.read_csv("skillia_voting_records.csv")

counties = df.drop(["state"], axis=1).groupby('county')
for county in counties:
    balance = []
    voter_type = []
    for group in county[1].groupby("voting_station_id"):
        #see the percentages for who voted for president
        count = group[1]["vote_president"].value_counts().sort_values()
        undervote_percent = count.iloc[0]/count.sum()*100
        a_percent = count.iloc[1]/count.sum()*100
        b_percent = count.iloc[2]/count.sum()*100
        ratio = (a_percent/b_percent)
        #this is sort of a random thing I did just to see how off balance things were - if the percentage of A and B were close, the number here should go to 1 (meaning we likely don't care about it)
        balance.append((group[0],a_percent,b_percent,undervote_percent, ratio))
        #get the percentage of in person and absentee voters
        count = group[1]["voter_type"].value_counts().sort_values()
        voter_type.append((group[0],count.iloc[0]/count.sum(),count.iloc[1]/count.sum())) #id, percent of absentee, percent of in_person
    balance_df = pd.DataFrame(balance, columns=["ID", "A Percent", "B Percent", "Undervote Percent", "Ratio"])
    balance_df.sort_values(by="Ratio", ascending=True).to_csv(county[0]+"_percentage_of_votes_president.csv")
    voters_df = pd.DataFrame(voter_type, columns=["ID", "Absentee Percent", "In Person Percent"])
    voters_df.sort_values(by="Absentee Percent", ascending=False).to_csv(county[0] + "_voter_turnout.csv")

###other code###
#idk what i was cooking here, but gets the number of times someone voted in a way
# votes = df.drop(labels=['state', 'county', 'voting_station_id'], axis = 1)
#votes.value_counts().reset_index().to_csv("counts.csv")
""" by_id = df.drop(['state', 'county'], axis=1).groupby('voting_station_id')
percentages = []
balance = []
voter_type = []
for group in by_id:
    #group[1].value_counts().reset_index().to_csv(group[0] + "counts.csv") there are like 30 groups dude this was a mistake
    #look at overall population and unique values - see if there are any outliers
    count = group[1].drop(["voter_type"], axis=1).value_counts().sort_values()
    percentage = count.max()/count.sum()
    percentages.append((group[0],percentage*100))
    #see the percentages for who voted for president
    count = group[1]["vote_president"].value_counts().sort_values()
    undervote_percent = count.iloc[0]/count.sum()*100
    a_percent = count.iloc[1]/count.sum()*100
    b_percent = count.iloc[2]/count.sum()*100
    ratio = (a_percent/b_percent)
    #this is sort of a random thing I did just to see how off balance things were - if the percentage of A and B were close, the number here should go to 1 (meaning we likely don't care about it)
    balance.append((group[0],a_percent,b_percent,undervote_percent, ratio))
    #get the percentage of in person and absentee voters
    count = group[1]["voter_type"].value_counts().sort_values()
    voter_type.append((group[0],count.iloc[0]/count.sum(),count.iloc[1]/count.sum())) #id, percent of absentee, percent of in_person
percentage_df = pd.DataFrame(percentages, columns=["ID", "Highest Count Percentage"])
percentage_df.sort_values(by="Highest Count Percentage", ascending=False).to_csv("highest_count_percentages.csv")
balance_df = pd.DataFrame(balance, columns=["ID", "A Percent", "B Percent", "Undervote Percent", "Ratio"])
balance_df.sort_values(by="Ratio", ascending=True).to_csv("percentage_of_votes_president.csv")
voters_df = pd.DataFrame(voter_type, columns=["ID", "Absentee Percent", "In Person Percent"])
voters_df.sort_values(by="Absentee Percent", ascending=False).to_csv("voter_turnout.csv")
 """
#list of IDs 1251749b, 4b45c819, 1fe457e4, a4defb9c, 329071ee, 81b7bc0c