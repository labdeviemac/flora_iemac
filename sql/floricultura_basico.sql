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
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT, -- f[0]
  `especie` varchar(80), -- f[1]
  `tipo_adubo` varchar(50), -- f[2]
  `tempo_vida` int, -- f[3]
  `intervalo_agua` int, -- f[4]
  `observacoes_especie` tinytext,  -- f[5]
  `fornecedor` int  -- f[6]
);

CREATE TABLE `fornecedor` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT, -- f[7]
  `razao_social` varchar(150), -- f[8]
  `nome_fantasia` varchar(150), -- f[9]
  `cnpj` varchar(60), -- f[10]
  `telefone` int -- f[11]
);

CREATE TABLE `categoria` (
  `id` int PRIMARY KEY NOT NULL AUTO_INCREMENT, -- f[0]
  `descricao_categoria` varchar(120) -- f[1]
);

ALTER TABLE `flores` ADD FOREIGN KEY (`especie`) REFERENCES `especie` (`id`);

ALTER TABLE `flores` ADD FOREIGN KEY (`categoria`) REFERENCES `categoria` (`id`);

ALTER TABLE `especie` ADD FOREIGN KEY (`fornecedor`) REFERENCES `fornecedor` (`id`);