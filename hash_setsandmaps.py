# hash function is something that maps the data to a position.
# sometimes it might render the same position for 2 or more data entries.
# this is a hash collision
# collisions are dealt with by using chaining
# open addressing: linear probing, quadratic probing, double hashing is another way to deal
# with hash collisions
# hash set look up O(1), adding O(1) or length of chain., deleting O(1)
# hashmaps (dictionaries) have all the functionality of hashsets but allow to store data
# key value pairs
# keys must be hashable : strings, ints, tuples : immutable data types
# from collections import defaultdict : this dict can have a default value for any key set
# to a datatype of your choice eg defaultdict(int) has 0's at every key.


s = set()
s.add(1)
s.add(3)
s.add(3)
print(s)
print(f"1 in set?:{1 in s}")
print(f"7 in set?:{7 in s}")

string = "sjboqhwpibfbqpwosfjbdfcbvnwiepjqpfpoqjsjfipdofiw"
print(string)
str_set = set(string) #O(len(string)) hash construction complexity
print(f"unique letters in the srting: {str_set}")
# now we can easily check for occurences
print(f"z in string?: {"z" in str_set}")
print(f"a in string?: {"a" in str_set}")
print(f"j in string?: {"j" in str_set}")

