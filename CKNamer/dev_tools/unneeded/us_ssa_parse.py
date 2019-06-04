SOURCE = "uk_bnw_source.txt" # Change to parse other file
OUTPUT = "uk_bnw_output.txt" # Change to output other file
SPECIAL = "# Information gotten from a source I can't find anymore :C\n"

# Custom for if change
custom = False

# to flip women one
# Becuase unknown source is like ?
woman_flip = 1 # True
if custom:
    SOURCE = "us_ssa_source_1000.txt"
    OUTPUT = "us_ssa_output_1000.txt"
    SPECIAL = "# Information gotten from https://www.ssa.gov/cgi-bin/popularnames.cgi\n"

import getpass

print("Opening "+SOURCE+"...")
with open(SOURCE, "r") as source:
    print("Reading "+SOURCE+"...")
    raw_data = source.readlines() # Turns data into list of rows
    print("2D-izing "+SOURCE+"...")
    raw_data = [x.split()[1:] for x in raw_data] # makes 2d by adding columns, also removes numbering at start

female_names = []
male_names   = []

print("Dictizing"+SOURCE+"...")
for row in raw_data:
    male_names.append( [row[0], row[1].replace(",","")] )
    female_names.append( [row[2], row[3].replace(",","")] )

output = "# This was processed by dev_tools/us_ssa_parse.py\n"+SPECIAL+"\n>MEN\n\n"

print("Packaging Dict into plaintext...")
print("Male names...")
for i in range(len(male_names)):
    output += male_names[i][0].title() + "::" + male_names[i][1] + "\n"

output += "\n>WOMEN\n\n"
print("Female names...")
for i in range(len(female_names)):
    output += female_names[i][0+woman_flip].title() + "::" + female_names[i][1-woman_flip] + "\n"

with open(OUTPUT, "w") as output_file:
    output_file.write(output)

print("Complete, printed to "+OUTPUT+"!")

getpass.getpass(prompt="Press return to exit ")