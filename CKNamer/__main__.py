import sys
import os
import nmv
import random

import os
os.chdir(os.path.dirname(__file__))

if len(sys.argv) < 3:
    print("USAGE: namer [option] [gender or other] extra args...")
    quit()

GENDER_CONV = {"f":"WOMEN","m":"MEN"}

gender = sys.argv[2]

first_names = []
last_names = []

with open("config.nmv", "r") as config_file:
    config = nmv.load(config_file)

if sys.argv[1] == "generate":
    if len(sys.argv) == 3:
        packages = config["DEFAULTS"]["def_pack"].split(";")
    else:
        packages = sys.argv[3:]
    for package in packages:
        with open(f"data/{package}/main.nmv") as package_file_obj:
            package_nmv = nmv.load(package_file_obj)["NONE"]
        print("Using Package "+package_nmv["title"]+"...")
        for file_ in package_nmv["first_names"].split(";"):
            print(f"Loading first name file {file_}...")
            with open(file_, "r") as file_obj:
                file_nmv = nmv.load(file_obj)

            for item in file_nmv[GENDER_CONV[gender]].items():

                # ADD OPTIMIZATION FOR
                # RANDOM HERE
                for i in range(int(item[1])//int(package_nmv["first_div"])): # //100 for speed and to prevent mem err
                    first_names.append(item[0])
        for file_ in package_nmv["last_names"].split(";"):
            print(f"Loading last name file {file_}...")
            with open(file_, "r") as file_obj:
                file_nmv = nmv.load(file_obj)

            for item in file_nmv["MAIN"].items():
                for i in range(int(item[1])//int(package_nmv["last_div"])): # //1000 to prevent memory error!
                    last_names.append(item[0])
    print("Loading Complete!")

    print("Your random name is:")
    print(random.choice(first_names) + " " + random.choice(last_names))

        
    

