# ---
# 1. Finding Common Interests
# You have two groups of people with different hobbies:
# hobbies_group1 = {"reading", "sports", "music"}
# hobbies_group2 = {"music", "painting", "sports"}
# Write a Python program to find their common hobbies.
from enum import unique

hobbies_group1 = {"reading", "sports", "music"}
hobbies_group2 = {"music", "painting", "sports"}
common_hobbies = hobbies_group1.intersection(hobbies_group2)
print(common_hobbies)

# ---
# 2. Identifying Unique Participants
# Two teams participated in different events:
# event1_players = {"Alice", "Bob", "Charlie"}
# event2_players = {"Charlie", "David", "Eve"}
# Find the players who participated in only one event.

event1_players = {"Alice", "Bob", "Charlie"}
event2_players = {"Charlie", "David", "Eve"}
event1_participants = event1_players.difference(event2_players)
print(event1_participants)
event2_participants = event2_players.difference(event1_players)
print(event2_participants)

# ---
# 3. Removing Duplicate Data
# You have a list of feedback with duplicate entries:
# feedback = ["Excellent", "Good", "Excellent", "Average", "Good"]
# Write a program to remove duplicates from the feedback list.
#

feedback = ["Excellent", "Good", "Excellent", "Average", "Good"]
unique_feedback = set(feedback)
print(unique_feedback)

# ---
# 4. Verifying Subsets
# You have a team and a larger organization:
# team = {"Alice", "Bob"}
# organization = {"Alice", "Bob", "Charlie", "David"}
# Check if the team is a subset of the organization.

team = {"Alice", "Bob"}
organization = {"Alice", "Bob", "Charlie", "David"}
print(team.issubset(organization))

# ---
# 5. Finding All Participants
# Participants from two coding events are:
# python_event = {"Alice", "Bob", "Charlie"}
# java_event = {"Charlie", "David", "Eve"}
# Write a Python program to find all unique participants.

python_event = {"Alice", "Bob", "Charlie"}
java_event = {"Charlie", "David", "Eve"}
print(python_event.union(java_event))

# ---
# 6. Identifying Non-Overlapping Groups
# You have two departments in a company:
# department1 = {"Alice", "Bob"}
# department2 = {"Charlie", "David"}
# Check if the two departments have completely distinct members.

department1 = {"Alice", "Bob"}
department2 = {"Charlie", "David"}
print(department1.issubset(department2))

# ---
# 7. Highlighting Missing Items
# Registered participants and attendees at an event are:
# registered = {"Alice", "Bob", "Charlie", "David"}
# attended = {"Alice", "Charlie"}
# Find the participants who missed the event.

registered = {"Alice", "Bob", "Charlie", "David"}
attended = {"Alice", "Charlie"}
print(attended.difference(registered))

# ---
# 8. Filtering Unique IDs
# You have a list of duplicate IDs:
# ids = [101, 102, 103, 101, 104, 102]
# Write a Python program to filter out unique IDs.
ids = [101, 102, 103, 101, 104, 102]
print(set(ids))

# ---
# 9. Eliminating Irrelevant Elements
# You have all IDs and a set of valid IDs:
# all_ids = {101, 102, 103, 104, 105}
# valid_ids = {102, 103, 104}
# Find and display the in valid IDs only.

all_ids = {101, 102, 103, 104, 105}
valid_ids = {102, 103, 104}
print(all_ids.difference(valid_ids))

# ---
# 10. Real-World Data Validation
# A user selects preferences from a set:
# valid_preferences = {"reading", "sports", "music", "traveling"}
# user_preferences = {"sports", "music"}
# Write a program to check if the user's preferences are valid.

valid_preferences = {"reading", "sports", "music", "traveling"}
user_preferences = {"sports", "music"}
print(user_preferences.issubset(valid_preferences))