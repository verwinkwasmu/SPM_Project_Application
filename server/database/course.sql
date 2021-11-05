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

--
-- Database: `is212_example`
--




CREATE TABLE `course` (
  `courseId` varchar(50) NOT NULL,
  `courseName` varchar(50) DEFAULT NULL,
  `courseDescription` varchar(10) DEFAULT NULL,
  `prerequisites` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `person`
--

INSERT INTO `course` (`courseId`, `courseName`, `courseDescription`, `prerequisites`) VALUES
('B-102', 'Common Fixes for Brother 225', 'Finish this course to understand the common problems of Brother 225 that our customers usually bring up along with the f', null),
('HP-111', 'Cleaning the HP 619', 'This course highlights the techniques required to clean the HP 619 Printer thoroughly.', null),
('HP-112', 'Boosting the HP 619 Performance', 'This course perfectly highlights the nuances and ways to increase the performance of the HP 619', null),
('XRX-101', 'Fundamentals of Xerox Work Centre 7845', 'An introductory course to the fundamentals of Xerox', null),
('XRX-102', 'Advanced Xerox Work Centre 7900', 'An advanced course on Xerox Work Centre 7900', 'XRX-101:Fundamentals of Xerox Work Centre 7845'),
('XRX-103', 'Final Xerox Work Centre 7900', 'The final extensive course on Xerox Work Centre 7900', 'XRX-102:Advanced Xerox Work Centre 7900'),
('XRX-201', 'Programming for Xerox Work Centre with Card Access and Integration', 'A programming course on Xerox Work Centre', null);

ALTER TABLE `course`
  ADD PRIMARY KEY (`courseId`);



