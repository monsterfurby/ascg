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
	subspeciestable = ["Athenian", "Cerberi", "Zero", "Meton"]
	subspecies = random.choice(subspeciestable)
	
#rollable table: gender
gender = ""
if species is not "Sleen":
	gendertable = ["Male", "Female"]
	gender = random.choice(gendertable)
	
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
	hairColor = random.choice(["brown", "chestnut", "dark brown", "blonde", "peroxide blonde", "strawberry blonde", "golden blonde", "mousy", "ash brown", "red", "brunette", "jet black", "salt and pepper", "silver fox", "bleached", "dyed"])
	skinColor = random.choice(["alabaster", "albino", "almond", "anemic", "apricot", "ashen", "beige", "bisque", "black", "blanched", "bloodless", "blue-tinged", "blushing", "brick-colored", "bronze", "brown", "butterscotch", "buttery", "cafe-au-lait", "caramel", "cedar", "chalky", "charcoal", "chestnut", "chocolate", "cinnamon", "coffee", "colored", "colorless", "copper", "coral", "cream-colored", "creamy", "dark", "dappled", "dusky", "ebony", "espresso", "fair", "fawn", "fiery", "florid", "flushed", "flushing", "freckled", "ghostly", "ginger", "golden", "granite-grey", "grey", "ivory", "jaundiced", "lily-white", "liver-spotted", "mahagoney", "mango", "milk-white", "milky", "mottled", "ochre", "olive", "painted", "pale", "pallid", "pasty", "peaches-and-cream", "peach-colored", "pearly", "pink", "porcelain", "red", "reddened", "rose-brown", "rosy", "rouged", "rubicund", "ruddy", "russet", "sallow", "sand-colored", "sepia", "shock-white", "sienna", "snowy", "sooty", "sorrel", "spotted", "sunny", "sunburnt", "swarthy", "tan", "tanned", "tarnished", "taupe", "tawny", "teak", "terra cotta", "toffee", "umber", "vanilla", "wan", "washed-out", "waxen", "white", "yellow"])
	if hairColor is "dyed":
		hairColor = random.choice(["dyed blue", "dyed red", "dyed green", "dyed orange", "dyed purple"])
	randomRoll = d(3)
	if randomRoll is 3:
		bodyShapeModifier = random.choice(["rather", "very", "pretty", "vaguely", "barely", "mostly", "arguably", "definitely", "extremely"]) + " "
	if randomRoll is not 3: 
		bodyShapeModifier = ""
	bodyShape = random.choice(["shaped like an hourglass", "a wisp of a person", "built like a brick shithouse", "beefy", "big", "tall and lanky", "burly", "of average shape", "of attractive shape", "buff", "gawky", "gangling", "heavy-set", "lank", "lanky", "leggy", "muscular", "muscly", "herculean", "shaped like a pear", "pigeon-chested", "round-shouldered", "slightly built", "solid", "statuesque", "stooped", "strapping", "taut", "thick-set", "well-built", "willowy"])
	descriptionText = genderPronounThey.capitalize() + " has " + skinColor + " skin and " + hairColor + " hair. " + genderPronounThey.capitalize() + " is " + bodyShapeModifier + bodyShape + "."
	descriptionTextSet = 1
	
## Cartheyn
if species is "Cartheyn":
	furColor = random.choice(["brown", "chestnut", "dark brown", "blonde", "peroxide blonde", "strawberry blonde", "golden blonde", "mousy", "ash brown", "red", "brunette", "jet black", "salt and pepper", "silver fox", "bleached", "dyed"])
	if furColor is "dyed":
		furColor = random.choice(["dyed blue", "dyed red", "dyed green", "dyed orange", "dyed purple"])
	descriptionText = genderPronounThey.capitalize() + " has " + furColor + " fur."	
	descriptionTextSet = 1
	
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
	
#rollable table: color
tableseg = d(8)
if tableseg == 1 :
	color = "red"
if tableseg == 2:
	color = "orange"
if tableseg == 3:
	color = "yellow"
if tableseg == 4:
	color = "green"
if tableseg == 5:
	color = "blue"
if tableseg == 6:
	color = "white"
if tableseg == 7:
	color = "brown"
if tableseg == 8:	
	color = "black"

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