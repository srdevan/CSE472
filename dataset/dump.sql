-- MySQL dump 10.13  Distrib 8.0.12, for osx10.14 (x86_64)
--
-- Host: localhost    Database: bot_identification_warehouse
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `bot_identification_warehouse`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `bot_identification_warehouse` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bot_identification_warehouse`;

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `videos` (
  `video_id` varchar(255) NOT NULL,
  `channel_id` varchar(255) NOT NULL,
  `view_count` bigint(20) DEFAULT NULL,
  `like_count` bigint(20) DEFAULT NULL,
  `dislike_count` bigint(20) DEFAULT NULL,
  `subscriber_count` bigint(20) DEFAULT NULL,
  `comment_count` bigint(20) DEFAULT NULL,
  `comments` blob,
  PRIMARY KEY (`video_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos`
--

LOCK TABLES `videos` WRITE;
/*!40000 ALTER TABLE `videos` DISABLE KEYS */;
INSERT INTO `videos` VALUES ('mHC82VVlPN0','UC7itJui050DPeh__1Ojs-nw',1667,253,7,422,10,_binary '{\'Vijay Kumar Khajuria\': \'My daughter holds you in high esteem you have taught her in an excellent manner.\', \'Tanu Jain\': \',DEAR SUCHI ,KEEP ON RISING AND SHINING DAY AFTER DAY AND BEST OF LUCK FOR YOUR FANTABULOUS LIFE AHEAD .\', \'Prableen Kour\': \'Lovely work... Keep gng on\\n..best of luck💞💞💞\', \'Balbir Gupta\': \'Very nice\', \'Shriya Raina\': \'Undoubtedly Shuchi Mam is the right and  perfect person to talk to and get counselling from. Her aura is execptional. Her classwork of Personality development class was so impact full. She made sure each and every student Comes to Know about his or her inner self . ❤️\', \'daizy goel\': \'Honest & genuine person❤❤\', \'ravi virk\': \'Best teacher of Nagbani school... N favourite teacher of my daughter... Inspiration for the students\', \'Yash Jamwal\': \'She was, is and will be my favourite ❤️\', \'Kamal Cheema\': \'Well said. Love u loads Shuchi maam\', \'Marvi Khajuria\': \'Shuchi mam is the best and among one the best mentors in my life.\'}'),('NHVnyfYqXnQ','UCMKOqiXkIBDtOmUXcRMfkWA',3859,154,6,2955,11,_binary '{\'Sarita Vyavahre\': \'Good work piyush doke camera man 😍😘\', \'Shrikant Thorat\': \'mast bhavano\', \'aniket ghadge\': \'really its very nice u give a nice message to people......\', \'sonali lohakare\': \'patillll tumchich hava\', \'Shreya Galani\': \'Nice work Mr patil. I m looking forward to work with you\', \'Akshay Jadhav\': \'छान... बदलते विचार...\', \'RANJEET BHURE\': \'BOTRE brothers and team awesome work yaro\', \'Sandeep Naik\': \'Super acting Omkar nice message\', \'Aditya K\': \'Good work .! Good direction prasad.\', \'Sudip Patil\': \'nice video and good message !\'}'),('y_jWAUJ_tv8','UC7itJui050DPeh__1Ojs-nw',631,44,1,422,3,_binary '{\'Renu Jain\': \'Grateful to the time and day I joined Cosmic. My life changed completely \\nThank you Maa.\', \'deepali dp\': \'Keep Inspiring Di 😘 👌🙏\'}');
/*!40000 ALTER TABLE `videos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-20  1:45:48
