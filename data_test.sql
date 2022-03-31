-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: shoes_online
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bill`
--

DROP TABLE IF EXISTS `bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill` (
  `id_bill` int NOT NULL AUTO_INCREMENT,
  `id_user` int DEFAULT NULL,
  `id_verifier` int DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  `date_create` datetime DEFAULT NULL,
  `total` varchar(250) DEFAULT NULL,
  `method` varchar(250) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_bill`),
  KEY `id_user` (`id_user`),
  KEY `id_verifier` (`id_verifier`),
  KEY `ix_bill_id_bill` (`id_bill`),
  CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE,
  CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`id_verifier`) REFERENCES `user` (`id_user`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill`
--

LOCK TABLES `bill` WRITE;
/*!40000 ALTER TABLE `bill` DISABLE KEYS */;
INSERT INTO `bill` VALUES (1,2,NULL,'chua xac Nhan','2022-03-23 00:00:00','230','COD',NULL),(2,2,NULL,'chua xac Nhan','2022-03-23 00:00:00','230','COD','Bac Lieu');
/*!40000 ALTER TABLE `bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bill_details`
--

DROP TABLE IF EXISTS `bill_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bill_details` (
  `id_bill_detail` int NOT NULL AUTO_INCREMENT,
  `id_bill` int DEFAULT NULL,
  `id_product` int DEFAULT NULL,
  `quantily` int DEFAULT NULL,
  `current_price` int DEFAULT NULL,
  `id_product_detail` int DEFAULT NULL,
  `id_size_quantity` int DEFAULT NULL,
  PRIMARY KEY (`id_bill_detail`),
  KEY `id_bill` (`id_bill`),
  KEY `id_product` (`id_product`),
  KEY `ix_bill_details_id_bill_detail` (`id_bill_detail`),
  CONSTRAINT `bill_details_ibfk_1` FOREIGN KEY (`id_bill`) REFERENCES `bill` (`id_bill`) ON DELETE CASCADE,
  CONSTRAINT `bill_details_ibfk_2` FOREIGN KEY (`id_product`) REFERENCES `product` (`id_product`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bill_details`
--

LOCK TABLES `bill_details` WRITE;
/*!40000 ALTER TABLE `bill_details` DISABLE KEYS */;
INSERT INTO `bill_details` VALUES (1,1,1,2,0,1,1),(2,2,1,1,0,1,1);
/*!40000 ALTER TABLE `bill_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id_category` int NOT NULL AUTO_INCREMENT,
  `id_promotion` int DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_category`),
  KEY `id_promotion` (`id_promotion`),
  KEY `ix_category_id_category` (`id_category`),
  CONSTRAINT `category_ibfk_1` FOREIGN KEY (`id_promotion`) REFERENCES `promotion` (`id_promotion`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,1,'Basas'),(2,NULL,'Vintas');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `color`
--

DROP TABLE IF EXISTS `color`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `color` (
  `id_color` int NOT NULL AUTO_INCREMENT,
  `hex` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_color`),
  KEY `ix_color_id_color` (`id_color`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `color`
--

LOCK TABLES `color` WRITE;
/*!40000 ALTER TABLE `color` DISABLE KEYS */;
INSERT INTO `color` VALUES (1,'#ffffff'),(2,'#000000');
/*!40000 ALTER TABLE `color` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comments` (
  `id_comments` int NOT NULL AUTO_INCREMENT,
  `id_user` int DEFAULT NULL,
  `Content` varchar(250) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  PRIMARY KEY (`id_comments`),
  KEY `id_user` (`id_user`),
  KEY `ix_comments_id_comments` (`id_comments`),
  CONSTRAINT `comments_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,2,'San pham hahah','2022-03-25 00:00:00'),(2,2,'San pham ok','2022-03-25 00:00:00');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gender`
--

DROP TABLE IF EXISTS `gender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gender` (
  `id_gender` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_gender`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_gender_id_gender` (`id_gender`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gender`
--

LOCK TABLES `gender` WRITE;
/*!40000 ALTER TABLE `gender` DISABLE KEYS */;
INSERT INTO `gender` VALUES (1,'Nam'),(2,'Nu');
/*!40000 ALTER TABLE `gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `image`
--

DROP TABLE IF EXISTS `image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `image` (
  `id_image` int NOT NULL AUTO_INCREMENT,
  `id_product_detail` int DEFAULT NULL,
  `path` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_image`),
  KEY `id_product_detail` (`id_product_detail`),
  KEY `ix_image_id_image` (`id_image`),
  CONSTRAINT `image_ibfk_1` FOREIGN KEY (`id_product_detail`) REFERENCES `product_detail` (`id_product_detail`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
INSERT INTO `image` VALUES (1,1,'media/products/1/images/2022-03-2209:01:33.380620.1_1jpg'),(2,1,'media/products/1/images/2022-03-2209:01:33.472191.jpg'),(3,1,'media/products/1/images/2022-03-2209:01:33.538542.jpg'),(4,1,'media/products/1/images/2022-03-2209:01:33.618561.jpg'),(5,2,'media/products/1/images/2022-03-2209:08:06.789872.jpg'),(6,2,'media/products/1/images/2022-03-2209:08:06.873483.jpg'),(7,2,'media/products/1/images/2022-03-2209:08:06.973481.jpg'),(8,2,'media/products/1/images/2022-03-2209:08:07.048163.jpg'),(9,3,'media/products/2/images/2022-03-2210:49:32.713055.jpg'),(10,3,'media/products/2/images/2022-03-2210:49:32.771690.jpg'),(11,3,'media/products/2/images/2022-03-2210:49:32.826655.jpg'),(12,4,'media/products/2/images/2022-03-2210:49:54.934684.jpg'),(13,4,'media/products/2/images/2022-03-2210:49:55.009852.jpg'),(14,4,'media/products/2/images/2022-03-2210:49:55.093828.jpg'),(15,4,'media/products/2/images/2022-03-2210:49:55.177693.jpg');
/*!40000 ALTER TABLE `image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `info`
--

DROP TABLE IF EXISTS `info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `info` (
  `id_info` int NOT NULL AUTO_INCREMENT,
  `phone` varchar(12) DEFAULT NULL,
  `full_name` varchar(250) DEFAULT NULL,
  `dob` datetime DEFAULT NULL,
  `email` varchar(250) DEFAULT NULL,
  `address` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_info`),
  KEY `ix_info_id_info` (`id_info`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES (1,'0828764625','Vu Ngoc Long','2000-03-30 00:00:00','long.speed@gmail.com','Bac Lieu'),(2,'0828764625','Vu Quang Hung','2000-10-21 00:00:00','user@gmail.com','Can Tho'),(3,'stringstri','string','2022-03-31 00:00:00','string','string'),(4,'0123456789','Quang Hưng','2000-10-21 00:00:00','xifmoocs@gmail.com','274b trang binh keit can t ho ');
/*!40000 ALTER TABLE `info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nameservices`
--

DROP TABLE IF EXISTS `nameservices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nameservices` (
  `id_name_services` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_name_services`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nameservices`
--

LOCK TABLES `nameservices` WRITE;
/*!40000 ALTER TABLE `nameservices` DISABLE KEYS */;
INSERT INTO `nameservices` VALUES (1,'Giat giay'),(2,'Sua giay');
/*!40000 ALTER TABLE `nameservices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permission`
--

DROP TABLE IF EXISTS `permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permission` (
  `id_permission` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_permission`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permission`
--

LOCK TABLES `permission` WRITE;
/*!40000 ALTER TABLE `permission` DISABLE KEYS */;
INSERT INTO `permission` VALUES (1,'Admin'),(3,'KhachHang'),(2,'NhanVien');
/*!40000 ALTER TABLE `permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `id_product` int NOT NULL AUTO_INCREMENT,
  `id_category` int DEFAULT NULL,
  `id_gender` int DEFAULT NULL,
  `name` varchar(250) DEFAULT NULL,
  `detail` text,
  `money` int DEFAULT NULL,
  PRIMARY KEY (`id_product`),
  KEY `id_category` (`id_category`),
  KEY `id_gender` (`id_gender`),
  KEY `ix_product_id_product` (`id_product`),
  CONSTRAINT `product_ibfk_1` FOREIGN KEY (`id_category`) REFERENCES `category` (`id_category`) ON DELETE CASCADE,
  CONSTRAINT `product_ibfk_2` FOREIGN KEY (`id_gender`) REFERENCES `gender` (`id_gender`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1,1,'BASAS BUMPER GUM EXT NE - LOW TOP - BLACK/GUM','Bumper Gum EXT (Extension) NE là bản nâng cấp được xếp vào dòng sản phẩm Basas, nhưng lại gây ấn tượng với diện mạo phá đi sự an toàn thường thấy. Với cách sắp xếp logo hoán đổi đầy ý tứ và mảng miếng da lộn (Suede) xuất hiện hợp lí trên chất vải canvas NE bền bỉ dày dặn nhấn nhá thêm bằng những sắc Gum dẻo dai. Tất cả làm nên 01 bộ sản phẩm với thiết kế đầy thoải mái trong trải nghiệm, đủ thanh lịch trong dáng vẻ.',580),(2,1,2,'BASAS BUMPER GUM EXT NE - LOW TOP - BLACK/GUM','Bumper Gum EXT (Extension) NE là bản nâng cấp được xếp vào dòng sản phẩm Basas, nhưng lại gây ấn tượng với diện mạo phá đi sự an toàn thường thấy. Với cách sắp xếp logo hoán đổi đầy ý tứ và mảng miếng da lộn (Suede) xuất hiện hợp lí trên chất vải canvas NE bền bỉ dày dặn nhấn nhá thêm bằng những sắc Gum dẻo dai. Tất cả làm nên 01 bộ sản phẩm với thiết kế đầy thoải mái trong trải nghiệm, đủ thanh lịch trong dáng vẻ.',580);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_detail`
--

DROP TABLE IF EXISTS `product_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_detail` (
  `id_product_detail` int NOT NULL AUTO_INCREMENT,
  `id_product` int DEFAULT NULL,
  `id_color` int DEFAULT NULL,
  PRIMARY KEY (`id_product_detail`),
  KEY `id_product` (`id_product`),
  KEY `id_color` (`id_color`),
  KEY `ix_product_detail_id_product_detail` (`id_product_detail`),
  CONSTRAINT `product_detail_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `product` (`id_product`) ON DELETE CASCADE,
  CONSTRAINT `product_detail_ibfk_2` FOREIGN KEY (`id_color`) REFERENCES `color` (`id_color`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_detail`
--

LOCK TABLES `product_detail` WRITE;
/*!40000 ALTER TABLE `product_detail` DISABLE KEYS */;
INSERT INTO `product_detail` VALUES (1,1,1),(2,1,2),(3,2,1),(4,2,2);
/*!40000 ALTER TABLE `product_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `promotion`
--

DROP TABLE IF EXISTS `promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `promotion` (
  `id_promotion` int NOT NULL AUTO_INCREMENT,
  `name` varchar(250) DEFAULT NULL,
  `detail` varchar(250) DEFAULT NULL,
  `reduction` int DEFAULT NULL,
  PRIMARY KEY (`id_promotion`),
  KEY `ix_promotion_id_promotion` (`id_promotion`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promotion`
--

LOCK TABLES `promotion` WRITE;
/*!40000 ALTER TABLE `promotion` DISABLE KEYS */;
INSERT INTO `promotion` VALUES (1,'Quốc tế phụ nữ','Mùng 8/3',25);
/*!40000 ALTER TABLE `promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rate` (
  `id_rate` int NOT NULL AUTO_INCREMENT,
  `number_star` int DEFAULT NULL,
  PRIMARY KEY (`id_rate`),
  KEY `ix_rate_id_rate` (`id_rate`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate`
--

LOCK TABLES `rate` WRITE;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
INSERT INTO `rate` VALUES (1,0),(2,1),(3,2),(4,3);
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rate_product`
--

DROP TABLE IF EXISTS `rate_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rate_product` (
  `id_rate_product` int NOT NULL AUTO_INCREMENT,
  `id_product` int DEFAULT NULL,
  `id_rate` int DEFAULT NULL,
  `id_comments` int DEFAULT NULL,
  PRIMARY KEY (`id_rate_product`),
  KEY `id_product` (`id_product`),
  KEY `id_rate` (`id_rate`),
  KEY `id_comments` (`id_comments`),
  KEY `ix_rate_product_id_rate_product` (`id_rate_product`),
  CONSTRAINT `rate_product_ibfk_1` FOREIGN KEY (`id_product`) REFERENCES `product` (`id_product`) ON DELETE CASCADE,
  CONSTRAINT `rate_product_ibfk_2` FOREIGN KEY (`id_rate`) REFERENCES `rate` (`id_rate`) ON DELETE CASCADE,
  CONSTRAINT `rate_product_ibfk_3` FOREIGN KEY (`id_comments`) REFERENCES `comments` (`id_comments`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate_product`
--

LOCK TABLES `rate_product` WRITE;
/*!40000 ALTER TABLE `rate_product` DISABLE KEYS */;
INSERT INTO `rate_product` VALUES (1,1,1,1),(2,1,1,2);
/*!40000 ALTER TABLE `rate_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `id_services` int NOT NULL AUTO_INCREMENT,
  `id_verifier` int DEFAULT NULL,
  `id_name_services` int DEFAULT NULL,
  `booking_date` datetime DEFAULT NULL,
  `date_create` datetime DEFAULT NULL,
  `status` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_services`),
  KEY `id_verifier` (`id_verifier`),
  KEY `id_name_services` (`id_name_services`),
  KEY `ix_services_id_services` (`id_services`),
  CONSTRAINT `services_ibfk_1` FOREIGN KEY (`id_verifier`) REFERENCES `user` (`id_user`) ON DELETE CASCADE,
  CONSTRAINT `services_ibfk_2` FOREIGN KEY (`id_name_services`) REFERENCES `nameservices` (`id_name_services`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (1,NULL,1,'2022-03-30 00:00:00',NULL,'Chua'),(2,NULL,1,'2022-03-30 00:00:00',NULL,'Chua'),(3,NULL,1,'2022-03-30 00:00:00',NULL,'Chua'),(4,NULL,1,'2022-03-30 00:00:00',NULL,'Chua'),(5,NULL,1,'2022-03-30 00:00:00',NULL,'Chua'),(6,NULL,1,'2022-03-30 00:00:00',NULL,'Chua'),(7,1,2,'2022-03-29 00:00:00','2022-03-29 00:00:00','Da xac nhan');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `size`
--

DROP TABLE IF EXISTS `size`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `size` (
  `id_size` int NOT NULL AUTO_INCREMENT,
  `size_number` float DEFAULT NULL,
  PRIMARY KEY (`id_size`),
  KEY `ix_size_id_size` (`id_size`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `size`
--

LOCK TABLES `size` WRITE;
/*!40000 ALTER TABLE `size` DISABLE KEYS */;
INSERT INTO `size` VALUES (1,42),(2,41),(3,40);
/*!40000 ALTER TABLE `size` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `size_quantity`
--

DROP TABLE IF EXISTS `size_quantity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `size_quantity` (
  `id_size_quantity` int NOT NULL AUTO_INCREMENT,
  `id_product_detail` int DEFAULT NULL,
  `id_size` int DEFAULT NULL,
  `quantity_sold` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  PRIMARY KEY (`id_size_quantity`),
  KEY `id_product_detail` (`id_product_detail`),
  KEY `id_size` (`id_size`),
  KEY `ix_size_quantity_id_size_quantity` (`id_size_quantity`),
  CONSTRAINT `size_quantity_ibfk_1` FOREIGN KEY (`id_product_detail`) REFERENCES `product_detail` (`id_product_detail`) ON DELETE CASCADE,
  CONSTRAINT `size_quantity_ibfk_2` FOREIGN KEY (`id_size`) REFERENCES `size` (`id_size`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `size_quantity`
--

LOCK TABLES `size_quantity` WRITE;
/*!40000 ALTER TABLE `size_quantity` DISABLE KEYS */;
INSERT INTO `size_quantity` VALUES (1,1,1,3,37),(2,1,2,0,30),(3,2,1,0,20),(4,2,2,0,10),(5,3,1,0,21),(6,3,2,0,31),(7,3,3,0,31),(8,4,3,0,22),(9,4,2,0,32);
/*!40000 ALTER TABLE `size_quantity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `id_info` int DEFAULT NULL,
  `id_permission` int DEFAULT NULL,
  `account` varchar(250) DEFAULT NULL,
  `password` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `account` (`account`),
  KEY `id_info` (`id_info`),
  KEY `id_permission` (`id_permission`),
  KEY `ix_user_id_user` (`id_user`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`id_info`) REFERENCES `info` (`id_info`) ON DELETE CASCADE,
  CONSTRAINT `user_ibfk_2` FOREIGN KEY (`id_permission`) REFERENCES `permission` (`id_permission`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,1,1,'long','$2b$12$ta5gTHyyKatzgvCkfvxMeOedMQYAlUSHa1t5uXRwpPLtguxB/uQTm'),(2,2,3,'hung2000','$2b$12$dzCM5t0PV7d3rVVy2jFmN.WOzdP6ts0ESpEfVvN5Vwf./u5bkixy6'),(3,3,3,'string','$2b$12$Eou1hUX59C0zoztjeCVg8e72Iv3.aPmB2G7MjYZ1zYNr.jmtfaKMO'),(4,4,3,'xifmoocs','$2b$12$R6Eqwh4lZRjrLLTPeJPBpOvOqGZNLgEoVkr7vdskj5SMLP9sS5/WO');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userservices`
--

DROP TABLE IF EXISTS `userservices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userservices` (
  `id_services` int NOT NULL,
  `id_user` int NOT NULL,
  PRIMARY KEY (`id_services`,`id_user`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `userservices_ibfk_1` FOREIGN KEY (`id_services`) REFERENCES `services` (`id_services`) ON DELETE CASCADE,
  CONSTRAINT `userservices_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id_user`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userservices`
--

LOCK TABLES `userservices` WRITE;
/*!40000 ALTER TABLE `userservices` DISABLE KEYS */;
INSERT INTO `userservices` VALUES (3,2),(4,2),(5,2),(6,2),(7,2);
/*!40000 ALTER TABLE `userservices` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-31 23:41:50
