counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe", "Denver", "Jefferson"]

if "El Paso" in counties:
    
    print("El Paso is in the list of counties.")

else:
    
   print("El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" in counties:

    print("Arapahoe and El Paso are in the list of counties.")

else:

    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:

   print("Arapahoe or El Paso is in the list of counties.")

else:

    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:

    print(county)

numbers = [0, 1, 2, 3, 4]

for num in numbers:

    print(num)

for i in range(len(counties)):

    print(counties[i])

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

#for key, value in dictionary_name.items():

   #print(key, value)

for county, voters in counties_dict.items():

    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
               {"county":"Denver", "registered_voters": 463353},
              {"county":"Jefferson", "registered_voters":  432438}]

for county_dict in voting_data:

   print(county_dict)

for county_dict in voting_data:

    for value in county_dict.values():
        print(value)
    
for county_dict in voting_data:

    print(county_dict['county'])

counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}

for county, voters in counties_dict.items():

    print(county + "county has" + str(voters) + "registered voters.")

for county, voters in counties_dict.items():

    print(f"{county} county has {voters} registere voters.")

#candidate_votes = int(input("How many votes did the candidate get in the election?"))

#total_votes = int(input("What is the total number of votes in the lection?"))

candidate_votes = 3345

total_votes = 23123

message_to_candidate = (
    
    f"You received {candidate_votes} number of votes."

    f"The total number of votes in the election was {total_votes}>"

    f"You received {candidate_votes / total_votes * 100}% of the total votes")