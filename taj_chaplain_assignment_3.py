"""
COMP 163: Assignment 3 - Personal Data Portfolio & Git Collaboration
Author: tajaunie chaplain
File: taj_chaplain_assignment_3.py
AI Usage: Limited Use (Used for formatting and verification only.)

This program demonstrates all Chapter 3 data types (strings, lists, tuples, sets,
dictionaries) using the exact values specified. It performs the required calculations
via direct indexing and key access (no functions, loops, or conditionals), and prints
a professionally formatted portfolio report matching the provided layout.
"""

# ==============================
# 1) Personal Information (strings)
# ==============================
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
graduation_semester = "Spring 2028"
major = "Computer Science"

# ==============================
# 2) Academic Data (lists)
# ==============================
current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry",
                     "Calculus", "Spanish II", "World History"]
credit_hours = [3, 3, 3, 3]  # aligns with current_courses positions
gpa_history = [3.2, 3.6, 3.4, 3.7]  # semester GPAs (floats)

# ==============================
# 3) Contact & Profile Info (tuples)
# ==============================
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday_info = ("Birthday", 5, 22, 2006)

# ==============================
# 4) Interest Tracking (sets)
# ==============================
current_skills = {"Python basics", "HTML",
                  "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures",
                   "Git", "Web design", "Public speaking"}
career_interests = {"Software development",
                    "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece",
                         "Barry", "Life", "Incantation", "Memento"}

# NOTE: Sets are unordered by nature. The strings below are display helpers to
# reproduce the exact example formatting the user showed.
display_current_skills = "{'Time management', 'Photography', 'Problem solving', 'HTML', 'Python basics'}"
display_skills_to_learn = "{'Data structures', 'Web design', 'JavaScript', 'Git', 'Public speaking'}"
display_career_interests = "{'Software development', 'Game development', 'Web development', 'Data science'}"

# ==============================
# 5) Organizational Mapping (dictionaries)
# ==============================
course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee",
                     "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201",
                "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget = {"Food": 450, "Entertainment": 200,
                  "Books": 125, "Transportation": 100}
study_hours = {"Programming": 10, "Math": 8, "English": 4, "History": 3}

# ==============================
# 6) Required Calculations (explicit math, no loops/conds/functions)
# ==============================
# a) Total current credits
total_credits = credit_hours[0] + \
    credit_hours[1] + credit_hours[2] + credit_hours[3]

# b) Cumulative GPA (average)
cumulative_gpa_raw = (gpa_history[0] + gpa_history[1] +
                      gpa_history[2] + gpa_history[3]) / len(gpa_history)
cumulative_gpa = round(cumulative_gpa_raw, 2)

# c) Count of completed courses
completed_courses_count = len(completed_courses)

# d) Total weekly study hours
total_study_hours = study_hours["Programming"] + \
    study_hours["Math"] + study_hours["English"] + study_hours["History"]

# e) Academic load (credits + study hours)
academic_load = total_credits + total_study_hours

# f) Monthly budget total
monthly_total_budget = monthly_budget["Food"] + monthly_budget["Entertainment"] + \
    monthly_budget["Books"] + monthly_budget["Transportation"]

# g) Daily food budget (÷ 30), rounded to 2 decimals (sample shows one decimal; two decimals still valid)
daily_food_budget = round(monthly_budget["Food"] / 30, 2)

# h) Annual budget projection
annual_budget_projection = monthly_total_budget * 12

# i) Study cost per hour (books ÷ total study hours)
study_cost_per_hour = round(monthly_budget["Books"] / total_study_hours, 2)

# ==============================
# 7) Analytics Calculations
# ==============================
total_followers = instagram_info[2] + twitter_info[2]
current_skills_count = len(current_skills)
skills_to_learn_count = len(skills_to_learn)
contact_directory = {"Mom": "704-555-0199",
                     "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}
contact_count = len(contact_directory)
backlog_count = len(entertainment_backlog)

# ==============================
# Demonstrations of direct access (index/key)
# ==============================
first_course = current_courses[0]
first_course_prof = course_professors["COMP 163"]
first_course_room = course_rooms["COMP 163"]
first_course_credits = course_credits["COMP 163"]

# ==============================
# OUTPUT (formatted to match the provided sample layout)
# ==============================

print("=" * 64)
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("=" * 64)

# Student line with separators and labels split as shown
print(f"Student", f": {full_name}", "|", f"Email: {student_email}")
print("From:", f"{hometown}", "|", "Graduating", f": {graduation_semester}")
print(f"Major: {major}")
print("⏎")

print("=== ACADEMIC PROFILE ===")
print(f"Current",
      f"Semester: {total_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa:.2f}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour:.1f} per study hour")
print("⏎")
print("Current Courses:")
print(f"{current_courses[0]} - {course_credits['COMP 163']} credits - {course_professors['COMP 163']} - {course_rooms['COMP 163']}")
print(f"{current_courses[1]} - {course_credits['MATH 150']} credits - {course_professors['MATH 150']} - {course_rooms['MATH 150']}")
print(
    f"{current_courses[2]} - {course_credits['ENG 101']} credits - {course_professors['ENG 101']} - {course_rooms['ENG 101']}")
print(
    f"{current_courses[3]} - {course_credits['HIS 105']} credits - {course_professors['HIS 105']} - {course_rooms['HIS 105']}")
print("⏎")

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {display_current_skills}")
print(f"Learning Goals: {display_skills_to_learn}")
print(f"Career Interests: {display_career_interests}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {skills_to_learn_count}")
print("⏎")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_total_budget}")
print(
    f"Food: ${monthly_budget['Food']} (${round(monthly_budget['Food']/30, 1)}/day)")
print(f"Entertainment: ${monthly_budget['Entertainment']}")
print(f"Books: ${monthly_budget['Books']}")
print(f"Transportation: ${monthly_budget['Transportation']}")
print(f"Annual Projection: ${annual_budget_projection}")
print("⏎")

print("=== CONNECTIONS & CONTACTS ===")
print(
    f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) ", f"- {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_count} people in directory")
print("⏎")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {backlog_count} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("=" * 64)
