    
input_file = open('scores.txt')

ratings_dict = {}


def restaurant_ratings(file):
    """Restaurant rating lister."""

    for lines in input_file:
        lines = lines.rstrip().split(":")
        ratings_dict[lines[0]] = lines[1]
    return ratings_dict.items()

def add_restaurant(file):
    """Asks user for input and adds it to the dictionary"""
    restaurant = input("Please write the name of the restaurant  ")
    rating = input("Please give the restaurant a rating from 1-5  ")
    ratings_dict[restaurant.capitalize()] = rating


def print_sorted_scores(file):
    """Prints restaurants and ratings in a phrase and sorted"""

    for restaurant, rating in sorted(ratings_dict.items()):
        print(f"{restaurant} is rated at {rating}.")

print(restaurant_ratings("scores.txt"))
print(add_restaurant("scores.txt"))
print(print_sorted_scores("scores.txt"))


