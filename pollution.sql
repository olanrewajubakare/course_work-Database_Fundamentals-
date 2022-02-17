-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema population-db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema population-db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `population-db` DEFAULT CHARACTER SET utf8 ;
USE `population-db` ;

-- -----------------------------------------------------
-- Table `population-db`.`stations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `population-db`.`stations` (
  `stationid` INT NOT NULL,
  `location` VARCHAR(48) NOT NULL,
  `geo_point_2d` VARCHAR(40) NOT NULL,
  PRIMARY KEY (`stationid`),
  UNIQUE INDEX `stationid_UNIQUE` (`stationid` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `population-db`.`readings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `population-db`.`readings` (
  `readingid` INT NOT NULL AUTO_INCREMENT,
  `datetime` DATETIME NOT NULL,
  `nox` FLOAT NULL,
  `no2` FLOAT NULL,
  `no` FLOAT NULL,
  `pm10` FLOAT NULL,
  `nvpm10` FLOAT NULL,
  `vpm10` FLOAT NULL,
  `nvpm2.5` FLOAT NULL,
  `pm2.5` FLOAT NULL,
  `vpm2.5` FLOAT NULL,
  `co` FLOAT NULL,
  `o3` FLOAT NULL,
  `so2` FLOAT NULL,
  `temperature` REAL NULL,
  `rh` INT NULL,
  `airpressure` INT NULL,
  `datestart` DATETIME NULL,
  `dateend` DATETIME NULL,
  `current` TEXT NULL,
  `instrumenttype` VARCHAR(32) NULL,
  `stationid` INT NOT NULL,
  PRIMARY KEY (`readingid`),
  UNIQUE INDEX `readingid_UNIQUE` (`readingid` ASC),
  INDEX `stationid_idx` (`stationid` ASC),
  CONSTRAINT `stationid`
    FOREIGN KEY (`stationid`)
    REFERENCES `population-db`.`stations` (`stationid`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `population-db`.`schema`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `population-db`.`schema` (
  `measure` VARCHAR(32) NOT NULL,
  `description` VARCHAR(80) NOT NULL,
  `unit` VARCHAR(24) NOT NULL,
  PRIMARY KEY (`measure`),
  UNIQUE INDEX `measure_UNIQUE` (`measure` ASC),
  UNIQUE INDEX `description_UNIQUE` (`description` ASC))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
