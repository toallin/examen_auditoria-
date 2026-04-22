# ================================
# IMPORTACIONES
# ================================
from openai import OpenAI
from flask import Flask, send_from_directory, request, jsonify
import re

# ================================
# CONFIGURACIÓN APP
# ================================
app = Flask(__name__)

# ================================
# SERVIR FRONTEND (React build)
# ================================
@app.route('/', methods=["GET"])
def serve_index():
    # Devuelve el index.html generado en /dist
    return send_from_directory('dist', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    # Sirve archivos estáticos (JS, CSS, etc.)
    return send_from_directory('dist', path)

# ================================
# CONFIGURACIÓN IA (OLLAMA LOCAL)
# ================================
client = OpenAI(
    base_url='http://localhost:11434/v1',  # Ollama local
    api_key='ollama'  # requerido pero no usado
)

# ================================
# ENDPOINT: ANALIZAR RIESGOS
# ================================
@app.route('/analizar-riesgos', methods=['POST'])
def analizar_riesgos():
    """
    Recibe un activo y devuelve:
    - Lista de riesgos
    - Lista de impactos
    """

    data = request.get_json()
    activo = data.get('activo')

    if not activo:
        return jsonify({"error": "El campo 'activo' es obligatorio"}), 400

    riesgos, impactos = obtener_riesgos(activo)

    return jsonify({
        "activo": activo,
        "riesgos": riesgos,
        "impactos": impactos
    })

# ================================
# ENDPOINT: GENERAR TRATAMIENTO
# ================================
@app.route('/sugerir-tratamiento', methods=['POST'])
def sugerir_tratamiento():
    """
    Recibe:
    - activo
    - riesgo
    - impacto

    Devuelve:
    - tratamiento recomendado por IA
    """

    data = request.get_json()
    activo = data.get('activo')
    riesgo = data.get('riesgo')
    impacto = data.get('impacto')

    # Validación
    if not activo or not riesgo or not impacto:
        return jsonify({
            "error": "Los campos 'activo', 'riesgo' e 'impacto' son obligatorios"
        }), 400

    entrada = f"{activo};{riesgo};{impacto}"
    tratamiento = obtener_tratamiento(entrada)

    return jsonify({
        "activo": activo,
        "riesgo": riesgo,
        "impacto": impacto,
        "tratamiento": tratamiento
    })

# ================================
# FUNCIÓN: GENERAR TRATAMIENTO IA
# ================================
def obtener_tratamiento(entrada):
    """
    Genera tratamiento basado en ISO 27001 usando IA
    """

    response = client.chat.completions.create(
        model="ramiro:instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un auditor de seguridad bancaria experto en ISO 27001. "
                    "Genera un tratamiento claro, concreto y aplicable en máximo 200 caracteres."
                )
            },
            {
                "role": "user",
                "content": (
                    "Ejemplo:\n"
                    "Activo: Teléfono móvil\n"
                    "Riesgo: Acceso no autorizado\n"
                    "Impacto: Robo de datos\n"
                )
            },
            {
                "role": "assistant",
                "content": "Implementar autenticación biométrica y cifrado de datos."
            },
            {
                "role": "user",
                "content": entrada
            }
        ]
    )

    return response.choices[0].message.content.strip()

# ================================
# FUNCIÓN: GENERAR RIESGOS
# ================================
def obtener_riesgos(activo):
    """
    Genera 5 riesgos + impactos usando IA
    """

    response = client.chat.completions.create(
        model="ramiro:instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "Eres un auditor de seguridad ISO 27001. "
                    "Genera 5 riesgos con su impacto en formato:\n"
                    "**Riesgo**: impacto"
                )
            },
            {
                "role": "user",
                "content": "Servidor web"
            },
            {
                "role": "assistant",
                "content": """**Acceso no autorizado**: exposición de datos críticos.
**Fallo de hardware**: interrupción del servicio.
**Ataques DDoS**: indisponibilidad del sistema.
**Errores de configuración**: vulnerabilidades explotables.
**Malware**: compromiso del sistema."""
            },
            {
                "role": "user",
                "content": activo
            }
        ]
    )

    answer = response.choices[0].message.content

    # ================================
    # PROCESAMIENTO CON REGEX
    # ================================
    patron = r'\*\*(.+?)\*\*:\s*(.+?)(?:\n|$)'
    resultados = re.findall(patron, answer)

    riesgos = [r[0].strip() for r in resultados]
    impactos = [r[1].strip() for r in resultados]

    return riesgos, impactos

# ================================
# MAIN
# ================================
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)