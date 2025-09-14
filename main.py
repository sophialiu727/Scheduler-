import json
import scheduler

sample_data = [
    {"name": "Analytical Geometry and Calculus 1", "id": "MAC 2311", "session_id": "58291",
     "periods": (["M1", "W1", "F1"]), "credits": 4},
    {"name": "Analytical Geometry and Calculus 1", "id": "MAC 2311", "session_id": "93215",
     "periods": (["M4", "W4", "F4"]), "credits": 4},
    {"name": "Analytical Geometry and Calculus 1", "id": "MAC 2311", "session_id": "10437",
     "periods": (["M5", "W5", "F5"]), "credits": 4},

    {"name": "Analytical Geometry and Calculus 2", "id": "MAC 2312", "session_id": "51820",
     "periods": (["M2", "W2", "F2"]), "credits": 4},
    {"name": "Analytical Geometry and Calculus 2", "id": "MAC 2312", "session_id": "79904",
     "periods": (["M6", "W6", "F6"]), "credits": 4},
    {"name": "Analytical Geometry and Calculus 2", "id": "MAC 2312", "session_id": "34309",
     "periods": (["M8", "W8", "F8"]), "credits": 4},

    {"name": "Introduction to Computational Mathematics", "id": "MAD 2502", "session_id": "74082",
     "periods": (["M3", "W3", "F3"]), "credits": 3},
    {"name": "Introduction to Computational Mathematics", "id": "MAD 2502", "session_id": "24819",
     "periods": (["M6", "W6", "F6"]), "credits": 3},

    {"name": "Introduction to Programming", "id": "COP 3502", "session_id": "66354", "periods": (["M4", "W4", "F4"]),
     "credits": 3},
    {"name": "Introduction to Programming", "id": "COP 3502", "session_id": "66354", "periods": (["M6", "W6", "F6"]),
     "credits": 3},
    {"name": "Introduction to Programming", "id": "COP 3502", "session_id": "54702", "periods": (["M8", "W8", "F8"]),
     "credits": 3},

    {"name": "Programming Fundamentals 1 Lab", "id": "COP 3502L", "session_id": "15789", "periods": (["T7"]),
     "credits": 1},
    {"name": "Programming Fundamentals 1 Lab", "id": "COP 3502L", "session_id": "96513", "periods": (["R7"]),
     "credits": 1},

    {"name": "Programming Fundamentals 2", "id": "COP 3503", "session_id": "82346", "periods": (["M7", "W7", "F7"]),
     "credits": 3},
    {"name": "Programming Fundamentals 2", "id": "COP 3503", "session_id": "20745", "periods": (["M8", "W8", "F8"]),
     "credits": 3},

    {"name": "Introduction to Statistics 1", "id": "STA 2023", "session_id": "70415", "periods": (["T3", "R3"]),
     "credits": 3},
    {"name": "Introduction to Statistics 1", "id": "STA 2023", "session_id": "38462", "periods": (["T4", "R4"]),
     "credits": 3},

    {"name": "Introduction to Statistics 2", "id": "STA 3024", "session_id": "56941", "periods": (["M2", "W2", "F2"]),
     "credits": 3},
    {"name": "Introduction to Statistics 2", "id": "STA 3024", "session_id": "19538", "periods": (["M5", "W5", "F5"]),
     "credits": 3},

    {"name": "Statistical Learning", "id": "STA 4210", "session_id": "44628", "periods": (["T5", "R5"]), "credits": 3},
    {"name": "Statistical Learning", "id": "STA 4210", "session_id": "81204", "periods": (["M7", "W7", "F7"]),
     "credits": 3},

    {"name": "Data Science Capstone", "id": "STA 4930", "session_id": "29674", "periods": (["W7"]), "credits": 3},
    {"name": "Data Science Capstone", "id": "STA 4930", "session_id": "57263", "periods": (["F5"]), "credits": 3},

    {"name": "Data Structures and Algorithms 1", "id": "COT 3100", "session_id": "69830",
     "periods": (["M8", "W8", "F8"]), "credits": 3},
    {"name": "Data Structures and Algorithms 1", "id": "COT 3100", "session_id": "40972",
     "periods": (["M7", "W7", "F7"]), "credits": 3},

    {"name": "Linear Algebra", "id": "MAS 3114", "session_id": "13680", "periods": (["M5", "W5", "F5"]), "credits": 3},
    {"name": "Linear Algebra", "id": "MAS 3114", "session_id": "87591", "periods": (["M6", "W6", "F6"]), "credits": 3},
]

