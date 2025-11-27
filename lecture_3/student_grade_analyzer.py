# 1. Student Data (The Starting Point)
# list of dictionaries
students = []

# 2. Main Program Loop (The Menu)
# infinite loop
while True:
    print("\n--- Student Grade Analyzer ---")
    choices = [
        "Add a new student",
        "Add a grades for a student",
        "Show report (all students)",
        "Find top performer",
        "Exit"]

    for i, option in enumerate(choices, start=1):
        print(f"{i}. {option}")

    # try/except block to handle potential input errors
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print(f"Error: incorrect value. Please enter a number from 1 to 5.")
        continue

# 3. Implement the Menu Options.
    # Option 1. Add new student
    if choice == 1:
        name = input("Enter student name: ").strip()

# Check if student already exists
        exists = any(s["name"].lower() == name.lower() for s in students)
        if exists:
            print(f"Student already exists!")
            continue

        # Add student
        students.append({"name": name, "grades": []})

# Option 2. Add grades to a student
    elif choice == 2:
        name = input("Enter student name: ").strip()
        student = None

        # Search for student
        for s in students:
            if s["name"].lower() == name.lower():
                student = s
                break

        if student is None:
            print(f"Student not found.")
            continue

        print(f"Enter a grade (0–100) or type 'done' to finish.")

        while True:
            grade_input = input("Enter a grade (or 'done' to finish): ").strip()

            if grade_input.lower() == "done":
                break

            # try/except block to handle potential errors
            try:
                grade = int(grade_input)
                if 0 <= grade <= 100:
                    student["grades"].append(grade)
                else:
                    print(f"Grade must be between 0 and 100.")
            except ValueError:
                print(f"Invalid input. Please enter a number.")

    # Option 3. Show report (all students)
    elif choice == 3:
        if not students:
            print(f"No students available.")
            continue

        print("\n--- Student Report ---")

        all_averages = []

        for s in students:
            try:
                avg = sum(s["grades"]) / len(s["grades"])
                print("{}'s average grades is {:.1f}".format(s['name'], avg))
                all_averages.append(avg)
            except ZeroDivisionError:
                # if no grades
                print(f"{s['name']}'s average grades is N/A")

        # Part for summary report
        if not all_averages:
            print(f"No grades entered for any student.")
        else:
            print("\n--- Summary report ---")

            # try/except block to handle potential errors
            try:
                print(f"Max average: {max(all_averages):.1f}")
                print(f"Min average: {min(all_averages):.1f}")
                print(f"Overall average: {sum(all_averages) / len(all_averages):.1f}")
            except ZeroDivisionError:
                print(f"No valid averages. Cannot compute summary.")

    # Option 4. Find top performer
    elif choice == 4:
        if not students:
            print(f"No students available.")
            continue

        # Filter out students with no grades
        graded_students = [
            s for s in students if s["grades"]
        ]

        if not graded_students:
            print(f"No student has any grades yet.")
            continue

        def safe_average(grades):
            """Return average of grades or None if no grades."""
            if not grades:
                return None
            return sum(grades) / len(grades)

        top_student = max(graded_students, key=lambda s: safe_average(s["grades"]))

        top_avg = safe_average(top_student["grades"])

        print(
            "Top performer is {} with average grade is {:.1f}".format(
                top_student["name"],
                top_avg
            )
        )

    # Option 5. Exit
    elif choice == 5:
        print(f"Goodbye!")
        break

    else:
        print(f"Invalid choice. Please select between 1 and 5.")
