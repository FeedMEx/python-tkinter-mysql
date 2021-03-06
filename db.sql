
/* Crear estructura de la base de datos */

CREATE DATABASE sistema;
USE sistema;

CREATE TABLE datos_cliente (
            `N` INT AUTO_INCREMENT,
            `ApellidosNombres` VARCHAR(50),
            `IP` VARCHAR(15),
            `Direccion` VARCHAR(30),
            `Telefono` VARCHAR(10),
            `Monto` VARCHAR(10),
            `Megas` VARCHAR(10),
            `FechaInstalacion` VARCHAR(10),
	        `Estado` VARCHAR (10),
            PRIMARY KEY (`N`)
        );

CREATE TABLE pago_mes(
            `N` INT AUTO_INCREMENT,
            `AGE` VARCHAR(10),
            `Mes` VARCHAR(50),
            `Monto` VARCHAR(10),
            `Fecha` VARCHAR(10),
	    `ID` INT,
	     PRIMARY KEY (`N`)
	    
        );

CREATE TABLE IF NOT EXISTS login (
            `N` INT AUTO_INCREMENT,
            `Usuario` VARCHAR(20),
            `Contra` VARCHAR(20),            
            PRIMARY KEY (`N`)
        );

CREATE TABLE datos_historial (
            `N` INT AUTO_INCREMENT,
            `Accion` VARCHAR(20),
            `Fecha` VARCHAR(10),
            `Monto` VARCHAR(10),
            `ID` VARCHAR(10),
            PRIMARY KEY (`N`)
        );

DELIMITER $$
CREATE PROCEDURE registrar_cliente (NP VARCHAR(10), ANP VARCHAR(50), IPP VARCHAR(15),
DirecP VARCHAR(30),TelefP VARCHAR(10), MontoP VARCHAR(10), MegasP VARCHAR(10), FIP VARCHAR(15))
BEGIN
    INSERT INTO datos_cliente VALUES(NP,ANP,IPP,DirecP,TelefP,MontoP,MegasP,FIP,'Activo'); 
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE eliminar_cliente (NP VARCHAR(10))
BEGIN
    DELETE FROM datos_cliente WHERE N=NP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cargar_cliente (NP VARCHAR(10))
BEGIN
    SELECT * FROM datos_cliente WHERE N=NP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_cliente (Orden VARCHAR(10),Formato VARCHAR(10))
BEGIN
    IF Orden='OA' THEN
        SELECT * FROM datos_cliente  WHERE CASE 
            WHEN Formato='All' THEN  Estado='Activo' or Estado='Inactivo'
            WHEN Formato='Deuda' THEN  Estado=Formato
            ELSE Estado=Formato
        END ORDER BY ApellidosNombres;
    ELSE
        SELECT * FROM datos_cliente  WHERE CASE 
            WHEN Formato='All' THEN  Estado='Activo' or Estado='Inactivo'
            WHEN Formato='Deuda' THEN  Estado=Formato
            ELSE Estado=Formato
        END ORDER BY IP;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE actualizar_cliente (NP VARCHAR(10), ANP VARCHAR(50),IPP VARCHAR(15),
DirecP VARCHAR(30), TelefP VARCHAR(10), MontoP VARCHAR(10), MegasP VARCHAR(10),FIP VARCHAR(10))
BEGIN
    UPDATE datos_cliente SET ApellidosNombres=ANP,IP=IPP,Direccion=DirecP,Telefono=TelefP,Monto=MontoP,Megas=MegasP,FechaInstalacion=FIP WHERE N=NP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE actualizar_estado (NP VARCHAR(10),EstadoP VARCHAR(10))
BEGIN
    IF EstadoP='Activo' THEN
        UPDATE datos_cliente SET Estado='Inactivo' WHERE N=NP;
    ELSE
        UPDATE datos_cliente SET Estado='Activo' WHERE N=NP;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE buscar_cliente (CAD VARCHAR(100),Orden VARCHAR(10), Vista VARCHAR(10))
BEGIN
    IF Orden='OA' THEN
        SELECT * FROM datos_cliente  WHERE CASE 
            WHEN Vista='All' THEN  Estado='Activo' or Estado='Inactivo'
            WHEN Vista='Deuda' THEN  Estado=Vista
            ELSE Estado=Vista
        END AND ApellidosNombres LIKE CAD ORDER BY ApellidosNombres;
    ELSE
        SELECT * FROM datos_cliente  WHERE CASE 
            WHEN Vista='All' THEN  Estado='Activo' or Estado='Inactivo'
            WHEN Vista='Deuda' THEN  Estado=Vista
            ELSE Estado=Vista
        END AND ApellidosNombres LIKE CAD ORDER BY IP;
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE relacionar_cliente ()
BEGIN
    SELECT MAX(N) FROM datos_cliente;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cargar_pagomes (IDP VARCHAR(10),AgeP VARCHAR(10),MesP VARCHAR(10))
BEGIN
    SELECT * FROM pago_mes WHERE ID=IDP AND Age=AgeP AND Mes=MesP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cargar_xan (ANP VARCHAR(100))
BEGIN
    SELECT * FROM datos_cliente WHERE ApellidosNombres=ANP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_pagomes (IDP VARCHAR(10))
BEGIN
    SELECT * FROM pago_mes WHERE ID=IDP AND Age=AgeP AND Mes=MesP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE actualizar_pagomes (IDP VARCHAR(10),AgeP VARCHAR(10),MesP VARCHAR(10),MontoP VARCHAR(10), FechaP VARCHAR(10))
BEGIN
    UPDATE pago_mes SET Monto=MontoP,Fecha=FechaP WHERE ID=IDP AND Age=AgeP AND Mes=MesP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE registrar_historial (AccionP VARCHAR(20), FechaP VARCHAR(10), MontoP VARCHAR(10),IDP VARCHAR(10))
BEGIN
    INSERT INTO datos_historial VALUES(null,AccionP,FechaP,MontoP,IDP); 
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE actualizar_historial (NP VARCHAR(10), AccionP VARCHAR(20), FechaP VARCHAR(10), MontoP VARCHAR(10))
BEGIN
    UPDATE datos_historial SET Accion=AccionP,Fecha=FechaP,Monto=MontoP WHERE N=NP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE actualizar_fih (IDP VARCHAR(10), AccionP VARCHAR(20), FechaP VARCHAR(10))
BEGIN
    UPDATE datos_historial SET Fecha=FechaP WHERE ID=IDP AND Accion=AccionP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE eliminar_historial (NP VARCHAR(10))
BEGIN
    DELETE FROM datos_historial WHERE N=NP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE consultar_historial(IDP VARCHAR(10))
BEGIN
    SELECT * FROM datos_historial WHERE ID=IDP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cargar_historial (NP VARCHAR(10))
BEGIN
    SELECT * FROM datos_historial WHERE N=NP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE eliminar_pagomes (IDP VARCHAR(10))
BEGIN
    DELETE FROM pago_mes WHERE ID=IDP;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE registrar_pagomes (AgeP VARCHAR(10), IDP VARCHAR(10))
BEGIN
    INSERT INTO pago_mes VALUES(null,AgeP,'Enero','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Febrero','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Marzo','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Abril','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Mayo','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Junio','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Julio','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Agosto','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Septiembre','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Octubre','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Noviembre','0','00-00-0000',IDP);
    INSERT INTO pago_mes VALUES(null,AgeP,'Diciembre','0','00-00-0000',IDP);
END $$
DELIMITER ;

INSERT INTO login VALUES ('1','admin','');
