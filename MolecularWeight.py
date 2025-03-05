import re #import the regular expressions module for pattern matching 
from periodictable import elements #import elements from the periodic table library

def chem_formula (formula): #breaking formula into element and number of atoms
    pattern = r'([A-Z][a-z]*)(\d*)' #extracting elements and their no of atoms
    matching = re.findall(pattern, formula) #searching the formula and matching them to the pattern
    parsed = {} #empty dictionary
    
#trying to populate the dictionary
    
    for element, count in matching: #element, count is the tuple in matching eg [(C,6),(H,12)]...
        count = int(count) if count else 1 #converting the count to an integer, if there's no count assume 1
        parsed[element] = parsed.get(element, 0) + count #storing elements as keys for the parsed dictionary, and count as values
        #parsed.get(element, 0) is searching the parsed dictionary to see if the element already exists. For example if the formula is C6H12,
        #parsed.get('C',0) will search the parsed dictionary to see if C exists and return the value, since it initially doesn't exist, it will return 0
        #Now it will add the count from the matching tuples where we have [(C,6),(H,12)]. Here the element C has a count of 6 so we have
        #parsed[element]= 0 + 6
    return parsed

def find_molecular_weight(formula):
    chemd_formula = chem_formula(formula) #stores the dictionary output from chem_formula() as we returned parsed
    molecular_weight = 0.0 #float
    for element, count in chemd_formula.items(): #in parsed, we labelled the key and value as element and count
        try:
             a_w = elements.symbol(element).mass
             molecular_weight += a_w * count #accumulating the molecular weight
        except AttributeError:
            return f"Invalid element: {element}" #this is an f-string, allows us to insert variables inside curly brackets
    return molecular_weight
        
formula = input("enter molecular formula:")
print (f"Molecular Weight: {find_molecular_weight(formula):.2f} g/mol")

       
        


    
    
    