#writes json file
with open("data.json", "w") as f:
    json.dump(sample_data, f, indent=4)

def load_courses(filename: str)-> list:
    """
    Converts data in a json file to Course objects
    :param filename: file to be read and data loaded
    :return: Course objects
    """
    with open(filename, "r") as infile:
        data = json.load(infile)
        courses = [
            scheduler.Course(
                record["name"],
                record["id"],
                record["session_id"],
                record["periods"],
                record["credits"]
            )
            for record in data
        ]
    return courses

def visualize_schedule(schedule: list):
    """
    Function: the function returns a visual representation of the schedule.

    Parameters:
        schedule (list): the schedule of the wanted classes with no conflicts

    Returns:
        schedule (list): the visual representation of the schedule as a matrix
    """

    #initailizing rows and columns
    days = ['M', 'T', 'W', 'R', 'F']
    periods = 1,2,3,4,5,6,7,8

    #creating blank grid
    grid = {}
    for d in days:
        grid[d] = {}
        for p in periods:
            grid[d][p] = ""

    for course in schedule:
        for time in course.get_times():
            #retrieving day of the week
            day = time[0]
            #retrieving period of day
            period = int(time[1])
            #adding id with getter after identifying which cells have courses
            if grid[day][period] == "":
                grid[day][period] = course.get_id()

    #printing headers
    print("Period |", end =" ")
    for d in days:
        #using 10-len(d) to fill the 10 spaces up after adding the day
        print(d + " " * (9 - len(d)) + "|", end=" ")
    print()
    print("-" * 63)

    # Step 4: Print each row
    for p in periods:
        row = f"{p}      | "
        for d in days:
            #checking each cell in the grid and adding spaces if it is empty or the course plus spaces to fill up rest of cell
            entry = grid[d][p]
            if entry == "":
                entry = " " * 9
            else:
                entry = entry + " " * (9 - len(entry))
            row += entry + "| "
        print(row)
    print("_" * 63)
    num_credits = 0
    for course in schedule:
        num_credits += course.get_credits()
    print(f"Credits: {num_credits}")


def main():
    filename = "data.json"

    courses = load_courses(filename)

    # print test
    print("Here are all of the loaded courses:\n")
    for course in courses:
        print(course)
    print()

    wanted_ids = ["MAC 2311", "MAD 2502", "COP 3502", "COP 3502L", "STA 2023"]
    wanted_courses = []
    for course in courses:
        if course.get_id() in wanted_ids:
            wanted_courses.append(course)

    early_schedule = scheduler.Course.get_early_schedule(wanted_courses)
    late_schedule = scheduler.Course.get_late_schedule(wanted_courses)

    print("Here are all of the courses that we want:\n")
    for course in wanted_courses:
        print(course)
    print()

    print("Here is the early class schedule that was made:\n")
    for course in early_schedule:
        print(course)
    print()

    print("Here is a visual of your early schedule: \n")
    visualize_schedule(early_schedule)

    print()
    print("_" * 120)
    print()

    print("Here is the late schedule that was made:\n")
    for course in late_schedule:
        print(course)
    print()

    print("Here is a visual of your late class schedule: \n")
    visualize_schedule(late_schedule)



if __name__ == "__main__":
    main()
