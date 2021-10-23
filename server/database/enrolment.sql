DROP TABLE IF EXISTS `enrolment`;
CREATE TABLE `enrolment` (
  `classId` varchar(50) NOT NULL,
  `learnerId` int(11) NOT NULL,
  `sectionsCompleted` int(11) DEFAULT NULL,
  `totalNumSections` int(11) DEFAULT NULL,
  `completedClass` boolean NOT NULL,
  PRIMARY KEY (`classId`,`learnerId`),
  FOREIGN KEY (`classId`) REFERENCES class(`classId`),
  FOREIGN KEY (`learnerId`) REFERENCES learner(`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dumping data for table `enrolment`
--

INSERT INTO `enrolment` (`classId`, `learnerId`,`sectionsCompleted`, `totalNumSections`, `completedClass`) VALUES
('XRX-101 Class 1', 1, 0, 10, False), 
('XRX-101 Class 1', 2, 10, 10, True);