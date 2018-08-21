import random
import global_cfg

def d(n): 
	return random.randint(1, n)

#BASIC INFORMATION
#rollable table: species
species = random.choice(["Sernan", "Cartheyn", "Aureian", "Crimley", "Zezz", "Sleen", "Savan", "Dust Bunny", "Nog", "Jay", "Sulskym"])

#rollable table: subspecies
subspecies = ""
if species == "Sernan":
	subspecies = random.choice(["Athenian", "Cerberi", "Zero", "Meton"])
	
#rollable table: gender
if species is not "Sleen":
	gender = random.choice(["Male", "Female"])
if species is "Sleen":
	gender = "Neutral"

#NullCharname
charName = "Chary McCharacterface"
	
#init gender pronouns for description
if gender is "Male":
	genderPronounThey = "he"
	genderPronounTheir = "his"
if gender is "Female":
	genderPronounThey = "she"
	genderPronounTheir = "her"
if gender is "Neutral":
	genderPronounThey = "xe"
	genderPronounTheir = "xeir"

#############################	
# physical description module
#region
descriptionTextSet = 0

if species is "Sernan":
	#hair color
	hairColor = random.choice(["brown", "chestnut", "dark brown", "blonde", "peroxide blonde", "strawberry blonde", "golden blonde", "mousy", "ash brown", "red", "brunette", "jet black", "salt and pepper", "silver fox", "bleached", "dyed"])
	if hairColor is "dyed":
		hairColor = random.choice(["dyed blue", "dyed red", "dyed green", "dyed orange", "dyed purple"])

	#skin color
	skinColor = random.choice(["alabaster", "albino", "almond", "anemic", "apricot", "ashen", "beige", "bisque", "black", "blanched", "bloodless", "blue-tinged", "blushing", "brick-colored", "bronze", "brown", "butterscotch", "buttery", "cafe-au-lait", "caramel", "cedar", "chalky", "charcoal", "chestnut", "chocolate", "cinnamon", "coffee", "colored", "colorless", "copper", "coral", "cream-colored", "creamy", "dark", "dappled", "dusky", "ebony", "espresso", "fair", "fawn", "fiery", "florid", "flushed", "flushing", "freckled", "ghostly", "ginger", "golden", "granite-grey", "grey", "ivory", "jaundiced", "lily-white", "liver-spotted", "mahagoney", "mango", "milk-white", "milky", "mottled", "ochre", "olive", "painted", "pale", "pallid", "pasty", "peaches-and-cream", "peach-colored", "pearly", "pink", "porcelain", "red", "reddened", "rose-brown", "rosy", "rouged", "rubicund", "ruddy", "russet", "sallow", "sand-colored", "sepia", "shock-white", "sienna", "snowy", "sooty", "sorrel", "spotted", "sunny", "sunburnt", "swarthy", "tan", "tanned", "tarnished", "taupe", "tawny", "teak", "terra cotta", "toffee", "umber", "vanilla", "wan", "washed-out", "waxen", "white", "yellow"])

	#body description
	randomRoll = d(3)
	if randomRoll is 3:
		bodyShapeModifier = random.choice(["rather", "very", "pretty", "vaguely", "barely", "mostly", "arguably", "definitely", "extremely"]) + " "
	if randomRoll is not 3: 
		bodyShapeModifier = ""
	bodyShape = random.choice(["shaped like an hourglass", "a wisp of a person", "built like a brick shithouse", "beefy", "big", "tall and lanky", "burly", "of average shape", "of attractive shape", "buff", "gawky", "gangling", "heavy-set", "lank", "lanky", "leggy", "muscular", "muscly", "herculean", "shaped like a pear", "pigeon-chested", "round-shouldered", "slightly built", "solid", "statuesque", "stooped", "strapping", "taut", "thick-set", "well-built", "willowy"])

	#name generator
	firstNameOrigin = random.choice(["Chinese", "Japanese", "Russian", "English", "English", "English", "German", "French", "Indian", "Arabic"])
	if gender is "Female":
		firstName = random.choice(["Jessica", "Carolyn", "Anna", "Julia", "Sarah", "Caitlin", "Catherine", "Stephanie"])
	if gender is "Male":
		firstName = random.choice(["John", "Alexander", "Alex", "James", "Michael", "Mike", "Thomas", "Tom", "Patrick"])
	
	lastName = random.choice(["Tolwyn", "O'Donnell", "McCormick", "Johnson", "Smith", "Peterson", "Michaels"])

	charName = firstName + " " + lastName

	########
	#OUTPUT#
	########

	descriptionText = genderPronounThey.capitalize() + " has " + skinColor + " skin and " + hairColor + " hair. " + genderPronounThey.capitalize() + " is " + bodyShapeModifier + bodyShape + "."
	descriptionTextSet = 1 

