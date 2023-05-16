
def predict_label(examples, features, k, label_key="is_intrusive"):
    

    k_nearest_neighbors = find_k_nearest_neighbors(examples, features, k)
    KNN_labels = [examples[pid][label_key] for pid in k_nearest_neighbors]
    return round(sum(KNN_labels) / k)


def find_k_nearest_neighbors(examples, features, k):
    distance_dict = {}
    KNN = []
      
    for key, value in examples.items():
       distance = 0 
       
       for feature, input_feature in zip(list(value.values())[0], features):
            distance += (feature - input_feature)**2 
            
            distance_dict[key] = [distance**0.5, list(value.values())[1]]
         
       sorted_distance_dict = sorted(distance_dict.items(), key=lambda x: x[1][0])  


    for i in range(k):
        KNN.append(sorted_distance_dict[i][0])
    print(KNN)
    return KNN   