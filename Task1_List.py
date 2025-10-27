
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"] # Justice League list created
print("Justice League members:", justice_league)


print("Number of members:", len(justice_league)) # Count number of members


justice_league.append("Batgirl") # Add Batgirl 
justice_league.append("Nightwing") # Nightwing
print("After adding Batgirl and Nightwing:", justice_league)


# Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Wonder Woman is now the leader:", justice_league)


# Put Superman between Aquaman and Flash
justice_league.remove("Superman")  # remove Superman first
pos = justice_league.index("Flash")  # find Flash position
justice_league.insert(pos, "Superman")  # insert Superman before Flash
print("Superman placed between Aquaman and Flash:", justice_league)


justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"] # New team formed
print("New Justice League team:", justice_league)


justice_league.sort()
print("Alphabetically sorted list:", justice_league) # Sort the list alphabetically


print("New leader is:", justice_league[0]) # New leader founded