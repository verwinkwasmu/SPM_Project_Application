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


CREATE TABLE `section` (
  `sectionId` varchar(10) NOT NULL,
  `classId` varchar(50) NOT NULL,
  PRIMARY KEY (`sectionId`,`classId`),
  FOREIGN KEY (`classId`) REFERENCES class(`classId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `person`
--

INSERT INTO `section` (`sectionId`, `classId`) VALUES
('Section 1', 'XRX-101 Class 1'),
('Section 2', 'XRX-101 Class 1')