my_hash_set = [
    ['Jones'],
    ['Bob'],
    ['Siri'],
    ['Pete']
]

def hash_function(value):
    return sum(ord(char) for char in value) % 10        # 3
    
def add(value):
    index = hash_function(value)
    print(index)        # 3
    bucket = my_hash_set[index]   # bucket = my_hash_set[3]
    if value not in bucket:
        bucket.append(value)      # bucket.append('stuart')
        
def contains(value):
    index = hash_function(value)
    bucket = my_hash_set[index]
    return value in bucket

add('Stuart')

print(my_hash_set)          # [['Jones'], ['Bob'], ['Siri'], ['Pete', 'Stuart']]
print('Contains Stuart:',contains('Stuart'))    # Contains Stuart: True
