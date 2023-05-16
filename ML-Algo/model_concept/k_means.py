import random
import operator

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()

    def updateLoc(self, user_feature_map):
        add_list = lambda x, y: map(operator.add, x, y)
        n_users = len(self.closest_users)
        new_loc = [0.0 for _ in range(len(self.location))]
        for uid in self.closest_users:
            new_loc =  add_list(new_loc, user_feature_map[uid])
        self.location = [x / n_users for x in new_loc]


def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the initial users, to be used as centroids.
    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)
    centroids = [Centroid(user_feature_map[user]) for user in  inital_centroid_users]
    for _ in range(10):
        for uid, feat in user_feature_map.items():
            dist = [(i, findDistance(feat, cent.location)) for i, cent in enumerate(centroids)]
            centroid_idx = min(dist, key=lambda x: x[-1])[0]
            centroids[centroid_idx].closest_users.add(uid)

        for centroid in centroids:
            centroid.updateLoc(user_feature_map)
            centroid.closest_users.clear()
    return [centroid.location for centroid in centroids]

def findDistance(x, y): 
     return sum(abs(x - y)for x, y in zip(x, y))