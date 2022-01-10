print("Hello World")
counties=["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print ("Aarapahoe or El Paso are in the list of counties.")

else:
    print ("Aarapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

counties_dict = {"Aarapahoe": "County has 422829 registered voters", "Denver": "County has 4633353 registered voters", "Jefferson": "County has 432438 registered voters"}
for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)   

for i in range(len(voting_data)):
      print(voting_data[i]['county'])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

for county_dict in voting_data:
    print(county_dict['registered_voters'])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},{"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson","registered_voters": 432438}]
for county_dict in voting_data:
    print(f"{county} county has {voters} registered voters.")    
   
