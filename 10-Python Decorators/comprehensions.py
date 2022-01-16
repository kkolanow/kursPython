alien_dict =  {"color":"green", "origin":"Mars"}

del alien_dict['origin']

print(alien_dict)

#print(alien_dict.get('color'))
if alien_dict.get('size')==None:
    pass
#    print("No key size")

try:
    alien_dict['size']
except:
    pass
#    print("Error in getting size")