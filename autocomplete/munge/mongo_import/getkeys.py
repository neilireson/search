from pymongo import MongoClient
MONGO_HOST = 'mongodb://136.243.103.29'
MONGO_PORT = 27017
all_keys = {}

cl = MongoClient(MONGO_HOST, MONGO_PORT)
tl = cl.annocultor_db.TermList.find({'entityType':'AgentImpl'})
for term in tl:
    rep = term['representation']
    for char in rep:
        if char in all_keys.keys():
            all_keys[char] = all_keys[char] + 1
        else:
            all_keys[char] = 0

print(all_keys)


