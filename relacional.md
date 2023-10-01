## Entidades

Postulante(_RUT_, nombre, telefono, correo, genero, edad)


Universidad(_nombre_, tipo, año, estudiantes, región, acreditación, académicos, ranking, infraestructura)


Compañia(_nombre_, dirección)


País(_nombre_, pib, población, esperanza de vida)

## Entidad débil

OfertasTrabajo(_NombreCompañia_, _idOferta_, Modalidad, Formato, Sueldo)

- _NombreCompañia_ REF Compañia(nombre)


## Relaciones

Estudia_en(_nombreUniversidad_, _RUT_, carrera, año, sector)

- _nombreUniversidad_ REF Universidad(nombre)

- _RUT_ REF Postulante(RUT)

Postula(_idOferta_, _RUT_)

- _idOferta_ REF OfertasTrabajo(idOferta)

- _RUT_ REF Postulante(RUT)


Ubicado(_N_compañia_, _N_pais_, ciudad)

- _N_compañia_ REF Compañia(nombre)

- _N_pais_ REF País(nombre)




