# examen_auditoria-
Informe de Auditoría de Sistemas - Examen de la Unidad I

Nombres y apellidos: Quispe Levano Cristian Aldair  
Fecha: 22/04/2026  
URL GitHub: [https://github.com/tuusuario/tu-repositorio](https://github.com/tuusuario/tu-repositorio)

1. Proyecto de Auditoría de Riesgos

**Login**  
Evidencia:  
![Captura del login](capturas/login.png)  
Descripción: El inicio de sesión ficticio se implementó sin base de datos, usando localStorage para almacenar el usuario y el estado de autenticación. Al ingresar credenciales válidas, se habilita el acceso a la aplicación principal y se muestra un mensaje de inicio de sesión exitoso.

**Motor de Inteligencia Artificial**  
Evidencia:  
![Captura del código de IA](capturas/backend.png)  
Descripción: El motor de IA se mejoró con llamadas reales a un backend local. Al agregar un activo se genera automáticamente un perfil de riesgo e impacto, y al presionar el botón de recomendaciones se obtiene un tratamiento alineado con ISO 27001.

2. Hallazgos

**Activo 1: Servidor de base de datos**  
Evidencia:  
![Captura Activo 1](capturas/evidencia(1).png)  
Condición: El servidor de base de datos presenta riesgo de acceso no autorizado y pérdida de confidencialidad por configuraciones inseguras.  
Recomendación: Aplicar controles de acceso estrictos, cifrado en reposo y auditorías periódicas de permisos.  
Riesgo: Probabilidad Alta

**Activo 2: API Transacciones**  
Evidencia:  
![Captura Activo 2](capturas/evidencia(2).png)  
Condición: La API de transacciones es vulnerable a inyección y ataques por validación insuficiente de entradas.  
Recomendación: Implementar validación de entradas, sanitización de datos y uso de HTTPS para todas las comunicaciones.  
Riesgo: Probabilidad Media

**Activo 3: Aplicación Web de Banca**  
Evidencia:  
![Captura Activo 3](capturas/activo3.png)  
Condición: La aplicación web de banca corre riesgo de exposición de datos sensibles debido a falta de cifrado y controles de sesión.  
Recomendación: Forzar HTTPS, proteger sesiones con tokens seguros y aplicar políticas de seguridad de contenido.  
Riesgo: Probabilidad Alta

**Activo 4: Servidor de Correo**  
Evidencia:  
![Captura Activo 4](capturas/activo4.png)  
Condición: El servidor de correo es vulnerable a phishing y distribución de malware si no se aplican filtros y autenticación adecuada.  
Recomendación: Activar filtros antispam, protección SPF/DKIM/DMARC y monitoreo de correos sospechosos.  
Riesgo: Probabilidad Media

**Activo 5: Firewall Perimetral**  
Evidencia:  
![Captura Activo 5](capturas/activo5.png)  
Condición: El firewall perimetral presenta reglas desactualizadas que pueden permitir accesos no autorizados.  
Recomendación: Revisar y actualizar políticas de firewall, bloquear puertos no utilizados y realizar pruebas de penetración.  
Riesgo: Probabilidad Baja
![Captura Activo 5](capturas/codigo(1).png)  
![Captura Activo 5](capturas/codigo(2).png)  
![Captura Activo 5](capturas/codigo(3).png)  
![Captura Activo 5](capturas/codigo(4).png)  


