CREATE DATABASE IF NOT EXISTS paises;

USE paises;

CREATE TABLE IF NOT EXISTS countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    poblacion INT NOT NULL
);

INSERT INTO countries (nombre, poblacion) VALUES
('Argentina', 45195777),
('Brazil', 212559417),
('Chile', 19116201),
('Colombia', 50882891),
('Mexico', 128932753);
