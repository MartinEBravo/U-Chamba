{\Large \textbf{Entidades}}\\


\textbf{Postulante}(\uline{RUT}: String, nombre: String, telefono: String, correo: String, genero: String, edad: Int)\\


\textbf{Universidad}(\uline{nombre}: String, tipo: String, año: Int, estudiantes: String, región: String, acreditación: Int, académicos: Int, ranking: Int, infraestructura: Int)\\


\textbf{Compañia}(\uline{nombre}: String, dirección: String)\\


\textbf{País}(\uline{nombre}: String, pib: Int, población: Int, esperanza de vida: Int)\\



%%------------------------------
{\Large \textbf{Entidad débil}}\\


\textbf{OfertasTrabajo}(\uline{NombreCompañia}, \uline{idOferta}: Int, Modalidad: String, Formato: String, Sueldo: Int)\\

\quad \uline{NombreCompañia} REF Compañia(nombre)\\


%%------------------------------
{\Large \textbf{Relaciones}}\\


\textbf{Estudia\_en}(\uline{nombreUniversidad}: String, \uline{RUT}: String, carrera: String, año: Int, sector: String)\\

\quad \uline{nombreUniversidad} REF Universidad(\uline{nombre})\\

\quad \uline{RUT} REF Postulante(\uline{RUT})\\


\textbf{Postula}(\uline{idOferta}: Int, \uline{RUT}: String, \uline{nombre\_compañia}: String, \uline{nombre\_país}: String)\\

\quad \uline{idOferta} REF OfertasTrabajo(\uline{idOferta})\\

\quad \uline{RUT} REF Postulante(\uline{RUT})\\

\quad \uline{nombre\_compañia} REF Compañia(\uline{nombre})\\

\quad \uline{nombre\_país} REF País(\uline{nombre})\\


\textbf{Ubicado}(\uline{N\_compañia}: String, \uline{N\_pais}: String, ciudad: String)\\

\quad \uline{N\_compañia} REF Compañia(\uline{nombre})\\

\quad  \uline{N\_pais} REF País(\uline{nombre})\\
