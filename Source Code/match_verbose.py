from product_listing import Product, Listing # Product and Listing classes store input data
import json # Parses JSON strings from input files

compares = 0

prod_manufacturers = []
prod_set = [] # Holds list of Project objects
prod_file = open('products.txt', 'r') # Open text file containing JSON formatted listings
list_set = [] # Holds lists of Listing objects, divided by manufacturer (will be two-dimensional)
list_file = open('listings.txt', 'r') # Open text file containing JSON formatted listings

prod_total = 0
for line in prod_file: # Loop through each line of prod_file, parse and add to prod_set
    prod_total += 1
    parse = json.loads(line) # Parse the JSON formatted product
    if 'family' in parse: # Some of the products don't have a 'family' item. Well played.
        prod = Product(parse['product_name'], parse['manufacturer'], parse['model'],
                        parse['announced-date'], parse['family'])
    else:
        prod = Product(parse['product_name'], parse['manufacturer'], parse['model'],
                        parse['announced-date'])
    man = prod.getManufacturer() # The manufacturer is used to divide the product listings
    man = man.lower()
    if man in prod_manufacturers:
        index = prod_manufacturers.index(man)
        compares += index
        prod_set[index].append(prod)
    else:      
        prod_manufacturers.append(man)
        prod_set.append([prod])
prod_file.close()

print ("Number of comparisons after first pass: %d" % compares)

for i in range(len(prod_manufacturers)):
    list_set.append([])

list_remaining = 0 # Tracks the number of listings left after the first pass
list_total = 0 # Tracks total listings
for line in list_file: # Loop through each line of list_file, parse and add to list_set if valid manufacturer
    
    parse = json.loads(line) # Parse the JSON formatted product
    line = line[:-1]
    listing = Listing(parse['title'], parse['manufacturer'], parse['currency'], parse['price'], line)
    man = listing.getManufacturer() # The manufacturer is used to divide the product listings
    man = man.lower()
    for i in range(len(prod_manufacturers)):
        compares += 1
        list_total += 1
        if prod_manufacturers[i] in man:
            list_set[i].append(listing)
            list_remaining += 1
            break
list_file.close()       

print ("Number of comparisons after first two passes: %d" % compares)


match_count = 0
match_list = []
prod_list = []
output_list = []
error_count = 0

for i in range(len(prod_manufacturers)):
    for product in prod_set[i]:
        matches = []
        for listing in list_set[i]:
            title = listing.getTitle()
            # if match, add listing to match array
            compares += 2
            if product.isMatch(title):
                valid = True
                
                # Test for issues
                if title in match_list:
                    index = match_list.index(title)
                    if not prod_list[index] == product.getProduct():
                        valid = False
                        print "Duplicate match:"
                        print prod_list[index]
                        print product.getProduct()
                        print title
                        for k in range(len(output_list)):
                            if output_list[k][0] == prod_list[index]:
                                listings = output_list[k][1]
                                listings.pop(listings.index(listing.getJSON()))
                                if len(listings) > 0:
                                    output_list[k][1] = listings
                                else:
                                    output_list.pop(k)
                        print ""
                        error_count += 1
                        match_count -= 1

                if valid:       
                    match_list.append(title)
                    prod_list.append(product.getProduct())
                    matches.append(listing.getJSON())
                    match_count += 1
                
        # now convert product and match array to string and output
        if len(matches) > 0:
            output_list.append([product.getProduct(), matches])

results_file = open('results.txt', 'w')
for j in range(len(output_list)):
    product = output_list[j][0]
    listings = output_list[j][1]
    match_string = '{"product_name":"' + product + '","listings":['
    if len(listings) > 1:
        for m in range(len(listings) - 1): # for all but the last match
            match_string += listings[m] + ","
    match_string += listings[len(listings) - 1] + ']}' # print final listing with closing brackets
    #output match_string to a file!
    results_file.write(match_string + '\n')
results_file.close()

print ("Listings left after first pass: %d" % list_remaining)           
print ("Number of matches: %d" % match_count)
print ("Total number of comparisons: %d" % compares)
print ("Number of errors (duplicate match): %d" % error_count)
print ("")
raw_input("Done. Press enter to close.")


