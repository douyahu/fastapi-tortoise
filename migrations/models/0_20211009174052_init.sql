-- upgrade --
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(20) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `User` (
    `id` CHAR(36) NOT NULL  PRIMARY KEY,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `hashed_password` VARCHAR(255) NOT NULL,
    `is_active` BOOL NOT NULL  DEFAULT 1,
    `is_superuser` BOOL NOT NULL  DEFAULT 0,
    `is_verified` BOOL NOT NULL  DEFAULT 0,
    KEY `idx_User_email_ba10f8` (`email`)
) CHARACTER SET utf8mb4;
