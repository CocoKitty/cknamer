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
def get_gender(gender):
    try:
        return GENDER_CONV[gender.lower()]
    except:
        print(f"Fatal: {gender} is not a valid gender!")
        print("Try m for male or f for female!")
        quit()

gender = sys.argv[2]

first_names = []
last_names = []

try:
    with open("config.nmv", "r") as config_file:
        config = nmv.load(config_file)
except FileNotFoundError:
    print("Fatal: Config file not found!")
    quit()
except:
    print("Fatal: Unknown Error in config file!")

if sys.argv[1] == "generate":
    if len(sys.argv) == 3:
        packages = config["DEFAULTS"]["def_pack"].split(";")
    else:
        packages = sys.argv[3:]
    for package in packages:

        try:
            with open(f"data/{package}/main.nmv") as package_file_obj:
                package_nmv = nmv.load(package_file_obj)["NONE"]
        except FileNotFoundError: # Package doesn't exist
            print(f"Fatal: Package '{package}' does not exist!'")
            quit()
        except: # Unknown Error in package
            print(f"Fatal: Unknown Error when loading package '{package}'!")
            quit()
        
        print("Using Package "+package_nmv["title"]+"...")
        for file_ in package_nmv["first_names"].split(";"):
            print(f"Loading first name file {file_}...")

            try:
                with open(file_, "r") as file_obj:
                    file_nmv = nmv.load(file_obj)
            except FileNotFoundError:
                print(f"Fatal: File {file_} is missing!")
                quit()
            except:
                print(f"Fatal: Unknown Error when reading {file_}")
            
            for item in file_nmv[get_gender(gender)].items():

                # ADD OPTIMIZATION FOR
                # RANDOM HERE
                for i in range(int(item[1])//int(package_nmv["first_div"])): # //100 for speed and to prevent mem err
                    first_names.append(item[0])
        for file_ in package_nmv["last_names"].split(";"):
            print(f"Loading last name file {file_}...")

            try:
                with open(file_, "r") as file_obj:
                    file_nmv = nmv.load(file_obj)
            except FileNotFoundError:
                print(f"Fatal: File {file_} is missing!")
            except:
                print(f"Fatal: Unknown Error when reading {file_}!")

            for item in file_nmv["MAIN"].items():
                for i in range(int(item[1])//int(package_nmv["last_div"])): # //1000 to prevent memory error!
                    last_names.append(item[0])
    print("Loading Complete!")

    print("Your random name is:")
    print(random.choice(first_names) + " " + random.choice(last_names))
else:
    print("USAGE: namer [option] [gender or other] extra args...")
    quit()
        
    

