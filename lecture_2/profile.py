# Function for determining age group
def generate_profile(age: int):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

# Collecting basic information
print("Welcome!")

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# A flexible user hobby list
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    else:
        hobbies.append(hobby)

# User life stage
life_stage = generate_profile(current_age)

# Dictionary for storing all collected information
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# Profile output
print(f"---")
print(f"Profile Summary: ")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if len(hobbies) == 0:
    print(f"You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")

for item in hobbies:
    print(f"- {item}")

print(f"---")
