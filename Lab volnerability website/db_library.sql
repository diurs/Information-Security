-- phpMyAdmin SQL Dump
-- version 4.4.12
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Авг 05 2020 г., 07:50
-- Версия сервера: 5.6.26
-- Версия PHP: 7.0.0beta2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `db_library`
--
CREATE DATABASE IF NOT EXISTS `db_library` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `db_library`;

-- --------------------------------------------------------

--
-- Структура таблицы `members`
--

CREATE TABLE IF NOT EXISTS `members` (
  `id` int(11) NOT NULL,
  `name` text COLLATE utf8_unicode_ci NOT NULL,
  `password` text COLLATE utf8_unicode_ci NOT NULL,
  `status` text COLLATE utf8_unicode_ci NOT NULL,
  `books` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=109 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `members`
--

INSERT INTO `members` (`id`, `name`, `password`, `status`, `books`) VALUES
(1, 'Demo', '111', 'user', '<ul>\r\n<li> Журнал Мурзилка (подшивка за 1986-1989 гг.) </li>\r\n<li>Вл. Ленин. Мир, труд, май! </li>\r\n<li>С.Минаев. Духless </li>\r\n</ul>\r\n'),
(2, 'Librarian', 'ptty', 'admin', '<ul>\r\n<li>Кали Линукс в картинках </li>\r\n<li>Кали Линукс для тех, у кого нет компьютера </li>\r\n<li>Кали Линукс для тех, кому за 60 </li>\r\n</ul>'),
(108, 'Spammer', '99gndl:f', 'user', 'Для спамеров ничего нет - ненавижу спамеров!');

-- --------------------------------------------------------

--
-- Структура таблицы `unused1`
--

CREATE TABLE IF NOT EXISTS `unused1` (
  `qq` int(11) NOT NULL,
  `qw` int(11) NOT NULL,
  `er` int(11) NOT NULL,
  `rty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `unused2`
--

CREATE TABLE IF NOT EXISTS `unused2` (
  `dfg` int(11) NOT NULL,
  `ff` text COLLATE utf8_unicode_ci NOT NULL,
  `hhh` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `members`
--
ALTER TABLE `members`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `members`
--
ALTER TABLE `members`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=109;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
