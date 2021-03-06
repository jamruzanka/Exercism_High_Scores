class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def best(self):
        return max(self.scores)

    def best_three(self):
        three = []
        sorted_list = sorted(self.scores,reverse=True)
        return sorted_list[:3]

    def last_added(self):
        return self.scores[-1]

scores = [4545,4765,3980,4201,5425,4001,3819,4448,5095]
our_scores = HighScores(scores)

print(our_scores.best())
print(our_scores.best_three())
print(our_scores.last_added())