if species is "Sleen":
	#fix gender
	gender = "Neutral"
	genderPronounThey = "zi"
	genderPronounTheir ="zir"

	#skin color
	skinColor = random.choice(["emerald", "sea-green", "sea-blue", "sky-blue", "mottled", "bright green", "light blue", "purplish", "deep-sea blue", "moss-green", "leaf-green", "azure", "cyan", "flush blue", "ice blue", "dirty blue", "dirty green", "blue-green", "olive", "apple", "aquamarine", "beryl", "chartreuse", "fir", "forest", "grass", "jade", "kelly", "lime", "malachite", "moss", "pea", "peacock", "pine", "sage", "sap", "sea", "spinach", "verdigris", "willow"])

	#voice type
	voiceType = random.choice(["soft", "young", "aged", "rough", "erratic", "sexy", "high-pitched", "low-pitched", "vigorous", "taut", "cracked"])

	##modifier
	randomRoll = d(3)
	if randomRoll is 3:
		voiceModifier = random.choice(["rather", "very", "pretty", "vaguely", "barely", "mostly", "arguably", "definitely", "extremely"]) + " "
	if randomRoll is not 3: 
		voiceModifier = ""

	#preparation for a/an distinction
	anA = "a "

	#name generator
	sleenName1 = random.choice(["Mo", "Ro", "Zo", "Zi", "Ro", "Go", "Da", "Do", "Lo", "Wo", "Zi", "Ze"])
	sleenName2 = random.choice(["ke","de","po","ba","te","bo","ge","le","ma","ro","go","ko","wo"])
	sleenName3 = random.choice(["","","","","","","","","","","ke","de","po","ba","te","bo","ge","le","ma","ro","go","ko","wo"])
	#firstName = random.choice(["Move","Sike","Zile","Gole","Goke","Aike","Dake","Dove","Gave","Mole","Sole","Zale","Gove","Zike","Aake","Deke","Aale","Deve","Gele","Mive","Aile","Sale","Male","Sive","Zoke","Dave","Dale","Aole","Sele","Gale","Dele","Give","Gike","Doke","Zele","Dive","Dile","Aave","Aoke","Meke","Sile","Geve","Dike","Zeve","Zove","Zake","Aove","Mave","Aive","Seve","Make","Zive","Sake","Meve","Seke","Gile","Save","Mike","Aele","Dole","Geke","Soke","Aeve","Mele","Gake","Zave","Moke","Zeke","Sove","Mile","Zole","Aeke"])

	########
	#OUTPUT#
	########
	charName = sleenName1 + sleenName2 + sleenName3
	descriptionText = genderPronounThey.capitalize() + " has " + skinColor + " skin and " + genderPronounTheir + " voicebox produces " + anA + voiceModifier + voiceType + " voice."
	descriptionTextSet = 1

if species is "Cartheyn":
	furShape = random.choice(["fuzzy", "well-kempt", "fashionable", "long", "short", "thick", "sparse", "singed", "natural", "spotty", "groomed"])

	randomRoll = d(3)
	if randomRoll is 3:
		bodyShapeModifier = random.choice(["rather", "very", "pretty", "vaguely", "barely", "mostly", "arguably", "definitely", "extremely"]) + " "
	if randomRoll is not 3: 
		bodyShapeModifier = ""

	furColor = random.choice(["brown", "chestnut", "dark brown", "blonde", "peroxide blonde", "strawberry blonde", "golden blonde", "mousy", "ash brown", "red", "brunette", "jet black", "salt and pepper", "silver fox", "bleached", "dyed"])
	if furColor is "dyed":
		furColor = random.choice(["dyed blue", "dyed red", "dyed green", "dyed orange", "dyed purple"])

	randomRoll = d(3)
	if randomRoll is 3:
		eyeModifier = random.choice(["rather", "very", "pretty", "vaguely", "barely", "mostly", "arguably", "definitely", "extremely"]) + " "
	if randomRoll is not 3: 
		eyeModifier = ""

	eyeColor = random.choice(["red", "golden", "grey", "brown", "dusty", "green", "white", "silver", "bronze", "quicksilver", "dark brown", "black", "steel-gray"])
	eyeDescriptor = random.choice(["watchful", "aggressive", "distrustful", "blank", "glaring", "begnign", "cute", "experienced", "old", "awake", "tired", "soft", "hard"])

	#name generator
	charName = "Doggy McDogface"

	########
	#OUTPUT#
	########

	descriptionText = genderPronounThey.capitalize() + " has " + bodyShapeModifier + furShape + " " + furColor + " fur" + " and " + eyeModifier + eyeDescriptor + " " + eyeColor + " eyes."
	descriptionTextSet = 1

## generic description if none other is provided
if descriptionTextSet is 0:
	descriptionText = (genderPronounThey.capitalize() + " is a typical " + species + ".")
#endregion 

#############################
#profession module
#region

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

#endregion

#############################
#personality module
#region
#endregion

#############################
#history module
#region
#endregion

################################################
################################################
###              OUTPUT                      ###
################################################
################################################


print ("")
print ("")
print ("==GENERAL INFO==")
print ("Name:", charName)
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