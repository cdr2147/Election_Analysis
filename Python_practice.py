counties = ["Araphoe","Denver","Jefferson"]
counties_dict = {"Araphoe":422829,"Denver":4633353,"Jefferson":432438}
voting_data = [{"county":"Araphoe","registered_voters": 42},
                {"county":"Denver","registered_voters": 43},
                {"county":"Jefferson","registered_voters": 45}]
for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters")




