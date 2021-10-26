DROP TABLE IF EXISTS `quiz`;
CREATE TABLE `quiz` (
  `classId` varchar(50) NOT NULL,
  `sectionId` varchar(50) NOT NULL,
  `quizId` varchar(50) NOT NULL,
  `time` integer DEFAULT NULL,
  PRIMARY KEY (`classId`,`sectionId`, `quizId`),
  FOREIGN KEY (`classId`,`sectionId`) REFERENCES section(`classId`,`sectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- Dumping data for table `quiz`
--

INSERT INTO `quiz` (`classId`, `sectionId`,`quizId`, `time`) VALUES
('XRX-101 Class 1', 'Section 1', 'Quiz 1', 10), 
('XRX-101 Class 1', 'Section 2', 'Quiz 2', 15)