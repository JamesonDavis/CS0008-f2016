hotdog_pack = 10
hotdog_bun_pack = 8

people_attending = int(input('Enter the number of people attending the cookout: '))
hotdogs_per_person = int(input('Enter the number of hot dogs for each person: '))

hotdogs_needed = people_attending * hotdogs_per_person

hotdog_packs_needed, hotdogs_leftover = divmod(hotdogs_needed, hotdog_pack)
hotdog_bun_packs_needed, hotdog_buns_leftover = divmod(hotdogs_needed, hotdog_bun_pack)

if hotdogs_leftover:
    hotdog_packs_needed += 1
    hotdogs_leftover = hotdog_pack - hotdogs_leftover

if hotdog_buns_leftover:
    hotdog_bun_packs_needed += 1
    hotdog_buns_leftover = hotdog_bun_pack - hotdog_buns_leftover

print('Minimum packages of hot dogs needed: ', hotdog_packs_needed)
print('Minimum packages of hot dog buns needed: ', hotdog_bun_packs_needed)
print('Hot dogs left over: ', hotdogs_leftover)
print('Hot dog buns left over: ', hotdog_buns_leftover)