/*
Navicat MySQL Data Transfer

Source Server         : pytest
Source Server Version : 80011
Source Host           : localhost:3306
Source Database       : py1

Target Server Type    : MYSQL
Target Server Version : 80011
File Encoding         : 65001

Date: 2019-02-22 15:56:30
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for stock
-- ----------------------------
DROP TABLE IF EXISTS `stock`;
CREATE TABLE `stock` (
  `Date` varchar(32) NOT NULL,
  `OpenPrice` varchar(8) NOT NULL,
  `HighPrice` varchar(8) NOT NULL,
  `LowPrice` varchar(8) NOT NULL,
  `ClosePrice` varchar(8) NOT NULL,
  `DiffrenceValue` varchar(8) NOT NULL,
  `DiffrencePercent` varchar(8) NOT NULL,
  `Amplitude` varchar(8) NOT NULL,
  `Volume` bigint(20) NOT NULL,
  `Amount` bigint(20) NOT NULL,
  `HandRate` varchar(8) NOT NULL,
  PRIMARY KEY (`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
