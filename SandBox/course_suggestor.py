
import random
from collections import Counter

courses = ["ABE 201", "CVE 201", "MCE 201", "MCE 203", "MCE 205", "ELE 201", "ELE 203", "CSC 201", "GNS 201", "MTS 201"]


def suggest_courses(courses):
    while True:
        suggestions = [random.choice(courses) for _ in range(5)]
        course_counts = Counter(suggestions)
        most_common_courses = course_counts.most_common(2)
        if len(most_common_courses) == 2:
            return [course[0] for course in most_common_courses]
        else:
            continue


suggested_courses = suggest_courses(courses)
print("Suggested courses for the day:", suggested_courses)
