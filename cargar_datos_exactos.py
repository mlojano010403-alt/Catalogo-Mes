import os
import django
from django.core.files import File

# 1. Configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carpinteria_project.settings')
django.setup()

from catalogo.models import Producto

# 2. Tu lista exacta de productos (Convertida a Python)
PRODUCTOS_DATA = [
    # SALA DE ESTAR
    {"name": "Sillón Orejero", "category": "sala", "desc": "Sillón clásico de respaldo alto para máximo confort.", "img": "Sala_Sillon_Orejero.png"},
    {"name": "Sillón Orejero II", "category": "sala", "desc": "Variante de sillón orejero con tapizado premium.", "img": "Sala_Sillon_Orejero_2.png"},
    {"name": "Sofá Floral", "category": "sala", "desc": "Sofá cómodo con estampado floral elegante.", "img": "Sala_Sofa_Floral.png"},
    {"name": "Sofá Vintage Blanco", "category": "sala", "desc": "Sofá estilo vintage con estructura de madera vista.", "img": "Sala_Sofa_Vintage_Blanco.png"},
    {"name": "Banqueta Capitoné", "category": "sala", "desc": "Banqueta larga tapizada con técnica capitoné.", "img": "Sala_Banqueta_Capitone.png"},
    {"name": "Estantería Divisor Negra", "category": "sala", "desc": "Estantería moderna ideal para dividir ambientes.", "img": "Sala_Estanteria_Divisor_Negra.png"},
    {"name": "Estantería Baja Madera", "category": "sala", "desc": "Mueble bajo de estantes en madera sólida.", "img": "Sala_Estanteria_Baja_Madera.png"},
    {"name": "Mueble Pared Modular", "category": "sala", "desc": "Centro de entretenimiento modular para TV.", "img": "Sala_Mueble_Pared_Modular.png"},
    {"name": "Bar Empotrado Escalera", "category": "sala", "desc": "Mueble bar diseñado a medida bajo la escalera.", "img": "Sala_Bar_Empotrado_Escalera.png"},
    {"name": "Vitrina Clásica Caoba", "category": "sala", "desc": "Vitrina elegante en madera de caoba y vidrio.", "img": "Sala_Vitrina_Clasica_Caoba.png"},

    # DORMITORIO
    {"name": "Cama Master King", "category": "dormitorio", "desc": "Cama King Size con cabecera de diseño.", "img": "Dormitorio_Cama_Master_King.png"},
    {"name": "Cama Master King II", "category": "dormitorio", "desc": "Variante de cama King Size, estructura robusta.", "img": "Dormitorio_Cama_Master_King_2.png"},
    {"name": "Velador Nogal Abierto", "category": "dormitorio", "desc": "Mesita de noche en nogal con repisa abierta.", "img": "Dormitorio_Velador_Nogal_Abierto.png"},
    {"name": "Velador Nogal Cerrado", "category": "dormitorio", "desc": "Mesita de noche en nogal con puerta.", "img": "Dormitorio_Velador_Nogal_Cerrado.png"},
    {"name": "Velador Azul Moderno", "category": "dormitorio", "desc": "Velador de diseño contemporáneo en tono azul.", "img": "Dormitorio_Velador_Azul_Moderno.png"},
    {"name": "Tocador Vintage Base", "category": "dormitorio", "desc": "Mueble base para tocador estilo vintage.", "img": "Dormitorio_Tocador_Vintage_Base.png"},
    {"name": "Tocador Barroco", "category": "dormitorio", "desc": "Tocador con espejo y detalles tallados estilo barroco.", "img": "Dormitorio_Tocador_Barroco.png"},
    {"name": "Tocador Camerino Negro", "category": "dormitorio", "desc": "Mueble de maquillaje moderno con iluminación.", "img": "Dormitorio_Tocador_Camerino_Negro.png"},
    {"name": "Cómoda Con Espejo", "category": "dormitorio", "desc": "Cómoda cajonera con espejo superior.", "img": "Dormitorio_Comoda_Con_Espejo.png"},
    {"name": "Ropero Antiguo Masivo", "category": "dormitorio", "desc": "Armario clásico de gran capacidad y madera sólida.", "img": "Dormitorio_Ropero_Antiguo_Masivo.png"},
    {"name": "Closet Empotrado Abierto", "category": "dormitorio", "desc": "Organización interna de closet a medida.", "img": "Dormitorio_Closet_Empotrado_Abierto.png"},
    {"name": "Closet Centro TV", "category": "dormitorio", "desc": "Armario diseñado con espacio central para TV.", "img": "Dormitorio_Closet_Centro_TV.png"},
    {"name": "Closet Puerta Espejo", "category": "dormitorio", "desc": "Armario moderno con puerta de espejo cuerpo entero.", "img": "Dormitorio_Closet_Puerta_Espejo.png"},
    {"name": "Cajonera Empotrada Blanca", "category": "dormitorio", "desc": "Mueble de cajones blancos ajustado a medida.", "img": "Dormitorio_Cajonera_Empotrada_Blanca.png"},

    # COMEDOR
    {"name": "Mesa Redonda Restaurada", "category": "comedor", "desc": "Mesa de comedor redonda restaurada a nuevo.", "img": "Comedor_Mesa_Redonda_Restaurada.jpg"},
    {"name": "Mesa Redonda Té", "category": "comedor", "desc": "Mesa pequeña redonda ideal para el té.", "img": "Comedor_Mesa_Redonda_Te.png"},
    {"name": "Mesa Redonda Lujo", "category": "comedor", "desc": "Mesa de comedor redonda con acabados de lujo.", "img": "Comedor_Mesa_Redonda_Lujo.png"},
    {"name": "Mesa Borde Ondulado", "category": "comedor", "desc": "Mesa con detalle de borde ondulado artesanal.", "img": "Comedor_Mesa_Borde_Ondulado.png"},
    {"name": "Mesa Ovalada Grande", "category": "comedor", "desc": "Mesa de comedor ovalada para familias numerosas.", "img": "Comedor_Mesa_Ovalada_Grande.png"},
    {"name": "Sillas Respaldo Araña", "category": "comedor", "desc": "Juego de sillas con respaldo trabajado estilo araña.", "img": "Comedor_Sillas_Respaldo_Araña.png"},
    {"name": "Bufetero Blanco I", "category": "comedor", "desc": "Aparador blanco moderno y funcional.", "img": "Comedor_Bufetero_Blanco_1.jpg"},
    {"name": "Bufetero Blanco II", "category": "comedor", "desc": "Variante de aparador blanco con cajonería.", "img": "Comedor_Bufetero_Blanco_2.png"},

    # INFANTIL
    {"name": "Silla Alta Bebé", "category": "infantil", "desc": "Silla de comer segura y robusta para bebés.", "img": "Infantil_Silla_Alta_Bebe.png"},
    {"name": "Estantería Casita Rosa", "category": "infantil", "desc": "Mueble organizador con forma de casa.", "img": "Infantil_Estanteria_Casita_Rosa.jpg"},
    {"name": "Cuna Cajonera Armada", "category": "infantil", "desc": "Cuna funcional con cajonera integrada.", "img": "Infantil_Cuna_Cajonera_Armada.png"},
    {"name": "Cuna Cajonera Lateral", "category": "infantil", "desc": "Vista lateral de la cuna con almacenamiento.", "img": "Infantil_Cuna_Cajonera_Lateral.png"},
    {"name": "Cuna Cajonera Frontal", "category": "infantil", "desc": "Vista frontal de los cajones de la cuna.", "img": "Infantil_Cuna_Cajonera_Frontal.png"},

    # OFICINA
    {"name": "Secreter Tallado Oriental", "category": "oficina", "desc": "Escritorio secreter con tallados estilo oriental.", "img": "Oficina_Secreter_Tallado_Oriental.png"},
    {"name": "Buró Antiguo Madera", "category": "oficina", "desc": "Escritorio clásico tipo buró en madera.", "img": "Oficina_Buro_Antiguo_Madera.png"},
    {"name": "Escritorio Blanco Vidrio", "category": "oficina", "desc": "Escritorio moderno blanco con tope de vidrio.", "img": "Oficina_Escritorio_Blanco_Vidrio.png"},
    {"name": "Recepción Madera Clara", "category": "oficina", "desc": "Mueble de recepción para oficina o negocio.", "img": "Oficina_Recepcion_Madera_Clara.png"},
    {"name": "Mostrador Interno", "category": "oficina", "desc": "Mueble de atención y trabajo interno.", "img": "Oficina_Mostrador_Interno.png"},
    {"name": "Vitrinas Mostrador", "category": "oficina", "desc": "Mostrador con vitrinas de vidrio para exhibición.", "img": "Oficina_Vitrinas_Mostrador.png"},
    {"name": "Módulo Caja", "category": "oficina", "desc": "Mueble específico para punto de cobro.", "img": "Oficina_Modulo_Caja.png"},
    {"name": "Mesa Reuniones/Cafetería", "category": "oficina", "desc": "Mesa versátil para juntas o área de café.", "img": "Oficina_Mesa_Reuniones_Cafeteria.png"},
    {"name": "Módulos Separadores", "category": "oficina", "desc": "Cubículos de madera para separar áreas de trabajo.", "img": "Oficina_Modulos_Separadores.png"},

    # ALMACENAMIENTO
    {"name": "Estructura Cocina Proceso", "category": "almacen", "desc": "Estructura interna de muebles de cocina.", "img": "Almacen_Estructura_Cocina_Proceso.jpg"},
    {"name": "Biblioteca Madera Alta", "category": "almacen", "desc": "Estantería de piso a techo en madera.", "img": "Almacen_Biblioteca_Madera_Alta.jpg"},
    {"name": "Mueble Bajo Largo", "category": "almacen", "desc": "Mueble de almacenamiento bajo y extendido.", "img": "Almacen_Mueble_Bajo_Largo.jpg"},
    {"name": "Gabinete Baño Inodoro", "category": "almacen", "desc": "Mueble organizador para colocar sobre el inodoro.", "img": "Almacen_Gabinete_Baño_Sobre_Inodoro.jpg"},
    {"name": "Cocina Escritorio Auxiliar", "category": "almacen", "desc": "Mueble auxiliar de cocina tipo escritorio.", "img": "Almacen_Cocina_Escritorio_Auxiliar.png"},
    {"name": "Cocina Muebles Altos", "category": "almacen", "desc": "Gabinetes superiores de cocina.", "img": "Almacen_Cocina_Muebles_Altos.png"},
    {"name": "Cocina Integral Caoba", "category": "almacen", "desc": "Cocina completa en madera tono caoba.", "img": "Almacen_Cocina_Integral_Caoba.png"},
    {"name": "Cocina Integral Pequeña", "category": "almacen", "desc": "Diseño de cocina para espacios reducidos.", "img": "Almacen_Cocina_Integral_Pequeña.png"},
    {"name": "Cocina Gabinetes Altos", "category": "almacen", "desc": "Detalle de muebles altos de cocina.", "img": "Almacen_Cocina_Gabinetes_Altos.png"},
    {"name": "Cocina Integral Blanca", "category": "almacen", "desc": "Cocina moderna en acabado blanco.", "img": "Almacen_Cocina_Integral_Blanca.png"},
    {"name": "Cocina Integral Isla Negra", "category": "almacen", "desc": "Cocina con isla central en tono negro.", "img": "Almacen_Cocina_Integral_Isla_Negra.png"},
    {"name": "Cocina Vista General", "category": "almacen", "desc": "Vista panorámica de cocina integral.", "img": "Almacen_Cocina_Vista_General.png"},
    {"name": "Cocina Mesón Granito", "category": "almacen", "desc": "Detalle de encimera de granito en cocina.", "img": "Almacen_Cocina_Meson_Granito.png"},
    {"name": "Isla Blanca Quartz", "category": "almacen", "desc": "Isla de cocina blanca con superficie de cuarzo.", "img": "Almacen_Isla_Blanca_Quartz.png"},
    {"name": "Isla Basurero Oculto", "category": "almacen", "desc": "Isla funcional con sistema de basura oculto.", "img": "Almacen_Isla_Basurero_Oculto.png"},
    {"name": "Barra Desayunador", "category": "almacen", "desc": "Barra alta de madera para cocina.", "img": "Almacen_Barra_Desayunador.png"},
    {"name": "Mueble Fregadero", "category": "almacen", "desc": "Mueble bajo para fregadero de cocina.", "img": "Almacen_Mueble_Fregadero.png"},
    {"name": "Gabinete Aéreo Blanco", "category": "almacen", "desc": "Mueble de pared blanco para almacenamiento.", "img": "Almacen_Gabinete_Aereo_Blanco.png"},
    {"name": "Cajonera Blanca Taller", "category": "almacen", "desc": "Mueble de cajones robusto multiuso.", "img": "Almacen_Cajonera_Blanca_Taller.png"},
    {"name": "Despensa Vertical Alta", "category": "almacen", "desc": "Columna alta para despensa de cocina.", "img": "Almacen_Despensa_Vertical_Alta.png"},
    {"name": "Alacena Puertas Abiertas", "category": "almacen", "desc": "Mueble alacena mostrando capacidad interna.", "img": "Almacen_Alacena_Puertas_Abiertas.png"},
    {"name": "Gabinete Madera Pequeño", "category": "almacen", "desc": "Pequeño mueble de guardado en madera.", "img": "Almacen_Gabinete_Madera_Pequeño.png"},
    {"name": "Baúl Cofre Antiguo", "category": "almacen", "desc": "Baúl de estilo antiguo para almacenamiento.", "img": "Almacen_Baul_Cofre_Antiguo.png"},
    {"name": "Baño Mueble Gris", "category": "almacen", "desc": "Mueble de baño bajo lavabo en gris.", "img": "Almacen_Baño_Mueble_Gris.png"},
    {"name": "Baño Mueble Chocolate", "category": "almacen", "desc": "Mueble de baño color chocolate.", "img": "Almacen_Baño_Mueble_Chocolate.png"},
    {"name": "Baño Vertical Espejo", "category": "almacen", "desc": "Columna de baño con espejo.", "img": "Almacen_Baño_Vertical_Espejo.png"},
        {"name": "Baño Vanity Negro", "category": "almacen", "desc": "Mueble vanity flotante en negro.", "img": "Almacen_Baño_Vanity_Negro.png"},
     {"name": "Baño Vanity Madera", "category": "almacen", "desc": "Mueble vanity flotante en madera natural.", "img": "Almacen_Baño_Vanity_Madera.png"},

    # DECORACIÓN
    {"name": "Techo Madera Luces", "category": "deco", "desc": "Techo decorativo con iluminación empotrada.", "img": "Deco_Techo_Madera_Luces.jpg"},
    {"name": "Techo Madera Vista", "category": "deco", "desc": "Estructura de techo de madera vista.", "img": "Deco_Techo_Madera_Vista.jpg"},
    {"name": "Marco Religioso", "category": "deco", "desc": "Marco de madera para imagen religiosa.", "img": "Deco_Marco_Religioso.jpg"},
    {"name": "Repisa Geométrica", "category": "deco", "desc": "Repisa de pared con diseño geométrico.", "img": "Deco_Repisa_Geometrica.png"},
    {"name": "Repisas Flotantes Blancas", "category": "deco", "desc": "Set de repisas flotantes minimalistas.", "img": "Deco_Repisas_Flotantes_Blancas.png"},
    {"name": "Repisas Cubo Negras", "category": "deco", "desc": "Juego de repisas cubo en color negro.", "img": "Deco_Repisas_Cubo_Negras.png"},
    {"name": "Repisas Cubo Blancas", "category": "deco", "desc": "Juego de repisas cubo en color blanco.", "img": "Deco_Repisas_Cubo_Blancas.png"},
    {"name": "Nicho Pared Iluminado", "category": "deco", "desc": "Nicho decorativo en madera con luz.", "img": "Deco_Nicho_Pared_Iluminado.png"},
    {"name": "Nichos Pared Oscuros", "category": "deco", "desc": "Nichos decorativos en madera oscura.", "img": "Deco_Nichos_Pared_Oscuros.png"},
        {"name": "Techo Pérgola Madera", "category": "deco", "desc": "Estructura tipo pérgola interior.", "img": "Deco_Techo_Pergola_Madera.png"},
     {"name": "Marco Caballete", "category": "deco", "desc": "Marco de madera sobre caballete.", "img": "Deco_Marco_Caballete.png"},
    {"name": "Puertas Blancas Doble", "category": "deco", "desc": "Juego de puertas dobles blancas.", "img": "Deco_Puertas_Blancas_Doble.jpg"},
    {"name": "Puerta Tallada Clásica", "category": "deco", "desc": "Puerta de madera sólida con tallados.", "img": "Deco_Puerta_Tallada_Clasica.png"},
    {"name": "Puerta Madera Arco", "category": "deco", "desc": "Puerta de madera con diseño de arco superior.", "img": "Deco_Puerta_Madera_Arco.png"},
    {"name": "Puerta Madera Brillante", "category": "deco", "desc": "Puerta de madera lisa con acabado brillante.", "img": "Deco_Puerta_Madera_Brillante.png"},
    {"name": "Puerta Tamborada Blanca", "category": "deco", "desc": "Puerta interior tamborada blanca.", "img": "Deco_Puerta_Tamborada_Blanca.png"},
        {"name": "Puerta Lisa Líneas", "category": "deco", "desc": "Puerta lisa con incrustaciones de líneas.", "img": "Deco_Puerta_Lisa_Lineas.png"},
     {"name": "Puerta Blanca Vidrio", "category": "deco", "desc": "Puerta blanca con franja de vidrio.", "img": "Deco_Puerta_Blanca_Vidrio.png"},
    {"name": "Puerta Negra Franjas", "category": "deco", "desc": "Puerta negra con franjas decorativas.", "img": "Deco_Puerta_Negra_Franjas.png"},
    {"name": "Puerta Negra Brillante", "category": "deco", "desc": "Puerta moderna negra alto brillo.", "img": "Deco_Puerta_Negra_Brillante.png"},
    {"name": "Puerta Entrada Roja", "category": "deco", "desc": "Puerta de entrada principal color rojo.", "img": "Deco_Puerta_Entrada_Roja.png"},
    {"name": "Puerta Doble Blanca", "category": "deco", "desc": "Entrada de doble hoja blanca.", "img": "Deco_Puerta_Doble_Blanca.png"},
    {"name": "Escalera Madera Peldaños", "category": "deco", "desc": "Revestimiento de peldaños en madera.", "img": "Deco_Escalera_Madera_Peldaños.png"},
    {"name": "Escalera Madera Baranda", "category": "deco", "desc": "Escalera completa con baranda de madera.", "img": "Deco_Escalera_Madera_Baranda.png"},
    {"name": "Escalera Madera Frontal", "category": "deco", "desc": "Vista frontal de escalera moderna.", "img": "Deco_Escalera_Madera_Frontal.png"},
    {"name": "Zócalo Barredera Madera", "category": "deco", "desc": "Instalación de zócalos de madera.", "img": "Deco_Zocalo_Barredera_Madera.png"},
    {"name": "Zócalo Barredera Blanco", "category": "deco", "desc": "Instalación de zócalos blancos.", "img": "Deco_Zocalo_Barredera_Blanco.png"},
    {"name": "Mesa Pedestal Cajones", "category": "deco", "desc": "Mesa auxiliar pedestal con cajonería.", "img": "Deco_Mesa_Pedestal_Cajones.png"},
    {"name": "Mesa Té Reina Ana", "category": "deco", "desc": "Mesa clásica estilo Reina Ana.", "img": "Deco_Mesa_Te_Reina_Ana.png"},
    {"name": "Mesas Nido Madera", "category": "deco", "desc": "Set de mesas nido auxiliares.", "img": "Deco_Mesas_Nido_Madera.png"},
    {"name": "Mesa Trípode Madera", "category": "deco", "desc": "Mesa auxiliar pequeña con base trípode.", "img": "Deco_Mesa_Tripode_Madera.png"},
    {"name": "Consola Bicolor I", "category": "deco", "desc": "Mesa de arrimo bicolor diseño I.", "img": "Deco_Consola_Bicolor_1.jpg"},
    {"name": "Consola Bicolor II", "category": "deco", "desc": "Mesa de arrimo bicolor diseño II.", "img": "Deco_Consola_Bicolor_2.png"},
    {"name": "Paneles Tallados", "category": "deco", "desc": "Paneles de madera con tallados artísticos.", "img": "Deco_Paneles_Tallados.png"},
    {"name": "Virgen Tallada", "category": "deco", "desc": "Talla religiosa de Virgen en madera.", "img": "Deco_Virgen_Tallada.png"},
    {"name": "Base Imagen", "category": "deco", "desc": "Base de madera para imagen religiosa.", "img": "Deco_Base_Imagen.png"},
    {"name": "Anda Procesional Azul", "category": "deco", "desc": "Anda religiosa pintada en azul.", "img": "Deco_Anda_Procesional_Azul.png"},
    {"name": "Anda Procesional Detalle", "category": "deco", "desc": "Detalle de anda procesional.", "img": "Deco_Anda_Procesional_Detalle.png"},
    {"name": "Anda Procesional Madera", "category": "deco", "desc": "Anda religiosa en madera natural.", "img": "Deco_Anda_Procesional_Madera.png"},

    # EXTERIOR
    {"name": "Techo Alero Madera", "category": "exterior", "desc": "Estructura de alero exterior en madera.", "img": "Exterior_Techo_Alero_Madera.jpg"},
    {"name": "Casa Perro Madera", "category": "exterior", "desc": "Casa para mascota en madera tratada.", "img": "Exterior_Casa_Perro_Madera.png"},
    {"name": "Mueble Terraza Café", "category": "exterior", "desc": "Mueble resistente para terraza.", "img": "Exterior_Mueble_Terraza_Café.png"},
    {"name": "Pérgola Techo Madera", "category": "exterior", "desc": "Pérgola de madera para sombra exterior.", "img": "Exterior_Pergola_Techo_Madera.png"},
    {"name": "Portón Garage Madera", "category": "exterior", "desc": "Portón vehicular sólido en madera.", "img": "Exterior_Porton_Garage_Madera.png"},
    {"name": "Portón Listones", "category": "exterior", "desc": "Portón exterior de diseño abierto con listones.", "img": "Exterior_Porton_Listones.png"}
]

