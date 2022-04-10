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
  `total` int DEFAULT NULL,
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
INSERT INTO `bill` VALUES (1,3,NULL,'Chua','2022-04-10 00:00:00',720000,'COD','Can tho'),(2,3,NULL,'Chua','2022-04-10 00:00:00',980000,'COD','Can tho');
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
INSERT INTO `bill_details` VALUES (1,1,6,1,720000,8,80),(2,2,5,2,490000,7,68);
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
INSERT INTO `category` VALUES (1,NULL,'BASAS'),(2,NULL,'VINTAS');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `color`
--

LOCK TABLES `color` WRITE;
/*!40000 ALTER TABLE `color` DISABLE KEYS */;
INSERT INTO `color` VALUES (1,'#2d2c2f'),(2,'#efeee5'),(3,'#30524e'),(4,'#d7c49e'),(5,'#889bae'),(6,'#f0f0ec');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `image`
--

LOCK TABLES `image` WRITE;
/*!40000 ALTER TABLE `image` DISABLE KEYS */;
INSERT INTO `image` VALUES (1,1,'http://drive.google.com/uc?export=view&id=1WgpdvEbd6KVnfbzYrfXwYQonl5ZjgW_v'),(2,1,'http://drive.google.com/uc?export=view&id=1_Nr0yWGpBob0BDoTxzwO-r2atH_BoJMS'),(3,1,'http://drive.google.com/uc?export=view&id=1_zoxNEdIY2jUZr4tR6tfBae-A-2unsRH'),(4,2,'http://drive.google.com/uc?export=view&id=1voPKtedSk-HF5VAwHz187xurJ4acmOwt'),(5,2,'http://drive.google.com/uc?export=view&id=1STHWNgX7t2ZGoSGZG5lCS_tOU9ftMgB8'),(6,2,'http://drive.google.com/uc?export=view&id=125OJBg1Fr9cpZbVnTGdvELJFNSOQsDQt'),(7,3,'http://drive.google.com/uc?export=view&id=1fBU6yewvcw54m9hATsr-HYZdW9MS4WU4'),(8,3,'http://drive.google.com/uc?export=view&id=1iQH-NzDWbxgaouBhWmp4Me9HLO8tcSKv'),(9,3,'http://drive.google.com/uc?export=view&id=1Y62DFhOb6ExP_9GzsdHwk22PhCWAQpR6'),(10,4,'http://drive.google.com/uc?export=view&id=11IsqVU4Ot1qE57TM_lwWBRB5vnGoMUxE'),(11,4,'http://drive.google.com/uc?export=view&id=1EfyRz-hrwNuzVRFC74FvNHGMk2B28H8d'),(12,4,'http://drive.google.com/uc?export=view&id=1wzBIEErTyZpUfY80f9Q70NG7jVVYBcRw'),(13,5,'http://drive.google.com/uc?export=view&id=1CSj21twprxVelsomYtix3JV_sT6oIcQy'),(14,5,'http://drive.google.com/uc?export=view&id=1WhkgZ0E70_TYezMG9AR0wZur7TVPbST7'),(15,5,'http://drive.google.com/uc?export=view&id=1Oh04LB9avRRdyTLYMc8c7ciIydiSpNnA'),(16,6,'http://drive.google.com/uc?export=view&id=1eEyOnsll9Dowxubkf7HMPui0uXEuAin8'),(17,6,'http://drive.google.com/uc?export=view&id=1GBUyj56iXRqCNyzTAadU4hGhUhpBnajw'),(18,6,'http://drive.google.com/uc?export=view&id=100USOiRD81Gsu6_ZSjZiYwc4Dwbp7s5f'),(19,7,'http://drive.google.com/uc?export=view&id=1Dg9HGSl1_mOB8nKktauHrDq6gKP5W5iH'),(20,7,'http://drive.google.com/uc?export=view&id=1s8505ohizNhW1XenxhWeWZN6ar5qWzyk'),(21,7,'http://drive.google.com/uc?export=view&id=1kmQLfmhDE9ZcQis_hD3ZTphS0Pms1_bc'),(22,8,'http://drive.google.com/uc?export=view&id=1zsim1oC5Geds_4L9XGarpNLwFzP8rbJf'),(23,8,'http://drive.google.com/uc?export=view&id=1JDCMDLKLXrp2deY81GQHzU7-_6AfvvcA'),(24,8,'http://drive.google.com/uc?export=view&id=1S9tZv3E_0fH0bEnJHdZ4zjypqsCtpE06');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `info`
--

