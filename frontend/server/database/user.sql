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

CREATE TABLE `spm_db`.`user` (
  `userId` INT NOT NULL,
  `employeeName` VARCHAR(50) NULL DEFAULT NULL,
  `userName` VARCHAR(50) NULL DEFAULT NULL,
  `email` VARCHAR(50) NULL DEFAULT NULL,
  `userType` VARCHAR(50) NULL DEFAULT NULL,
  `Designation` VARCHAR(50) NULL DEFAULT NULL,
  `Department` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`userId`),
  UNIQUE INDEX `userName_UNIQUE` (`userName` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 51;

-- --------------------------------------------------------

INSERT INTO `user` (`userId`, `employeeName`, `userName`, `email`, `userType`, `Designation`, `Department`) VALUES
(1, 'Phris Coskitt', 'learner1', 'phris@gmail.com', 'Learner', null, null),
(2, 'Hhris Coskitt', 'learner2', 'hhris@gmail.com', 'Learner', null, null),
(3, 'Lhris Coskitt', 'trainer3', 'lhris@gmail.com', 'Trainer', null, null),
(4, 'uhris Coskitt', 'trainer4', 'uhris@gmail.com', 'Trainer', null, null),
(5, 'jhris Coskitt', 'trainer5', 'jhris@gmail.com', 'Trainer', null, null),
(6, 'khris Coskitt', 'hr6', 'khris@gmail.com', 'HR', null, null),
(7, 'ohris Coskitt', 'hr7', 'ohris@gmail.com', 'HR', null, null),
(8, 'Ezra', 'trainer8', 'ezra@gmail.com', 'Trainer', null, null),
(9, 'Fiona', 'trainer9', 'fionz@gmail.com', 'Trainer', null, null),
(10, 'wx', 'learner10', 'wx@sis.com', 'Learner', null, null),
(11, 'Wayne', 'learner11', 'wayne@bruce.com', 'Learner', null, null),
(12, 'Verwin Kwa', 'learner12', 'verwin@gmail.com', 'Learner', null, null),
(13, 'Verwin Kwaa', 'learner13', 'verwinkwa@gmail.com', 'Learner', null, null),
(15, 'Sung', 'learner15', 'sung@smu.com', 'Learner', null, null),
(50, 'Jacob', 'trainer50', 'sunggg@smu.com', 'Learner', null, null);

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
(2),
(10),
(11),
(12),
(13),
(15),
(50);


CREATE TABLE `trainer` (
  `userId` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `trainer` (`userId`) VALUES
(3),
(4),
(5),
(8),
(9);


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


