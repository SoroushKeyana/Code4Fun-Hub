-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2023 at 01:02 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `music_player`
--

-- --------------------------------------------------------

--
-- Table structure for table `comment`
--

CREATE TABLE `comment` (
  `comm_ID` int(11) NOT NULL,
  `comm_Name` varchar(255) NOT NULL,
  `comm_Comment` text NOT NULL,
  `Comm_Date` datetime NOT NULL DEFAULT current_timestamp(),
  `co_Fo_songs_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `comment`
--

INSERT INTO `comment` (`comm_ID`, `comm_Name`, `comm_Comment`, `Comm_Date`, `co_Fo_songs_ID`) VALUES
(32, 'Arash', 'it was incredeble wooow', '2023-11-20 21:01:17', 46),
(33, 'Arash', 'it was incredeble wooow', '2023-11-20 21:01:17', 46),
(34, 'Ali jan', 'I do not hava any idia', '0000-00-00 00:00:00', 59),
(35, 'mostafa', 'nae donam', '2023-11-28 13:12:08', 56),
(36, 'mostafa', 'nae donam', '2023-11-28 13:12:17', 56),
(37, 'sodaba', 'it was not bad for me', '2023-11-28 13:15:28', 59);

-- --------------------------------------------------------

--
-- Table structure for table `file`
--

CREATE TABLE `file` (
  `file_ID` int(11) NOT NULL,
  `file_File` varchar(255) NOT NULL,
  `file_Tyip` enum('Video','Audio','','') NOT NULL,
  `File_Fo_songs_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `file`
--

INSERT INTO `file` (`file_ID`, `file_File`, `file_Tyip`, `File_Fo_songs_ID`) VALUES
(53, 'tasveri.mp4', 'Audio', 55),
(58, 'tasveri.mp4', 'Video', 56),
(62, 'صوتی.mp3', 'Audio', 58),
(63, 'tasveri.mp4', 'Video', 59),
(64, 'صوتی.mp3', 'Audio', 58),
(66, 'tasveri.mp4', 'Video', 59),
(69, 'vid1.mp4', 'Video', 48),
(70, 'صوتی.mp3', 'Audio', 46);

-- --------------------------------------------------------

--
-- Table structure for table `singer`
--

CREATE TABLE `singer` (
  `Psinger_ID` int(11) NOT NULL,
  `singer_Name` varchar(255) NOT NULL,
  `singer_Last_Name` varchar(255) NOT NULL,
  `singer_Photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `singer`
--

INSERT INTO `singer` (`Psinger_ID`, `singer_Name`, `singer_Last_Name`, `singer_Photo`) VALUES
(32, 'Zhila', 'Ahmadii', '-5019610734073588596_120.jpg'),
(41, 'Sefo', 'sifolla', 'IMG_20220809_002712_045.jpg'),
(42, 'Areyana', 'sayed', 'IMG_20220821_003923_127.jpg'),
(44, 'Ali Zhila', 'Ahmadi', 'IMG_20220614_001552_256.jpg'),
(46, 'Ali', 'Hidded', 'IMG_20220823_145732_350.jpg'),
(51, 'Jamal', 'Mobariz', 'IMG_20220303_192444_395.jpg'),
(52, 'Mostafa', 'Azizyar', 'IMG_20211226_173314_654.jpg'),
(53, 'Mozhda', 'jamalZads', 'IMG_20220628_193747_745.jpg'),
(54, 'Jamal', 'Mobariz', 'IMG_20220303_192444_395.jpg'),
(56, 'Farzad', 'Honar dost', '-5172438971978984163_121.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `songs`
--

CREATE TABLE `songs` (
  `Psongs_ID` int(11) NOT NULL,
  `songs_Name` varchar(255) NOT NULL,
  `songs_Catagory` enum('Rap','Pop','Clasic','Rock') NOT NULL,
  `songs_Lyrix` text NOT NULL,
  `Fsinger_ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `songs`
--

INSERT INTO `songs` (`Psongs_ID`, `songs_Name`, `songs_Catagory`, `songs_Lyrix`, `Fsinger_ID`) VALUES
(46, ' chob', 'Rock', 'lalalalalalalal', 42),
(48, ' look', 'Clasic', 'please say for me', 32),
(55, ' Areyana', 'Pop', 'sayeed', 52),
(56, ' Afganitan', 'Rap', 'Love My cuntry', 44),
(58, 'sooty', 'Pop', 'test mekonam', 53),
(59, ' tasvery', 'Clasic', 'test mekonam', 56);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_ID` int(11) NOT NULL,
  `User_Name` varchar(255) NOT NULL,
  `User_Last_Name` varchar(255) NOT NULL,
  `User_Email` varchar(255) NOT NULL,
  `User_Password` varchar(255) NOT NULL,
  `user_photo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_ID`, `User_Name`, `User_Last_Name`, `User_Email`, `User_Password`, `user_photo`) VALUES
(23, 'Zhila', 'Ahmadi', 'zhila@gmail.com', 'z1234', 'IMG_20220605_182421_086.jpg'),
(24, 'Sadaf', 'Nabizada zhila', 'sadaf@gmail.com', 's1234', 'IMG_20220605_181850_725.jpg'),
(27, 'Zabiada', 'Arman', 'zabiada@gmail.com', '828c88f34ecb4c1ca8d89e018c6fad1a', '-5878440920091832412_120.jpg'),
(29, 'ismail', 'Rasikh', 'ismail@gemail.com', '3edf87bce4f5dd21020011731a82d7da', 'IMG_20220709_141715_658.jpg'),
(30, 'Zhila', 'Ahmadi', 'zhila@gmail.com', 'efefde9c9afefd929aa84de1ed70faf3', '-5019610734073588596_120.jpg'),
(34, 'Zabiada', 'Arman', 'zabiada@gmail.com', 'za12345', '-5852924429191985409_121.jpg'),
(36, 'Hasiba', 'Sadat', 'hasiba@gmail.com', ' 533107c202fe579936fb59f9bde33e2e', '-5028472845038103329_121.jpg'),
(37, 'Hasiba', 'Sadat', 'hasiba@gmail.com', ' eed23196e62f8b98b6fd2ea881fec77a', '-5048968459039386298_120.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comment`
--
ALTER TABLE `comment`
  ADD PRIMARY KEY (`comm_ID`),
  ADD KEY `Song_ID` (`co_Fo_songs_ID`);

--
-- Indexes for table `file`
--
ALTER TABLE `file`
  ADD PRIMARY KEY (`file_ID`),
  ADD KEY `Song_ID` (`File_Fo_songs_ID`);

--
-- Indexes for table `singer`
--
ALTER TABLE `singer`
  ADD PRIMARY KEY (`Psinger_ID`);

--
-- Indexes for table `songs`
--
ALTER TABLE `songs`
  ADD PRIMARY KEY (`Psongs_ID`),
  ADD KEY `singer_ID` (`Fsinger_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comment`
--
ALTER TABLE `comment`
  MODIFY `comm_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `file`
--
ALTER TABLE `file`
  MODIFY `file_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=71;

--
-- AUTO_INCREMENT for table `singer`
--
ALTER TABLE `singer`
  MODIFY `Psinger_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;

--
-- AUTO_INCREMENT for table `songs`
--
ALTER TABLE `songs`
  MODIFY `Psongs_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comment`
--
ALTER TABLE `comment`
  ADD CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`co_Fo_songs_ID`) REFERENCES `songs` (`Psongs_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `file`
--
ALTER TABLE `file`
  ADD CONSTRAINT `file_ibfk_1` FOREIGN KEY (`File_Fo_songs_ID`) REFERENCES `songs` (`Psongs_ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `songs`
--
ALTER TABLE `songs`
  ADD CONSTRAINT `songs_ibfk_1` FOREIGN KEY (`Fsinger_ID`) REFERENCES `singer` (`Psinger_ID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
