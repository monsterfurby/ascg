import random

def d(n): 
	return random.randint(1, n)

#BASIC INFORMATION
#rollable table: species
speciestable = ["Sernan", "Cartheyn", "Aureian", "Crimley", "Zezz", "Sleen", "Savan", "Dust Bunny", "Nog", "Jay", "Sulskym"]
species = random.choice(speciestable)

#rollable table: subspecies
subspecies = ""
if species == "Sernan":
	subspecies = random.choice(["Athenian", "Cerberi", "Zero", "Meton"])
	
#rollable table: gender
gender = ""
if species is not "Sleen":
	gender = random.choice(["Male", "Female"])
	
#init gender pronouns for description
if gender is "Male":
	genderPronounThey = "he"
	genderPronounTheir = "his"
if gender is "Female":
	genderPronounThey = "she"
	genderPronounTheir = "her"
if gender is "":
	genderPronounThey = "they"
	genderPronounTheir = "their"
	
#rollable table: physical description
descriptionTextSet = 0

## Sernan
if species is "Sernan":
	from chargenSernan import descriptionText
	from chargenSernan import descriptionTextSet
	
## Cartheyn
if species is "Cartheyn":
	from chargenCartheyn import descriptionText
	from chargenCartheyn import descriptionTextSet
	
if descriptionTextSet is not 1:
	descriptionText = (genderPronounThey.capitalize() + " is a typical " + species + ".")
	
#rollable table: profession
professiongroup = random.choice(["Military", "Trader", "Civilian", "Scientist", "Criminal"])

## Military
if professiongroup is "Military":
	militaryBranch = random.choice(["Navy", "Marines", "Infantry", "Atmospheric Air Force"])
	if militaryBranch is "Navy":
		militaryRank = random.choice(random.choices(["Shiphand", "Senior Shiphand", "Warrant Officer", "Ensign", "Lieutenant", "Commander", "Captain", "Admiral"], [8, 7, 6, 5, 4, 3, 2, 1]))
	if militaryBranch is not "Navy":
		militaryRank = random.choice(random.choices(["Private", "Corporal", "Sergeant", "Warrant Officer", "Lieutenant", "Captain", "Major", "Colonel", "General"], [9, 8, 7, 6, 5, 4, 3, 2, 1]))
	militaryReputation = random.choice (["straight arrow", "brilliant marksman", "pencil-pusher", "troublemaker", "problem-solver", "hotshot", "awkward", "greenhorn", "first unto the breach", "tough guy", "moral support", "technical specialist", "survivor", "career soldier"])
	
## Trader
if professiongroup is "Trader":
	traderReputation = random.choice(["honest trader", "scoundrel", "womanizer", "hunted", "mystic", "roamer", "treasure hunter", "well-connected", "ruthless", "generous", "shady connections", "legend", "used car salesman", "old dog"])
	traderBusiness = random.choice(["broker", "weapons trader", "ship trader", "ship parts trader", "ground vehicle trader", "junk merchant", "travelling peddler", "wholesale merchant", "artifact trader", "banker", "slave trader"])
	
## Scientist
if professiongroup is "Scientist":
	scientistBranch = random.choice(["Physician", "Physicist", "Biologist", "Biochemist", "Economist", "Data-Scientist", "Astrophysicist", "Xenobiologist", "Cultural Scientist"])

## Criminal
if professiongroup is "Criminal":
	criminalAssociation = random.choice(["working alone", "major syndicate", "minor syndicate", "corrupt officials", "guerilla organization", "foreign power", "corporation"])
	criminalCrimes = random.choice(["murder", "theft", "embezzlement", "espionage", "drug trafficking", "lifeform trafficking", "smuggling", "rebellion", "arson", "sabotage"])
	criminalStatus = random.choice(["hunted", "kill on sight", "wanted dead or alive", "wanted alive", "off the grid", "unnoticed", "legendary", "untouchable", "wanted for questioning"])
	criminalPower = random.choice(["local", "systemwide", "authoritywide", "sectorwide", "unimportant"])



################################################
################################################
###              OUTPUT                      ###
################################################
################################################


print ("")
print ("")
print ("==GENERAL INFO==")
print ("Species:", species)
if subspecies is not (""):
	print ("Subspecies:", subspecies)
if gender is not (""):
	print ("Gender:", gender)
print ("")
print ("==PROFESSION==")
print ("Profession Group:", professiongroup)
if professiongroup is "Military":
	print ("Branch:", militaryBranch)
	print ("Rank:", militaryRank)
	print ("Reputation:", militaryReputation)
if professiongroup is "Trader":
	print ("Business:", traderBusiness)
	print ("Reputation:", traderReputation)
if professiongroup is "Scientist":
	print ("Branch:", scientistBranch)
if professiongroup is "Criminal":
	print ("Association:", criminalAssociation)
	print ("Main crime:", criminalCrimes)
	print ("Status:", criminalStatus)
	print ("Importance:", criminalPower)
print ("")
print ("==DESCRIPTION==")
print (descriptionText)
print ("")