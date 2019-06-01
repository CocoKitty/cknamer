SOURCE = "mbay_source_ext.txt"
OUTPUT = "mbay_output_ext.txt"
SPECIAL= "# Information gotten from https://names.mongabay.com/most_common_surnames.htm and the other connected pages\n"

import getpass

print("Opening "+SOURCE+"...")
with open(SOURCE, "r") as source:
    print("Reading "+SOURCE+"...")
    raw_data = source.readlines()
    print("2D-izing"+SOURCE+"...")
    raw_data = [x.split() for x in raw_data]

output = "# This was processed by dev_tools/mbay_parse.py\n"+SPECIAL+"\n>MAIN\n\n"

print("Compiling "+SOURCE+"...")

number = 0
with open(OUTPUT, "w") as output_file:
    output_file.write(output)
    for f in raw_data:
        if (number % 100) == 0:
            print(f"{number//len(raw_data)*100}% Complete", end="\r")
        output_file.write(f[0].title() + "::" + f[1].replace(",","") + "\n")

getpass.getpass(prompt="Press return to exit...")