

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `spm_db`
--
CREATE DATABASE IF NOT EXISTS `spm_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `spm_db`;


-- --------------------------------------------------------

--
-- Table structure for table `course`
--

-- DROP TABLE IF EXISTS `course`;
-- CREATE TABLE IF NOT EXISTS `course` (
--   `courseId` varchar(40) NOT NULL,
--   `courseName` varchar(40) NOT NULL,
--   `courseDescription` varchar(120) NOT NULL,
--   `prerequisites` varchar(120) NOT NULL,
-- ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `course`
--

-- INSERT INTO `course` (`courseId`, `courseName`, `courseDescription`, `prerequisites`) VALUES
-- ("XRX-101", "Fundamentals of Xerox I", "First introductory course to Xerox", Null), 
-- ("XRX-102", "Fundamentals of Xerox II", "Second introductory course to Xerox", "XRX-101 Fundamentals of Xerox I"), 
-- ("XRX-103", "Advance Course on Xerox", "An advance course to Xerox", "XRX-102 Fundamentals of Xerox II");

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL,
  `userName` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `userType` varchar(40) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `userName`, `email`, `password`, `userType`) VALUES
('1', "Timmy", "timmy@gmail.com", "dummy", "Trainer"), 
('2', "Timmyy", "timyy@gmail.com", "dummy", "Learner"), 
('3', "Timmyyy", "timmy@gmail.com", "dummy", "Learner"); 

--
-- Indexes for dumped tables
--
CREATE TABLE `trainer` (
  `id` int(11) NOT NULL,
  `userName` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `learner` (
  `id` int(11) NOT NULL,
  `userName` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `hr` (
  `id` int(11) NOT NULL,
  `userName` varchar(40) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Indexes for table course`
--
-- ALTER TABLE `course`
--   ADD PRIMARY KEY (`courseId`);

ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `learner`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `trainer`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `hr`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `trainer`
  ADD CONSTRAINT `trainer_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`);
  ADD CONSTRAINT `trainer_ibfk_2` FOREIGN KEY (`userName`) REFERENCES `user` (`userName`);
  ADD CONSTRAINT `trainer_ibfk_3` FOREIGN KEY (`email`) REFERENCES `user` (`email`);


ALTER TABLE `learner`
  ADD CONSTRAINT `learner_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`);
  ADD CONSTRAINT `learner_ibfk_2` FOREIGN KEY (`userName`) REFERENCES `user` (`userName`);
  ADD CONSTRAINT `learner_ibfk_3` FOREIGN KEY (`email`) REFERENCES `user` (`email`);

ALTER TABLE `hr`
  ADD CONSTRAINT `hr_ibfk_1` FOREIGN KEY (`id`) REFERENCES `user` (`id`);
  ADD CONSTRAINT `hr_ibfk_2` FOREIGN KEY (`userName`) REFERENCES `user` (`userName`);
  ADD CONSTRAINT `hr_ibfk_3` FOREIGN KEY (`email`) REFERENCES `user` (`email`);