DROP TABLE IF EXISTS `question`;
CREATE TABLE `question` (
  classId varchar(50) NOT NULL,
  sectionId varchar(50) NOT NULL,
  `quizId` varchar(50) NOT NULL,
  `questionId` varchar(50) NOT NULL,
  `question` varchar(500) DEFAULT NULL,
  `option` varchar(500) DEFAULT NULL,
  `answer` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`classId`,`sectionId`, `quizId`, `questionId`),
  FOREIGN KEY (`classId`,`sectionId`, `quizId`) REFERENCES quiz(`classId`,`sectionId`, `quizId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `question`
--

INSERT INTO `question` (`classId`, `sectionId`,`quizId`, `questionId`, `question`, `option`, `answer`) VALUES
("XRX-101 Class 1", "Section 1", "Quiz 1", "Question 1", "What is your mother's name?", "Mary;Laobu;Karen;Ni Mama", "Ni Mama")