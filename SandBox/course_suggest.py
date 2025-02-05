
#import random

#courses = ["ABE 201", "CVE 201", "MCE 201", "MCE 203", "MCE 205", "ELE 201", "ELE 203", "CSC 201", "GNS 201", "MTS 201"]

#suggestion_1 = random.choice(courses)
#suggestion_2 = random.choice(courses)
#suggestion_3 = random.choice(courses)
#suggestion_4 = random.choice(courses)
#suggestion_5 = random.choice(courses)

#items = [suggestion_1, suggestion_2, suggestion_3, suggestion_4, suggestion_5]


#print(items)

import random
from collections import Counter

courses = ["ABE 201", "CVE 201", "MCE 201", "MCE 203", "MCE 205", "ELE 201", "ELE 203", "CSC 201", "GNS 201", "MTS 201"]

def suggest_courses(courses):
    while True:
        suggestions = [random.choice(courses) for _ in range(5)]
        course_counts = Counter(suggestions)
        most_common_courses = course_counts.most_common(2)  # Get the two most common courses
        if len(most_common_courses) == 2:  # Ensure there are at least two different courses suggested
            return [course[0] for course in most_common_courses]  # Return the two most common courses
        else:
            continue

# Get suggested courses for the day
suggested_courses = suggest_courses(courses)
print("Suggested courses for the day:", suggested_courses)