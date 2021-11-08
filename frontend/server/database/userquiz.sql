DROP TABLE IF EXISTS `userquiz`;
CREATE TABLE `userquiz` (
  `classId` varchar(50) NOT NULL,
  `sectionId` varchar(50) NOT NULL,
  `quizId` varchar(50) NOT NULL,
  `learnerId` varchar(500) NOT NULL,
  `option` varchar(500) DEFAULT NULL,
  `grade` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`classId`,`sectionId`, `quizId`, `learnerId`),
  FOREIGN KEY (`classId`,`sectionId`, `quizId`) REFERENCES quiz(`classId`,`sectionId`, `quizId`),
  FOREIGN KEY (`learnerId`) REFERENCES learner(`learnerId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `question`
--

INSERT INTO `question` (`classId`, `sectionId`,`quizId`, `learnerId`, `option`, `grade`) VALUES
("XRX-101 Class 1", "Section 1", "Quiz 1", 1, "True;Recruit solid teammates such as Visa interns;Proton;whee", NULL)