LOCK TABLES `info` WRITE;
/*!40000 ALTER TABLE `info` DISABLE KEYS */;
INSERT INTO `info` VALUES (1,'0828764625','Vu Ngoc Long','2000-03-30 00:00:00','long.speed00@gmail.com','Bac Lieu'),(2,'0828764622','Nhan Vien 1','2000-02-20 00:00:00','nhanvie1n@gmail.com','Bac Lieu'),(3,'0828764632','Vu Quang Hung','2000-10-21 00:00:00','hung2000@gmail.com','Can tho');
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nameservices`
--

LOCK TABLES `nameservices` WRITE;
/*!40000 ALTER TABLE `nameservices` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,1,1,'BASAS BUMPER GUM EXT NE - LOW TOP – BLACK/GUM','Bumper Gum EXT (Extension) NE là bản nâng cấp được xếp vào dòng sản phẩm Basas, nhưng lại gây ấn tượng với diện mạo phá đi sự an toàn thường thấy. Với cách sắp xếp logo hoán đổi đầy ý tứ và mảng miếng da lộn (Suede) xuất hiện hợp lí trên chất vải canvas NE bền bỉ dày dặn nhấn nhá thêm bằng những sắc Gum dẻo dai. Tất cả làm nên 01 bộ sản phẩm với thiết kế đầy thoải mái trong trải nghiệm, đủ thanh lịch trong dáng vẻ.',580000),(2,1,1,'BASAS BUMPER GUM EXT NE - HIGH TOP - BLACK/GUM','Bumper Gum EXT (Extension) NE là bản nâng cấp được xếp vào dòng sản phẩm Basas, nhưng lại gây ấn tượng với diện mạo phá đi sự an toàn thường thấy. Với cách sắp xếp logo hoán đổi đầy ý tứ và mảng miếng da lộn (Suede) xuất hiện hợp lí trên chất vải canvas NE bền bỉ dày dặn nhấn nhá thêm bằng những sắc Gum dẻo dai. Tất cả làm nên 01 bộ sản phẩm với thiết kế đầy thoải mái trong trải nghiệm, đủ thanh lịch trong dáng vẻ.',640000),(3,1,1,'BASAS BUMPER GUM EXT NE - LOW TOP - OFFWHITE/GUM','Bumper Gum EXT (Extension) NE là bản nâng cấp được xếp vào dòng sản phẩm Basas, nhưng lại gây ấn tượng với diện mạo phá đi sự an toàn thường thấy. Với cách sắp xếp logo hoán đổi đầy ý tứ và mảng miếng da lộn (Suede) xuất hiện hợp lí trên chất vải canvas NE bền bỉ dày dặn nhấn nhá thêm bằng những sắc Gum dẻo dai. Tất cả làm nên 01 bộ sản phẩm với thiết kế đầy thoải mái trong trải nghiệm, đủ thanh lịch trong dáng vẻ.',580000),(4,2,1,'VINTAS AUNTER - LOW TOP - BOTANICAL GARDEN','Kết hợp cùng diện mạo quai dán (hook\'n loop) mới mẻ, Aunter chính là một bản phối lạ lẫm nhưng đầy thú vị lần đầu tiên xuất hiện của dòng Vintas. Vẫn là chất vải Canvas thường gặp, đi cặp cùng các lựa chọn màu sắc phong phú nhưng vẫn ẩn sâu bên trong nét điềm đạm. Tất cả làm nên điểm nhấn chững chạc tổng thể, dễ dàng tôn lên nét thu hút cần thiết mọi lần lên chân.',690000),(5,1,2,'BASAS SIMPLE LIFE NE - LOW TOP','Giữ vững nét tối giản đặc trưng thuộc dòng Basas, Basas Simple Life - NE (New Episode) sở hữu những đặc điểm nâng cấp ở chất liệu cùng họa tiết foxing mới, sự kết hợp tinh giản không hề đơn điệu, bình thường nhưng không tầm thường cho những ai thực sự yêu thích sự thoải mái đơn giản cho ngày dài hoạt động.',490000),(6,2,2,'VINTAS MONOGUSO - LOW TOP','Thiết kế mới Vintas Monoguso mang đến âm hưởng của những nét đẹp cổ điển không tuổi. Sử dụng chất liệu Heavy Canvas sợi lớn dày dặn-nhân đôi, đặc biệt bền bỉ theo thời gian; viền giày được bọc lớp da “bề mặt” (Full Grain Leather) cho cảm giác cổ điển hơn. Điểm nhấn màu sắc từ chất liệu Suede (da lộn) tại lưỡi gà-gót giày tăng vẻ ấn tượng trên nền màu nhã nhặn tổng thể. Vintas Monoguso chính là lựa chọn sở hữu diện mạo đủ chất “cũ” nhưng đầy mới lạ khi lên chân.',720000);
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_detail`
--

