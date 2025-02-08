#import decisions

from homework.c_decisions import decisions


def main():
    # Prompt user for input
    options = float(input("Enter the number of options: "))
    total = float(input("Enter the total: "))
    
    # Calculate ratio
    result = decisions.get_options_ratio(options, total)
    
    # Get and display faculty rating
    rating = decisions.get_faculty_rating(result)
    print(f"The faculty rating is: {rating}")

if __name__ == "__main__":
    main()