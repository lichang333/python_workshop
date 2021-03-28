#!/usr/local/bin/python3


guest_list = ['Oscar Wilde', 'Lady Gaga', 'Sherlock Holmes']
for guest in guest_list:
    print("Dear " + guest + ", would you like to dine at my house at half past 8?")

print(guest_list[1] + " cannot come for dinner this evening.")
guest_list[1] = 'Warren Buffet'
for guest in guest_list:
    print("Dear " + guest + ", would you like to dine at my house at half past 8?")

guest_list.insert(0, 'Elon Musk')
guest_list.insert(3, 'Edward Hopper')
guest_list.append('Joseph Christian Leyendecker')
for guest in guest_list:
    print("Dear " + guest + ", would you like to dine at my house at half past 8?")

print(len(guest_list))
while (len(guest_list) > 2):
    cancelled_guest = guest_list.pop()
    print("Unfortunately " + cancelled_guest + " won't be able to join us this evening.")


del guest_list[0]
del guest_list[0]
print(guest_list)