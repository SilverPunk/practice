'''
language = {
    'Nazar': 'python',
    'Andriy': 'php',
}
for name, value in language.items():
    print("It`s working for " + value + ".")
    print("You must be happy " + name + '.')
'''
'''
alien_0 = {'color': 'green', 'point': '5'}
alien_1 = {'color': 'yellow', 'point': '10'}
alien_2 = {'color': 'red', 'point': '15'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
'''

# aliens = []
# #Creating 30 aliens
# for alien_number in range (0,30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
# aliens.append(new_alien)
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# #Output a first 5 aliens
# for alien in aliens[0:5]:
#     print(alien)
#     print("...")
#All aliens which will outpooted
#print("Total number of aliens: " + str(len(aliens)))


a = input("Input something: ")
print(a)
