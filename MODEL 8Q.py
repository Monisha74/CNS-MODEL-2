import hashlib

sensor_data = input("Enter temperature sensor data: ")

hash_object = hashlib.sha1(sensor_data.encode())
sensor_hash = hash_object.hexdigest()

print("\nSHA-1 hash of the sensor data:")
print(sensor_hash)

received_data = sensor_data  
received_hash = hashlib.sha1(received_data.encode()).hexdigest()

if received_hash == sensor_hash:
    print(" Data integrity verified. No tampering detected.")
else:
    print(" Data integrity verification failed. Data may be tampered.")
