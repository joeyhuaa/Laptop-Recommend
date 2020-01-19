import Laptop_Rec_UI as lru

storage_dict = {1: (64,256), 2: (256, 512), 3: (512,10000)}
screen_dict = {1: (11.6,13.5), 2: (13.6,15.4), 3: (15.5, 17.3), 4: (17.3, 100)}
ram_dict = {1: 4, 2: 8, 3: 16, 4: 32}

class User:
    def __init__(self, budget, screen_size, storage_cap, ram):
        self.budget = budget
        self.screen_range = screen_dict[screen_size]
        self.storage_range = storage_dict[storage_cap]
        self.ram = ram_dict[ram]

    def __str__(self):
        return 'budget: ' + str(self.budget) + '\n' + \
               'screen range: ' + str(self.screen_range) + '\n' + \
               'storage range: ' + str(self.storage_range) + '\n' + \
               'ram: ' + str(self.ram)

user = User(lru.b, lru.ss, lru.sc, lru.r)


# study_df[study_df.price <= user.budget & study_df.screen ]