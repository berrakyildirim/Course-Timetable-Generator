class Course:
    def __init__(self, name, section, start_hour, end_hour, day):
        self.name = name
        self.section = section
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.day = day

# Initialize timetable and hours
def initialize_timetable():
    """Initialize an empty timetable with days and hours."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    hours = list(range(8, 18))  # Timetable from 8:00 to 17:00
    timetable = {day: [""] * len(hours) for day in days}
    return timetable, hours

# Update timetable with course addition/removal
def update_timetable(timetable, hours, course, action="add"):
    """Update the timetable by adding or removing a course."""
    if course.day not in timetable:
        print(f"Error: {course.day} is not a valid day.")
        return timetable

    start_index = course.start_hour - hours[0]
    end_index = course.end_hour - hours[0]

    if start_index < 0 or end_index > len(hours):
        print(f"Error: {course.name} timing is out of timetable bounds.")
        return timetable

    if action == "add":
        for i in range(start_index, end_index):
            if timetable[course.day][i]:  # Check for conflicts
                print(f"Conflict: {course.name} overlaps with {timetable[course.day][i]} on {course.day}.")
                return timetable
            timetable[course.day][i] = f"{course.name} (Section {course.section})"
        print(f"{course.name} has been added to the timetable.")
    elif action == "remove":
        for i in range(start_index, end_index):
            if timetable[course.day][i] == f"{course.name} (Section {course.section})":
                timetable[course.day][i] = ""
        print(f"{course.name} has been removed from the timetable.")
    else:
        print("Invalid action. Use 'add' or 'remove'.")

    return timetable

# Display timetable
def display_timetable(timetable, hours):
    """Display the timetable in a readable format."""
    hour_width = 6
    day_width = 20
    header = f"{'Hour':<{hour_width}}" + "".join([f"{day:<{day_width}}" for day in timetable.keys()])
    print(header)
    print("-" * len(header))
    for hour_index, hour in enumerate(hours):
        row = f"{hour}:00".ljust(hour_width)
        for day in timetable.keys():
            cell = timetable[day][hour_index] if timetable[day][hour_index] else "Free"
            row += cell.ljust(day_width)
        print(row)

# Check conflicts
def is_conflict(user_schedule, new_course):
    for course in user_schedule:
        if course.day == new_course.day and not (new_course.end_hour <= course.start_hour or new_course.start_hour >= course.end_hour):
            return True
    return False

# Load courses from file
def load_courses_from_file(file_name):
    courses = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    name, section, start_hour, end_hour, day = parts
                    try:
                        courses.append(Course(name, int(section), int(start_hour), int(end_hour), day))
                    except ValueError:
                        print(f"Invalid data in line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    return courses

# Print user's schedule
def print_schedule(user_schedule):
    if not user_schedule:
        print("\nYour schedule is empty.")
        return
    print(f"{'Day':<10}{'Time':<20}{'Course (Section)':<30}")
    print("-" * 60)
    sorted_schedule = sorted(user_schedule, key=lambda c: (c.day, c.start_hour))
    for course in sorted_schedule:
        time = f"{course.start_hour}:00 - {course.end_hour}:00"
        print(f"{course.day:<10}{time:<20}{course.name} (Section {course.section})")

# Main program
print("Welcome to the course scheduler!")
file_name = "courses.txt"
courses = load_courses_from_file(file_name)

if not courses:
    print("No courses available. Exiting program.")
    exit()

# Initialize timetable
timetable, hours = initialize_timetable()
user_schedule = []

while True:
    print("\nAvailable courses:")
    available_courses = [course for course in courses if not is_conflict(user_schedule, course)]
    if not available_courses:
        print("No courses available without conflicts.")
        break

    for course in available_courses:
        print(f"{course.name} (Section {course.section}) on {course.day}: {course.start_hour}:00-{course.end_hour}:00")

    input_name = input("\nEnter the name of the course you want to add (for example:EEE 445):").strip()
    try:
        section = int(input("Enter the section of the course: "))
    except ValueError:
        print("Invalid input for section. Please enter a number.")
        continue

    found = False
    for course in available_courses:
        if input_name == course.name and section == course.section:
            found = True
            user_schedule.append(course)
            timetable = update_timetable(timetable, hours, course, action="add")
            break

    if not found:
        print("Course or section not found. Please try again.")

    choice = input("\nDo you want to add another course? (y/n): ")
    if choice.lower() != 'y':
        break

print("\nFinal timetable:")
display_timetable(timetable, hours)

print("\nFinal schedule:")
print_schedule(user_schedule)
