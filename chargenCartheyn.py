#import base functionality
import random
from ascg import d
from ascg import genderPronounThey
from ascg import genderPronounTheir

#important basic species information
from ascg import species

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

descriptionText = genderPronounThey.capitalize() + " has " + bodyShapeModifier + furShape + " " + furColor + " fur" + " and " + eyeModifier + eyeDescriptor + " " + eyeColor + " eyes."
descriptionTextSet = 1