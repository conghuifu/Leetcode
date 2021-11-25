import math
# Should use the `find_k_nearest_neighbors` function below.
def predict_label(examples, features, k, label_key="is_intrusive"):
    # Write your code here.
    pred = [examples[key]['is_intrusive'] for key in find_k_nearest_neighbors(examples, features, k)]
    res = sum(pred)
    if res >= k/2:
        return 1
    else:
        return 0

def find_k_nearest_neighbors(examples, features, k):
    # Write your code here.
    res = []
    for key in examples:
        res.append([euclidean_dis(features, examples[key]['features']), key])

    return [j for i,j in sorted(res)[:k]]
    
def euclidean_dis(x1, x2):
    summ = 0
    n = len(x1)
    for i in range(n):
        summ += (x1[i] - x2[i]) ** 2
    return math.sqrt(summ)