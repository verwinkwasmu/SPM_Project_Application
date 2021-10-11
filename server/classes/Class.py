
class Class:
    def __init__(self, classId, className, assignedTrainer, classDuration, enrollmentPeriod, courseId, classSize, classTimeline):
        self.classId = classId
        self.className = className
        self.assignedTrainer = assignedTrainer
        self.classDuration = classDuration
        self.enrollmentPeriod = enrollmentPeriod
        self.courseId = courseId
        self.classSize = classSize
        self.classTimeline = classTimeline

    def get_classId(self):
        return self.classId
    
    def get_className(self):
        return self.className

    def get_assignedTrainer(self):
        return self.assignedTrainer

    def get_classDuration(self):
        return self.classDuration

    def get_courseId(self):
        return self.courseId
    
    def get_classSize(self):
        return self.classSize
    
    def get_classTimeline(self):
        return self.classTimeline
    
    def get_enrollmentPeriod(self):
        return self.enrollmentPeriod
