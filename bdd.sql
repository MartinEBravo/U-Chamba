-- ############################# --
-- ###      INTEGRANTES      ### --   
-- ############################# --
-- ###      Martín Bravo     ### --
-- ###    Franco González    ### --
-- ###      Iván Vidal       ### --
-- ###     Felipe Fierro     ### --
-- ############################# --


-- ############################# --
-- ###       Entidades       ### --
-- ############################# --


-- Tabla Regiones
CREATE TABLE uchamba.Region (
  id              integer      primary key,
  nombre          varchar(255) not null,
  pib             bigint,
  esperanza_vida  integer
);

-- Tabla Comunas
CREATE TABLE uchamba.Comuna (
  id        integer      primary key,
  nombre    varchar(255) not null,
  region_id integer      not null,

  foreign key (region_id) REFERENCES uchamba.Region(id)
);

-- Tabla de Postulantes
CREATE TABLE uchamba.Postulante (
    rut      varchar (12)  primary key,
    nombre   varchar (255) not null,
    telefono varchar (255) not null,
    email    varchar (255) not null,
    genero   varchar (255) not null,
    edad     integer       not null,

    CONSTRAINT genero_valido CHECK (genero IN ('Hombre', 'Mujer'))
);

-- Tabla de Universidades
CREATE TABLE uchamba.Universidad (
    nombre          varchar (255) primary key,
    tipo            varchar (255) not null,
    anho            integer       not null,
    estudiantes     integer       not null,
    acreditacion    varchar (255) not null,
    academicos      integer       not null,
    ranking         integer       not null,
    infraestructura integer       not null
);

-- Tabla de Compañias
CREATE TABLE uchamba.Companhia (
    rut       varchar (12)  primary key,
    nombre    varchar (255) not null,
    registro  varchar (10),
    capital   bigint
);


-- ############################# --
-- ###   Entidades Débiles   ### --
-- ############################# -- 

-- Tabla de Ofertas de Trabajo
CREATE TABLE uchamba.OfertasTrabajo (
    id         integer       not null,
    comp_rut   varchar (12)  not null,

    modalidad  varchar (255) not null,
    formato    varchar (255) not null,
    sueldo     integer       not null,

    primary key (id, comp_rut),

    foreign key (comp_rut) references uchamba.Companhia(rut)
);

-- ############################# --
-- ###      Relaciones       ### --
-- ############################# --

-- Tabla de Estudia en
CREATE TABLE uchamba.Estudia_en (
    uni_nombre varchar (255) not null,
    post_rut   varchar (12)  not null,

    carrera  varchar (255) not null,
    anho     integer       not null,
    sector   varchar (255) not null,

    primary key (uni_nombre, post_rut),

    foreign key (uni_nombre) references uchamba.Universidad(nombre),
    foreign key (post_rut)   references uchamba.Postulante(rut)
);

-- Tabla de Postula
CREATE TABLE uchamba.Postula (
    oferta_id integer       not null,
    comp_rut  varchar (12) not null,
    post_rut  varchar (12) not null,
    comuna_id integer       not null,

    primary key (oferta_id, comp_rut, post_rut, comuna_id),

    foreign key (oferta_id, comp_rut) references uchamba.OfertasTrabajo(id, comp_rut),
    foreign key (post_rut)            references uchamba.Postulante(rut),
    foreign key (comuna_id)           references uchamba.Comuna(id)
);

-- Tabla de Ubicacion_Compnahia
CREATE TABLE uchamba.Ubicacion_Companhia (
    comp_rut    varchar (12) not null,
    comuna_id   integer      not null,

    primary key (comp_rut, comuna_id),

    foreign key (comp_rut)  references uchamba.Companhia(rut),
    foreign key (comuna_id) references uchamba.Comuna(id)
); 

-- Tabla de Ubicacion_Universidad
CREATE TABLE uchamba.Ubicacion_Universidad (
    uni_nombre  varchar (255) not null,
    region_id   integer       not null,

    primary key (uni_nombre, region_id),

    foreign key (uni_nombre) references uchamba.Universidad(nombre),
    foreign key (region_id)  references uchamba.Region(id)
); 