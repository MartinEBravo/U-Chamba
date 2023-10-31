-- ############################# --
-- ###      INTEGRANTES      ### --   
-- ############################# --
-- ###      Martín Bravo     ### --
-- ###    Franco González    ### --
-- ###      Iván Vidal       ### --
-- ############################# --


-- ############################# --
-- ###       Entidades       ### --
-- ############################# --

-- Tabla de Postulantes
CREATE TABLE uchamba.Postulante (
    rut varchar (255) primary key,
    nombre varchar (255) not null,
    telefono varchar (255) not null,
    email varchar (255) not null,
    genero varchar (255) not null,
    edad integer not null,
);

-- Tabla de Universidades
CREATE TABLE uchamba.Universidad (
    nombre varchar (255) primary key,
    tipo varchar (255) not null,
    año integer not null,
    estudiantes integer not null,
    region varchar (255) not null,
    acreditacion varchar (255) not null,
    academicos integer not null,
    ranking integer not null,
    infraestructura integer not null,
);

-- Tabla de Compañias
CREATE TABLE uchamba.Compañia (
    nombre varchar (255) primary key,
    direccion varchar (255) not null,
);

-- Tabla de Países
CREATE TABLE uchamba.Pais (
    nombre varchar (255) primary key,
    pib integer not null,
    poblacion integer not null,
    esperanza_vida integer not null,
);

-- ############################# --
-- ###   Entidades Débiles   ### --
-- ############################# -- 

-- Tabla de Ofertas de Trabajo
CREATE TABLE uchamba.OfertasTrabajo (
    nombre_compañia varchar (255) not null,
    id_oferta integer not null,
    modalidad varchar (255) not null,
    formato varchar (255) not null,
    sueldo integer not null,
    primary key (nombre_compañia, id_oferta),
    foreign key (nombre_compañia) references uchamba.Compañia(nombre)
);

-- ############################# --
-- ###      Relaciones       ### --
-- ############################# --

-- Tabla de Estudia en
CREATE TABLE uchamba.Estudia_en (
    nombreUniversidad varchar (255) not null,
    rut varchar (255) not null,
    carrera varchar (255) not null,
    año integer not null,
    sector varchar (255) not null,
    primary key (nombreUniversidad, rut),
    foreign key (nombreUniversidad) references uchamba.Universidad(nombre),
    foreign key (rut) references uchamba.Postulante(rut)
);

-- Tabla de Postula
CREATE TABLE uchamba.Postula (
    idOferta integer not null,
    rut varchar (255) not null,
    nombre_compañia varchar (255) not null,
    nombre_pais varchar (255) not null,
    primary key (idOferta, rut, nombre_compañia, nombre_pais),
    foreign key (idOferta) references uchamba.OfertasTrabajo(id_oferta),
    foreign key (rut) references uchamba.Postulante(rut),
    foreign key (nombre_compañia) references uchamba.Compañia(nombre),
    foreign key (nombre_pais) references uchamba.Pais(nombre)
);

-- Tabla de Ubicado
CREATE TABLE uchamba.Ubicado (
    nombre_compañia varchar (255) not null,
    nombre_pais varchar (255) not null,
    ciudad varchar (255) not null,
    primary key (nombre_compañia, nombre_pais),
    foreign key (nombre_compañia) references uchamba.Compañia(nombre),
    foreign key (nombre_pais) references uchamba.Pais(nombre)
);
