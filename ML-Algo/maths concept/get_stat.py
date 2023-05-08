def get_statistics(input_list):

    """
   Function to calculate basic stat like mean, median, sample variance, sample standard deviation, mean confidence interval
    """
    
    sorted_list = sorted(input_list)
    input_length = len(sorted_list)

    mean = sum(sorted_list) / input_length

    middle_idx = (len(sorted_list) - 1) // 2

    median = sorted_list[middle_idx]

    if len(sorted_list) % 2 == 0:
        middle_idx_1 = sorted_list[middle_idx]
        middle_idx_2 = sorted_list[middle_idx + 1]

        median = (middle_idx_1 + middle_idx_2 ) / 2

    number_count = {x: sorted_list.count(x) for x in set(sorted_list)}
    mode = max(number_count.keys(), key=lambda unique_number: number_count[unique_number])

    sample_variance = sum([(number - mean) **2 / (input_length -1) for number in sorted_list])
    sample_standard_deviation = sample_variance ** 0.5

    mean_standard_error = sample_standard_deviation / input_length ** 0.5
    z_score_standard_error = 1.96 * mean_standard_error
    mean_confidence_interval = [round(mean - z_score_standard_error, 4), round(mean + z_score_standard_error, 4)]

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }
    
if __name__ == "__main__":
    input = [2, 1, 3, 4, 4, 5, 6, 7]
    print(get_statistics(input))