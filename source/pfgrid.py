'''
		pfgrid.py
		
Synopsis:
	Generates a grid of parameter files for the python radiative transfer code.
	Note that this will only generate models with the same general type due to keyword order.

'''




keywords, values = np.loadtxt('template.pf', dtype='string', unpack=True)
keywords_to_change, values_to_change = np.loadtxt('grid_values', dtype='string', unpack=True)


nx = len(values_to_change[0])
ny = len(keywords_to_change)


# calculate total number of runs
n_runs = nx ** ny

print "Welcome to pfgrid. Creating grids for %i runs..." % n_runs
print "You have %i variables with %i degrees of freedom" % (ny, nx)


all_values = []
for i in range(n_runs):
	all_values.append(values)
	

# you know have n_runs copies of the initial parameter file
	
all_values = np.array(values)


for i in range(n_runs):
	

for i in range(nx):
	for j in range()
	



while np.sum(indexing_array) < nx*ny*



''''
for i in range(ny):
	
	constant_keyword = keywords_to_change[i]
	
	for j in range(nx):
		
		keywords_temp = keywords
		values_temp = values 
		
		index_to_array = np.where(keywords == constant_keyword)
		values_temp[index_to_array] = values_to_change
		
	
		 
		all_values_array.append ( values )
		 
		 
		 


# we read a number of arguments from the command line
# the user can decide to change certain keywords
for i in range(len(keywords_to_change)):
	
	keyword = keywords_to_change[i]
	
	for j in range(len(values_to_change[i])):
	
	

		# search keyword array for keyword desired
		index_to_array = np.where(keywords == keyword)
	
		# create an array of values that have a keyword match - should be length 1!!
		value_matches = values[ index_to_array ]

		if len(value_matches)>1:	# if we havemore than one match this an error
			Error('Multiple keyword matches in parameter file!')

		elif len(value_matches)>0:	# if we have one match, change the value
			old_value = value_matches[0]
			new_value = sys.argv[i+1]
			values [index_to_array] = new_value

			print 'Changed keyword %s from %s to %s' % (keyword, old_value, new_value)'''
	
	
