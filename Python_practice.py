voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

  
for county_dict in voting_data:
        print(f"{county_dict['county']} has {county_dict['registered_voters']:,} registered voters")