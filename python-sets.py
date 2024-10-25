"""
1. Python Sets Adventure
Objective: The aim of this assignment is to deepen your understanding and application of Python sets.

Task 1: Flight Route Comparison Imagine you work for an airline and need to compare the flight routes of your airline with a competitor. You have two sets of flight destinations, one for each airline. Write a Python program to find out:

1. Destinations that both airlines fly to.

2. Destinations unique to your airline.

3. Whether there are any destinations that neither airline shares.

Example Code:

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
"""

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

common_routes = our_routes.intersection(competitor_routes)
print("Destinations that both airlines fly to:", common_routes)

unique_our_routes = our_routes.difference(competitor_routes)
print("Destinations unique to our airline:", unique_our_routes)

all_routes = our_routes.union(competitor_routes)
shared_routes = our_routes.intersection(competitor_routes)
unique_routes = all_routes.difference(shared_routes)

print("Destinations that neither airline shares:", unique_routes)



"""
2. Set Operations in Data Analysis
Objective: The aim of this assignment is to enhance your skills in using Python sets for data analysis tasks. You will apply various set operations to handle real-world data scenarios, focusing on their practical application and efficiency.

Task 1: Duplicate Entries Cleanup You are given a list of customer IDs, some of which are duplicated. Write a Python script to remove duplicates and display the unique customer IDs.

Example Code:

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
Expected Outcome: A set of unique customer IDs, ensuring no duplicates. For instance, `{'C001', 'C002', 'C003', 'C004'}`. 
"""

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_customer_ids = set(customer_ids)
print(unique_customer_ids)