#Study Drills ex 39

#create a dict with some kind of mapping
# use Python docs to do more things to the dict

neighborhoods = { 
	'Richmond': 'northwest',
	'Sunset': 'west',
	'Marina': 'north',
	'Russian Hill': 'north',
	'Mission': 'southeast',
	'Palo Alto': 'south south'
}

neighborhoods['Noe Valley'] = 'south'


print neighborhoods.keys()

PA= 'Palo Alto' in neighborhoods
print PA

area_codes = {
	'San Francisco': '415',
	'Mill Valley': '415',
	'Palo Alto': '650',
	'Sunnyvale': '408',
	'Oakland': '510'
}
for place in neighborhoods.keys():
	area_codes[place]= area_codes['San Francisco']


print list(enumerate(area_codes))

# print area_codes

for key, value in area_codes.items():
	print "the area code for %s is %s" % (key, value)



