# this does file i/o
import pickle
# sys is for stdin
import sys

# this is a hash lookup table where the key is the first of these two elements
# it is called a dict

recipes = {
    "Light Infantry": "2 oz whiskey\n1 oz Lillet Blanc\n1/2 oz vermouth (which?)\n4 dashes orange bitters\nOrange peel for glass\nMaraschino cherry (optional)",
    "Chilcano": "2 oz pisco\n1/2 oz fresh lime juice\n1/4 oz fresh ginger juice\n3/4 oz simple syrup\nGinger ale\nAngostura bitters\n(Very gingery, mostly loses the taste of the pisco)",
    "Foghorn": "1/4 oz absinthe (rinse the glass)\n2 oz gin (Plymouth recommended)\n1/2 oz Lillet Blanc\n1/2 oz Cointreau or triple sec\nLemon twist for garnish\nShake with ice and strain into glass\n(If you don't have the lemon twist the drink is better with a few drops of lemon juice)",
    "Sunset Sour": "1/2 oz frangelico\n1 1/4 oz bourbon\n1 oz lemon juice\n1/2 oz 'spiced simple syrup'\n1 egg white\nDash of grated nutmeg\n(Might do fine without the egg white. Also perhaps a touch less simple syrup.)",
    "Genoa": "1.5 oz grappa\n2 teaspoons sambuca\n2 teaspoons dry vermouth\nShake with ice and strain\n(Delicious, refreshing, crisp)",
    "Empress 75": "1.5 oz Empress gin\n0.75 oz lemon juice\n0.5 0z simple syrup\nProsecco to top off the glass\nMis all except prosecco in shaker with ice.  Strain into champagne flute.  Top off with prosecco.",
    "Sidecar": "2 oz cognac\n0.75 oz triple sec\n0.75 oz lemon juice\nShake with ice, strain into cocktail glass.",
    "Medicine ;)": "2 oz bourbon\nJuice of half a lemon\n4 oz water\nTablespoon of honey",
    "Flight of the Concorde": "2 oz grappa\n0.75 oz creme de violet\n0.75 oz lemon juice\nShake with ice, strain into martini glass.",
    "Mulberry and Lillet Blanc": "2:1 mulberry gin and Lillet Blanc.  Pour over ice.",
    "Smoky Martini": "2 oz gin\n0.5 oz dry vermouth\n0.5 oz whiskey",
    "Daiquiri": "2 oz rum\n1 oz lime juice\n3 'bar spoons' (teaspoons?) simple syrup",
    "Ginger Lemongrass Thing": "3 tablespoons vodka\n1 cube (0.75 oz?) lemon juice\n1/2 tablespoon simple syrup\n1/2 tablespoon Domaine Canton\n1 teaspoon ginger juice\n1/2 teaspoon lemongrass puree\nShake with ice, strain through fine strainer into a martini glass",
    "Old Fashioned": "3 oz gin\n1 oz simple syrup\n1 dash orange bitters",
    "Basil Gimlet": "5 large basil leaves\n1.5 oz gin\n0.75 oz fresh lime juice\n0.5 oz simple syrup\nMuddle the leaves in a shaker, add the rest, fill with ice, shake a lot, strain into chilled 'coupe' whatever that is.",
    "Golden Pear": "4 oz vodka\n1 oz Domaine Canton\n1 oz St George spiced pear",
    "Suffering Bastard": "1 oz bourbon or whiskey\n1 oz gin\n1 oz lime juice\n4 oz ginger beer *\nDash of Angostura bitters\nBuild this in the glass and stir.\n* Many recipes call for ginger syrup and seltzer.  Some use the seltzer as a float."
}

fp = open("drink_recipes.dat", "wb")
pickle.dump(recipes, fp)
fp.close()

fp2 = open("drink_recipes.dat", "rb")
recipes2 = pickle.load(fp2)
fp2.close()

'''
for drink in recipes:
    print(drink)
    print(recipes[drink]) # this looks up the key and returns its value
    print()
'''

def find_ingredient(ingredient):
    if (ingredient == ""):
        print ("I can tell you're bored.")
        exit # how the hell do I stop the program?
    print "Here are all the ones containing", ingredient
    for drink,recipe in recipes2.items(): # this iterator returns key,value pairs
        if recipe.find(ingredient) != -1: # returns byte index of substring
            print
            print(drink)
            print(recipe)

# print()
# find_ingredient("vodka")

print
print("Look for an ingredient: ")

thingy = sys.stdin.readline()
thingy = thingy.strip() # take the newline off
find_ingredient(thingy)

print
