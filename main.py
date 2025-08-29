#main.py
#Student ID 0011973906

import csv
from datetime import datetime, timedelta
from hash import Truck, Package, hashTable

def load_distance_data(distance_csv, distance_data):

    with open(distance_csv, mode='r') as file:
        reader = csv.reader(file, delimiter=',') #create csv reader
        for row in reader: #iterate over each row in csv
            #using list comprehension convert non-empty elements to float
            #distlist = [float(x) for x in row if x != ""]
            distance_data.append(row) # append cleaned list to distance_data


#function to load address data from address CSV
def load_address_data(address_csv):
    address_data = []  # initiliaze empty list to store address data
    with open(address_csv, mode='r') as file:
        reader = csv.reader(file, delimiter = ',') # create csv reader
        # iterate over reach row in csv file
        for address in reader:
            address_data.append(address[2]) #append index 2 to address data
# Return the address data
    return address_data

# Path to CSV files
distance_csv = "distanceCSV.csv"
address_csv = "addressCSV.csv"

# define a function to return distance between two addresses
def distanceBetween(address1, address2):
    if address1 in address_data and address2 in address_data:
        idx1 = address_data.index(address1)
        idx2 = address_data.index(address2)
        if idx2 > idx1:
            return float(distance_data[idx2][idx1])
        else:
            return float(distance_data[idx1][idx2])
    else:
        return None



#define function to read the packageCSV file
def loadPackageData(hash_table):
    with open('packageCSV.csv', mode='r') as file:
        reader = csv.reader(file)

        for row in reader:
            package_id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            delivery_deadline = row[5]
            weight = float(row[6])

            #create a package object
            package = Package(package_id, address, city, state, zip_code, delivery_deadline, weight)

            #insert package object
            hash_table.insert(package_id, package)

#define a greedy algorithm
def greedyTruck(truck):

    #print("checking for nearest distance")
    while len(truck.packages) > 0:
        minDistance = float('inf')
        closestPackage = None #list to store packages at the closest address

        for packageID in truck.packages:
            package = hash_table.lookup(packageID)
            trckLocation = truck.currentLocation
            pckAddress = package.address
            distance = distanceBetween(trckLocation, pckAddress)
            #print(packageID," ", distance)

            if distance < minDistance:
                minDistance = distance
                closestPackage = package
            #elif distance == minDistance:
            #    closestPackage.append(package)

        #if not closestPackage:
        #    break #no package to deliver found

        #update trick mileage and current time for closest address
        truck.total_mileage += minDistance
        truck.current_time += timedelta(hours=minDistance / 18.0)
        truck.currentLocation = closestPackage.address
        closestPackage.delivery_time = truck.current_time
        closestPackage.delivery_status = "DELIVERED"
        hash_table.insert(closestPackage.package_id, closestPackage)
        #print("min package found", minDistance, package.package_id, truck.current_time, truck.total_mileage)
        truck.packages.remove(closestPackage.package_id)
    #print(truck.total_mileage)


    return

#function to print info of a given package at a given time
def print_all_package_status_and_total_mileage(trucks):
    total_mileage = 0.0
    for truck in trucks:
        total_mileage += truck.total_mileage
    print(f"Truck Total Mileage: {total_mileage:.2f}")
    for i in range(1,41):
        package = hash_table.lookup(i)
        print(package)

#function to print single package with time input
def get_single_package_statusTime(package_id, query_time):
    package = hash_table.lookup(package_id)
    if query_time < package.loading_time:
        package.delivery_status = "At the hub"
        package.loading_time = None
        package.delivery_time = None
    elif query_time < package.delivery_time:
        package.delivery_status = "En route"
        package.delivery_time = None
    if package.package_id == 9 and query_time < timedelta(hours=10, minutes=20):
        package.address = "300 State St"
    print(package)
#function to print all packages status with a time
def get_all_package_status_with_time(query_time):
    for i in range(1, 41):
        package = hash_table.lookup(i)
        if query_time < package.loading_time:
            package.delivery_status = "At the hub"
            package.loading_time = None
            package.delivery_time = None
        elif query_time < package.delivery_time:
            package.delivery_status = "En route"
            package.delivery_time = None
        if package.package_id == 9 and query_time < timedelta(hours=10, minutes=20):
            package.address = "300 State St"
        print(package)

