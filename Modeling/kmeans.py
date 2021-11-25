import random
import sys
import numpy as np

class Centroid:
    def __init__(self, location):
        self.location = location
        self.closest_users = set()


def get_k_means(user_feature_map, num_features_per_user, k):
    # Don't change the following two lines of code.
    random.seed(42)
    # Gets the inital users, to be used as centroids.
    inital_centroid_users = random.sample(sorted(list(user_feature_map.keys())), k)
    centers = [user_feature_map[key] for key in inital_centroid_users]

    for _ in range(10):
        dis = [[] for i in range(k)]
        # assign clusters
        for key in user_feature_map:
            dis_record = []
            for center in centers:
                dis_record.append(manhantan(user_feature_map[key], center))
            index = dis_record.index(min(dis_record))
            dis[index].append(user_feature_map[key])

        # re-calculate the new centers
        for i in range(k):
            tmp = np.asarray(dis[i])
            centers[i] = list(tmp.mean(axis=0))
    return centers


def manhantan(x1, x2):
    res = 0
    n = len(x1)
    for i in range(n):
        res += abs(x1[i] - x2[i])
    # Write your code here.
    return res
