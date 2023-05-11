class Metrics():
   def euclidean_distance(self, X, Y):
       # Write your code here.
       return round(sum((x - y)**2 for x, y in zip(X, Y)) ** 0.5, 4)

   def manhattan_distance(self, X, Y):
       # Write your code here.
       return sum(abs(x -y) for x, y in zip(X, Y))

   def cosine_similarity(self, X, Y):
       numerator = sum(x * y for x, y in zip(X, Y))
       mod_x = sum((x**2) for x in X) ** 0.5
       mod_y = sum((y**2) for y in Y) ** 0.5
       
       return round((numerator / (mod_x * mod_y)), 4)

   def jaccard_similarity(self, X, Y):
       # Write your code here.
       return round(len(set.intersection(*[set(X), set(Y)])) / len(set.union(*[set(X), set(Y)])), 4)


def distances_and_similarities(X = [1, 3, 4, 5], Y = [7, 6, 3, 1]):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]


if __name__ == "__main__":
    print(distances_and_similarities())
    