CREATE TABLE `class` (
  `classId` varchar(50) NOT NULL,
  `courseId` varchar(50) NOT NULL,
  `classSize` int DEFAULT NULL,
  `classTitle` varchar(50) DEFAULT NULL,
  `classTiming` varchar(120) DEFAULT NULL,
  `classTimeline` varchar(120) DEFAULT NULL,
  `enrolmentPeriod` varchar(120) DEFAULT NULL,
  `trainerAssigned` int DEFAULT NULL,
  PRIMARY KEY (`classId`),
  FOREIGN KEY (`courseId`) REFERENCES course(`courseId`),
  FOREIGN KEY (`trainerAssigned`) REFERENCES trainer(`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `class`
--

INSERT INTO `class` (`classId`, `courseId`, `classSize`, `classTitle`, `classTiming`, `classTimeline`, `enrolmentPeriod`, `trainerAssigned`) VALUES
('XRX-101 Class 1', 'XRX-101', '30', 'class1', '10:00 to 13:00', '2021-11-30 to 2021-12-30', '2021-10-30 to 2021-11-29', '4');

