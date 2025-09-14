class Course:
    def __init__(self, name, id, session_id, times, credits):
        self.name = name
        self.id = id
        self.session_id = session_id
        self.times = times
        self.credits = credits

    #getters and setters
    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_times(self):
        return self.times

    def get_credits(self):
        return self.credits

    def get_session_id(self):
        return self.session_id

    def set_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def set_times(self, times):
        self.times = times

    def set_credits(self, credits):
        self.credits = credits

    def set_session_id(self, session_id):
        self.session_id = session_id

    def __str__(self):
        return f"Course Name: {self.name}, Class ID: {self.id}, Session ID: {self.session_id}, Credits: {self.credits}, Times: {self.times}"


    def check_overlap(self, courses: list)-> bool:
        """
            Function: checks for overlap between classes chosen

            Parameters: courses(list)
                other class that's being compared

            Returns:
                boolean of whether there is overlap or not
        """
        # if overlap returns true, otherwise returns false
        ret = False
        for time in self.get_times():
            for course in courses: #for every course already in schedule
                if time in course.get_times() or self.get_id() == course.get_id(): #if the time of the course is ine the times of the already scheduled course
                    ret = True #ret becomes True, meaning there is overlap
        return ret


    @classmethod
    def get_total_credits(cls, schedule: list)-> int:
        """
        Function: the function returns the total credits of your schedule.
        Parameter: schedule(list) contains all the courses used to count the credits
        Return: int
        """
        credits = 0
        for course in schedule:
            credits += course.get_credits()
        return credits

    @classmethod
    def get_early_schedule(cls, courses: list)-> list:
        """
        Function: the function returns a schedule of the entered classes, prioritizing classes listed first and keeping in mind the preferences of early classes.

        Parameters:
            courses (list): the list of classes to schedule.

        Returns:
            schedule (list): the schedule of the entered classes.
        """

        schedule = []


        for course in courses:
            # check number of credits and if there is overlap
            if cls.get_total_credits(schedule) + course.get_credits() <= 18 and course.check_overlap(schedule) == False:
                schedule.append(course)
        return schedule

    @classmethod
    def get_late_schedule(cls, courses: list)-> list:
        """
        Function: the function returns a schedule of the entered classes, prioritizing a late class scheduler based on later class times.

        Parameters:
            courses (list): the list of classes to schedule.

        Returns:
            schedule (list): the schedule of the entered classes.
        """

        # Sort courses by their latest period in descending order
        courses.sort(key=lambda late_course: max(int(time[1]) for time in late_course.get_times()), reverse=True)

        schedule = []

        for course in courses:
            # check number of credits and if there is overlap
            if cls.get_total_credits(schedule) + course.get_credits() <= 18 and course.check_overlap(schedule) == False:
                schedule.append(course)
        return schedule
