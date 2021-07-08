counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

for key, values in counties_dict.items():
    print(f"{key} county has {values} registered voters.")


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {
    "county":"Denver", "registered_voters": 463353}, 
    {"county":"Jefferson", "registered_voters": 432438}]

for vote in voting_data:
    #print(vote['county'])
    
    print(f"{vote['county']} county has {vote['registered_voters']:,} registered voters")
