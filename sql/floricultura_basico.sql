CREATE DATABASE `flora_iemac`;
USE `flora_iemac`;

CREATE TABLE `flores` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `descricao` varchar(80),
  `quantidade` int,
  `valor_unit` double,
  `valor_buque` double,
  `especie` int,
  `categoria` int NOT NULL
);

CREATE TABLE `especie` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `especie` varchar(80),
  `tipo_adubo` varchar(50),
  `tempo_vida` int,
  `intervalo_agua` int,
  `observacoes_especie` tinytext,
  `fornecedor` int
);

CREATE TABLE `fornecedor` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `razao_social` varchar(150),
  `nome_fantasia` varchar(150),
  `cnpj` varchar(60),
  `telefone` int
);

CREATE TABLE `categoria` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `descricao_categoria` varchar(120)
);

ALTER TABLE `flores` ADD FOREIGN KEY (`especie`) REFERENCES `especie` (`id`);

ALTER TABLE `flores` ADD FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id`);

ALTER TABLE `especie` ADD FOREIGN KEY (`fornecedor`) REFERENCES `fornecedor` (`id`);