#instantiate the hash table
hash_table = hashTable()

#load package data intp the hash table
loadPackageData(hash_table)
distance_data = []
#address_data = []
load_distance_data(distance_csv,distance_data)
address_data = load_address_data(address_csv)

# manually load trucks
truck1_list = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2_list = [2, 3, 6, 8, 10, 12, 18, 21, 23, 25, 27, 28, 32, 36, 38]
truck3_list = [4, 5, 7, 9, 11, 17, 22, 24, 26, 33, 35, 39]

# create instances of the truck classes
current_time = timedelta(hours=8, minutes=0)
truck1 = Truck(1,truck1_list, current_time)
for i in truck1_list:
    pkg = hash_table.lookup(i)
    pkg.loading_time = truck1.current_time
    pkg.trucknum = "1"
    hash_table.insert(i, pkg)

current_time = timedelta(hours=9, minutes=6)
truck2 = Truck(2, truck2_list, current_time)
for i in truck2_list:
    pkg = hash_table.lookup(i)
    pkg.loading_time = truck2.current_time
    pkg.trucknum = "2"
    hash_table.insert(i, pkg)

current_time = timedelta(hours =10, minutes =21)
pkg9 = hash_table.lookup(9)
pkg9.address = "410 S State St"
hash_table.insert(9, pkg9)
truck3 = Truck(3, truck3_list, current_time)
for i in truck3_list:
    pkg = hash_table.lookup(i)
    pkg.loading_time = truck3.current_time
    pkg.trucknum = "3"
    hash_table.insert(i, pkg)

#trucks variable to pass into the function for truck total mileage
trucks = [truck1, truck2, truck3]

"""print(address_data)
    print(distance_data)
    print(distance_data[9][0])
    print(distanceBetween('4001 South 700 East', '1060 Dalton Ave S'))
"""


greedyTruck(truck1)
'''print("truck1 list")
for i in [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]:
    print(hash_table.lookup(i))'''

greedyTruck(truck2)
'''print("truck2 list")
for i in [2, 3, 6, 8, 10, 12, 18, 21, 23, 25, 27, 28, 32, 36, 38]:
    print(hash_table.lookup(i))'''

greedyTruck(truck3)
'''print("truck3 list")
for i in [4, 5, 7, 9, 11, 17, 22, 24, 26, 33, 35, 39]:
    print(hash_table.lookup(i))
for i in range(1,41):
    print("Package: {}".format(hash_table.lookup(i)))  # 1 to 40 is sent to hash_table.lookup()
greedyTruck(truck2)
for i in [2, 3, 6, 8, 10, 12, 18, 21, 23, 25, 27, 28, 32, 36, 38]:
    print(hash_table.lookup(i))
greedyTruck(truck3)
for i in [4, 5, 7, 9, 11, 17, 22, 24, 26, 33, 35, 39]:
    print(hash_table.lookup(i))'''


# menu
print("\n Welcome to C950: WGUPS")

#intiate while loop until user chooses to exit
isExit = True
while(isExit):
    print("\nOptions:")
    print("1.Print All Package Status and Total Mileage for all Trucks")
    print("2.Get Single Package Status with a Time")
    print("3.Get ALL Package Status with a Time")
    print("4. Exit the Program")
    #user chooses through input
    option = input("Choose Option 1, 2, 3 or 4: ")
    #initiate conditional upon user input
    if option == "1":
        print_all_package_status_and_total_mileage(trucks)
    elif option == "2":
        package_id = int(input("Enter the package ID: "))
        query_time_str = input("Enter the query time (HH:MM): ")
        query_time = timedelta(hours=int(query_time_str.split(':')[0]), minutes=int(query_time_str.split(':')[1]))
        get_single_package_statusTime(package_id, query_time)
    elif option == "3":
        query_time_str = input("Enter the query time (HH:MM): ")
        query_time = timedelta(hours=int(query_time_str.split(':')[0]), minutes=int(query_time_str.split(':')[1]))
        get_all_package_status_with_time(query_time)
    elif option == "4":
        print("Exiting the program, GOOD BYE")
        isExit = False
    else:
        print("Invalid choice, Pick Between 1 and 4, Thank you")