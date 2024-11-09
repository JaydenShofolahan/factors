#Name: Jayden Shofolahan 
#Date: 11/09/24 
#Description: This code will ask for a CSV file and list the top three contributing factors for vehicle collisions 

import pandas as pd 
import matplotlib.pyplot as plt 
csvu = input("Enter a csv file") 
max = pd.read_csv(csvu)
print("The top 3 contributing factors to vehicle collisions are: ", max["CONTRIBUTING FACTOR VEHICLE 1"], max["CONTRIBUTING FACTOR VEHICLE 2"], max["CONTRIBUTING FACTOR VEHICLE 1"]) 
max["CONTRIBUTING FACTOR VEHICLE 1"]
