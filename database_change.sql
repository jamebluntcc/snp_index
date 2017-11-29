DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(80) NOT NULL,
  `password` VARCHAR(100) NOT NULL,
  `email` VARCHAR(50) DEFAULT NULL,
  `create_at` DATETIME NOT NULL,
  `is_active` VARCHAR(1) DEFAULT 'N',
  `is_admin` VARCHAR(1) DEFAULT 'N',
  `snp_table` VARCHAR(200) DEFAULT NULL,
  `expr_table` VARCHAR(200) DEFAULT NULL,
  `locus_table` VARCHAR(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


/*
DROP TABLE IF EXISTS `link_table`;
CREATE TABLE `link_table`(
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user` VARCHAR(80) NOT NULL,
  `snp_table` VARCHAR(50) DEFAULT NULL,
  `expr_table` VARCHAR(50) DEFAULT NULL,
  `locus_table` VARCHAR(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
*/