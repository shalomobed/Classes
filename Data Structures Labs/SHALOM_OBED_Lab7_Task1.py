import math
class MyCustomMap:
    def __init__(self, N):
        self.size = N
        self.keys = [None] * self.size  # Stores keys
        self.values = [None] * self.size  # Stores corresponding values

    #Returns a hash code for the given key
    def hash(self, key):
        if type(key) == int:
            return key
        elif type(key) == float:
            return math.modf(key)[0]
        elif type(key) == str:
            a = 31
            m = int(1e9 + 9)
            hash_value = 0
            pow = 1 #initial power of a^0 or 1
            for c in key:
                hash_value += ((ord(c) - ord('a') + 1) * pow) % m
                pow = (pow * a) % m
            return hash_value
        else:
            raise Exception("The given key is not supported!")

    #Inserts the key and value into the hash map 
    def put(self, key, value):
        N = self.size
        hash_key = self.hash(key)

        h1 = hash_key % 13 #primary hash
        h2 = 1 + hash_key % 11 # secondary hash

        j = h1
        i = 0

        while self.keys[j] is not None and self.keys[j] != key:
            print(f"Collision at index {j}, trying next slot...")
            i += 1
            #Resolving collision using double hashing
            j = (h1 + i * h2) % N
            if i >= N:
                raise Exception("Hash table is full")
                
           
        self.keys[j] = key
        self.values[j] = value
        print(f"Inserted key {key} at index {j}")
        
    #Finds and returns the value associated with the given key
    def get(self, key):
        N = self.size
        j = self.hash(key) % N
        original_index = j

        while self.keys[j] is not None:
            if self.keys[j] == key:
                return self.values[j]
            j = (j + 1) % N
            if j == original_index:
                break
        return None
        

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


# Example usage
map = MyCustomMap(11)
map.put(10, 'a')
map.put(22, 'b')
map.put(31, 'c')
map[9] = 'd'
map[15] = 'e'



# Testing with double hashing 
print("\nTest with double hashing:")
map.put(13, "f") # should collide with key 9
