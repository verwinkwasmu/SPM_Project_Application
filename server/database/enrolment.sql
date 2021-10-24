DROP TABLE IF EXISTS `enrolment`;
CREATE TABLE `enrolment` (
  `courseId` varchar(50) NOT NULL,
  `classId` varchar(50) NOT NULL,
  `learnerId` int(11) NOT NULL,
  `sectionsCompleted` int(11) DEFAULT NULL,
  `totalNumSections` int(11) DEFAULT NULL,
  `completedClass` boolean NOT NULL,
  PRIMARY KEY (`classId`,`learnerId`),
  FOREIGN KEY (`courseId`) REFERENCES class(`courseId`),
  FOREIGN KEY (`classId`) REFERENCES class(`classId`),
  FOREIGN KEY (`learnerId`) REFERENCES learner(`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dumping data for table `enrolment`
--

INSERT INTO `enrolment` (`courseId`, `classId`, `learnerId`,`sectionsCompleted`, `totalNumSections`, `completedClass`) VALUES
('XRX-101', 'XRX-101 Class 1', 1, 0, 10, False), 
('XRX-101','XRX-101 Class 1', 2, 10, 10, True),
('XRX-102', 'XRX-102 Class 1', 8, 4, 4, True);