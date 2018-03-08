from student import *


class HighSchoolStudent(Student):
    Highschool_name = "Nairobi School"

    def get_school_name(self):
        return 'THis is a high school student'

    def get_name_capitalize(self):
        original_name = super().get_name_capitalize()
        return original_name + '-HS'