LOCK TABLES `product_detail` WRITE;
/*!40000 ALTER TABLE `product_detail` DISABLE KEYS */;
INSERT INTO `product_detail` VALUES (1,1,1),(2,2,1),(3,3,2),(4,4,3),(5,4,4),(6,4,5),(7,5,6),(8,6,1);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `promotion`
--

LOCK TABLES `promotion` WRITE;
/*!40000 ALTER TABLE `promotion` DISABLE KEYS */;
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
INSERT INTO `rate` VALUES (1,0),(2,1),(3,2),(4,3),(5,4),(6,5);
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate_product`
--

LOCK TABLES `rate_product` WRITE;
/*!40000 ALTER TABLE `rate_product` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `size`
--

LOCK TABLES `size` WRITE;
/*!40000 ALTER TABLE `size` DISABLE KEYS */;
INSERT INTO `size` VALUES (1,36),(2,37),(3,38),(4,39),(5,40),(6,41),(7,42),(8,43),(9,44),(10,45),(11,46);
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
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `size_quantity`
--

LOCK TABLES `size_quantity` WRITE;
/*!40000 ALTER TABLE `size_quantity` DISABLE KEYS */;
INSERT INTO `size_quantity` VALUES (1,1,1,0,9),(2,1,2,0,9),(3,1,3,0,10),(4,1,4,0,11),(5,1,5,0,15),(6,1,6,0,25),(7,1,7,0,30),(8,1,8,0,15),(9,1,9,0,16),(10,1,10,0,17),(11,1,11,0,18),(12,2,1,0,8),(13,2,2,0,11),(14,2,3,0,10),(15,2,4,0,11),(16,2,5,0,15),(17,2,6,0,25),(18,2,7,0,30),(19,2,8,0,15),(20,2,9,0,16),(21,2,10,0,17),(22,2,11,0,18),(23,3,1,0,7),(24,3,2,0,10),(25,3,3,0,10),(26,3,4,0,11),(27,3,5,0,15),(28,3,6,0,25),(29,3,7,0,30),(30,3,8,0,15),(31,3,9,0,16),(32,3,10,0,17),(33,3,11,0,18),(34,4,1,0,9),(35,4,2,0,9),(36,4,3,0,10),(37,4,4,0,11),(38,4,5,0,15),(39,4,6,0,25),(40,4,7,0,30),(41,4,8,0,15),(42,4,9,0,16),(43,4,10,0,17),(44,4,11,0,18),(45,5,1,0,9),(46,5,2,0,9),(47,5,3,0,10),(48,5,4,0,11),(49,5,5,0,15),(50,5,6,0,25),(51,5,7,0,30),(52,5,8,0,15),(53,5,9,0,16),(54,5,10,0,17),(55,5,11,0,18),(56,6,1,0,10),(57,6,2,0,9),(58,6,3,0,10),(59,6,4,0,11),(60,6,5,0,15),(61,6,6,0,25),(62,6,7,0,30),(63,6,8,0,15),(64,6,9,0,16),(65,6,10,0,17),(66,6,11,0,18),(67,7,1,0,9),(68,7,2,2,7),(69,7,3,0,10),(70,7,4,0,11),(71,7,5,0,15),(72,7,6,0,25),(73,7,7,0,30),(74,7,8,0,15),(75,7,9,0,16),(76,7,10,0,17),(77,7,11,0,18),(78,8,1,0,9),(79,8,2,0,9),(80,8,3,1,9),(81,8,4,0,11),(82,8,5,0,15),(83,8,6,0,25),(84,8,7,0,30),(85,8,8,0,15),(86,8,9,0,16),(87,8,10,0,17),(88,8,11,0,18);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,1,1,'long','$2b$12$Ph62RyiwKZfwgZBdmvZpQOWzIpoSVQNfKAG/I6HyTPKj/msHHHWNC'),(2,2,2,'nhanvien1','$2b$12$HkKZAlav8M1f2s7vxIUtAegkfu8PdES1NTXtATeIkTzxKDmfSIjki'),(3,3,3,'hung','$2b$12$c737ZfewqiEik4GKcljnyOeiDWeb0N52n41tlplj7jxgRqKi0n9D2');
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

-- Dump completed on 2022-04-10 14:41:43
