from datetime import datetime, timedelta
class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.delivery_time = None
        self.loading_time = None
        self.delivery_status = 'At the hub'
        self.closestPackage = None
        self.trucknum = None

    def __str__(self):
        return ("ID: %s, Address: %s, %s, %s, %s, Deadline: %s, Weight: %s, Delivery Time: %s, Loading Time: %s, Status: %s, Truck#: %s" % (self.package_id, self.address, self.city, self.state, self.zip_code, self.delivery_deadline, self.weight, self.delivery_time, self.loading_time, self.delivery_status, self.trucknum ))


class hashTable:
   #initialize a hashtable
    def __init__(self, num_buckets=10):
        self.table = [[] for _ in range(num_buckets)]
    #create hash key
    def get_key(self, package_id):
        return package_id % len(self.table)

    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item

                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)

        return True


    def lookup(self, key):
        # get the bucket list where this key would be.

        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)
        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None


#Create a truck object
class Truck:
    def __init__(self, id, packages,current_time, currentLocation='4001 South 700 East'):
        self.id = id
        self.currentLocation = currentLocation
        self.total_mileage = 0.0
        self.current_time = current_time
        self.packages = packages
        self.time_left = current_time

    def __str__(self):
        return f"Truck at {self.currentLocation} with {len(self.packages)} packages."


##define a function that returns the package destination address
"""def minDistanceFrom(truck):
    min_distance = float('inf')
    closest_address = None
    package_id = 0
    #iterate through list of packages and calc dist between current loc and package's address
    for package in truck.packages:
        package_address = package.address
        package_id = package.package_id
        distance = distanceBetween(truck.currentLocation, package_address)
        if distance is not None and distance < min_distance:
            min_distance = distance
            closest_address = package_address
            package_id = package.package_id
    #return address with minimum distance
    return closest_address, min_distance, package_id"""

#define a function that delivers packages
"""def truckDeliverPackages(truck):
    while any(package.delivery_status != 'DELIVERED' for package in truck.packages):
        closest_package = minDistanceFrom(truck)
        if closest_package is None:
            break

        #update truck location:
        truck.currentLocation = closest_package.address

        #calculate delivery time using 18mph
        delivery_time = datetime.now()
        closest_package.delivery_time = delivery_time
        closest_package.delivery_status = 'DELIVERED'

        #Update total mileage
        distance_traveled = distanceBetween(truck.currentLocation, closest_package.address)
        truck.total_mileage += distance_traveled"""

