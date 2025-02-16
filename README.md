# README

## Course Scheduler Application

This application allows users to schedule and manage their courses effectively. It checks for conflicts, updates a timetable, and displays a user-friendly schedule. The application uses a `courses.txt` file to load the course data.

---

## Features
- Load course details from a `courses.txt` file.
- Automatically detect conflicts between selected courses.
- Add courses from your schedule.
- View a detailed timetable and a summarized schedule.

---

## Requirements
To run this program, you need the following:
- **Python 3.8 or higher**
- A text file named `courses.txt` containing course data formatted as:
  ```
  CourseName,Section,StartHour,EndHour,Day
  ```
  Example:
  ```
  CNG 111,1,8,9,Monday
  MAT 219,4,8,9,Monday
  ```

---

## Installation and Setup

1. Place the `courses.txt` file in the same directory as the script.

---

## Usage

1. Follow the prompts:
   - View available courses.
   - Enter the course name and section to add courses to your schedule.
   - Display the final timetable and schedule.

2. Exit the program by choosing not to add more courses.

---

## Output
### Example Timetable:
```
Hour  Monday               Tuesday              Wednesday            Thursday             Friday
8:00  CNG 111 (Section 1)  CNG 315 (Section 1)  Free                 Free                 Free
9:00  MAT 219 (Section 4)  Free                 MAT 219 (Section 5)  Free                 Free
...
```

### Example Schedule:
```
Day       Time                Course (Section)
Monday    8:00 - 9:00         CNG 111 (Section 1)
Monday    9:00 - 10:00        MAT 219 (Section 4)
...
```

---
