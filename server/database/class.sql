CREATE TABLE `class` (
  `classId` varchar(50) NOT NULL,
  `courseId` varchar(50) NOT NULL,
  `classSize` int DEFAULT NULL,
  `classTitle` varchar(50) DEFAULT NULL,
  `startTime` varchar(50) DEFAULT NULL,
  `endTime` varchar(50) DEFAULT NULL,
  `startDate` varchar(50) DEFAULT NULL,
  `endDate` varchar(50) DEFAULT NULL,
  `enrolmentPeriod` varchar(120) DEFAULT NULL,
  `trainerAssigned` int DEFAULT NULL,
  `trainerName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`classId`),
  KEY `courseId` (`courseId`),
  KEY `trainerAssigned` (`trainerAssigned`),
  CONSTRAINT `class_ibfk_1` FOREIGN KEY (`courseId`) REFERENCES `course` (`courseId`),
  CONSTRAINT `class_ibfk_2` FOREIGN KEY (`trainerAssigned`) REFERENCES `trainer` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8

--
-- Dumping data for table `class`
--

INSERT INTO `spm_db`.`class`(`classId`,`courseId`,`classSize`,`classTitle`,`startTime`,`endTime`,`startDate`,`endDate`,`enrolmentPeriod`,`trainerAssigned`,`trainerName`) VALUES 
('XRX-101 Class 1', 'XRX-101', 30, 'class1', '10:00', '13:00', '2021-11-30', '2021-12-30', '2021-10-30 to 2021-11-29', 13, 'VerwinKwa'),
('XRX-101 Class 2', 'XRX-101', 50, 'class2', '10:00', '12:00', '2021-10-01', '2021-11-30', '2021-09-26 to 2021-09-29', 5, 'jhris Coskitt'),
('XRX-101 Class 3', 'XRX-101', 64, 'class3', '11:00', '11:00', '2021-10-01', '2021-10-30', '2021-09-02 to 2021-09-29'),
('XRX-101 Class 4', 'XRX-101', 21, 'class4', '15:00', '18:00', '2021-12-05', '2021-12-30', '2021-10-30 to 2021-11-29'),
('XRX-101 Class 1', 'XRX-102', 35, 'class1', '12:00', '17:00', '2021-08-30', '2021-12-30', '2021-07-30 to 2021-08-29');


1	XRX-101/Class 1/Section 1/hello.png	1
1	XRX-101/Class2/Section1/Consent_1.pdf	1
1	XRX-101/Class2/Section1/genx.png	1
1	XRX-101/Class2/Section1/genz.png	1
1	XRX-101/Class2/Section1/mili.png	1
1	XRX-101/Class2/Section1/Project_Instructions.pdf	1
1	XRX-101/Class2/Section1/TechSeries-Demo.mp4	1


INSERT INTO `spm_db`.`file` (`learnerId`, `fileId`, `completed`) VALUES
('1', 'XRX-101/Class2/Section1/Consent_1.pdf', 1),
('1', 'XRX-101/Class2/Section1/genx.png', 1),
('1', 'XRX-101/Class2/Section1/genz.png', 1),
('1', 'XRX-101/Class2/Section1/mili.png', 1),
('1', 'XRX-101/Class2/Section1/Project_Instructions.pdf', 1),
('1', 'XRX-101/Class2/Section1/TechSeries-Demo.mp4', 1);