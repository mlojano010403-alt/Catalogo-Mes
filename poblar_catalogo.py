import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'carpinteria_project.settings')
django.setup()

from catalogo.models import Categoria, Mueble

def cargar_datos_reales():
    # 1. Asegurar Categorías (IDs maestros)
    cats_data = {
        1: 'Muebles de Sala', 2: 'Muebles de Dormitorio', 3: 'Muebles de Comedor',
        4: 'Muebles de Oficina / Estudio', 5: 'Muebles Infantil', 6: 'Muebles de Exterior / Jardín',
        7: 'Muebles de Almacenamiento', 8: 'Muebles Decorativos y Auxiliares', 9: 'Antigüedades Restauradas'
    }
    for cid, nombre in cats_data.items():
        Categoria.objects.get_or_create(id=cid, defaults={'nombre': nombre})

    # 2. Lista Maestra con Extensiones Verificadas y Descripciones Técnicas
    muebles_lista = [
        # --- ALMACENAMIENTO (7) ---
        (7, 'Alacena Blanca Cristal', 'Almacen_Alacena_Blanca_Cristal.png', 'Alacena de cocina con puertas de vidrio y acabados en blanco brillante.'),
        (7, 'Gabinete Sobre Inodoro', 'Almacen_Bano_Gabinete_Sobre_Inodoro.jpg', 'Mueble organizador para baño diseñado para optimizar el espacio.'), #
        (7, 'Vanity Baño Chocolate', 'Almacen_Bano_Vanity_Chocolate.png', 'Mueble de baño en tono chocolate con mesón integrado.'),
        (7, 'Vanity Flotante Madera', 'Almacen_Bano_Vanity_Flotante_Madera.png', 'Vanity moderno de estilo flotante en madera natural.'),
        (7, 'Vanity Flotante Oscuro', 'Almacen_Bano_Vanity_Flotante_Oscuro.png', 'Mueble de baño contemporáneo en acabado wengue profundo.'),
        (7, 'Vanity Gris Patas', 'Almacen_Bano_Vanity_Gris_Patas.png', 'Vanity de baño en gris mate con soporte de diseño industrial.'),
        (7, 'Cajoneras de Taller', 'Almacen_Cocina_Cajoneras_Taller.jpg', 'Módulos de cajoneras robustas para organización técnica.'), #
        (7, 'Escritorio Cocina Blanco', 'Almacen_Cocina_Escritorio_Blanco.png', 'Mesa auxiliar multifuncional para áreas de servicio.'),
        (7, 'Gabinete Aéreo Blanco', 'Almacen_Cocina_Gabinete_Aereo_Blanco.png', 'Módulo superior de cocina con apertura neumática.'),
        (7, 'Gabinetes Altos Modernos', 'Almacen_Cocina_Gabinetes_Altos_Modernos.jpg', 'Set de muebles superiores con diseño minimalista.'), #
        (7, 'Cocina Integral Blanca', 'Almacen_Cocina_Integral_Blanca.png', 'Proyecto completo de cocina en melamina de alta resistencia.'),
        (7, 'Cocina Integral Caoba', 'Almacen_Cocina_Integral_Caoba.png', 'Cocina de lujo con frentes en madera de caoba seleccionada.'),
        (7, 'Cocina Panorámica', 'Almacen_Cocina_Integral_Panoramica.jpg', 'Diseño de cocina abierta con organización modular.'), #
        (7, 'Isla Basurero Oculto', 'Almacen_Cocina_Isla_Basurero_Oculto.png', 'Isla funcional con sistema de gestión de residuos integrado.'),
        (7, 'Isla Blanca Cuarzo', 'Almacen_Cocina_Isla_Blanca_Cuarzo.png', 'Isla central con mesón de cuarzo blanco resistente.'),
        (7, 'Isla para Plancha', 'Almacen_Cocina_Isla_Plancha.jpg', 'Isla de trabajo diseñada para preparación de alimentos.'), #
        (7, 'Mesón Granito Wengue', 'Almacen_Cocina_Meson_Granito_Wengue.png', 'Encimera de cocina en granito natural sobre base oscura.'),
        (7, 'Módulo Bajo Proceso', 'Almacen_Cocina_Modulo_Bajo_Proceso.png', 'Muestra del proceso constructivo de estructuras.'),
        (7, 'Bajos Fregadero', 'Almacen_Cocina_Modulos_Bajos_Fregadero.jpg', 'Compartimentos inferiores para instalaciones sanitarias.'),
        (7, 'Muebles Altos Madera', 'Almacen_Cocina_Muebles_Altos_Madera.png', 'Gabinetes superiores con acabados en madera natural.'),
        (7, 'Organizador Blanco', 'Almacen_Cocina_Organizador_Blanco.png', 'Mueble vertical para despensa o utensilios.'),
        (7, 'Despensa Madera', 'Almacen_Despensa_Vertical_Madera.png', 'Columna de almacenamiento de gran capacidad.'),

        # --- COMEDOR (3) ---
        (3, 'Bufetero Moderno Blanco', 'Comedor_Bufetero_Moderno_Blanco.png', 'Mueble de apoyo para comedor con diseño minimalista.'),
        (3, 'Juego Sillas Clásicas', 'Comedor_Juego_Sillas_Clasicas.png', 'Set de sillas con respaldo tallado y tapicería fina.'),
        (3, 'Mesa Borde Ondulado', 'Comedor_Mesa_Borde_Ondulado_Clasica.png', 'Mesa señorial con bordes trabajados artesanalmente.'),
        (3, 'Mesa Patas Coloniales', 'Comedor_Mesa_Cuadrada_Patas_Coloniales.jpg', 'Mesa tradicional con patas robustas de diseño colonial.'),
        (3, 'Mesa Familiar Grande', 'Comedor_Mesa_Rectangular_Grande.png', 'Mesa de gran formato para reuniones numerosas.'),
        (3, 'Mesa Redonda Lujo', 'Comedor_Mesa_Redonda_Lujo_Brillante.png', 'Mesa circular con acabado espejo y detalles de lujo.'),
        (3, 'Mesa Pedestal Grueso', 'Comedor_Mesa_Redonda_Pedestal_Grueso.jpg', 'Mesa con base central de madera maciza torneada.'),
        (3, 'Sillas Medallón', 'Comedor_Mesa_Redonda_Sillas_Medallon.jpg', 'Juego de comedor clásico con sillas de respaldo tipo medallón.'),
        (3, 'Mesa Té Madera', 'Comedor_Mesa_Redonda_Te_Madera.png', 'Mesa circular ideal para áreas de café o té.'),
        (3, 'Vitrina Esquinera Curva', 'Comedor_Vitrina_Esquinera_Curva.jpg', 'Vitrina diseñada para esquinas con frentes de vidrio.'),

        # --- DECORATIVOS (8) ---
        (8, 'Escalera Madera U Moderna', 'Deco_Escalera_Madera_U_Moderna.jpeg', 'Escalera arquitectónica moderna con diseño en U de madera maciza.'), #
        (8, 'Gabinete Madera Pequeño', 'Deco_Gabinete_Madera_Pequeno.png', 'Mueble auxiliar compacto ideal para decoración o espacios pequeños.'),
        (8, 'Marco Caballete Madera', 'Deco_Marco_Caballete_Madera.png', 'Soporte artístico de madera para cuadros o lienzos.'),
        (8, 'Mesa Auxiliar Luis XV', 'Deco_Mesa_Auxiliar_Luis_XV.png', 'Pequeña mesa lateral con diseño clásico francés.'),
        (8, 'Mesa Negra Torneada', 'Deco_Mesa_Auxiliar_Negra_Torneada.jpg', 'Mesa decorativa con patas de diseño torneado artesanal.'),
        (8, 'Mesa Patas Cruzadas A', 'Deco_Mesa_Auxiliar_Patas_Cruzadas_1.png', 'Mesa auxiliar con base estructural en X.'),
        (8, 'Mesa Patas Cruzadas B', 'Deco_Mesa_Auxiliar_Patas_Cruzadas_2.png', 'Variante de mesa decorativa con soporte cruzado.'),
        (8, 'Mesa Madera U 1', 'Deco_Mesas_Auxiliares_Madera_U_1.png', 'Mesa minimalista tallada en forma de U.'),
        (8, 'Mesa Madera U 2', 'Deco_Mesas_Auxiliares_Madera_U_2.png', 'Diseño arquitectónico de mesa auxiliar en madera.'),
        (8, 'Joyero Trípode', 'Deco_Mesita_Joyero_Tripode.png', 'Mesa de tres patas diseñada para accesorios de joyería.'),
        (8, 'Nicho Iluminado', 'Deco_Nicho_Madera_Iluminado.png', 'Caja de exhibición con sistema de iluminación LED.'),
        (8, 'Puerta Cuadrículas', 'Deco_Puerta_Francesa_Cuadriculas.png', 'Puerta interior con paneles de vidrio cuadriculado.'),
        (8, 'Puerta Blanca Curva', 'Deco_Puerta_Interior_Blanca_Curva.png', 'Puerta con marco arqueado y acabado lacado blanco.'),
        (8, 'Puerta Blanca Vidrio', 'Deco_Puerta_Interior_Blanca_Vidrio.png', 'Puerta de paso con panel central de vidrio esmerilado.'),
        (8, 'Puerta Lisa Líneas', 'Deco_Puerta_Interior_Lisa_Lineas.png', 'Puerta moderna con relieves horizontales.'),
        (8, 'Puerta Madera Brillo', 'Deco_Puerta_Interior_Madera_Brillante.png', 'Puerta de madera fina con laca de alto brillo.'),
        (8, 'Puerta Tallada Clásica', 'Deco_Puerta_Interior_Tallada_Clasica.png', 'Puerta señorial con tallados artísticos hechos a mano.'),
        (8, 'Puerta Principal Metal', 'Deco_Puerta_Principal_Franjas_Metal.png', 'Puerta de seguridad con detalles metálicos horizontales.'),
        (8, 'Puertas Blancas Lisas', 'Deco_Puertas_Interiores_Blancas_Lisas.jpg', 'Set de puertas minimalistas para estancias interiores.'),
        (8, 'Puertas Oscuras Lisas', 'Deco_Puertas_Interiores_Oscuras_Lisas.png', 'Puertas contemporáneas en acabado nogal o wengue.'),
        (8, 'Anda Procesional Azul', 'Deco_Religioso_Anda_Procesional_Azul.png', 'Estructura religiosa pintada para procesiones locales.'),
        (8, 'Anda Procesional Madera', 'Deco_Religioso_Anda_Procesional_Madera.png', 'Anda tallada en madera natural para imágenes sacras.'),
        (8, 'Marco Arcángel', 'Deco_Religioso_Cuadro_Arcangel_Marco.jpg', 'Marco de arte sacro tallado con detalles coloniales.'),
        (8, 'Peana Escultura', 'Deco_Religioso_Escultura_Peana.jpg', 'Base sólida para exhibición de estatuaria religiosa.'),
        (8, 'Virgen Tallada', 'Deco_Religioso_Virgen_Tallada.png', 'Escultura tallada íntegramente en un bloque de madera.'),
        (8, 'Repisa Escalonada', 'Deco_Repisa_Pared_Escalonada.png', 'Mueble de pared con niveles asimétricos para decoración.'),
        (8, 'Cubos Blancos', 'Deco_Repisas_Cubos_Blancos.png', 'Set de repisas flotantes tipo cubo en color blanco.'),
        (8, 'Cubos Negros', 'Deco_Repisas_Cubos_Negros.png', 'Organizadores de pared acabado negro mate.'),
        (8, 'Repisas Flotantes', 'Deco_Repisas_Flotantes_Blancas.png', 'Repisas minimalistas de fijación invisible.'),
        (8, 'Nichos Pared Oscuros', 'Deco_Repisas_Nichos_Pared_Oscuros.png', 'Huecos decorativos revestidos en madera oscura.'),
        (8, 'Zócalo Madera', 'Deco_Zocalo_Barredera_Madera.png', 'Terminación de carpintería para pisos interiores.'),

        # --- DORMITORIO (2) ---
        (2, 'Cama Master King', 'Dormitorio_Cama_Master_King.png', 'Estructura de cama tamaño King en madera maciza seleccionada.'),
        (2, 'Clóset Blanco Cajoneras', 'Dormitorio_Closet_Blanco_Cajones.png', 'Módulo de armario con sistema de cajoneras de cierre suave.'),
        (2, 'Clóset Despensa Oscura', 'Dormitorio_Closet_Despensa_Oscura.png', 'Armario empotrado de gran capacidad funcional.'),
        (2, 'Clóset Madera Abierto', 'Dormitorio_Closet_Empotrado_Abierto_Madera.png', 'Vestidor abierto que resalta la veta natural de la madera.'),
        (2, 'Ropero Blanco Espejo', 'Dormitorio_Ropero_Blanco_Espejo.png', 'Armario exento con puertas de espejo integradas.'),
        (2, 'Tocador Clásico Oscuro', 'Dormitorio_Tocador_Clasico_Oscuro.png', 'Mueble de belleza con espejo y gavetas tradicionales.'),
        (2, 'Tocador Vintage Madera', 'Dormitorio_Tocador_Vintage_Madera.png', 'Tocador de líneas retro con acabado rústico natural.'),
        (2, 'Velador Bicolor Moderno', 'Dormitorio_Velador_Bicolor_Moderno.png', 'Mesa de noche con combinación de lacado y madera.'),
        (2, 'Velador Nogal Abierto', 'Dormitorio_Velador_Nogal_Abierto.png', 'Velador minimalista con espacio de almacenamiento abierto.'),

        # --- EXTERIOR (6) ---
        (6, 'Aleros de Madera', 'Exterior_Carpinteria_Techos_Aleros.jpg', 'Protección estructural para fachadas exteriores.'),
        (6, 'Casa Mascota Madera', 'Exterior_Casa_Mascota_Madera.png', 'Refugio fabricado en madera tratada para resistir el clima.'),
        (6, 'Estructura Pérgola', 'Exterior_Estructura_Pergola_Madera.png', 'Columnas macizas para zonas de descanso exteriores.'),
        (6, 'Techo Pérgola', 'Exterior_Estructura_Techo_Pergola.png', 'Detalle de enlatado superior para pérgolas de jardín.'),
        (6, 'Organizador Terraza', 'Exterior_Organizador_Terraza_Cafe.png', 'Mueble auxiliar en tono café rústico.'),
        (6, 'Portón Garage Listones', 'Exterior_Porton_Garaje_Listones.png', 'Portón vehicular moderno con listones horizontales.'),
        (6, 'Portón Garage Paneles', 'Exterior_Porton_Garaje_Paneles.png', 'Puerta de garage robusta con diseño de paneles macizos.'),

        # --- INFANTIL (5) ---
        (5, 'Cuna Funcional Blanca', 'Infantil_Cuna_Funcional_Blanca.jpg', 'Cuna de seguridad con diseño adaptable y moderno.'),
        (5, 'Organizador Rosa', 'Infantil_Organizador_Rustico_Rosa.jpg', 'Estantería infantil con detalles rústicos y decorativos.'),
        (5, 'Silla Comer Torneada', 'Infantil_Silla_Comer_Torneada.png', 'Silla alta para bebés con diseño tradicional estable.'),

        # --- OFICINA (4) ---
        (4, 'Archivador Bajo Largo', 'Oficina_Archivador_Bajo_Largo.jpg', 'Mueble horizontal para organización de documentos ejecutivos.'), #
        (4, 'Archivador Modular Largo', 'Oficina_Archivador_Modular_Largo.jpg', 'Sistema de almacenamiento corporativo expandible.'),
        (4, 'Biblioteca Abierta Madera', 'Oficina_Biblioteca_Abierta_Madera.jpg', 'Estantería con estantes vistos en madera natural.'),
        (4, 'Biblioteca Madera Alta', 'Oficina_Biblioteca_Madera_Alta.jpg', 'Mueble de gran altura para archivo de oficina o libros.'), #
        (4, 'Cabinas de Madera', 'Oficina_Cabinas_Separadores_Madera.png', 'Paneles de madera para división de puestos de trabajo.'),
        (4, 'Pizarra Caballete', 'Oficina_Comercial_Pizarra_Caballete.jpg', 'Soporte publicitario para anuncios en locales comerciales.'),
        (4, 'Escritorio Moderno', 'Oficina_Escritorio_Blanco_Moderno.png', 'Mesa ergonómica con diseño limpio y actual.'),
        (4, 'Exhibidores Comerciales', 'Oficina_Exhibidores_Comerciales_Vidrio.png', 'Muebles de cristal para exposición de productos de lujo.'),
        (4, 'Mesa Reuniones Larga', 'Oficina_Mesa_Reuniones_Larga.png', 'Mesa ejecutiva de gran formato diseñada para juntas.'),
        (4, 'Mostrador Atención', 'Oficina_Mostrador_Atencion_Publico.png', 'Módulo de recepción frontal para locales o empresas.'),
        (4, 'Mostrador Trabajo', 'Oficina_Mostrador_Trabajo_Cajones.png', 'Mesa técnica con almacenamiento integrado.'),
        (4, 'Recepción Diagonal', 'Oficina_Recepcion_Madera_Diagonal.png', 'Mueble de entrada con diseño de listones diagonales.'),

        # --- RESTAURADOS (9) ---
        (9, 'Aparador Columnas', 'Restaurado_Aparador_Antiguo_Columnas.jpg', 'Pieza restaurada con detalles arquitectónicos coloniales.'),
        (9, 'Armario Brillante', 'Restaurado_Armario_Antiguo_Brillante.jpg', 'Armario recuperado con acabado en laca brillante resistente.'),
        (9, 'Armario Masivo 1', 'Restaurado_Armario_Antiguo_Masivo_1.jpg', 'Pieza histórica restaurada íntegramente con acabados originales.'), #
        (9, 'Armario Masivo 3', 'Restaurado_Armario_Antiguo_Masivo_3.jpg', 'Variante de armario antiguo con cornisa trabajada.'),
        (9, 'Baúl Herrajes', 'Restaurado_Baul_Antiguo_Herrajes.png', 'Cofre antiguo con piezas originales recuperadas.'),
        (9, 'Buró Abatible', 'Restaurado_Buro_Madera_Abatible.png', 'Escritorio antiguo con tapa de apertura funcional.'),
        (9, 'Cómoda Espejo', 'Restaurado_Comoda_Antigua_Espejo_Triptico.png', 'Tocador restaurado con sistema de espejos tríptico original.'),
        (9, 'Escritorio Directorio', 'Restaurado_Escritorio_Clasico_Directorio.jpg', 'Mesa de despacho antigua estilo ejecutivo tradicional.'),
        (9, 'Secreter Marquetería', 'Restaurado_Escritorio_Secreter_Marqueteria.jpg', 'Escritorio fino con incrustaciones de madera de colores.'),
        (9, 'Gabinete Ruedas', 'Restaurado_Gabinete_Antiguo_Ruedas.jpg', 'Mueble auxiliar antiguo adaptado con movilidad.'),
        (9, 'Ropero Masivo', 'Restaurado_Ropero_Antiguo_Masivo_2.png', 'Armario de gran formato restaurado para dormitorio.'),
        (9, 'Secreter Oriental', 'Restaurado_Secreter_Tallado_Oriental.png', 'Pieza de colección con tallados profundos estilo asiático.'),
        (9, 'Sofá Victoriano', 'Restaurado_Sofa_Clasico_Victoriano.png', 'Mueble de época con estructura de madera vista restaurada.'),
        (9, 'Vitrina Monumental', 'Restaurado_Vitrina_Monumental_Comedor.jpg', 'Vitrina de gran porte para comedores de lujo.'),

        # --- SALA (1) ---
        (1, 'Banqueta Puff Capitoné', 'Sala_Banqueta_Puff_Capitone.png', 'Mueble auxiliar de descanso con tapizado capitoné.'),
        (1, 'Biblioteca Asimétrica', 'Sala_Biblioteca_Moderna_Asimetrica.png', 'Estantería con diseño geométrico moderno para sala.'),
        (1, 'Centro TV Simétrico', 'Sala_Centro_Entretenimiento_Simetrico.png', 'Mueble multimedia con organización equilibrada.'),
        (1, 'Divisor Ambientes', 'Sala_Estanteria_Divisor_Ambientes.png', 'Estructura abierta para separar espacios en el hogar.'),
        (1, 'Estantería Madera Curva', 'Sala_Estanteria_Madera_Curva_1.png', 'Librero único con perfiles de madera arqueados.'),
        (1, 'Sillón Orejero Tapizado', 'Sala_Sillon_Orejero_Tapizado.png', 'Sillón individual clásico tapizado para descanso.'),
        (1, 'Sofá Floral Clásico', 'Sala_Sofa_Floral_Clasico.png', 'Sofá tradicional con tapicería de motivos florales.'),
    ]


    print(f"Cargando {len(muebles_lista)} muebles...")
    for cid, nombre, archivo, desc in muebles_lista:
        cat = Categoria.objects.get(id=cid)
        # Sincronizamos por archivo_imagen (UNIQUE)
        obj, created = Mueble.objects.update_or_create(
            archivo_imagen=archivo,
            defaults={
                'nombre_mueble': nombre,
                'categoria': cat,
                'descripcion': desc
            }
        )
        if created: print(f"  + Nuevo: {nombre}")

    print(f"✅ ¡Carga exitosa! Total: {Mueble.objects.count()} muebles.")

if __name__ == '__main__':
    cargar_datos_reales()