#import base functionality
import random
from ascg import d
from ascg import genderPronounThey
from ascg import genderPronounTheir

#important basic species information
from ascg import species

#hair color
hairColor = random.choice(["brown", "chestnut", "dark brown", "blonde", "peroxide blonde", "strawberry blonde", "golden blonde", "mousy", "ash brown", "red", "brunette", "jet black", "salt and pepper", "silver fox", "bleached", "dyed"])
if hairColor is "dyed":
	hairColor = random.choice(["dyed blue", "dyed red", "dyed green", "dyed orange", "dyed purple"])
skinColor = random.choice(["alabaster", "albino", "almond", "anemic", "apricot", "ashen", "beige", "bisque", "black", "blanched", "bloodless", "blue-tinged", "blushing", "brick-colored", "bronze", "brown", "butterscotch", "buttery", "cafe-au-lait", "caramel", "cedar", "chalky", "charcoal", "chestnut", "chocolate", "cinnamon", "coffee", "colored", "colorless", "copper", "coral", "cream-colored", "creamy", "dark", "dappled", "dusky", "ebony", "espresso", "fair", "fawn", "fiery", "florid", "flushed", "flushing", "freckled", "ghostly", "ginger", "golden", "granite-grey", "grey", "ivory", "jaundiced", "lily-white", "liver-spotted", "mahagoney", "mango", "milk-white", "milky", "mottled", "ochre", "olive", "painted", "pale", "pallid", "pasty", "peaches-and-cream", "peach-colored", "pearly", "pink", "porcelain", "red", "reddened", "rose-brown", "rosy", "rouged", "rubicund", "ruddy", "russet", "sallow", "sand-colored", "sepia", "shock-white", "sienna", "snowy", "sooty", "sorrel", "spotted", "sunny", "sunburnt", "swarthy", "tan", "tanned", "tarnished", "taupe", "tawny", "teak", "terra cotta", "toffee", "umber", "vanilla", "wan", "washed-out", "waxen", "white", "yellow"])
randomRoll = d(3)
if randomRoll is 3:
	bodyShapeModifier = random.choice(["rather", "very", "pretty", "vaguely", "barely", "mostly", "arguably", "definitely", "extremely"]) + " "
if randomRoll is not 3: 
	bodyShapeModifier = ""
bodyShape = random.choice(["shaped like an hourglass", "a wisp of a person", "built like a brick shithouse", "beefy", "big", "tall and lanky", "burly", "of average shape", "of attractive shape", "buff", "gawky", "gangling", "heavy-set", "lank", "lanky", "leggy", "muscular", "muscly", "herculean", "shaped like a pear", "pigeon-chested", "round-shouldered", "slightly built", "solid", "statuesque", "stooped", "strapping", "taut", "thick-set", "well-built", "willowy"])
descriptionText = genderPronounThey.capitalize() + " has " + skinColor + " skin and " + hairColor + " hair. " + genderPronounThey.capitalize() + " is " + bodyShapeModifier + bodyShape + "."
descriptionTextSet = 1 