class Course:
    def __init__(self, course_id, course_name, credit_hours, base_rate=150.0):
        self.course_id = course_id
        self.course_name = course_name
        self.base_rate = base_rate
        self.__credit_hours = 0 
        self.set_credit_hours(credit_hours)

    def get_credit_hours(self):
        return self.__credit_hours

    def set_credit_hours(self, hours):
        if isinstance(hours, int) and 1 <= hours <= 6:
            self.__credit_hours = hours
        else:
            raise ValueError("Credit hours must be an integer between 1 and 6.")

    def calculate_tuition(self):
        raise NotImplementedError("Subclasses must implement calculate_tuition()")

    def __str__(self):
        return f"[{self.course_id}] {self.course_name} ({self.__credit_hours} Credits)"


class PracticalLab(Course):
    def __init__(self, course_id, course_name, credit_hours, equipment_fee, base_rate=150.0):
        super().__init__(course_id, course_name, credit_hours, base_rate)
        self.equipment_fee = equipment_fee

    def calculate_tuition(self):
        return (self.get_credit_hours() * self.base_rate) + self.equipment_fee
        
    def __str__(self):
        return super().__str__() + f" | Lab Fee: ${self.equipment_fee}"


class TheoreticalLecture(Course):
    def __init__(self, course_id, course_name, credit_hours, hall_capacity, base_rate=150.0):
        super().__init__(course_id, course_name, credit_hours, base_rate)
        self.hall_capacity = hall_capacity

    def calculate_tuition(self):
        return self.get_credit_hours() * self.base_rate
        
    def __str__(self):
        return super().__str__() + f" | Hall Capacity: {self.hall_capacity} seats"


class StudentSchedule:
    def __init__(self, student_name):
        self.student_name = student_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"\nSuccessfully added: {course.course_name}")

    def calculate_total_tuition(self):
        total = 0
        for course in self.courses:
            total += course.calculate_tuition()
        return total

    def display_schedule(self):
        print(f"\n--- Schedule for {self.student_name} ---")
        if not self.courses:
            print("No courses added yet.")
            return
            
        for course in self.courses:
            print(course)
            print(f"Tuition: ${course.calculate_tuition():.2f}")
        
        print("-" * 30)
        print(f"TOTAL TUITION DUE: ${self.calculate_total_tuition():.2f}")


def main():
    print("Welcome to the Interactive University Registration System")
    student_name = input("Enter student name: ")
    schedule = StudentSchedule(student_name)

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a Practical Lab")
        print("2. Add a Theoretical Lecture")
        print("3. View Schedule & Total Tuition")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            c_id = input("Enter Course ID: ")
            c_name = input("Enter Course Name: ")
            try:
                credits = int(input("Enter Credit Hours (1-6): "))
                fee = float(input("Enter Equipment Fee ($): "))
                lab = PracticalLab(c_id, c_name, credits, fee)
                schedule.add_course(lab)
            except ValueError as e:
                print(f"Error: Invalid input. {e}")

        elif choice == '2':
            c_id = input("Enter Course ID: ")
            c_name = input("Enter Course Name: ")
            try:
                credits = int(input("Enter Credit Hours (1-6): "))
                capacity = int(input("Enter Hall Capacity: "))
                lecture = TheoreticalLecture(c_id, c_name, credits, capacity)
                schedule.add_course(lecture)
            except ValueError as e:
                print(f"Error: Invalid input. {e}")

        elif choice == '3':
            schedule.display_schedule()

        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()