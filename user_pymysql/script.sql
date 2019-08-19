CREATE DATABASE IF NOT EXISTS flask_test;

USE flask_test;

CREATE TABLE users (
    id bigint(20) NOT NULL AUTO_INCREMENT,
    name varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
    email varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
    password varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;