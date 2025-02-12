-- Criação da base de dados
CREATE DATABASE IF NOT EXISTS Paises;

-- Seleciona a base de dados
USE Paises;

-- Criação da tabela
CREATE TABLE IF NOT EXISTS Paises_Requisitos (
    id_paises INT AUTO_INCREMENT PRIMARY KEY,
    nome_pais VARCHAR(100) NOT NULL,
    idade_minima INT NOT NULL,
    requisitos TEXT NOT NULL
);

-- Inserção dos dados na tabela
INSERT INTO Paises_Requisitos (nome_pais, idade_minima, requisitos) VALUES
('Alemanha', 18, 'Exame psicológico, testes de aptidão, Treinamento'),
('Argentina', 21, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Brasil', 25, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Colômbia', 18, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Espanha', 18, 'Exame psicológico, Antecedentes criminais, Treinamento, Autorização do Governo'),
('Estados Unidos', 21, 'Antecedentes criminais, Treinamento, Autorização do Governo'),
('França', 18, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Grécia', 18, 'Exame psicológico, Antecedentes criminais'),
('Hungria', 18, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Israel', 21, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Itália', 18, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('México', 18, 'Exame psicológico, Testes de aptidão, treinamento'),
('Peru', 18, 'Processo rigoroso Antecedentes criminais, Autorizacao do Governo'),
('Polônia', 21, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Portugal', 18, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('República Tcheca', 21, 'Exame psicológico, Antecedentes criminais, Treinamento'),
('Romênia', 18, 'Exame psicológico, Antecedentes criminais, curso de segurança'),
('Suécia', 18, 'Exame psicológico, Antecedentes criminais, curso de segurança'),
('Suíça', 18, 'Exame psicológio, Antecedentes criminais, curso de segurança'),
('Venezuela', 18, 'Antecedentes criminais, Treinamento'),
('Venezuela', 18, 'Exame psicológico, Antecedentes criminais, Autorizacao do Governo');

SELECT *FROM paises;
