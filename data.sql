-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ARTBASE
-- ------------------------------------------------------
-- Server version	5.5.54-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `ARTIST`
--

DROP TABLE IF EXISTS `ARTIST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ARTIST` (
  `AName` varchar(30) NOT NULL,
  `Birthplace` varchar(40) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `Style` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`AName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ARTIST`
--

LOCK TABLES `ARTIST` WRITE;
/*!40000 ALTER TABLE `ARTIST` DISABLE KEYS */;
INSERT INTO `ARTIST` VALUES ('beethoven','germany',120,'classical'),('elon','sa',55,'future'),('pablo','old',100,'classical'),('pianog','utah',55,'instrumental'),('sasa','norw',88,'tragedy');
/*!40000 ALTER TABLE `ARTIST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ARTWORK`
--

DROP TABLE IF EXISTS `ARTWORK`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ARTWORK` (
  `Title` varchar(30) NOT NULL DEFAULT '',
  `Year` int(11) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL,
  `AName` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Title`),
  KEY `AName` (`AName`),
  CONSTRAINT `ARTWORK_ibfk_1` FOREIGN KEY (`AName`) REFERENCES `ARTIST` (`AName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ARTWORK`
--

LOCK TABLES `ARTWORK` WRITE;
/*!40000 ALTER TABLE `ARTWORK` DISABLE KEYS */;
INSERT INTO `ARTWORK` VALUES ('dae',1900,'classical',200000,'pablo'),('fidelio',1799,'classical',500000,'beethoven'),('paypal',2003,'tech',1000000000,'elon');
/*!40000 ALTER TABLE `ARTWORK` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CLASSIFY`
--

DROP TABLE IF EXISTS `CLASSIFY`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CLASSIFY` (
  `Title` varchar(30) NOT NULL DEFAULT '',
  `GName` varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (`Title`,`GName`),
  KEY `GName` (`GName`),
  CONSTRAINT `CLASSIFY_ibfk_1` FOREIGN KEY (`Title`) REFERENCES `ARTWORK` (`Title`),
  CONSTRAINT `CLASSIFY_ibfk_2` FOREIGN KEY (`GName`) REFERENCES `GROUPS` (`GName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CLASSIFY`
--

LOCK TABLES `CLASSIFY` WRITE;
/*!40000 ALTER TABLE `CLASSIFY` DISABLE KEYS */;
INSERT INTO `CLASSIFY` VALUES ('dae','classical'),('fidelio','classical'),('paypal','tech');
/*!40000 ALTER TABLE `CLASSIFY` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CUSTOMER`
--

DROP TABLE IF EXISTS `CUSTOMER`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CUSTOMER` (
  `CustID` int(11) NOT NULL AUTO_INCREMENT,
  `CName` varchar(30) DEFAULT NULL,
  `Address` varchar(40) DEFAULT NULL,
  `Amount` int(11) DEFAULT NULL,
  PRIMARY KEY (`CustID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CUSTOMER`
--

LOCK TABLES `CUSTOMER` WRITE;
/*!40000 ALTER TABLE `CUSTOMER` DISABLE KEYS */;
INSERT INTO `CUSTOMER` VALUES (1,'Sashi','Pomona,CA',900000000);
/*!40000 ALTER TABLE `CUSTOMER` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `GROUPS`
--

DROP TABLE IF EXISTS `GROUPS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GROUPS` (
  `GName` varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (`GName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `GROUPS`
--

LOCK TABLES `GROUPS` WRITE;
/*!40000 ALTER TABLE `GROUPS` DISABLE KEYS */;
INSERT INTO `GROUPS` VALUES ('classical'),('tech');
/*!40000 ALTER TABLE `GROUPS` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIKE_ARTIST`
--

DROP TABLE IF EXISTS `LIKE_ARTIST`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIKE_ARTIST` (
  `CustID` int(11) NOT NULL DEFAULT '0',
  `AName` varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (`CustID`,`AName`),
  KEY `AName` (`AName`),
  CONSTRAINT `LIKE_ARTIST_ibfk_1` FOREIGN KEY (`CustID`) REFERENCES `CUSTOMER` (`CustID`),
  CONSTRAINT `LIKE_ARTIST_ibfk_2` FOREIGN KEY (`AName`) REFERENCES `ARTIST` (`AName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIKE_ARTIST`
--

LOCK TABLES `LIKE_ARTIST` WRITE;
/*!40000 ALTER TABLE `LIKE_ARTIST` DISABLE KEYS */;
INSERT INTO `LIKE_ARTIST` VALUES (1,'beethoven'),(1,'elon'),(1,'pablo');
/*!40000 ALTER TABLE `LIKE_ARTIST` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `LIKE_GROUP`
--

DROP TABLE IF EXISTS `LIKE_GROUP`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `LIKE_GROUP` (
  `CustID` int(11) NOT NULL DEFAULT '0',
  `GName` varchar(30) NOT NULL DEFAULT '',
  PRIMARY KEY (`CustID`,`GName`),
  KEY `GName` (`GName`),
  CONSTRAINT `LIKE_GROUP_ibfk_1` FOREIGN KEY (`CustID`) REFERENCES `CUSTOMER` (`CustID`),
  CONSTRAINT `LIKE_GROUP_ibfk_2` FOREIGN KEY (`GName`) REFERENCES `GROUPS` (`GName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `LIKE_GROUP`
--

LOCK TABLES `LIKE_GROUP` WRITE;
/*!40000 ALTER TABLE `LIKE_GROUP` DISABLE KEYS */;
INSERT INTO `LIKE_GROUP` VALUES (1,'classical'),(1,'tech');
/*!40000 ALTER TABLE `LIKE_GROUP` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-02-08  4:43:39
