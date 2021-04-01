-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : jeu. 01 avr. 2021 à 20:21
-- Version du serveur :  10.4.17-MariaDB
-- Version de PHP : 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `efood`
--

-- --------------------------------------------------------

--
-- Structure de la table `choixmenu`
--

CREATE TABLE `choixmenu` (
  `Entree` varchar(255) NOT NULL,
  `Plat` varchar(255) NOT NULL,
  `Dessert` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `choixmenu`
--

INSERT INTO `choixmenu` (`Entree`, `Plat`, `Dessert`) VALUES
('Andives', 'Boeuf Bourgigons et pomme de terre', 'Banane'),
('Betterave Vinaigrette', 'Chili con carne et riz', 'Cake'),
('Carottes rapées vinaigrettes', 'Cordon bleu et poêlé de légume', 'Carré de chocolat'),
('Celerys rémoulades', 'Cuisses de poulets et pomme de terre sautées', 'Cerise'),
('Choux rouges', 'Filet de colin et gratin de brocolis', 'Clafoutie'),
('Concombres à la crème', 'Frites kebab', 'Clémentine'),
('Concombres vinaigrettes', 'Hachie parmentier de poisson', 'Clémentine'),
('Friands', 'Lasagnes', 'Eclaire'),
('Macédoines', 'Merguez frites', 'Faisselle'),
('Melons', 'Moules Frites', 'Flancs'),
('Morceau Quiche', 'Omelette épinard', 'Fromage blanc'),
('Morceau Flammenkueches', 'Pâtes bolognaise', 'Gâteau'),
('Morceau Pizza', 'Paupiettes de veaux et poêlés de légumes', 'Glace'),
('Oeufs dur', 'Pavé de saumon et brocolis', 'Ile flottante'),
('Patés', 'Poulet rotis et gratin de chou-fleur', 'Kiwi'),
('Piémontaise', 'Poulets rotis et petit poids', 'Mille feuille'),
('Potage', 'Purée et Saucisses', 'Morceau de Tarte'),
('Radis au beurre', 'Ragout de boeuf et Pâtes', 'Mousse au chocolat'),
('Salade de riz', 'Ravioli', 'Nectarine'),
('Salade croutons', 'Riz et poissons pannés', 'Orange'),
('Salades de pâtes', 'Riz omelette', 'Pamplemouse'),
('Salade de quinoa', 'Rotis de porc et haricot vert', 'Pêche'),
('Saucissons', 'Saucisse et flageolets', 'Poire'),
('Taboulets', 'Sauté de poulets et courgettes', 'Pomme'),
('Tomates Maïs', 'Sautés de veaux et polenta', 'Riz au lait'),
('Tomates vinaigrettes', 'Steack frites', 'Salade de fruits'),
('Veloutés', 'Tartiflettes', 'Yaourt');

-- --------------------------------------------------------

--
-- Structure de la table `choixplatetudiant`
--

CREATE TABLE `choixplatetudiant` (
  `Date` date NOT NULL,
  `ChoixEntree` varchar(255) NOT NULL,
  `ChoixPlat` varchar(255) NOT NULL,
  `ChoixDessert` varchar(255) NOT NULL,
  `GachisEntree` varchar(255) NOT NULL,
  `GachisPlat` varchar(255) NOT NULL,
  `GachisDessert` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `choixplatetudiant`
--

INSERT INTO `choixplatetudiant` (`Date`, `ChoixEntree`, `ChoixPlat`, `ChoixDessert`, `GachisEntree`, `GachisPlat`, `GachisDessert`) VALUES
('2021-02-05', 'Melons', 'Frites kebab', 'Cerise', 'Gachis Faible', 'Gachis Moyen', 'Gachis Important'),
('2021-02-05', 'Melons', 'Frites kebab', 'Cerise', 'Gachis Important', 'Gachis Moyen', 'Gachis Faible'),
('2021-02-05', 'Concombres à la crème', 'Moules Frites', 'Clafoutie', 'Gachis Faible', 'Gachis Important', 'Gachis Moyen'),
('2021-02-05', 'Concombres à la crème', 'Frites kebab', 'Clafoutie', 'Gachis Moyen', 'Gachis Faible', 'Gachis Important'),
('2021-02-05', 'Concombres à la crème', 'Moules Frites', 'Clafoutie', 'Gachis Important', 'Gachis Faible', 'Gachis Moyen'),
('2021-02-05', 'Concombres à la crème', 'Frites kebab', 'Clafoutie', 'Gachis Faible', 'Gachis Faible', 'Gachis Faible'),
('2021-02-05', 'Concombres à la crème', 'Frites kebab', 'Cerise', 'Gachis Faible', 'Gachis Important', 'Gachis Moyen'),
('2021-02-05', 'Choux rouges', 'Saucisse et flageolets', 'Flancs', 'Gachis Moyen', 'Gachis Faible', 'Gachis Important'),
('2021-02-05', 'Choux rouges', 'Lasagnes', 'Cake', 'Gachis Faible', 'Gachis Moyen', 'Gachis Important'),
('2021-02-05', 'Friands', 'Saucisse et flageolets', 'Flancs', 'Gachis Faible', 'Gachis Moyen', 'Gachis Moyen'),
('2021-02-05', 'Choux rouges', 'Lasagnes', 'Flancs', 'Gachis Important', 'Gachis Moyen', 'Gachis Faible'),
('2021-02-05', 'Choux rouges', 'Saucisse et flageolets', 'Cake', 'Gachis Moyen', 'Gachis Faible', 'Gachis Faible'),
('2021-02-06', 'Friands', 'Lasagnes', 'Cake', 'Gachis Faible', 'Gachis Moyen', 'Gachis Important'),
('2021-02-06', 'Choux rouges', 'Saucisse et flageolets', 'Flancs', 'Gachis Important', 'Gachis Moyen', 'Gachis Moyen'),
('2021-02-06', 'Friands', 'Saucisse et flageolets', 'Cake', 'Gachis Important', 'Gachis Important', 'Gachis Moyen'),
('2021-02-06', 'Choux rouges', 'Saucisse et flageolets', 'Flancs', 'Gachis Important', 'Gachis Moyen', 'Gachis Faible'),
('2021-02-06', 'Friands', 'Lasagnes', 'Cake', 'Gachis Faible', 'Gachis Moyen', 'Gachis Moyen'),
('2021-02-06', 'Choux rouges', 'Saucisse et flageolets', 'Flancs', 'Gachis Faible', 'Gachis Moyen', 'Gachis Moyen'),
('2021-02-06', 'Choux rouges', 'Lasagnes', 'Flancs', 'Gachis Important', 'Gachis Moyen', 'Gachis Important'),
('2021-02-08', 'Taboulets', 'Riz omelette', 'Riz au lait', 'Gachis Moyen', 'Gachis Faible', 'Gachis Important'),
('2021-03-04', 'Oeufs dur', 'Ravioli', 'Yaourt', 'Gachis Faible', 'Gachis Faible', 'Gachis Faible'),
('2021-03-04', 'Saucissons', 'Rotis de porc et haricot vert', 'Poire', 'Gachis Faible', 'Gachis Moyen', 'Gachis Important'),
('2021-03-04', 'Oeufs dur', 'Rotis de porc et haricot vert', 'Yaourt', 'Gachis Moyen', 'Gachis Faible', 'Gachis Important'),
('2021-03-04', 'Oeufs dur', 'Ravioli', 'Poire', 'Gachis Moyen', 'Gachis Faible', 'Gachis Faible'),
('2021-03-04', 'Oeufs dur', 'Rotis de porc et haricot vert', 'Yaourt', 'Gachis Faible', 'Gachis Faible', 'Gachis Faible'),
('2021-03-04', 'Oeufs dur', 'Rotis de porc et haricot vert', 'Poire', 'Gachis Important', 'Gachis Moyen', 'Gachis Faible'),
('2021-03-04', 'Oeufs dur', 'Ravioli', 'Yaourt', 'Gachis Faible', 'Gachis Moyen', 'Gachis Important'),
('2021-03-05', 'Salades de pâtes', 'Sautés de veaux et polenta', 'Faisselle', 'Gachis Important', 'Gachis Moyen', 'Gachis Important'),
('2021-03-05', 'Macédoines', 'Sautés de veaux et polenta', 'Banane', 'Gachis Faible', 'Gachis Faible', 'Gachis Faible'),
('2021-03-05', 'Salades de pâtes', 'Sautés de veaux et polenta', 'Faisselle', 'Gachis Faible', 'Gachis Moyen', 'Gachis Moyen'),
('2021-03-05', 'Macédoines', 'Moules Frites', 'Faisselle', 'Gachis Faible', 'Gachis Faible', 'Gachis Faible'),
('2021-03-05', 'Macédoines', 'Moules Frites', 'Faisselle', 'Gachis Moyen', 'Gachis Important', 'Gachis Moyen'),
('2021-03-05', 'Macédoines', 'Sautés de veaux et polenta', 'Banane', 'Gachis Faible', 'Gachis Moyen', 'Gachis Moyen'),
('2021-03-05', 'Macédoines', 'Moules Frites', 'Banane', 'Gachis Faible', 'Gachis Faible', 'Gachis Faible'),
('2021-03-05', 'Salades de pâtes', 'Sautés de veaux et polenta', 'Faisselle', 'Gachis Moyen', 'Gachis Important', 'Gachis Faible'),
('2021-03-25', 'Concombres à la crème', 'Boeuf Bourgigons et pomme de terre', 'Faisselle', 'Gachis Faible', 'Gachis Faible', 'Gachis Faible'),
('2021-04-01', 'Andives', 'Cordon bleu et poêlé de légume', 'Clémentine', 'Pas De Gachis', 'Gachis Faible', 'Gachis Faible'),
('2021-04-01', 'Betterave Vinaigrette', 'Cordon bleu et poêlé de légume', 'Orange', 'Pas De Gachis', 'Gachis Moyen', 'Gachis Important');

-- --------------------------------------------------------

--
-- Structure de la table `gachis_tableau`
--

CREATE TABLE `gachis_tableau` (
  `Date` varchar(255) NOT NULL,
  `Entree` varchar(255) NOT NULL,
  `Gachis_Entree` int(11) NOT NULL,
  `Plat` varchar(255) NOT NULL,
  `Gachis_Plat` int(11) NOT NULL,
  `Dessert` varchar(255) NOT NULL,
  `Gachis_Dessert` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `gachis_tableau`
--

INSERT INTO `gachis_tableau` (`Date`, `Entree`, `Gachis_Entree`, `Plat`, `Gachis_Plat`, `Dessert`, `Gachis_Dessert`) VALUES
('Fevrier2021', 'Melons', 50, '-1', -1, '-1', -1),
('Fevrier2021', 'Concombres à la crème', 37, '-1', -1, '-1', -1),
('Fevrier2021', 'Choux rouges', 58, '-1', -1, '-1', -1),
('Fevrier2021', 'Friands', 34, '-1', -1, '-1', -1),
('Fevrier2021', 'Taboulets', 50, '-1', -1, '-1', -1),
('Fevrier2021', '-1', -1, 'Frites kebab', 43, '-1', -1),
('Fevrier2021', '-1', -1, 'Moules Frites', 50, '-1', -1),
('Fevrier2021', '-1', -1, 'Saucisse et flageolets', 45, '-1', -1),
('Fevrier2021', '-1', -1, 'Lasagnes', 50, '-1', -1),
('Fevrier2021', '-1', -1, 'Riz omelette', 17, '-1', -1),
('Fevrier2021', '-1', -1, '-1', -1, 'Cerise', 50),
('Fevrier2021', '-1', -1, '-1', -1, 'Clafoutie', 50),
('Fevrier2021', '-1', -1, '-1', -1, 'Flancs', 50),
('Fevrier2021', '-1', -1, '-1', -1, 'Cake', 56),
('Fevrier2021', '-1', -1, '-1', -1, 'Riz au lait', 83);

-- --------------------------------------------------------

--
-- Structure de la table `menudujour`
--

CREATE TABLE `menudujour` (
  `Date` date NOT NULL,
  `Entree1` varchar(255) NOT NULL,
  `Entree2` varchar(255) NOT NULL,
  `Plat1` varchar(255) NOT NULL,
  `Plat2` varchar(255) NOT NULL,
  `Dessert1` varchar(255) NOT NULL,
  `Dessert2` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `menudujour`
--

INSERT INTO `menudujour` (`Date`, `Entree1`, `Entree2`, `Plat1`, `Plat2`, `Dessert1`, `Dessert2`) VALUES
('2021-02-04', 'Betterave', 'Concombre', 'Lasagne', 'Frite steack', 'Pomme', 'Poire'),
('2021-02-05', 'Melons', 'Concombres à la crème', 'Frites kebab', 'Moules Frites', 'Cerise', 'Clafoutie'),
('2021-02-06', 'Friands', 'Choux rouges', 'Lasagnes', 'Saucisse et flageolets', 'Cake', 'Flancs'),
('2021-02-08', 'Patés', 'Taboulets', 'Riz omelette', 'Rotis de porc et haricot vert', 'Pomme', 'Riz au lait'),
('2021-03-04', 'Saucissons', 'Oeufs dur', 'Ravioli', 'Rotis de porc et haricot vert', 'Poire', 'Yaourt'),
('2021-03-05', 'Macédoines', 'Salades de pâtes', 'Moules Frites', 'Sautés de veaux et polenta', 'Faisselle', 'Banane'),
('2021-03-06', 'Friands', 'Taboulets', 'Merguez frites', 'Saucisse et flageolets', 'Flancs', 'Banane'),
('2021-03-25', 'Concombres à la crème', 'Andives', 'Boeuf Bourgigons et pomme de terre', 'Lasagnes', 'Faisselle', 'Banane'),
('2021-04-01', 'Andives', 'Betterave Vinaigrette', 'Chili con carne et riz', 'Cordon bleu et poêlé de légume', 'Clémentine', 'Orange');

-- --------------------------------------------------------

--
-- Structure de la table `stock`
--

CREATE TABLE `stock` (
  `Aliment` varchar(255) NOT NULL,
  `Quantité` int(11) NOT NULL,
  `QuantitéPrise` int(11) NOT NULL,
  `GachisNull` int(11) NOT NULL,
  `GachisFaible` int(11) NOT NULL,
  `GachisMoyen` int(11) NOT NULL,
  `GachisImportant` int(11) NOT NULL,
  `ProportionGachis` int(11) NOT NULL,
  `NouvelleQuantité` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `stock`
--

INSERT INTO `stock` (`Aliment`, `Quantité`, `QuantitéPrise`, `GachisNull`, `GachisFaible`, `GachisMoyen`, `GachisImportant`, `ProportionGachis`, `NouvelleQuantité`) VALUES
('Andives', 100, 1, 1, 0, 0, 0, 0, 11),
('Boeuf Bourgigons et pomme de terre', 100, 1, 0, 1, 0, 0, 17, 11),
('Banane', 100, 3, 0, 2, 1, 0, 28, 12),
('Betterave Vinaigrette', 100, 1, 1, 0, 0, 0, 0, 11),
('Chili con carne et riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Cake', 100, 5, 0, 1, 2, 2, 56, 12),
('Carottes rapées vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Cordon bleu et poêlé de légume', 100, 2, 0, 1, 1, 0, 33, 11),
('Carré de chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Celerys rémoulades', 100, 0, 0, 0, 0, 0, 0, 10),
('Cuisses de poulets et pomme de terre sautées', 100, 0, 0, 0, 0, 0, 0, 10),
('Cerise', 100, 3, 0, 1, 1, 1, 50, 12),
('Choux rouges', 100, 8, 0, 2, 2, 4, 58, 13),
('Filet de colin et gratin de brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Clafoutie', 100, 4, 0, 1, 2, 1, 50, 12),
('Concombres à la crème', 100, 6, 0, 4, 1, 1, 33, 14),
('Frites kebab', 100, 5, 0, 2, 2, 1, 43, 13),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Concombres vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Hachie parmentier de poisson', 100, 0, 0, 0, 0, 0, 0, 10),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Friands', 100, 4, 0, 3, 1, 1, 34, 13),
('Lasagnes', 100, 5, 0, 0, 5, 0, 50, 13),
('Eclaire', 100, 0, 0, 0, 0, 0, 0, 10),
('Macédoines', 100, 5, 0, 4, 1, 0, 24, 14),
('Merguez frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Faisselle', 100, 6, 0, 3, 2, 1, 39, 14),
('Melons', 100, 2, 0, 1, 1, 1, 50, 11),
('Moules Frites', 100, 5, 0, 3, 2, 2, 43, 13),
('Flancs', 100, 7, 0, 2, 3, 2, 50, 14),
('Morceau Quiche', 100, 0, 0, 0, 0, 0, 0, 10),
('Omelette épinard', 100, 0, 0, 0, 0, 0, 0, 10),
('Fromage blanc', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Flammenkueches', 100, 0, 0, 0, 0, 0, 0, 10),
('Pâtes bolognaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Gâteau', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Pizza', 100, 0, 0, 0, 0, 0, 0, 10),
('Paupiettes de veaux et poêlés de légumes', 100, 0, 0, 0, 0, 0, 0, 10),
('Glace', 100, 0, 0, 0, 0, 0, 0, 10),
('Oeufs dur', 100, 6, 0, 3, 2, 1, 39, 14),
('Pavé de saumon et brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Ile flottante', 100, 0, 0, 0, 0, 0, 0, 10),
('Patés', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulet rotis et gratin de chou-fleur', 100, 0, 0, 0, 0, 0, 0, 10),
('Kiwi', 100, 0, 0, 0, 0, 0, 0, 10),
('Piémontaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulets rotis et petit poids', 100, 0, 0, 0, 0, 0, 0, 10),
('Mille feuille', 100, 0, 0, 0, 0, 0, 0, 10),
('Potage', 100, 0, 0, 0, 0, 0, 0, 10),
('Purée et Saucisses', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau de Tarte', 100, 0, 0, 0, 0, 0, 0, 10),
('Radis au beurre', 100, 0, 0, 0, 0, 0, 0, 10),
('Ragout de boeuf et Pâtes', 100, 0, 0, 0, 0, 0, 0, 10),
('Mousse au chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Ravioli', 100, 3, 0, 2, 1, 0, 28, 12),
('Nectarine', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade croutons', 100, 0, 0, 0, 0, 0, 0, 10),
('Riz et poissons pannés', 100, 0, 0, 0, 0, 0, 0, 10),
('Orange', 100, 1, 0, 0, 0, 1, 83, 10),
('Salades de pâtes', 100, 3, 0, 1, 1, 1, 50, 12),
('Riz omelette', 100, 1, 0, 1, 0, 0, 17, 11),
('Pamplemouse', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de quinoa', 100, 0, 0, 0, 0, 0, 0, 10),
('Rotis de porc et haricot vert', 100, 4, 0, 2, 2, 0, 33, 13),
('Pêche', 100, 0, 0, 0, 0, 0, 0, 10),
('Saucissons', 100, 1, 0, 1, 0, 0, 17, 11),
('Saucisse et flageolets', 100, 7, 0, 2, 4, 1, 45, 14),
('Poire', 100, 3, 0, 2, 0, 1, 39, 12),
('Taboulets', 100, 1, 0, 0, 1, 0, 50, 11),
('Sauté de poulets et courgettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Pomme', 100, 0, 0, 0, 0, 0, 0, 10),
('Tomates Maïs', 100, 0, 0, 0, 0, 0, 0, 10),
('Sautés de veaux et polenta', 100, 5, 0, 1, 3, 1, 50, 13),
('Riz au lait', 100, 1, 0, 0, 0, 1, 83, 10),
('Tomates vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Steack frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de fruits', 100, 0, 0, 0, 0, 0, 0, 10),
('Veloutés', 100, 0, 0, 0, 0, 0, 0, 10),
('Tartiflettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Yaourt', 100, 4, 0, 2, 0, 2, 50, 12),
('Andives', 100, 1, 1, 0, 0, 0, 0, 11),
('Boeuf Bourgigons et pomme de terre', 100, 1, 0, 1, 0, 0, 17, 11),
('Banane', 100, 3, 0, 2, 1, 0, 28, 12),
('Betterave Vinaigrette', 100, 1, 1, 0, 0, 0, 0, 11),
('Chili con carne et riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Cake', 100, 5, 0, 1, 2, 2, 56, 12),
('Carottes rapées vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Cordon bleu et poêlé de légume', 100, 2, 0, 1, 1, 0, 33, 11),
('Carré de chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Celerys rémoulades', 100, 0, 0, 0, 0, 0, 0, 10),
('Cuisses de poulets et pomme de terre sautées', 100, 0, 0, 0, 0, 0, 0, 10),
('Cerise', 100, 3, 0, 1, 1, 1, 50, 12),
('Choux rouges', 100, 8, 0, 2, 2, 4, 58, 13),
('Filet de colin et gratin de brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Clafoutie', 100, 4, 0, 1, 2, 1, 50, 12),
('Concombres à la crème', 100, 6, 0, 4, 1, 1, 33, 14),
('Frites kebab', 100, 5, 0, 2, 2, 1, 43, 13),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Concombres vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Hachie parmentier de poisson', 100, 0, 0, 0, 0, 0, 0, 10),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Friands', 100, 4, 0, 3, 0, 1, 34, 13),
('Lasagnes', 100, 5, 0, 0, 5, 0, 50, 13),
('Eclaire', 100, 0, 0, 0, 0, 0, 0, 10),
('Macédoines', 100, 5, 0, 4, 1, 0, 24, 14),
('Merguez frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Faisselle', 100, 6, 0, 3, 2, 1, 39, 14),
('Melons', 100, 2, 0, 1, 0, 1, 50, 11),
('Moules Frites', 100, 5, 0, 3, 0, 2, 43, 13),
('Flancs', 100, 7, 0, 2, 3, 2, 50, 14),
('Morceau Quiche', 100, 0, 0, 0, 0, 0, 0, 10),
('Omelette épinard', 100, 0, 0, 0, 0, 0, 0, 10),
('Fromage blanc', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Flammenkueches', 100, 0, 0, 0, 0, 0, 0, 10),
('Pâtes bolognaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Gâteau', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Pizza', 100, 0, 0, 0, 0, 0, 0, 10),
('Paupiettes de veaux et poêlés de légumes', 100, 0, 0, 0, 0, 0, 0, 10),
('Glace', 100, 0, 0, 0, 0, 0, 0, 10),
('Oeufs dur', 100, 6, 0, 3, 2, 1, 39, 14),
('Pavé de saumon et brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Ile flottante', 100, 0, 0, 0, 0, 0, 0, 10),
('Patés', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulet rotis et gratin de chou-fleur', 100, 0, 0, 0, 0, 0, 0, 10),
('Kiwi', 100, 0, 0, 0, 0, 0, 0, 10),
('Piémontaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulets rotis et petit poids', 100, 0, 0, 0, 0, 0, 0, 10),
('Mille feuille', 100, 0, 0, 0, 0, 0, 0, 10),
('Potage', 100, 0, 0, 0, 0, 0, 0, 10),
('Purée et Saucisses', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau de Tarte', 100, 0, 0, 0, 0, 0, 0, 10),
('Radis au beurre', 100, 0, 0, 0, 0, 0, 0, 10),
('Ragout de boeuf et Pâtes', 100, 0, 0, 0, 0, 0, 0, 10),
('Mousse au chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Ravioli', 100, 3, 0, 2, 1, 0, 28, 12),
('Nectarine', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade croutons', 100, 0, 0, 0, 0, 0, 0, 10),
('Riz et poissons pannés', 100, 0, 0, 0, 0, 0, 0, 10),
('Orange', 100, 1, 0, 0, 0, 1, 83, 10),
('Salades de pâtes', 100, 3, 0, 1, 1, 1, 50, 12),
('Riz omelette', 100, 1, 0, 1, 0, 0, 17, 11),
('Pamplemouse', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de quinoa', 100, 0, 0, 0, 0, 0, 0, 10),
('Rotis de porc et haricot vert', 100, 4, 0, 2, 2, 0, 33, 13),
('Pêche', 100, 0, 0, 0, 0, 0, 0, 10),
('Saucissons', 100, 1, 0, 1, 0, 0, 17, 11),
('Saucisse et flageolets', 100, 7, 0, 2, 4, 1, 45, 14),
('Poire', 100, 3, 0, 2, 0, 1, 39, 12),
('Taboulets', 100, 1, 0, 0, 1, 0, 50, 11),
('Sauté de poulets et courgettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Pomme', 100, 0, 0, 0, 0, 0, 0, 10),
('Tomates Maïs', 100, 0, 0, 0, 0, 0, 0, 10),
('Sautés de veaux et polenta', 100, 5, 0, 1, 3, 1, 50, 13),
('Riz au lait', 100, 1, 0, 0, 0, 1, 83, 10),
('Tomates vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Steack frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de fruits', 100, 0, 0, 0, 0, 0, 0, 10),
('Veloutés', 100, 0, 0, 0, 0, 0, 0, 10),
('Tartiflettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Yaourt', 100, 4, 0, 2, 0, 2, 50, 12),
('Andives', 100, 1, 1, 0, 0, 0, 0, 11),
('Boeuf Bourgigons et pomme de terre', 100, 1, 0, 1, 0, 0, 17, 11),
('Banane', 100, 3, 0, 2, 1, 0, 28, 12),
('Betterave Vinaigrette', 100, 1, 1, 0, 0, 0, 0, 11),
('Chili con carne et riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Cake', 100, 5, 0, 1, 2, 2, 56, 12),
('Carottes rapées vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Cordon bleu et poêlé de légume', 100, 2, 0, 1, 1, 0, 33, 11),
('Carré de chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Celerys rémoulades', 100, 0, 0, 0, 0, 0, 0, 10),
('Cuisses de poulets et pomme de terre sautées', 100, 0, 0, 0, 0, 0, 0, 10),
('Cerise', 100, 3, 0, 1, 1, 1, 50, 12),
('Choux rouges', 100, 8, 0, 2, 2, 4, 58, 13),
('Filet de colin et gratin de brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Clafoutie', 100, 4, 0, 1, 2, 1, 50, 12),
('Concombres à la crème', 100, 6, 0, 4, 1, 1, 33, 14),
('Frites kebab', 100, 5, 0, 2, 2, 1, 43, 13),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Concombres vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Hachie parmentier de poisson', 100, 0, 0, 0, 0, 0, 0, 10),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Friands', 100, 4, 0, 3, 0, 1, 34, 13),
('Lasagnes', 100, 5, 0, 0, 5, 0, 50, 13),
('Eclaire', 100, 0, 0, 0, 0, 0, 0, 10),
('Macédoines', 100, 5, 0, 4, 1, 0, 24, 14),
('Merguez frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Faisselle', 100, 6, 0, 3, 2, 1, 39, 14),
('Melons', 100, 2, 0, 1, 0, 1, 50, 11),
('Moules Frites', 100, 5, 0, 3, 0, 2, 43, 13),
('Flancs', 100, 7, 0, 2, 3, 2, 50, 14),
('Morceau Quiche', 100, 0, 0, 0, 0, 0, 0, 10),
('Omelette épinard', 100, 0, 0, 0, 0, 0, 0, 10),
('Fromage blanc', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Flammenkueches', 100, 0, 0, 0, 0, 0, 0, 10),
('Pâtes bolognaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Gâteau', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Pizza', 100, 0, 0, 0, 0, 0, 0, 10),
('Paupiettes de veaux et poêlés de légumes', 100, 0, 0, 0, 0, 0, 0, 10),
('Glace', 100, 0, 0, 0, 0, 0, 0, 10),
('Oeufs dur', 100, 6, 0, 3, 2, 1, 39, 14),
('Pavé de saumon et brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Ile flottante', 100, 0, 0, 0, 0, 0, 0, 10),
('Patés', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulet rotis et gratin de chou-fleur', 100, 0, 0, 0, 0, 0, 0, 10),
('Kiwi', 100, 0, 0, 0, 0, 0, 0, 10),
('Piémontaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulets rotis et petit poids', 100, 0, 0, 0, 0, 0, 0, 10),
('Mille feuille', 100, 0, 0, 0, 0, 0, 0, 10),
('Potage', 100, 0, 0, 0, 0, 0, 0, 10),
('Purée et Saucisses', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau de Tarte', 100, 0, 0, 0, 0, 0, 0, 10),
('Radis au beurre', 100, 0, 0, 0, 0, 0, 0, 10),
('Ragout de boeuf et Pâtes', 100, 0, 0, 0, 0, 0, 0, 10),
('Mousse au chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Ravioli', 100, 3, 0, 2, 1, 0, 28, 12),
('Nectarine', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade croutons', 100, 0, 0, 0, 0, 0, 0, 10),
('Riz et poissons pannés', 100, 0, 0, 0, 0, 0, 0, 10),
('Orange', 100, 1, 0, 0, 0, 1, 83, 10),
('Salades de pâtes', 100, 3, 0, 1, 1, 1, 50, 12),
('Riz omelette', 100, 1, 0, 1, 0, 0, 17, 11),
('Pamplemouse', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de quinoa', 100, 0, 0, 0, 0, 0, 0, 10),
('Rotis de porc et haricot vert', 100, 4, 0, 2, 2, 0, 33, 13),
('Pêche', 100, 0, 0, 0, 0, 0, 0, 10),
('Saucissons', 100, 1, 0, 1, 0, 0, 17, 11),
('Saucisse et flageolets', 100, 7, 0, 2, 4, 1, 45, 14),
('Poire', 100, 3, 0, 2, 0, 1, 39, 12),
('Taboulets', 100, 1, 0, 0, 1, 0, 50, 11),
('Sauté de poulets et courgettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Pomme', 100, 0, 0, 0, 0, 0, 0, 10),
('Tomates Maïs', 100, 0, 0, 0, 0, 0, 0, 10),
('Sautés de veaux et polenta', 100, 5, 0, 1, 3, 1, 50, 13),
('Riz au lait', 100, 1, 0, 0, 0, 1, 83, 10),
('Tomates vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Steack frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de fruits', 100, 0, 0, 0, 0, 0, 0, 10),
('Veloutés', 100, 0, 0, 0, 0, 0, 0, 10),
('Tartiflettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Yaourt', 100, 4, 0, 2, 0, 2, 50, 12),
('Andives', 100, 1, 1, 0, 0, 0, 0, 11),
('Boeuf Bourgigons et pomme de terre', 100, 1, 0, 1, 0, 0, 17, 11),
('Banane', 100, 3, 0, 2, 1, 0, 28, 12),
('Betterave Vinaigrette', 100, 1, 1, 0, 0, 0, 0, 11),
('Chili con carne et riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Cake', 100, 5, 0, 1, 2, 2, 56, 12),
('Carottes rapées vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Cordon bleu et poêlé de légume', 100, 2, 0, 1, 1, 0, 33, 11),
('Carré de chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Celerys rémoulades', 100, 0, 0, 0, 0, 0, 0, 10),
('Cuisses de poulets et pomme de terre sautées', 100, 0, 0, 0, 0, 0, 0, 10),
('Cerise', 100, 3, 0, 1, 1, 1, 50, 12),
('Choux rouges', 100, 8, 0, 2, 2, 4, 58, 13),
('Filet de colin et gratin de brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Clafoutie', 100, 4, 0, 1, 2, 1, 50, 12),
('Concombres à la crème', 100, 6, 0, 4, 1, 1, 33, 14),
('Frites kebab', 100, 5, 0, 2, 2, 1, 43, 13),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Concombres vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Hachie parmentier de poisson', 100, 0, 0, 0, 0, 0, 0, 10),
('Clémentine', 100, 1, 0, 1, 0, 0, 17, 11),
('Friands', 100, 4, 0, 3, 0, 1, 34, 13),
('Lasagnes', 100, 5, 0, 0, 5, 0, 50, 13),
('Eclaire', 100, 0, 0, 0, 0, 0, 0, 10),
('Macédoines', 100, 5, 0, 4, 1, 0, 24, 14),
('Merguez frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Faisselle', 100, 6, 0, 3, 2, 1, 39, 14),
('Melons', 100, 2, 0, 1, 0, 1, 50, 11),
('Moules Frites', 100, 5, 0, 3, 0, 2, 43, 13),
('Flancs', 100, 7, 0, 2, 3, 2, 50, 14),
('Morceau Quiche', 100, 0, 0, 0, 0, 0, 0, 10),
('Omelette épinard', 100, 0, 0, 0, 0, 0, 0, 10),
('Fromage blanc', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Flammenkueches', 100, 0, 0, 0, 0, 0, 0, 10),
('Pâtes bolognaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Gâteau', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau Pizza', 100, 0, 0, 0, 0, 0, 0, 10),
('Paupiettes de veaux et poêlés de légumes', 100, 0, 0, 0, 0, 0, 0, 10),
('Glace', 100, 0, 0, 0, 0, 0, 0, 10),
('Oeufs dur', 100, 6, 0, 3, 2, 1, 39, 14),
('Pavé de saumon et brocolis', 100, 0, 0, 0, 0, 0, 0, 10),
('Ile flottante', 100, 0, 0, 0, 0, 0, 0, 10),
('Patés', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulet rotis et gratin de chou-fleur', 100, 0, 0, 0, 0, 0, 0, 10),
('Kiwi', 100, 0, 0, 0, 0, 0, 0, 10),
('Piémontaise', 100, 0, 0, 0, 0, 0, 0, 10),
('Poulets rotis et petit poids', 100, 0, 0, 0, 0, 0, 0, 10),
('Mille feuille', 100, 0, 0, 0, 0, 0, 0, 10),
('Potage', 100, 0, 0, 0, 0, 0, 0, 10),
('Purée et Saucisses', 100, 0, 0, 0, 0, 0, 0, 10),
('Morceau de Tarte', 100, 0, 0, 0, 0, 0, 0, 10),
('Radis au beurre', 100, 0, 0, 0, 0, 0, 0, 10),
('Ragout de boeuf et Pâtes', 100, 0, 0, 0, 0, 0, 0, 10),
('Mousse au chocolat', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de riz', 100, 0, 0, 0, 0, 0, 0, 10),
('Ravioli', 100, 3, 0, 2, 1, 0, 28, 12),
('Nectarine', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade croutons', 100, 0, 0, 0, 0, 0, 0, 10),
('Riz et poissons pannés', 100, 0, 0, 0, 0, 0, 0, 10),
('Orange', 100, 1, 0, 0, 0, 1, 83, 10),
('Salades de pâtes', 100, 3, 0, 1, 1, 1, 50, 12),
('Riz omelette', 100, 1, 0, 1, 0, 0, 17, 11),
('Pamplemouse', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de quinoa', 100, 0, 0, 0, 0, 0, 0, 10),
('Rotis de porc et haricot vert', 100, 4, 0, 2, 2, 0, 33, 13),
('Pêche', 100, 0, 0, 0, 0, 0, 0, 10),
('Saucissons', 100, 1, 0, 1, 0, 0, 17, 11),
('Saucisse et flageolets', 100, 7, 0, 2, 4, 1, 45, 14),
('Poire', 100, 3, 0, 2, 0, 1, 39, 12),
('Taboulets', 100, 1, 0, 0, 1, 0, 50, 11),
('Sauté de poulets et courgettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Pomme', 100, 0, 0, 0, 0, 0, 0, 10),
('Tomates Maïs', 100, 0, 0, 0, 0, 0, 0, 10),
('Sautés de veaux et polenta', 100, 5, 0, 1, 3, 1, 50, 13),
('Riz au lait', 100, 1, 0, 0, 0, 1, 83, 10),
('Tomates vinaigrettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Steack frites', 100, 0, 0, 0, 0, 0, 0, 10),
('Salade de fruits', 100, 0, 0, 0, 0, 0, 0, 10),
('Veloutés', 100, 0, 0, 0, 0, 0, 0, 10),
('Tartiflettes', 100, 0, 0, 0, 0, 0, 0, 10),
('Yaourt', 100, 4, 0, 2, 0, 2, 50, 12);

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `ID` int(11) NOT NULL,
  `Pseudo` varchar(255) NOT NULL,
  `mdp` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`ID`, `Pseudo`, `mdp`) VALUES
(1, 'Admin', 'Admin'),
(2, 'Lambda', 'Lambda');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
