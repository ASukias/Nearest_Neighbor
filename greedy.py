from hash import Truck, hashTable
from main import distanceBetween
#define a greedy algorithm
def greedyTruck(truck):
    '''Truck.location =
    Truck.mileage = 0.0
    Truck.currentTime = timedelta(hours=8, minutes=0)
    truckSpeed = 18  # Miles per hour given'''

    while len(truck.packages) > 0:
        minDistance = float('inf')
        closestPackage = None  # no package

        for packageID in truck.packages:
            package = hash_table.lookup(packageID)
            trckLocation = truck.currentLocation
            pckAddress = package.address
            distance = distanceBetween(trckLocation, pckAddress)

            if distance < minDistance:
                minDistance = distance
                closestPackage = package

        truck.total_mileage += distance

        truck.current_time += timedelta(hours=minDistance / 18.0)

        closestPackage.delivery_time = truck.current_time

        closestPackage.delivery_status = "DELIVERED"
        #print(closestPackage)

        hash_table.insert(closestPackage.package_id, closestPackage)

        truck.packages.remove(closestPackage.package_id)

    return