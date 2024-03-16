import nickname_manager

#list of 20 military nick names
military_nicknames = ['Rambo', 'Groundskeeper', 'Commander', 'General', 'Captain', 'Colonel', 'Major', 'Lieutenant', 
                      'Sergeant', 'Corporal', 'Soldier', 'Pilot', 'Captain', 'Commander', 'General', 'Captain', 
                      'Colonel', 'Major', 'Lieutenant', 'Sergeant', 'Corporal', 'Soldier']

manager = nickname_manager.NickManager(military_nicknames)
print(manager.assign_nick_name('John'))
print(manager.assign_nick_name('Jane'))
print(manager.assign_nick_name('Jim'))
print(manager.assign_nick_name('Jill'))
print(manager.assign_nick_name('Jack'))

print("releases")
try:
    print(manager.release_nick_name('Soldier'))

    print(manager.release_nick_name('Aaaaaa'))
except ValueError as e:
    print(e)
