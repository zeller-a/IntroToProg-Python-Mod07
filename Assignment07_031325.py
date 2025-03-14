# ------------------------------------------------- #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes with structured error handling
# ChangeLog: zellera, 03/10/2025, A07
# ------------------------------------------------- #
import json

# Data -------------------------------------------- #
FILE_NAME: str = 'Enrollments.json'
MENU: str = '''
---- Course Registration Program ------------------------------
  Select from the following menu:
    1. Show Current Data
    2. Register a Student for a Course
    3. Save Data to a File
    4. Exit the Program
--------------------------------------------------
'''

students: list = []  # a table of student data
menu_choice: str = ''


class Person:
    """
    A class representing person data.

    Properties:
        student_first_name (str): The student's first name.
        student_last_name (str): The student's last name.
        course_name (str): Python Course Registration

    """

    # TODO 2 Create a constructor with private attributes for the first_name and last_name data
    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    # TODO 3 Create property getter and setter for first name using the same code as in the Student class
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO 4 Create property getter and setter for last name using the same code as in the Student class
    @property
    def last_name(self):
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")


    # TODO Override the __str__() method to return Person data
    # TODO 5. Override the default __str__() method's behavior and return a coma-separated string of data


    def __str__(self):
        return f'{self.first_name},{self.last_name},{self.course_name}'

# TODO Create a Student class inheriting from the Person class (Done)
# TODO Add code to inherit code from the person class
class Student(Person):
    """
    A class representing student data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        course_name (str): Python Course Registration

    """

    # TODO 7 Comment out the code for the first_name and last_name attributes and pass the parameter data to the Person "super" class
    # TODO call to the Person constructor and pass it the first_name and last_name data (Done)
    def __init__(self, first_name: str = '', last_name: str = ''):
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(first_name=first_name, last_name=last_name)


   # def __init__(self, course_name):
        #self.course_name = course_name

    # TODO 8 Comment out the code for the first_name and last_name properties

    @property  # (Use this decorator for the getter or accessor)
    def course_name(self):
         return self.__course_name.title()  # formatting code
    #
    @course_name.setter
    def course_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__course_name = value
        else:
            raise ValueError("The course name should not contain numbers.")
    # TODO 9. Override the Parent __str__() method behavior to return a coma-separated string of data
   # def __str__(self)
    #    return f'{self.first_name}{self.last_name}, {self.course_name}'
    #"""
    #Returns a string representation of an object, combining the first_name, last_name, and course_name attributes in the format "first_name last_name - course_name".
    #:return:
    #"""


class FileProcessor:

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        students = []

        """
        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows

        :return :list []
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        #else:
         #           student_json = json.load(file)
          #          file.close()
           #         for student in student_json:
            #            student_object: Student = student(first_name=student["First Name"],
             #                                     last_name=student["Last Name"],
              #                                    course_name=student["Course Name"])

        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    zellera,3.12.2025,Created Class
    zellera,3.12.2025,Added menu output and input functions
    zellera,3.12.2025,,Added a function to display the data
    zellera,3.12.2025,,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        zellera,3.12.2025,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_student_data_and_course_names(student_data: list):
        """This function displays student and course names.
        ChangeLog: zellera, March 5 2025, Created function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["First_Name"]} '
                  f'{student["Last_Name"]} is enrolled in {student["Course_Name"]}')

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and GPA from the user

        ChangeLog: zellera, March 5 2025, Created function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        #try:
        #    student = Student()
        #    student.first_name = input("What is the student's first name? ")
        #    student.last_name = input("What is the student's last name? ")
        #    student.course_name = input("What is the course name? ")
        #    student_data.append(student)
        #    print()
        #    print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")

        #except ValueError as e:
        #    IO.output_error_messages("That value is not the correct type of data!", e)
        #except Exception as e:
        #    IO.output_error_messages("There was a non-specific error!", e)

        #return student_data
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"First_Name": student_first_name,
                            "Last_Name": student_last_name,
                            "Course_Name": course_name}
            student_data.append(student)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data



#  End of function definitions

# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        IO.output_student_data_and_course_names(students)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        students = IO.input_student_data(student_data=students)
        #print(students)
        continue

    elif menu_choice == "3":  # Save data in a file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
