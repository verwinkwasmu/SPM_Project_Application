DROP TABLE IF EXISTS `file`;
CREATE TABLE `file` (
  `learnerId` int(11) NOT NULL,
  `fileId` varchar(100) NOT NULL,
  `completed` boolean NOT NULL,
  PRIMARY KEY (`learnerId`, `fileId`),
  FOREIGN KEY (`learnerId`) REFERENCES learner(`userId`),
  FOREIGN KEY (`sectionId`) REFERENCES section(`sectionId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table `file`
--

INSERT INTO `file` (`learnerId`, `fileId`, `completed`) VALUES
(1, "XRX-101/Class 1/Section 1/hello.png", True)