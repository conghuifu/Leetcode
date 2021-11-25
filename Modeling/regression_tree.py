import sys

class TreeNode(object):
    def __init__(self, examples):
        self.examples = examples
        self.left = None
        self.right = None
        self.best_split = None
        self.size = len(self.examples)
        self.features = self.examples[0].keys() if self.size > 0 else []
        

    def split(self):
        if self.size <= 1:
            return

        best_split = {
            'mse': sys.maxsize,
            'feature': None,
            'split_value': None,
            'split_index': None
        }
        
        for feature in self.features:
            if feature == 'bpd':
                continue

            self.examples.sort(key = lambda x: x[feature])
            for i in range(self.size - 1):
                split_value = (self.examples[i][feature] + self.examples[i+1][feature]) / 2
                mse, split_index = self.get_split_mse(feature, split_value)
                if mse < best_split['mse']:
                    best_split['mse'] = mse
                    best_split['feature'] = feature
                    best_split['split_value'] = split_value
                    best_split['split_index'] = split_index
        self.best_split = best_split

        self.examples.sort(key = lambda x: x[best_split['feature']])
        self.left = TreeNode(self.examples[:best_split['split_index']])
        self.right = TreeNode(self.examples[best_split['split_index']:])
        self.left.split()
        self.right.split()
    
    def get_split_mse(self, feature, split_value):
        ### it is label!!
        left_values = [example['bpd'] for example in self.examples if example[feature] <= split_value]
        right_values = [example['bpd'] for example in self.examples if example[feature] > split_value]
        l_n = len(left_values)
        r_n = len(right_values)

        if (l_n == 0) or (r_n == 0):
            return None, None

        left_mse = get_mse(left_values)
        right_mse = get_mse(right_values)

        mse = (left_mse * l_n + right_mse*r_n) / (l_n + r_n)
        return mse, l_n

def get_mse(values):
    avg = get_mean(values)
    return sum([(value - avg) ** 2 for value in values]) / len(values)

def get_mean(values):
    if len(values) == 0:
        return None
    return sum(values) / len(values)

class RegressionTree:
    def __init__(self, examples):
        # Don't change the following two lines of code.
        self.root = TreeNode(examples)
        self.train()

    def train(self):
        # Don't edit this line.
        self.root.split()

    def predict(self, example):
        cur = self.root
        while cur.left and cur.right:
            feature = cur.best_split['feature']
            if example[feature] <= cur.best_split['split_value']:
                cur = cur.left
            else:
                cur = cur.right

        values = [leaf_example['bpd'] for leaf_example in cur.examples]
        return get_mean(values)