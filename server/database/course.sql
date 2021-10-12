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
('XRX-101', 'hello', 'ur mother', 'coursename'),
('XRX-102', 'hello2', 'ur father', 'coursename');

ALTER TABLE `course`
  ADD PRIMARY KEY (`courseId`);



