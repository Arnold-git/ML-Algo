def probability_of_disease(accuracy, prevalence):
    prob_sick = prevalence
    prob_healthy = 1 - prevalence 
    prob_test_inaccuracy = 1 - accuracy

    prob_positive = (prob_sick * accuracy) + (prob_healthy * prob_test_inaccuracy)
    prob_negative = (prob_sick * prob_test_inaccuracy) + (prob_healthy * accuracy)

    prob_sick_given_positive = (prob_sick * accuracy) / prob_positive
    prob_healthy_given_negative = (prob_healthy * accuracy) / prob_negative

    return [prob_sick_given_positive * 100, prob_healthy_given_negative * 100]


if __name__ == "__main__":
    print(probability_of_disease(.95, .03))