
class Course:
    def __init__(self, courseId, courseName, courseDescription, prerequisites):
        self.courseId = courseId
        self.courseName = courseName
        self.courseDescription = courseDescription
        self.prerequisites = prerequisites

    def get_courseId(self):
        return self.courseId
    
    def get_courseName(self):
        return self.courseName

    def get_courseDescription(self):
        return self.courseDescription

    def get_prerequisites(self):
        return self.prerequisites
