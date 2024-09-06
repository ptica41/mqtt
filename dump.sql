-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `indication`
--

DROP TABLE IF EXISTS `indication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `indication` (
  `id` int NOT NULL AUTO_INCREMENT,
  `start` datetime NOT NULL,
  `end` datetime NOT NULL,
  `point_id` int NOT NULL,
  `sensor_id` int NOT NULL,
  `value` float NOT NULL,
  `status` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `point_id` (`point_id`),
  KEY `sensor_id` (`sensor_id`),
  CONSTRAINT `indication_ibfk_1` FOREIGN KEY (`point_id`) REFERENCES `point` (`id`) ON DELETE CASCADE,
  CONSTRAINT `indication_ibfk_2` FOREIGN KEY (`sensor_id`) REFERENCES `sensor` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `indication`
--

LOCK TABLES `indication` WRITE;
/*!40000 ALTER TABLE `indication` DISABLE KEYS */;
INSERT INTO `indication` VALUES (1,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,1,23.05,'normal'),(2,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,3,36.71,'normal'),(3,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,4,748.35,'normal'),(4,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,5,0,'normal'),(5,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,6,66.5,'normal'),(6,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,7,0,'normal'),(7,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,8,1419.42,'normal'),(8,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,9,5,'normal'),(9,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,10,5,'normal'),(10,'2023-08-14 16:38:17','2023-08-14 16:42:02',3,11,3.92,'normal'),(11,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,1,23.49,'normal'),(12,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,3,36.14,'normal'),(13,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,4,748.37,'normal'),(14,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,5,0,'normal'),(15,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,6,63.82,'normal'),(16,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,7,0,'normal'),(17,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,8,1298.47,'normal'),(18,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,9,4.88,'normal'),(19,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,10,4.88,'normal'),(20,'2023-08-14 16:48:16','2023-08-14 16:53:44',3,11,3.59,'normal'),(21,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,1,23.06,'normal'),(22,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,3,46.64,'normal'),(23,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,4,747.82,'normal'),(24,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,5,0,'normal'),(25,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,6,82.5,'normal'),(26,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,7,0,'normal'),(27,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,8,1568.5,'normal'),(28,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,9,11,'normal'),(29,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,10,10,'normal'),(30,'2023-08-15 12:43:00','2023-08-15 12:44:01',3,11,8,'normal'),(41,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,1,25.2,'normal'),(42,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,3,40.26,'normal'),(43,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,4,747.5,'normal'),(44,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,5,0,'normal'),(45,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,6,58.6,'normal'),(46,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,7,0,'normal'),(47,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,8,1291.24,'normal'),(48,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,9,5.81,'normal'),(49,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,10,5.8,'normal'),(50,'2023-08-15 17:17:57','2023-08-15 17:53:50',3,11,3.97,'normal'),(51,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,1,27,'normal'),(52,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,3,41.57,'normal'),(53,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,4,748.21,'normal'),(54,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,5,0,'normal'),(55,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,6,52.88,'normal'),(56,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,7,0,'normal'),(57,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,8,1329.38,'normal'),(58,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,9,7.88,'normal'),(59,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,10,7.5,'normal'),(60,'2023-08-16 09:17:13','2023-08-16 10:03:41',3,11,5.49,'normal');
/*!40000 ALTER TABLE `indication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `point`
--

DROP TABLE IF EXISTS `point`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `point` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `latitude` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `longitude` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `point`
--

LOCK TABLES `point` WRITE;
/*!40000 ALTER TABLE `point` DISABLE KEYS */;
INSERT INTO `point` VALUES (3,NULL,'53.178236','45.008828');
/*!40000 ALTER TABLE `point` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sensor`
--

DROP TABLE IF EXISTS `sensor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sensor` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `unit` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sensor`
--

LOCK TABLES `sensor` WRITE;
/*!40000 ALTER TABLE `sensor` DISABLE KEYS */;
INSERT INTO `sensor` VALUES (1,'Температура','*С'),(3,'Влажность','%'),(4,'Давление','мм/рт.ст'),(5,'Уровень CO2','ppm'),(6,'Уровень NO2','ppm'),(7,'Уровень SO2','ppm'),(8,'Уровень CO','ppm'),(9,'Концентрация крупных частиц пыли (PM 10)','мг/м3'),(10,'Концентрация мелкодисперсных частиц пыли (PM 2,5)','мг/м3'),(11,'Концентрация ультрадисперсных частиц пыли (PM 1,0)','мг/м3');
/*!40000 ALTER TABLE `sensor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-16 10:33:08
