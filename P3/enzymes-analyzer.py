"""
Enzyme Activity Analyzer

In this program, enzyme activity values (units/mL) from a laboratory experiment
are analyzed and classified as low, normal, or high.

Normal range: 40–70 units/mL (inclusive)

Students are expected to complete the logic inside the functions
by following the comments provided.
"""


def classify_activity(activity_value):
    """
    Classifies a single enzyme activity value.

    Parameters:
        activity_value (int or float): Enzyme activity in units/mL

    Returns:
        str: 'low', 'normal', or 'high'
    """

    # Enzyme activity below 40 units/mL is considered low
    # Enzyme activity between 40 and 70 units/mL (inclusive) is normal
    # Enzyme activity above 70 units/mL is high

    # Write conditional logic here to return the correct classification
    pass

def analyze_activities(activity_list):
    """
    Analyzes a list of enzyme activity values.

    Parameters:
        activity_list (list): List of enzyme activity values

    Returns:
        dict: A dictionary containing analysis results with the following keys:
              - 'low_count'
              - 'normal_count'
              - 'high_count'
              - 'average_activity'
              - 'min_activity'
              - 'max_activity'
              - 'normal_values'
    """

    # Initialize counters and accumulators
    total_activity = 0
    low_count = 0
    normal_count = 0
    high_count = 0
    normal_values = []

    # Loop through each activity value in the list
    # - Add the value to total_activity
    # - Classify the value using classify_activity()
    # - Update the appropriate counter
    # - Store normal activity values in normal_values


    # Calculate the average enzyme activity
    # (Total activity divided by number of samples)
    average_activity = None
    

    # Determine the minimum and maximum activity values
    # Use built-in Python functions for lists
    min_activity = None
    max_activity = None
    

    # Store all results in a dictionary and return it
    return {
        "low_count": low_count,
        "normal_count": normal_count,
        "high_count": high_count,
        "average_activity": average_activity,
        "min_activity": min_activity,
        "max_activity": max_activity,
        "normal_values": normal_values
    }


def print_summary(results, total_samples):
    """
    Prints a formatted summary of the enzyme activity analysis.

    Parameters:
        results (dict): Dictionary returned by analyze_activities()
        total_samples (int): Total number of enzyme activity measurements
    """

    print("Enzyme Activity Analysis Summary")
    print("--------------------------------")
    print(f"Total samples: {total_samples}")
    print(f"Low activity samples: {results['low_count']}")
    print(f"Normal activity samples: {results['normal_count']}")
    print(f"High activity samples: {results['high_count']}")
    print(f"Average activity: {results['average_activity']} units/mL")
    print(f"Highest activity: {results['max_activity']} units/mL")
    print(f"Lowest activity: {results['min_activity']} units/mL")
    print(f"Normal activity values: {results['normal_values']}")


def main():
    """
    Main function to run the enzyme activity analysis.
    """

    enzyme_activity_data = [35, 42, 68, 75, 55, 29, 80, 61, 47]

    results = analyze_activities(enzyme_activity_data)

    print_summary(results, len(enzyme_activity_data))


# This ensures the program runs only when executed directly
if __name__ == "__main__":
    main()