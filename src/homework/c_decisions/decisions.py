def get_options_ratio(option, total):
    """
    Returns the ratio of options to total.
    
    :param option: The number of options
    :param total: The total value
    :return: The ratio of option/total
    """
    if total == 0:
        return 0  # Prevent division by zero error
    return option / total

def get_faculty_rating(ratio):
    """
    Returns the faculty rating based on the given ratio.
    
    :param ratio: The ratio to determine the faculty rating
    :return: A string representing the faculty rating
    """
    if 0.9 <= ratio < 1:
        return "Excellent"
    elif 0.8 <= ratio < 0.9:
        return "Very Good"
    elif 0.7 <= ratio < 0.8:
        return "Good"
    elif 0.6 <= ratio < 0.7:
        return "Needs Improvement"
    else:
        return "Unacceptable"






