#Dictionary - using dictionary to represent a model such an object
# instantiated with {} braces

# Defining BlackStone Stock
bxStock = {"COMPANY_NAME":"BlackStone","INDUSTRY":"Finance","SUB-INDUSTRY":"Private Equity","PRICE":22.50}
# Accessing Value in Model
print("SUB-INDUSTRY: %s" % bxStock['SUB-INDUSTRY'])

# Adding Values to dictionary
bxStock["SANCTION"] = "NON-SANCTION"
print(bxStock)