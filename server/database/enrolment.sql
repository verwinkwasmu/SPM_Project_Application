CREATE TABLE `enrolment` (
  `classId` varchar(50) NOT NULL,
  `learnerId` int(11) NOT NULL,
  PRIMARY KEY (`classId`,`learnerId`),
  FOREIGN KEY (`classId`) REFERENCES class(`classId`),
  FOREIGN KEY (`learnerId`) REFERENCES learner(`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dumping data for table `enrolment`
--

INSERT INTO `enrolment` (`classId`, `learnerId`) VALUES
('XRX-101 Class 1', '12');