def ejecutar_carga():
    ruta_fotos_nuevas = 'fotos_nuevas' # Cambia esto si tu carpeta se llama distinto

    # Verificación de carpeta
    if not os.path.exists(ruta_fotos_nuevas):
        print(f"❌ Error: La carpeta '{ruta_fotos_nuevas}' no existe.")
        return

    print(f"--- Iniciando carga de {len(PRODUCTOS_DATA)} muebles ---")

    exitos = 0
    errores = 0

    for item in PRODUCTOS_DATA:
        img_name = item['img']
        ruta_completa = os.path.join(ruta_fotos_nuevas, img_name)

        if os.path.exists(ruta_completa):
            try:
                # Abrimos el archivo de imagen
                with open(ruta_completa, 'rb') as f:
                    # Creamos el objeto Producto
                    p = Producto(
                        nombre=item['name'],
                        categoria=item['category'],
                        descripcion=item['desc']
                    )
                    # Guardamos la imagen (Django la copia a /media/muebles/)
                    p.imagen.save(img_name, File(f), save=True)

                print(f"✅ Cargado: {item['name']}")
                exitos += 1
            except Exception as e:
                print(f"❌ Error guardando {item['name']}: {e}")
                errores += 1
        else:
            print(f"⚠️ Imagen no encontrada: {img_name} (Saltando {item['name']})")
            errores += 1

    print(f"\n--- Resumen ---")
    print(f"Total éxitos: {exitos}")
    print(f"Total fallidos/saltados: {errores}")

if __name__ == "__main__":
    ejecutar_carga()