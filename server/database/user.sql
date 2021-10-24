-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Sep 27, 2021 at 08:33 AM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

-- Table structure for table `user`

CREATE TABLE `user` (
  `userId` int NOT NULL AUTO_INCREMENT,
  `employeeName` varchar(50) DEFAULT NULL,
  `userName` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `password` varchar(120) DEFAULT NULL,
  `userType` varchar(50) DEFAULT NULL,
  `Designation` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8
-- --------------------------------------------------------

INSERT INTO `user` (`userId`, `employeeName`, `email`, `password`, `userType`) VALUES
(1, 'Phris Coskitt', 'phris@gmail.com', 'dummy', 'Learner'),
(2, 'Hhris Coskitt', 'hhris@gmail.com', 'dummy', 'Learner'),
(3, 'Lhris Coskitt', 'lhris@gmail.com', 'dummy', 'Trainer'),
(4, 'uhris Coskitt', 'uhris@gmail.com', 'dummy', 'Trainer'),
(5, 'jhris Coskitt', 'jhris@gmail.com', 'dummy', 'Trainer'),
(6, 'khris Coskitt', 'khris@gmail.com', 'dummy', 'HR'),
(7, 'ohris Coskitt', 'ohris@gmail.com', 'dummy', 'HR');

--
-- Table structure for table `learner`
--

CREATE TABLE `learner` (
  `userId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `doctor`
--

INSERT INTO `learner` (`userId`) VALUES
(1),
(2);


CREATE TABLE `trainer` (
  `userId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `trainer` (`userId`) VALUES
(3),
(4),
(5);

CREATE TABLE `hr` (
  `userId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `hr` (`userId`) VALUES
(6),
(7);




--
-- Indexes for table `doctor`
--
ALTER TABLE `learner`
  ADD PRIMARY KEY (`userId`);

--
-- Indexes for table `patient`
--
ALTER TABLE `trainer`
  ADD PRIMARY KEY (`userId`);
--
ALTER TABLE `hr`
  ADD PRIMARY KEY (`userId`);

--
-- Indexes for table `person`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`userId`);

--
--


--
-- AUTO_INCREMENT for table `person`
--
ALTER TABLE `user`
  MODIFY `userId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--


--
-- Constraints for table `doctor`
--
ALTER TABLE `learner`
  ADD CONSTRAINT `learner_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`);
ALTER TABLE `trainer`
  ADD CONSTRAINT `trainer_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`);
ALTER TABLE `hr`
  ADD CONSTRAINT `hr_ibfk_1` FOREIGN KEY (`userId`) REFERENCES `user` (`userId`);


