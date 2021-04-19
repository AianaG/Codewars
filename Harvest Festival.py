def plant(seed, water, fert, temp):
    plant = water*(water*'-' + fert*'seed')
#     print(plant)
    if temp <20 or temp >30:
        return plant[:-4].replace('seed', '') + seed
    else:
        return plant.replace('seed', seed)