CREATE DATABASE IF NOT EXISTS flask_test;

USE flask_test;

CREATE TABLE books (
    id bigint(20) NOT NULL AUTO_INCREMENT,
    title varchar(45) COLLATE utf8_unicode_ci NOT NULL,
    author varchar(45) COLLATE utf8_unicode_ci NOT NULL,
    genres varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;