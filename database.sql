CREATE DATABASE chatbot_db;

\c chatbot_db;

CREATE TABLE faq (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO faq (question, answer) VALUES 
('horario', 'Nuestro horario de atención es de lunes a viernes de 9:00 AM a 6:00 PM'),
('contacto', 'Puedes contactarnos al email soporte@empresa.com o al teléfono 123-456-7890'),
('productos', 'Ofrecemos servicios de desarrollo web, aplicaciones móviles y consultoría tecnológica'),
('precios', 'Los precios varían según el proyecto. Contáctanos para una cotización personalizada'),
('ubicacion', 'Estamos ubicados en el centro de la ciudad, disponemos de oficinas virtuales'),
('soporte', 'Nuestro equipo de soporte está disponible 24/7 para ayudarte con cualquier consulta');