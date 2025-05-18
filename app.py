from flask import Flask, render_template, request

app = Flask(__name__)

# Base de datos con platillos chiapanecos y descripciones extendidas de vinos
maridajes = {
    "Tamales Chiapanecos": {
        "descripcion": "Tamales de masa de maíz con cerdo y mole envueltos en hoja de plátano",
        "vinos": {
            "tinto": [
                {"nombre": "Monte Xanic Cabernet Sauvignon", 
                 "notas": "Un vino robusto que despliega una sinfonía de frutos negros maduros, como mora y ciruela, entrelazados con sutiles matices de cacao y especias tostadas. Su estructura tánica firme abraza la intensidad del mole, potenciando las capas de sabor del cerdo y la masa, mientras su final prolongado deja un eco armonioso en el paladar.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "Casa Madero Cabernet Sauvignon", 
                 "notas": "Con una personalidad estructurada y elegante, este tinto revela aromas profundos de cassis y grosella negra, acompañados de notas de vainilla y madera ahumada provenientes de su crianza en barrica. Su cuerpo medio y taninos aterciopelados se alinean perfectamente con el mole, resaltando las especias y la riqueza del platillo.", 
                 "region": "Valle de Parras, Coahuila", "precio": 550},
                {"nombre": "El Cielo Orion (Cabernet-Malbec)", 
                 "notas": "Este blend combina la fuerza del Cabernet con la suavidad del Malbec, ofreciendo una paleta de frutos rojos oscuros, como zarzamora y cereza negra, junto a toques de pimienta y chocolate amargo. Su intensidad envolvente y su textura sedosa crean un diálogo vibrante con el mole chiapaneco, elevando la experiencia del tamal a nuevas alturas.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 750},
                {"nombre": "Vinícola San Lorenzo Syrah", 
                 "notas": "Un Syrah especiado que despliega aromas de mora silvestre y pimienta negra recién molida, con un trasfondo de cuero y hierbas secas. Su carácter audaz y taninos marcados realzan la jugosidad del cerdo y las notas terrosas del mole, ofreciendo un contraste dinámico que perdura en cada bocado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 620}
            ],
            "blanco": [
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Fresco y vibrante, este Chenin Blanc despliega un bouquet de manzana verde, pera y cítricos como limón y mandarina, con un toque sutil de miel. Su acidez chispeante corta la densidad del mole y refresca el paladar, creando un contraste ligero y armonioso que resalta la suavidad de la masa del tamal.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "Monte Xanic Chardonnay", 
                 "notas": "Un Chardonnay con cuerpo que revela notas cremosas de mantequilla, vainilla y nuez tostada, gracias a su paso por barrica, junto a matices de piña y melocotón maduro. Su textura sedosa envuelve el mole, suavizando sus especias y complementando la untuosidad del cerdo con elegancia.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "L.A. Cetto Sauvignon Blanc", 
                 "notas": "Crispado y lleno de vida, este Sauvignon Blanc ofrece un perfil cítrico de toronja y lima, con notas herbáceas de albahaca y pasto recién cortado. Su frescura vibrante atraviesa la riqueza del mole, limpiando el paladar y destacando los sabores sutiles de la hoja de plátano.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 350},
                {"nombre": "Santo Tomás Chenin Blanc", 
                 "notas": "Un blanco fresco con aromas de frutas blancas como pera y manzana, acompañados de delicados toques florales y un dejo de miel silvestre. Su equilibrio entre acidez y suavidad aporta una sensación refrescante que contrarresta la intensidad del mole, realzando la textura del tamal.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 380}
            ],
            "rosado": [
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante que combina aromas de fresas frescas y frambuesas con un toque de cítricos como mandarina. Su ligereza y frescura frutal envuelven el mole con suavidad, equilibrando sus especias y aportando un contrapunto jugoso que resalta la carne del tamal.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Con un perfil elegante, este rosado despliega notas de frutos rojos como cereza y granada, matizadas con un leve toque de rosa y cítricos. Su frescura equilibrada y textura sutil suavizan la intensidad del mole, ofreciendo una armonía delicada con la masa y el cerdo.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, este rosado presenta aromas de sandía y cítricos, con un fondo floral que evoca pétalos de jazmín. Su acidez viva y carácter delicado limpian el paladar tras la riqueza del mole, destacando los matices terrosos de la hoja de plátano.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Un rosado fresco con aromas de frutos rojos como fresa y grosella, acompañados de un sutil toque cítrico y mineral. Su cuerpo ligero y final refrescante ofrecen un equilibrio perfecto con el mole, resaltando la jugosidad del cerdo y la suavidad de la masa.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400}
            ]
        },
        "caracteristica": "sabor intenso"
    },
    "Cochito al Horno": {
        "descripcion": "Cerdo asado lentamente con achiote y especias",
        "vinos": {
            "tinto": [
                {"nombre": "L.A. Cetto Petite Sirah", 
                 "notas": "Un tinto audaz que despliega aromas de frutos negros como mora y arándano, con un trasfondo especiado de pimienta negra y clavo que resuena con el achiote. Sus taninos firmes y su cuerpo pleno potencian la textura carnosa del cerdo, dejando un final cálido y persistente.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Este Merlot sedoso ofrece una paleta de ciruelas maduras y cerezas, con toques de vainilla y tabaco dulce. Su suavidad envuelve la riqueza del cochito, mientras sus taninos aterciopelados realzan la jugosidad de la carne asada, creando una armonía reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado que despliega aromas de mora, pimienta y un toque ahumado, evocando la parrilla. Su estructura robusta y taninos marcados acompañan la intensidad del achiote, mientras su final largo deja una sensación cálida que complementa el asado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600},
                {"nombre": "Santo Tomás Cabernet Sauvignon", 
                 "notas": "Con aromas de cassis, grosella y un toque de cedro, este Cabernet ofrece una estructura firme que soporta la riqueza del cochito. Sus taninos elegantes y su acidez equilibrada realzan las especias, creando un maridaje clásico y satisfactorio.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 500}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Viognier", 
                 "notas": "Un blanco floral y exuberante que ofrece aromas de durazno maduro, jazmín y un toque de miel, con una textura rica que envuelve el paladar. Su suavidad contrasta la intensidad del achiote, refrescando el plato y destacando las especias con elegancia.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Casa Madero Chardonnay", 
                 "notas": "Este Chardonnay cremoso despliega notas de manzana asada, vainilla y un toque de mantequilla, con una acidez equilibrada que corta la grasa del cerdo. Su cuerpo medio y final suave acompañan la textura del cochito, ofreciendo un contraste delicado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 450},
                {"nombre": "L.A. Cetto Chenin Blanc", 
                 "notas": "Fresco y afrutado, con aromas de pera, melón y un toque cítrico, este Chenin Blanc aporta una ligereza que refresca el paladar tras la riqueza del asado. Su acidez vibrante realza las especias del achiote, creando un maridaje dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 320},
                {"nombre": "Tres Valles Sauvignon Blanc", 
                 "notas": "Un Sauvignon Blanc chispeante con notas de toronja, maracuyá y hierbas frescas, que ofrece una frescura vibrante para contrarrestar la intensidad del cochito. Su acidez crujiente y final limpio limpian el paladar, destacando los sabores del asado.", 
                 "region": "Valle de San Vicente, Baja California", "precio": 400}
            ],
            "rosado": [
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, este rosado despliega notas de fresas maduras y cítricos como naranja sanguina, con un fondo mineral que aporta profundidad. Su ligereza equilibra las especias del cochito, refrescando el paladar y resaltando la suculencia de la carne asada.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su frescura frutal y acidez equilibrada cortan la grasa del cerdo, mientras su textura suave acompaña la ternura de la carne, creando un maridaje alegre y armonioso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Con notas de cereza, granada y un toque de hierbas provenzales, este rosado ofrece una elegancia que suaviza las especias del cochito. Su cuerpo medio y final refrescante aportan un contrapunto delicado a la riqueza del asado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía, limón y un toque de menta, este rosado limpia el paladar con su acidez viva, realzando las notas terrosas del achiote y ofreciendo un respiro tras cada bocado del cochito.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "carnoso"
    },
    "Sopa de Chipilín": {
        "descripcion": "Sopa tradicional con hojas de chipilín y bolitas de masa",
        "vinos": {
            "tinto": [
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto ligero con aromas de cereza fresca y un toque de pimienta, que ofrece una suavidad que acompaña la delicadeza de la sopa. Sus taninos suaves y acidez equilibrada realzan las notas herbáceas del chipilín sin opacar las bolitas de masa.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450},
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Este Merlot sedoso despliega notas de ciruela y mora, con un toque de vainilla que aporta calidez. Su cuerpo medio y taninos aterciopelados envuelven la sopa, complementando la textura de las bolitas de masa y realzando las hierbas del chipilín.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "El Cielo G&G (Grenache)", 
                 "notas": "Un Grenache frutal que ofrece aromas de frambuesa, fresa y un toque de especias dulces. Su ligereza y frescura frutal aportan un contrapunto jugoso a la sopa, mientras su acidez viva resalta las notas verdes del chipilín.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Con aromas de rosa, cereza y un toque terroso, este Nebbiolo ofrece una elegancia que acompaña la sopa sin abrumarla. Sus taninos suaves y acidez brillante realzan las hierbas y la textura de la masa, creando un maridaje refinado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550}
            ],
            "blanco": [
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Un blanco fresco y vivaz que despliega aromas de manzana verde y cítricos como lima, con un toque herbáceo que resuena con el chipilín. Su acidez brillante eleva las bolitas de masa, refrescando el paladar tras cada cucharada.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "Monte Xanic Sauvignon Blanc", 
                 "notas": "Crispado y lleno de energía, este Sauvignon Blanc ofrece notas de toronja, maracuyá y hierbas frescas, que aportan una frescura vibrante a la sopa. Su acidez chispeante realza las notas verdes del chipilín, creando un maridaje ligero y armonioso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con aromas de piña, melocotón y un toque de vainilla, que aporta una suavidad que envuelve la sopa. Su textura rica y acidez equilibrada complementan la delicadeza de las bolitas de masa, ofreciendo un contrapunto reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Santo Tomás Sauvignon Blanc", 
                 "notas": "Con notas de limón, pomelo y un toque de albahaca, este Sauvignon Blanc ofrece una frescura herbácea que resalta el chipilín. Su acidez viva y final limpio refrescan el paladar, haciendo que cada sorbo sea un respiro entre cucharadas.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 360}
            ],
            "rosado": [
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Un rosado ligero con aromas de sandía, limón y un toque de menta, que ofrece una frescura que complementa la sopa. Su acidez viva y carácter delicado realzan las hierbas del chipilín, creando un maridaje refrescante y equilibrado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Con notas de frambuesa, pomelo y un toque floral, este rosado aporta una frescura frutal que envuelve la sopa. Su ligereza y acidez equilibrada refrescan el paladar, destacando la textura de las bolitas de masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Un rosado elegante con aromas de cereza, granada y un toque de hierbas provenzales, que ofrece una suavidad que acompaña la sopa. Su cuerpo medio y final refrescante aportan un contrapunto delicado a la riqueza de la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con notas de fresas maduras y cítricos, este rosado ofrece una ligereza que equilibra la sopa. Su acidez viva y final refrescante realzan las notas herbáceas del chipilín, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400}
            ]
        },
        "caracteristica": "ligero"
    },
    "Chalupas Chiapanecas": {
        "descripcion": "Tortillas pequeñas con carne deshebrada y salsa",
        "vinos": {
            "tinto": [
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto ligero con aromas de cereza fresca y un toque de pimienta, que ofrece una suavidad que acompaña la carne deshebrada. Sus taninos suaves y acidez equilibrada realzan la salsa sin opacar la tortilla, creando un maridaje sutil y agradable.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450},
                {"nombre": "Monte Xanic Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de frutos negros como mora y cassis, entrelazados con notas de especias tostadas. Su estructura tánica firme abraza la intensidad de la salsa, potenciando la jugosidad de la carne y dejando un final cálido que complementa la tortilla.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Con aromas de cereza madura, rosa y un toque terroso, este Nebbiolo aporta una elegancia que resalta la carne deshebrada. Sus taninos suaves y acidez brillante cortan la riqueza de la salsa, ofreciendo un equilibrio refinado con la tortilla.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con notas de mora, pimienta negra y un dejo ahumado que evoca la preparación de la carne. Su cuerpo pleno y taninos marcados potencian la salsa, creando una armonía intensa y satisfactoria con las chalupas.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Sauvignon Blanc", 
                 "notas": "Crispado y lleno de energía, este Sauvignon Blanc ofrece notas de toronja, maracuyá y hierbas frescas, que aportan una frescura vibrante a las chalupas. Su acidez chispeante realza la salsa y refresca el paladar tras la carne deshebrada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Un blanco fresco con aromas de manzana verde, cítricos y un toque de miel, que aporta una ligereza que contrarresta la intensidad de la salsa. Su acidez viva eleva la carne, ofreciendo un respiro entre cada bocado de tortilla.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de piña, vainilla y un toque de mantequilla, que envuelve las chalupas con suavidad. Su textura rica y acidez equilibrada complementan la carne deshebrada, suavizando la salsa con elegancia.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Tres Valles Viognier", 
                 "notas": "Un blanco floral con aromas de jazmín, durazno y un toque de miel, que ofrece una suavidad que contrasta con la salsa. Su cuerpo medio y final refrescante aportan un contrapunto delicado a la intensidad de las chalupas.", 
                 "region": "Valle de San Vicente, Baja California", "precio": 450}
            ],
            "rosado": [
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral, que aporta una frescura frutal que envuelve la carne deshebrada. Su ligereza y acidez equilibrada refrescan el paladar, destacando la textura crujiente de la tortilla.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Con notas de cereza, granada y un toque de hierbas, este rosado ofrece una elegancia que suaviza la intensidad de la salsa. Su cuerpo medio y final refrescante complementan la carne, creando un maridaje delicado y jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con notas de fresas y cítricos, este rosado aporta una ligereza que equilibra la riqueza de las chalupas. Su acidez viva y final refrescante resaltan la carne deshebrada, haciendo cada bocado más vibrante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado limpia el paladar con su acidez viva. Su carácter sutil realza la salsa y la carne, ofreciendo un contraste fresco con la tortilla.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "picante"
    },
    "Poc Chuc": {
        "descripcion": "Carne de cerdo marinada en cítricos y asada a la parrilla",
        "vinos": {
            "tinto": [
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con aromas de mora, pimienta y un toque ahumado que evoca la parrilla. Su estructura robusta y taninos marcados acompañan la intensidad de la marinada, mientras su final largo resuena con los cítricos del poc chuc.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600},
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Este Merlot sedoso ofrece una paleta de ciruelas maduras y cerezas, con toques de vainilla que aportan suavidad. Su cuerpo medio y taninos aterciopelados envuelven la carne asada, realzando la jugosidad y los cítricos de la marinada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "Santo Tomás Cabernet Sauvignon", 
                 "notas": "Con aromas de cassis, grosella y un toque de cedro, este Cabernet ofrece una estructura firme que soporta la intensidad del poc chuc. Sus taninos elegantes y acidez equilibrada realzan los cítricos, creando un maridaje clásico y satisfactorio.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 500},
                {"nombre": "El Cielo G&G (Grenache)", 
                 "notas": "Un Grenache frutal que despliega aromas de frambuesa, fresa y un toque de especias dulces. Su ligereza y frescura frutal aportan un contrapunto jugoso a la carne asada, mientras su acidez viva resalta los cítricos de la marinada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650}
            ],
            "blanco": [
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de piña, vainilla y un toque de mantequilla, que ofrece una suavidad que contrasta con la intensidad de la carne. Su acidez equilibrada y textura rica complementan los cítricos, creando un maridaje reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Monte Xanic Sauvignon Blanc", 
                 "notas": "Crispado y lleno de vida, este Sauvignon Blanc despliega aromas de toronja, maracuyá y hierbas frescas, que aportan una frescura vibrante que resalta los cítricos del poc chuc. Su acidez chispeante limpia el paladar tras cada bocado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Fresco y afrutado, con aromas de manzana verde, pera y un toque de miel, este Chenin Blanc ofrece una ligereza que refresca el paladar. Su acidez viva y carácter jugoso realzan la marinada, creando un contraste armonioso con la carne asada.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "Santo Tomás Sauvignon Blanc", 
                 "notas": "Un blanco herbáceo con notas de limón, pomelo y un toque de albahaca, que aporta una frescura que complementa los cítricos del poc chuc. Su acidez crujiente y final limpio ofrecen un respiro tras la intensidad de la carne.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 360}
            ],
            "rosado": [
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Un rosado elegante con aromas de cereza, granada y un toque de hierbas provenzales, que ofrece una suavidad que acompaña la carne asada. Su frescura equilibrada y textura sutil realzan los cítricos, creando un maridaje delicado y jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Con notas de frambuesa, pomelo y un toque floral, este rosado aporta una frescura frutal que envuelve el poc chuc. Su ligereza y acidez viva refrescan el paladar, destacando la textura de la carne y los cítricos de la marinada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas de fresas maduras y cítricos, este rosado ofrece una ligereza que equilibra la intensidad del poc chuc. Su acidez viva y final refrescante realzan la carne, creando un maridaje armonioso y vibrante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía, limón y un toque de menta, este rosado limpia el paladar con su acidez viva, realzando los cítricos y ofreciendo un contrapunto fresco a la carne asada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "cítrico"
    },
    "Queso Relleno": {
        "descripcion": "Queso de bola relleno de carne molida y especias",
        "vinos": {
            "tinto": [
                {"nombre": "El Cielo Orion (Cabernet-Malbec)", 
                 "notas": "Un blend potente que combina la estructura del Cabernet con la suavidad del Malbec, ofreciendo aromas de zarzamora, cereza negra y un toque de pimienta. Su intensidad y taninos firmes abrazan la riqueza del queso y la carne, mientras su final prolongado resuena con las especias del relleno.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 750},
                {"nombre": "Monte Xanic Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis, mora y un toque de cedro, que aporta una estructura firme para soportar la intensidad del queso relleno. Sus taninos elegantes y acidez equilibrada realzan las especias, creando un maridaje clásico y satisfactorio.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Con aromas de rosa, cereza madura y un toque terroso, este Nebbiolo ofrece una elegancia que complementa la carne molida. Sus taninos suaves y acidez brillante cortan la untuosidad del queso, equilibrando el platillo con refinamiento.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con notas de mora, pimienta y un dejo ahumado, que resuena con las especias del relleno. Su cuerpo pleno y taninos marcados envuelven el queso, creando una armonía intensa y cálida.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600}
            ],
            "blanco": [
                {"nombre": "Casa Madero Semillón", 
                 "notas": "Un blanco suave con aromas de pera, melocotón y un toque de miel, que ofrece una textura sedosa que contrasta la intensidad del queso. Su acidez equilibrada y cuerpo medio aportan frescura, realzando las especias de la carne.", 
                 "region": "Valle de Parras, Coahuila", "precio": 380},
                {"nombre": "Monte Xanic Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de mantequilla, vainilla y piña madura, que envuelve el queso con su textura rica. Su acidez equilibrada corta la grasa, ofreciendo un contrapunto elegante y reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "L.A. Cetto Chenin Blanc", 
                 "notas": "Fresco y afrutado, con aromas de manzana verde, pera y un toque de miel, este Chenin Blanc aporta una ligereza que aligera la riqueza del queso. Su acidez viva resalta las especias, creando un maridaje dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 320},
                {"nombre": "Santo Tomás Sauvignon Blanc", 
                 "notas": "Un blanco herbáceo con notas de limón, pomelo y albahaca, que ofrece una frescura vibrante para contrarrestar la intensidad del queso. Su acidez crujiente limpia el paladar, destacando los sabores de la carne.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 360}
            ],
            "rosado": [
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas de fresas maduras y cítricos, este rosado ofrece una ligereza que equilibra la riqueza del queso. Su acidez viva y final refrescante realzan la carne, creando un maridaje armonioso y vibrante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado frutal con notas de frambuesa, pomelo y un toque floral, que aporta una frescura que corta la untuosidad del queso. Su textura suave y acidez equilibrada complementan las especias, ofreciendo un contrapunto alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza, granada y hierbas, este rosado ofrece una suavidad que acompaña el queso. Su cuerpo medio y frescura equilibrada realzan la carne, creando un maridaje delicado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado limpia el paladar con su acidez viva. Su carácter sutil resalta las especias, ofreciendo un respiro tras la riqueza del queso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "rico"
    },
    "Tostadas de Pata": {
        "descripcion": "Tostadas con pata de res encurtida y salsa",
        "vinos": {
            "tinto": [
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Un tinto elegante con aromas de cereza, rosa y un toque terroso, que ofrece una estructura que complementa la carne encurtida. Sus taninos suaves y acidez brillante cortan la grasa, realzando la salsa con refinamiento.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Este Merlot sedoso despliega notas de ciruela, mora y vainilla, que envuelven la pata con suavidad. Su cuerpo medio y taninos aterciopelados acompañan la salsa, creando una armonía reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "Casa Madero Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis, grosella y un toque de cedro, que aporta una estructura firme para soportar la intensidad de la salsa. Sus taninos elegantes realzan la carne, ofreciendo un maridaje clásico.", 
                 "region": "Valle de Parras, Coahuila", "precio": 550},
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto frutal con notas de cereza fresca y pimienta, que ofrece una ligereza que acompaña la pata. Sus taninos suaves y acidez equilibrada realzan la salsa, creando un maridaje sutil y agradable.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con aromas de toronja, maracuyá y hierbas frescas, que aporta una frescura que corta la grasa de la pata. Su acidez chispeante realza la salsa, ofreciendo un contrapunto dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Fresco y afrutado, con notas de manzana verde y cítricos, este Chenin Blanc ofrece una ligereza que refresca el paladar. Su acidez viva contrasta con la riqueza de la carne, creando un maridaje jugoso.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con aromas de piña, vainilla y mantequilla, que envuelve la pata con suavidad. Su textura rica y acidez equilibrada complementan la salsa, ofreciendo un contrapunto reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Tres Valles Sauvignon Blanc", 
                 "notas": "Un blanco chispeante con notas de pomelo y maracuyá, que aporta una frescura vibrante para aligerar la intensidad de la pata. Su acidez crujiente limpia el paladar, destacando los sabores de la salsa.", 
                 "region": "Valle de San Vicente, Baja California", "precio": 400}
            ],
            "rosado": [
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado ofrece una frescura que equilibra la riqueza de la pata. Su acidez viva realza la salsa, creando un maridaje delicado y jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado frutal con notas de frambuesa y pomelo, que aporta una ligereza que contrasta con la intensidad de la carne. Su textura suave y acidez equilibrada complementan la salsa, ofreciendo un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza y granada, este rosado ofrece una suavidad que acompaña la pata. Su cuerpo medio y frescura equilibrada realzan la salsa, creando un maridaje delicado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con notas de fresas y cítricos, este rosado aporta una ligereza que refresca el paladar. Su acidez viva y final refrescante resaltan la carne, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400}
            ]
        },
        "caracteristica": "salado"
    },
    "Pichones en Mole": {
        "descripcion": "Pichones cocidos en mole chiapaneco",
        "vinos": {
            "tinto": [
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Un Merlot sedoso con aromas de ciruela, mora y un toque de vainilla, que ofrece una suavidad que abraza la riqueza del mole. Sus taninos aterciopelados y cuerpo medio complementan la carne del pichón, creando una armonía reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con notas de mora, pimienta y un dejo ahumado, que resuena con las especias del mole. Su estructura robusta y taninos marcados envuelven la carne, ofreciendo un maridaje intenso y cálido.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600},
                {"nombre": "El Cielo Orion (Cabernet-Malbec)", 
                 "notas": "Un blend potente que combina la fuerza del Cabernet con la suavidad del Malbec, ofreciendo aromas de zarzamora y chocolate amargo. Su intensidad y taninos firmes dialogan con el mole, elevando la experiencia del pichón.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 750},
                {"nombre": "Santo Tomás Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis y cedro, que aporta una estructura firme para soportar la intensidad del mole. Sus taninos elegantes realzan la carne, creando un maridaje clásico y satisfactorio.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 500}
            ],
            "blanco": [
                {"nombre": "Casa Madero Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de mantequilla y piña madura, que ofrece una textura sedosa que contrasta con el mole. Su acidez equilibrada refresca el paladar, resaltando la suavidad del pichón.", 
                 "region": "Valle de Parras, Coahuila", "precio": 450},
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Fresco y vibrante, con aromas de manzana y cítricos, este Chenin Blanc aporta una acidez chispeante que corta la densidad del mole. Su ligereza resalta la carne, ofreciendo un contrapunto armonioso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "L.A. Cetto Sauvignon Blanc", 
                 "notas": "Crispado y lleno de vida, con notas de toronja y hierbas, este Sauvignon Blanc ofrece una frescura que atraviesa la riqueza del mole. Su acidez vibrante realza el pichón, limpiando el paladar.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 350},
                {"nombre": "Santo Tomás Sauvignon Blanc", 
                 "notas": "Un blanco herbáceo con aromas de limón y albahaca, que aporta una suavidad que contrarresta el mole. Su acidez brillante resalta la carne, creando un maridaje refrescante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 360}
            ],
            "rosado": [
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de fresas y pomelo, que ofrece una frescura frutal que suaviza el mole. Su ligereza y acidez equilibrada resaltan la carne, creando un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con notas de cereza y granada, este rosado ofrece una frescura que contrasta con el mole. Su cuerpo medio complementa el pichón, creando una armonía delicada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con notas de fresas y cítricos, este rosado aporta una ligereza que realza el pichón. Su acidez viva y final refrescante equilibran el mole, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado limpia el paladar tras el mole. Su acidez viva resalta la carne, ofreciendo un contrapunto fresco.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "sabor intenso"
    },
    "Pepita con Tasajo": {
        "descripcion": "Salsa de pepita de calabaza con carne seca de res",
        "vinos": {
            "tinto": [
                {"nombre": "Casa Madero Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis y grosella, que ofrece una estructura firme para soportar la intensidad de la salsa. Sus taninos elegantes realzan la carne, creando un maridaje clásico.", 
                 "region": "Valle de Parras, Coahuila", "precio": 550},
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Este Merlot sedoso despliega notas de ciruela y mora, con un toque de vainilla que aporta suavidad. Su cuerpo medio y taninos aterciopelados acompañan la salsa, ofreciendo una armonía reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Con aromas de cereza y rosa, este Nebbiolo ofrece una elegancia que resalta la carne seca. Su acidez brillante corta la riqueza de la pepita, equilibrando el platillo.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto frutal con notas de cereza y pimienta, que ofrece una ligereza que acompaña la salsa. Sus taninos suaves realzan la carne, creando un maridaje sutil.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Un blanco fresco con aromas de manzana y cítricos, que aporta una acidez chispeante que aligera la pepita. Su ligereza resalta la carne, ofreciendo un contrapunto jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "Casa Madero Semillón", 
                 "notas": "Suave y sedoso, con notas de pera y melocotón, este Semillón ofrece una textura que contrasta con la salsa. Su acidez equilibrada realza la carne, creando un maridaje delicado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 380},
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con aromas de piña y vainilla, que envuelve la salsa con suavidad. Su textura rica y acidez equilibrada complementan la carne, ofreciendo un contrapunto reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Tres Valles Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con notas de pomelo y maracuyá, que aporta una frescura que aligera la intensidad de la pepita. Su acidez crujiente resalta la salsa, creando un maridaje dinámico.", 
                 "region": "Valle de San Vicente, Baja California", "precio": 400}
            ],
            "rosado": [
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas de fresas y cítricos, este rosado ofrece una ligereza que refresca el paladar. Su acidez viva realza la salsa, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado frutal con notas de frambuesa y pomelo, que aporta una frescura que contrasta con la intensidad de la carne. Su textura suave complementa la salsa, ofreciendo un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza y granada, este rosado ofrece una suavidad que acompaña la pepita. Su cuerpo medio realza la carne, creando un maridaje delicado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado limpia el paladar con su acidez viva. Su carácter sutil resalta la salsa, ofreciendo un contrapunto fresco.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "rico"
    },
    "Chiles Rellenos de Queso": {
        "descripcion": "Chiles poblanos rellenos de queso y capeados",
        "vinos": {
            "tinto": [
                {"nombre": "El Cielo G&G (Grenache)", 
                 "notas": "Un Grenache frutal con aromas de frambuesa y fresa, que ofrece una ligereza que acompaña el chile. Sus taninos suaves y acidez equilibrada realzan el queso, creando un maridaje sutil.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "Monte Xanic Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis y mora, que aporta una estructura firme para soportar la intensidad del capeado. Sus taninos elegantes complementan el queso, ofreciendo un maridaje clásico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Con aromas de cereza y rosa, este Nebbiolo ofrece una elegancia que resalta el queso. Su acidez brillante corta la grasa del capeado, equilibrando el platillo.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto frutal con notas de cereza y pimienta, que ofrece una suavidad que acompaña el chile. Sus taninos suaves realzan el queso, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450}
            ],
            "blanco": [
                {"nombre": "L.A. Cetto Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con aromas de toronja y hierbas, que aporta una frescura que resalta el queso. Su acidez chispeante corta la grasa del capeado, ofreciendo un contrapunto dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 350},
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Fresco y afrutado, con notas de manzana y cítricos, este Chenin Blanc ofrece una ligereza que aligera el platillo. Su acidez viva resalta el chile, creando un maridaje jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "Casa Madero Chardonnay", 
                 "notas": "Un Chardonnay cremoso con aromas de piña y vainilla, que envuelve el queso con suavidad. Su textura rica complementa el capeado, ofreciendo un maridaje reconfortante.", 
                 "region": "Valle de Parras, Coahuila", "precio": 450},
                {"nombre": "Santo Tomás Sauvignon Blanc", 
                 "notas": "Un blanco herbáceo con notas de limón y albahaca, que aporta una frescura que resalta el chile. Su acidez crujiente refresca el paladar, creando un maridaje ligero.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 360}
            ],
            "rosado": [
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza y granada, este rosado ofrece una suavidad que acompaña el queso. Su frescura equilibrada realza el capeado, creando un maridaje delicado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado frutal con notas de frambuesa y pomelo, que aporta una ligereza que contrasta con la intensidad del chile. Su acidez viva resalta el queso, ofreciendo un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con notas de fresas y cítricos, este rosado ofrece una ligereza que refresca el paladar. Su acidez viva realza el capeado, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado limpia el paladar con su acidez viva. Su carácter sutil resalta el queso, ofreciendo un contrapunto fresco.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "suave"
    },
    "Nuegados": {
        "descripcion": "Postre de yuca frita con miel de piloncillo",
        "vinos": {
            "tinto": [
                {"nombre": "Santo Tomás Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis y cedro, que ofrece una estructura que contrasta con la dulzura de la miel. Sus taninos elegantes realzan la yuca, creando un maridaje interesante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Este Merlot sedoso despliega notas de ciruela y mora, con un toque de vainilla que complementa la miel. Su suavidad envuelve la yuca, ofreciendo una armonía reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con notas de mora y pimienta, que ofrece un carácter audaz que contrasta con la dulzura. Su cuerpo pleno equilibra la miel, creando un maridaje intenso.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600},
                {"nombre": "El Cielo Orion (Cabernet-Malbec)", 
                 "notas": "Un blend potente con aromas de zarzamora y chocolate, que ofrece una intensidad que soporta la dulzura de la miel. Sus taninos firmes realzan la yuca, creando un maridaje robusto.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 750}
            ],
            "blanco": [
                {"nombre": "Casa Madero Moscatel", 
                 "notas": "Un blanco dulce con aromas de flores y miel, que resuena con la dulzura de la miel de piloncillo. Su suavidad envuelve la yuca, creando un maridaje armonioso.", 
                 "region": "Valle de Parras, Coahuila", "precio": 400},
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Fresco y vibrante, con notas de manzana y cítricos, este Chenin Blanc ofrece una acidez que contrasta con la dulzura. Su ligereza refresca el paladar, realzando la yuca.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con aromas de piña y vainilla, que ofrece una suavidad que complementa la miel. Su textura rica envuelve la yuca, creando un maridaje reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Santo Tomás Sauvignon Blanc", 
                 "notas": "Un blanco herbáceo con notas de limón y albahaca, que aporta una frescura que contrasta con la dulzura. Su acidez crujiente refresca el paladar, ofreciendo un contrapunto dinámico.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 360}
            ],
            "rosado": [
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado frutal con aromas de frambuesa y pomelo, que ofrece una frescura que suaviza la dulzura de la miel. Su ligereza y acidez equilibrada realzan la yuca, creando un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con notas de cereza y granada, este rosado ofrece una suavidad que acompaña la miel. Su cuerpo medio complementa la yuca, creando una armonía delicada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con notas de fresas y cítricos, este rosado aporta una ligereza que refresca el paladar. Su acidez viva realza la dulzura, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado limpia el paladar con su acidez viva. Su carácter sutil resalta la yuca, ofreciendo un contrapunto fresco.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ]
        },
        "caracteristica": "dulce"
    },
    "Sopa de Pan": {
        "descripcion": "Sopa con pan, pasas, plátano y especias",
        "vinos": {
            "tinto": [
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Un Merlot sedoso con aromas de ciruela y mora, que ofrece una suavidad que abraza las especias de la sopa. Sus taninos aterciopelados complementan las pasas, creando una armonía reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "Casa Madero Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis y cedro, que aporta una estructura firme para soportar el dulzor de la sopa. Sus taninos elegantes realzan las especias, ofreciendo un maridaje clásico.", 
                 "region": "Valle de Parras, Coahuila", "precio": 550},
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto frutal con notas de cereza y pimienta, que ofrece una ligereza que acompaña la sopa. Sus taninos suaves realzan las pasas, creando un maridaje sutil.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450},
                {"nombre": "El Cielo G&G (Grenache)", 
                 "notas": "Un Grenache frutal con aromas de frambuesa y fresa, que ofrece una frescura que contrasta con el dulzor. Su acidez viva resalta las especias, creando un maridaje dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650}
            ],
            "blanco": [
                {"nombre": "Casa Madero Semillón", 
                 "notas": "Un blanco suave con aromas de pera y melocotón, que ofrece una textura sedosa que complementa la sopa. Su acidez equilibrada realza las pasas, creando un maridaje delicado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 380},
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Fresco y vibrante, con notas de manzana y cítricos, este Chenin Blanc ofrece una acidez que aligera la sopa. Su ligereza refresca el paladar, ofreciendo un contrapunto jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con aromas de piña y vainilla, que envuelve la sopa con suavidad. Su textura rica complementa las especias, ofreciendo un maridaje reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Santo Tomás Moscatel", 
                 "notas": "Un blanco dulce con aromas de flores y miel, que resuena con el dulzor de la sopa. Su suavidad abraza las pasas, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 420}
            ],
            "rosado": [
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía y cítricos, este rosado ofrece una frescura que contrasta con el dulzor. Su acidez viva resalta las especias, creando un maridaje dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado frutal con notas de frambuesa y pomelo, que aporta una ligereza que suaviza la sopa. Su textura suave complementa las pasas, ofreciendo un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza y granada, este rosado ofrece una suavidad que acompaña la sopa. Su cuerpo medio realza las especias, creando un maridaje delicado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con notas de fresas y cítricos, este rosado aporta una ligereza que refresca el paladar. Su acidez viva resalta el dulzor, creando un maridaje armonioso.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400}
            ]
        },
        "caracteristica": "dulce"
    },
    "Tamales de Chipilín": {
        "descripcion": "Tamales elaborados con masa de maíz y chipilín, una hierba aromática que aporta un sabor herbal y terroso.",
        "vinos": {
            "tinto": [
                {"nombre": "Monte Xanic Cabernet Sauvignon", 
                 "notas": "Un tinto robusto que despliega una sinfonía de frutos negros maduros, como mora y ciruela, entrelazados con matices de cacao y especias tostadas. Su estructura tánica firme abraza la textura terrosa del chipilín, potenciando las notas herbales y dejando un final prolongado que armoniza con la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "Barón Balché Siete", 
                 "notas": "Este blend complejo combina notas de cassis, cereza negra y un toque de cuero, con matices de tabaco y clavo provenientes de su crianza en barrica. Su cuerpo pleno y taninos elegantes resaltan la profundidad del chipilín, ofreciendo un contrapunto sofisticado a la simplicidad de la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 700},
                {"nombre": "Vinos Don Leo Cabernet Sauvignon", 
                 "notas": "Un Cabernet intenso con aromas de grosella negra, pimiento verde y un dejo ahumado. Su estructura firme y taninos pulidos dialogan con el carácter herbal del chipilín, mientras su final especiado envuelve la masa en una experiencia cálida y equilibrada.", 
                 "region": "Valle de Parras, Coahuila", "precio": 680},
                {"nombre": "Adobe Guadalupe Gabriel", 
                 "notas": "Un blend de Cabernet y Merlot que ofrece aromas de frutos rojos maduros, violeta y un toque de cacao. Su textura aterciopelada y acidez vibrante complementan la ligereza del tamal, realzando las notas terrosas del chipilín con elegancia.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 720}
            ],
            "blanco": [
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Fresco y vibrante, este Chenin Blanc despliega un bouquet de manzana verde, pera y cítricos como limón, con un toque sutil de miel. Su acidez chispeante corta la densidad de la masa y refresca el paladar, resaltando las notas herbales del chipilín con un equilibrio delicado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "Mogor Badan Chardonnay", 
                 "notas": "Un Chardonnay elegante con aromas de melocotón, manzana asada y un toque de avellana tostada. Su textura cremosa y acidez equilibrada envuelven la masa, mientras su frescura resalta el chipilín, creando un maridaje suave y sofisticado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Cava Maciel Blanco", 
                 "notas": "Un blanco fresco con notas de cítricos como lima y pomelo, acompañadas de matices florales y un toque mineral. Su ligereza y acidez vibrante cortan la densidad del tamal, realzando las notas verdes del chipilín con un final refrescante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420},
                {"nombre": "Vinicola Tres Raíces Sauvignon Blanc", 
                 "notas": "Crispado y lleno de vida, este Sauvignon Blanc ofrece aromas de maracuyá, hierba fresca y un toque de toronja. Su acidez brillante y carácter herbáceo dialogan con el chipilín, limpiando el paladar y destacando la textura de la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400}
            ],
            "rosado": [
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante que combina aromas de fresas frescas y frambuesas con un toque de cítricos como mandarina. Su ligereza y frescura frutal envuelven el chipilín con suavidad, equilibrando sus notas terrosas y aportando un contrapunto jugoso a la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Vinicola San Lorenzo Rosado", 
                 "notas": "Con aromas de granada, cereza fresca y un toque de hierbas mediterráneas, este rosado ofrece una textura sedosa y acidez equilibrada. Su frescura resalta las notas herbales del chipilín, mientras su final limpio complementa la simplicidad del tamal.", 
                 "region": "Valle de Parras, Coahuila", "precio": 460},
                {"nombre": "Tres Valles Rosado", 
                 "notas": "Un rosado ligero con notas de sandía, pomelo y un toque floral que evoca pétalos de rosa. Su acidez viva y carácter refrescante cortan la densidad de la masa, realzando el chipilín con un equilibrio delicado y vibrante.", 
                 "region": "Valle de San Vicente, Baja California", "precio": 430},
                {"nombre": "Château Camou Rosado", 
                 "notas": "Elegante y fresco, este rosado despliega aromas de frutos rojos como fresa y un toque de cítricos. Su textura suave y final refrescante envuelven el tamal, resaltando las notas terrosas del chipilín con un contrapunto jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450}
            ]
        },
        "caracteristica": "herbal"
    },
    "Tamales de Mole": {
        "descripcion": "Tamales rellenos de mole, una salsa rica y compleja con chiles y especias.",
        "vinos": {
            "tinto": [
                {"nombre": "L.A. Cetto Petite Sirah", 
                 "notas": "Un tinto audaz que despliega aromas de frutos negros como mora y arándano, con un trasfondo especiado de pimienta negra y clavo. Sus taninos firmes y cuerpo pleno potencian la complejidad del mole, resaltando sus capas de especias y dejando un final cálido que abraza la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "Casa Grande Shiraz", 
                 "notas": "Este Shiraz intenso ofrece aromas de mora silvestre, cacao amargo y un toque de cuero. Su estructura robusta y taninos pulidos dialogan con la riqueza del mole, mientras su final especiado resuena con las notas picantes, creando un maridaje vibrante.", 
                 "region": "Valle de Parras, Coahuila", "precio": 620},
                {"nombre": "Vinicola Pozo de Luna Merlot", 
                 "notas": "Un Merlot sedoso con aromas de ciruela madura, cereza y un toque de tabaco dulce. Su textura aterciopelada y acidez equilibrada envuelven el mole, suavizando sus especias y complementando la masa con una armonía cálida y reconfortante.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 580},
                {"nombre": "Cuna de Tierra Cabernet Sauvignon", 
                 "notas": "Un Cabernet estructurado con notas de cassis, grosella negra y un toque de menta. Sus taninos firmes y cuerpo medio potencian la intensidad del mole, mientras su final largo resalta las especias, ofreciendo un maridaje elegante y robusto.", 
                 "region": "Dolores Hidalgo, Guanajuato", "precio": 670}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de mantequilla, vainilla y piña madura, gracias a su paso por barrica. Su textura sedosa envuelve el mole, suavizando sus especias, mientras su acidez equilibrada resalta la masa, creando un maridaje rico y reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400},
                {"nombre": "Santo Tomás Viognier", 
                 "notas": "Un blanco floral con aromas de jazmín, durazno maduro y un toque de miel. Su cuerpo medio y suavidad contrarrestan la intensidad del mole, mientras su acidez viva refresca el paladar, resaltando las capas de especias del tamal.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 460},
                {"nombre": "Casa Madero Semillón", 
                 "notas": "Suave y sedoso, este Semillón despliega aromas de pera, melocotón y un toque de cera de abeja. Su textura rica y acidez moderada complementan la densidad del mole, ofreciendo un contrapunto elegante que realza la masa.", 
                 "region": "Valle de Parras, Coahuila", "precio": 390},
                {"nombre": "Vinicola San Juanito Sauvignon Blanc", 
                 "notas": "Un Sauvignon Blanc vibrante con notas de lima, maracuyá y un toque de hierba fresca. Su acidez chispeante corta la riqueza del mole, refrescando el paladar y destacando las notas especiadas del tamal con un final limpio y dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 410}
            ],
            "rosado": [
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, este rosado despliega aromas de fresas maduras y cítricos como naranja sanguina, con un fondo mineral que aporta profundidad. Su ligereza y acidez viva cortan la densidad del mole, refrescando el paladar y resaltando la textura de la masa.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 380},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza, granada y un toque de hierbas provenzales. Su frescura equilibrada y textura suave suavizan las especias del mole, ofreciendo un contrapunto delicado que complementa la riqueza del tamal.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Cava Maciel Rosado", 
                 "notas": "Un rosado ligero con notas de frambuesa, pomelo y un toque de pétalos de rosa. Su acidez vibrante y carácter refrescante limpian el paladar tras el mole, resaltando las especias con un final jugoso y armonioso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 440},
                {"nombre": "Vinicola Pozo de Luna Rosado", 
                 "notas": "Con aromas de sandía, fresa fresca y un toque de cítricos, este rosado ofrece una textura sedosa y frescura que contrarresta la intensidad del mole. Su acidez equilibrada resalta la masa, creando un maridaje alegre y dinámico.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 460}
            ]
        },
        "caracteristica": "especiado"
    },
    "Tamales de Azafrán": {
        "descripcion": "Tamales con azafrán, que les da un color amarillo y un sabor único.",
        "vinos": {
            "tinto": [
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto ligero con aromas de cereza fresca, frambuesa y un toque de pimienta blanca. Su suavidad y taninos delicados acompañan la sutileza del azafrán, resaltando su aroma único mientras envuelve la masa con una calidez frutal.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 420},
                {"nombre": "El Cielo G&G (Grenache)", 
                 "notas": "Un Grenache frutal que despliega aromas de fresa, frambuesa y un toque de especias dulces como canela. Su ligereza y acidez vibrante realzan el carácter aromático del azafrán, ofreciendo un contrapunto jugoso que complementa la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "Château Camou Merlot", 
                 "notas": "Un Merlot elegante con notas de ciruela madura, violeta y un toque de tabaco. Su textura aterciopelada y taninos suaves envuelven el azafrán, resaltando su delicadeza con una armonía cálida que abraza la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 600},
                {"nombre": "Vinicola San Lorenzo Nebbiolo", 
                 "notas": "Con aromas de cereza madura, rosa seca y un toque terroso, este Nebbiolo ofrece una estructura ligera que resalta el azafrán. Su acidez brillante y taninos finos complementan la masa, creando un maridaje refinado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 640}
            ],
            "blanco": [
                {"nombre": "Casa Madero Semillón", 
                 "notas": "Un blanco suave con aromas de pera, melocotón y un toque de cera de abeja. Su textura sedosa y acidez moderada complementan la delicadeza del azafrán, envolviendo la masa con una suavidad que resalta su sabor único.", 
                 "region": "Valle de Parras, Coahuila", "precio": 360},
                {"nombre": "Monte Xanic Viognier", 
                 "notas": "Un blanco floral con aromas de jazmín, albaricoque y un toque de miel. Su cuerpo medio y suavidad realzan el carácter aromático del azafrán, mientras su acidez equilibrada refresca el paladar, creando un maridaje elegante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Cava Maciel Chenin Blanc", 
                 "notas": "Fresco y afrutado, con aromas de manzana verde, cítricos y un toque de flores blancas. Su acidez chispeante y ligereza cortan la densidad de la masa, resaltando el azafrán con un contrapunto refrescante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 430},
                {"nombre": "Vinicola Tres Raíces Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de melocotón, vainilla y un toque de nuez tostada. Su textura rica y acidez equilibrada envuelven el azafrán, complementando la masa con una suavidad que resalta su aroma único.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470}
            ],
            "rosado": [
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, este rosado presenta aromas de sandía, limón y un toque de menta. Su acidez viva y carácter delicado realzan el azafrán, limpiando el paladar y ofreciendo un contrapunto fresco a la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas de fresas maduras y cítricos como naranja sanguina. Su ligereza y acidez equilibrada complementan el azafrán, resaltando su sutileza con un final refrescante que abraza la masa.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Vinicola San Juanito Rosado", 
                 "notas": "Un rosado vibrante con notas de granada, frambuesa y un toque de hierbas frescas. Su textura suave y frescura equilibrada realzan el carácter aromático del azafrán, ofreciendo un maridaje ligero y dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "Cuna de Tierra Rosado", 
                 "notas": "Con aromas de cereza fresca, pomelo y un toque floral, este rosado ofrece una acidez viva que corta la densidad de la masa. Su frescura resalta el azafrán, creando un contrapunto jugoso y armonioso.", 
                 "region": "Dolores Hidalgo, Guanajuato", "precio": 480}
            ]
        },
        "caracteristica": "aromático"
    },
    "Tamales de Cambray": {
        "descripcion": "Tamales dulces con pasas y nueces, típicos de la costa.",
        "vinos": {
            "tinto": [
                {"nombre": "El Cielo Orion (Cabernet-Malbec)", 
                 "notas": "Un blend potente que combina la fuerza del Cabernet con la suavidad del Malbec, ofreciendo aromas de zarzamora, cereza negra y un toque de chocolate amargo. Su intensidad y taninos firmes soportan la dulzura de las pasas, mientras su final largo resalta las nueces.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 700},
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con aromas de mora, pimienta negra y un dejo ahumado. Su estructura robusta y taninos marcados contrastan con la dulzura del tamal, mientras su calidez envuelve las nueces, creando un maridaje audaz.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600},
                {"nombre": "Adobe Guadalupe Kerubiel", 
                 "notas": "Un blend de Syrah y Grenache que despliega aromas de frutos rojos maduros, especias dulces y un toque de cuero. Su textura sedosa y acidez equilibrada complementan las pasas, ofreciendo un contrapunto cálido que resalta las nueces.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 740},
                {"nombre": "Vinicola Pozo de Luna Cabernet Sauvignon", 
                 "notas": "Un Cabernet estructurado con notas de cassis, grosella y un toque de tabaco. Sus taninos firmes y cuerpo medio soportan la dulzura del tamal, mientras su final especiado realza las nueces, creando un maridaje elegante.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 690}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Fresco y vibrante, este Chenin Blanc despliega aromas de manzana verde, pera y un toque de miel. Su acidez chispeante corta la dulzura de las pasas, refrescando el paladar y resaltando las nueces con un equilibrio jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 380},
                {"nombre": "Casa Madero Moscatel", 
                 "notas": "Un blanco dulce con aromas de flores blancas, miel y un toque de cítricos. Su suavidad y dulzura natural resuenan con las pasas, envolviendo las nueces con una textura sedosa que crea un maridaje armonioso.", 
                 "region": "Valle de Parras, Coahuila", "precio": 400},
                {"nombre": "Santo Tomás Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de piña, vainilla y un toque de mantequilla. Su textura rica y acidez equilibrada complementan la dulzura del tamal, resaltando las nueces con una suavidad reconfortante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450},
                {"nombre": "Cava Maciel Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con aromas de maracuyá, lima y un toque de hierba fresca. Su acidez chispeante y frescura cortan la dulzura de las pasas, ofreciendo un contrapunto dinámico que resalta las nueces.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ],
            "rosado": [
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza, granada y un toque de hierbas provenzales. Su frescura equilibrada y textura suave suavizan la dulzura de las pasas, resaltando las nueces con un contrapunto delicado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su ligereza y acidez viva refrescan el paladar, complementando las pasas y resaltando las nueces con un final jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Vinicola San Lorenzo Rosado", 
                 "notas": "Con aromas de granada, cereza fresca y un toque de hierbas, este rosado ofrece una textura sedosa y frescura que contrarresta la dulzura. Su acidez equilibrada resalta las nueces, creando un maridaje alegre.", 
                 "region": "Valle de Parras, Coahuila", "precio": 460},
                {"nombre": "Château Camou Rosado", 
                 "notas": "Fresco y elegante, con notas de fresa, pomelo y un toque mineral. Su acidez viva y textura suave envuelven las pasas, ofreciendo un contrapunto refrescante que resalta las nueces.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470}
            ]
        },
        "caracteristica": "dulce"
    },
    "Tamales de Bola": {
        "descripcion": "Tamales con dos masas y chile Simojovel, símbolo de Simojovel de Allende.",
        "vinos": {
            "tinto": [
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con aromas de mora, pimienta negra y un toque ahumado que resuena con el chile. Su estructura robusta y taninos marcados potencian la intensidad del Simojovel, mientras su final cálido abraza la masa.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600},
                {"nombre": "Monte Xanic Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis, mora y un toque de especias tostadas. Su estructura tánica firme dialoga con el picante del chile, resaltando la textura de la masa con un final largo y equilibrado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "Cuna de Tierra Nebbiolo", 
                 "notas": "Un Nebbiolo elegante con aromas de cereza madura, rosa seca y un toque terroso. Sus taninos suaves y acidez brillante cortan la intensidad del chile, ofreciendo un contrapunto refinado que resalta la masa.", 
                 "region": "Dolores Hidalgo, Guanajuato", "precio": 670},
                {"nombre": "Barón Balché Tres", 
                 "notas": "Un blend complejo con notas de frutos negros, cacao y un toque de vainilla. Su cuerpo pleno y taninos pulidos potencian el chile Simojovel, mientras su final especiado complementa la textura de la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 720}
            ],
            "blanco": [
                {"nombre": "L.A. Cetto Sauvignon Blanc", 
                 "notas": "Crispado y lleno de vida, este Sauvignon Blanc ofrece aromas de toronja, maracuyá y hierbas frescas. Su acidez chispeante corta la intensidad del chile, refrescando el paladar y resaltando la textura de la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 320},
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Fresco y afrutado, con aromas de manzana verde, pera y un toque de miel. Su acidez viva y ligereza contrarrestan el picante del chile, ofreciendo un contrapunto jugoso que complementa la masa.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "Mogor Badan Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con notas de lima, hierba fresca y un toque mineral. Su acidez brillante y frescura cortan la intensidad del Simojovel, limpiando el paladar y resaltando la textura de la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 460},
                {"nombre": "Vinicola Tres Raíces Viognier", 
                 "notas": "Un blanco floral con aromas de albaricoque, jazmín y un toque de miel. Su suavidad y acidez equilibrada suavizan el picante, envolviendo la masa con un contrapunto elegante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480}
            ],
            "rosado": [
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su ligereza y acidez viva refrescan el paladar tras el picante del chile, resaltando la textura de la masa con un final jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza, granada y un toque de hierbas. Su frescura equilibrada suaviza el chile, ofreciendo un contrapunto delicado que complementa la masa.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Cava Maciel Rosado", 
                 "notas": "Un rosado ligero con notas de frambuesa, pomelo y pétalos de rosa. Su acidez vibrante limpia el paladar tras el Simojovel, resaltando la masa con un final refrescante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 440},
                {"nombre": "Vinicola San Juanito Rosado", 
                 "notas": "Con aromas de granada, fresa fresca y un toque de cítricos, este rosado ofrece una frescura que contrarresta el picante. Su textura suave resalta la masa, creando un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450}
            ]
        },
        "caracteristica": "picante"
    },
    "Huevos a la Chiapaneca": {
        "descripcion": "Platillo de desayuno con huevos, frijoles y tortillas.",
        "vinos": {
            "tinto": [
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto ligero con aromas de cereza fresca, frambuesa y un toque de pimienta blanca. Su suavidad y taninos delicados acompañan la simplicidad de los huevos, resaltando los frijoles con una calidez frutal que no opaca las tortillas.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 420},
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Un Nebbiolo elegante con aromas de cereza madura, rosa seca y un toque terroso. Sus taninos suaves y acidez brillante complementan los frijoles, ofreciendo un contrapunto refinado que resalta la textura de las tortillas.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Cuna de Tierra Merlot", 
                 "notas": "Un Merlot sedoso con notas de ciruela, mora y un toque de tabaco dulce. Su textura aterciopelada y taninos suaves envuelven los huevos, complementando los frijoles con una armonía cálida.", 
                 "region": "Dolores Hidalgo, Guanajuato", "precio": 610},
                {"nombre": "Vinicola Pozo de Luna Grenache", 
                 "notas": "Un Grenache frutal con aromas de fresa, frambuesa y un toque de especias dulces. Su ligereza y acidez equilibrada realzan los huevos, ofreciendo un contrapunto jugoso que resalta los frijoles.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 590}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Sauvignon Blanc", 
                 "notas": "Crispado y lleno de vida, este Sauvignon Blanc ofrece aromas de toronja, maracuyá y hierbas frescas. Su acidez chispeante realza los sabores de los huevos, refrescando el paladar y complementando los frijoles con un final limpio.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 390},
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Fresco y afrutado, con aromas de manzana verde, pera y un toque de miel. Su acidez viva y ligereza cortan la densidad de los frijoles, ofreciendo un contrapunto jugoso que resalta las tortillas.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "Mogor Badan Chardonnay", 
                 "notas": "Un Chardonnay elegante con aromas de melocotón, manzana asada y un toque de avellana. Su textura cremosa y acidez equilibrada envuelven los huevos, complementando los frijoles con una suavidad sofisticada.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 480},
                {"nombre": "Vinicola Tres Raíces Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con notas de maracuyá, hierba fresca y un toque de toronja. Su acidez brillante y frescura cortan la riqueza de los frijoles, resaltando los huevos con un final dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 400}
            ],
            "rosado": [
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, este rosado presenta aromas de sandía, limón y un toque de menta. Su acidez viva y carácter delicado cortan la densidad de los frijoles, resaltando los huevos con un contrapunto fresco.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su ligereza y acidez equilibrada refrescan el paladar, complementando los frijoles y resaltando las tortillas.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas de fresas maduras y cítricos. Su ligereza y acidez viva realzan los huevos, ofreciendo un contrapunto refrescante que complementa los frijoles.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Vinicola San Juanito Rosado", 
                 "notas": "Con aromas de granada, fresa fresca y un toque de cítricos, este rosado ofrece una frescura que contrarresta la riqueza de los frijoles. Su textura suave resalta los huevos, creando un maridaje alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450}
            ]
        },
        "caracteristica": "suave"
    },
    "Ningüijuti": {
        "descripcion": "Mole de cerdo con semillas, típico de Chiapas.",
        "vinos": {
            "tinto": [
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Un Merlot sedoso con aromas de ciruela madura, mora y un toque de vainilla. Su textura aterciopelada y taninos suaves envuelven la riqueza del mole, resaltando la jugosidad del cerdo con una armonía cálida.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Casa Grande Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis, grosella negra y un toque de especias tostadas. Su estructura tánica firme dialoga con la intensidad del mole, resaltando las semillas con un final largo y equilibrado.", 
                 "region": "Valle de Parras, Coahuila", "precio": 630},
                {"nombre": "Adobe Guadalupe Serafiel", 
                 "notas": "Un blend de Syrah y Grenache con aromas de frutos rojos maduros, pimienta y un toque de cacao. Su textura sedosa y acidez equilibrada complementan el cerdo, ofreciendo un contrapunto cálido que resalta el mole.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 710},
                {"nombre": "Vinicola Pozo de Luna Shiraz", 
                 "notas": "Un Shiraz especiado con notas de mora, clavo y un toque ahumado. Su cuerpo pleno y taninos pulidos potencian la riqueza del mole, mientras su final cálido resalta las semillas.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 670}
            ],
            "blanco": [
                {"nombre": "Casa Madero Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de mantequilla, piña madura y un toque de vainilla. Su textura sedosa suaviza las especias del mole, mientras su acidez equilibrada resalta la jugosidad del cerdo.", 
                 "region": "Valle de Parras, Coahuila", "precio": 400},
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Fresco y vibrante, con aromas de manzana verde, pera y un toque de miel. Su acidez chispeante corta la densidad del mole, refrescando el paladar y complementando el cerdo.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 380},
                {"nombre": "Santo Tomás Viognier", 
                 "notas": "Un blanco floral con aromas de jazmín, albaricoque y un toque de miel. Su suavidad y cuerpo medio contrarrestan la intensidad del mole, resaltando las semillas con un contrapunto elegante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 460},
                {"nombre": "Cava Maciel Blanco", 
                 "notas": "Un blanco fresco con notas de cítricos, flores blancas y un toque mineral. Su ligereza y acidez vibrante limpian el paladar tras el mole, resaltando el cerdo con un final refrescante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ],
            "rosado": [
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas de fresas maduras y cítricos como naranja sanguina. Su ligereza y acidez viva cortan la riqueza del mole, resalt-cores del cerdo con un final refrescante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 380},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su frescura y textura suave suavizan las especias del mole, complementando el cerdo con un contrapunto alegre.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía, limón y un toque de menta. Su acidez viva limpia el paladar tras el mole, resaltando las semillas con un final jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470},
                {"nombre": "Vinicola San Juanito Rosado", 
                 "notas": "Con aromas de granada, fresa fresca y un toque de cítricos, este rosado ofrece una frescura que contrarresta la intensidad del mole. Su textura suave resalta el cerdo, creando un maridaje dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450}
            ]
        },
        "caracteristica": "rico"
    },
    "Chipilín con Bolitas": {
        "descripcion": "Platillo tradicional con chipilín y bolitas de masa.",
        "vinos": {
            "tinto": [
                {"nombre": "L.A. Cetto Nebbiolo", 
                 "notas": "Un Nebbiolo elegante con aromas de cereza madura, rosa seca y un toque terroso. Sus taninos suaves y acidez brillante complementan las bolitas de masa, resaltando las notas herbales del chipilín con un contrapunto refinado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Santo Tomás Tempranillo", 
                 "notas": "Un tinto ligero con aromas de cereza fresca, frambuesa y un toque de pimienta blanca. Su suavidad y taninos delicados acompañan la simplicidad de las bolitas, resaltando el chipilín con una calidez frutal.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 420},
                {"nombre": "Cuna de Tierra Grenache", 
                 "notas": "Un Grenache frutal con aromas de fresa, frambuesa y un toque de especias dulces. Su ligereza y acidez equilibrada realzan el chipilín, ofreciendo un contrapunto jugoso que complementa las bolitas.", 
                 "region": "Dolores Hidalgo, Guanajuato", "precio": 610},
                {"nombre": "Vinicola Pozo de Luna Merlot", 
                 "notas": "Un Merlot sedoso con notas de ciruela madura, mora y un toque de tabaco dulce. Su textura aterciopelada envuelve las bolitas, resaltando el chipilín con una armonía cálida.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 580}
            ],
            "blanco": [
                {"nombre": "Monte Xanic Viognier", 
                 "notas": "Un blanco floral con aromas de jazmín, albaricoque y un toque de miel. Su suavidad y cuerpo medio realzan las notas herbales del chipilín, envolviendo las bolitas con un contrapunto elegante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420},
                {"nombre": "Casa Madero Chenin Blanc", 
                 "notas": "Fresco y afrutado, con aromas de manzana verde, pera y un toque de miel. Su acidez viva y ligereza cortan la densidad de las bolitas, resaltando el chipilín con un final jugoso.", 
                 "region": "Valle de Parras, Coahuila", "precio": 350},
                {"nombre": "Mogor Badan Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con notas de lima, hierba fresca y un toque mineral. Su acidez brillante y frescura realzan el chipilín, limpiando el paladar tras las bolitas.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 460},
                {"nombre": "Cava Maciel Blanco", 
                 "notas": "Un blanco fresco con notas de cítricos, flores blancas y un toque mineral. Su ligereza y acidez vibrante complementan las bolitas, resaltando el chipilín con un final refrescante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ],
            "rosado": [
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su ligereza y acidez viva refrescan el paladar, resaltando las notas herbales del chipilín con un final jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas RTP de fresas maduras y cítricos. Su ligereza y acidez equilibrada complementan las bolitas, resaltando el chipilín con un contrapunto refrescante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía, limón y un toque de menta. Su acidez viva limpia el paladar, resaltando el chipilín con un final jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470},
                {"nombre": "Vinicola San Juanito Rosado", 
                 "notas": "Con aromas de granada, fresa fresca y un toque de cítricos, este rosado ofrece una frescura que realza el chipilín. Su textura suave complementa las bolitas, creando un maridaje dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450}
            ]
        },
        "caracteristica": "ligero"
    },
    "Cocada": {
        "descripcion": "Postre de coco, huevo y azúcar, a veces con piña.",
        "vinos": {
            "tinto": [
                {"nombre": "El Cielo G&G (Grenache)", 
                 "notas": "Un Grenache frutal que despliega aromas de fresa, frambuesa y un toque de especias dulces. Su ligereza y acidez equilibrada complementan la dulzura del coco, resaltando la piña con un contrapunto jugoso.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 650},
                {"nombre": "Casa Madero Shiraz", 
                 "notas": "Un Shiraz especiado con aromas de mora, pimienta negra y un dejo ahumado. Su estructura robusta contrasta con la dulzura del postre, mientras su calidez envuelve el coco, creando un maridaje audaz.", 
                 "region": "Valle de Parras, Coahuila", "precio": 600},
                {"nombre": "Adobe Guadalupe Kerubiel", 
                 "notas": "Un blend de Syrah y Grenache con aromas de frutos rojos maduros, especias dulces y un toque de cuero. Su textura sedosa complementa el coco, ofreciendo un contrapunto cálido que resalta la piña.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 740},
                {"nombre": "Vinicola Pozo de Luna Merlot", 
                 "notas": "Un Merlot sedoso con notas de ciruela, mora y un toque de tabaco dulce. Su suavidad envuelve la dulzura del postre, resaltando el coco con una armonía cálida.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 580}
            ],
            "blanco": [
                {"nombre": "Casa Madero Moscatel", 
                 "notas": "Un blanco dulce con aromas de flores blancas, miel y un toque de cítricos. Su suavidad y dulzura natural resuenan con el coco, envolviendo la piña con una textura sedosa que crea un maridaje armonioso.", 
                 "region": "Valle de Parras, Coahuila", "precio": 370},
                {"nombre": "Monte Xanic Chenin Blanc", 
                 "notas": "Fresco y vibrante, con aromas de manzana verde, pera y un toque de miel. Su acidez chispeante corta la dulzura del coco, refrescando el paladar y resaltando la piña.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 380},
                {"nombre": "Santo Tomás Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de piña, vainilla y un toque de mantequilla. Su textura rica complementa el coco, resaltando la piña con una suavidad reconfortante.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 450},
                {"nombre": "Cava Maciel Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con aromas de maracuyá, lima y un toque de hierba fresca. Su acidez chispeante contrasta con la dulzura, ofreciendo un contrapunto dinámico que resalta el coco.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ],
            "rosado": [
                {"nombre": "Monte Xanic Rosado", 
                 "notas": "Elegante y sutil, con aromas de cereza, granada y un toque de hierbas provenzales. Su frescura equilibrada suaviza la dulzura del coco, resaltando la piña con un contrapunto delicado.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su ligereza y acidez viva refrescan el paladar, complementando el coco y resaltando la piña.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Vinicola San Lorenzo Rosado", 
                 "notas": "Con aromas de granada, cereza fresca y un toque de hierbas, este rosado ofrece una textura sedosa que contrarresta la dulzura. Su frescura resalta el coco, creando un maridaje alegre.", 
                 "region": "Valle de Parras, Coahuila", "precio": 460},
                {"nombre": "Château Camou Rosado", 
                 "notas": "Fresco y elegante, con notas de fresa, pomelo y un toque mineral. Su acidez viva envuelve el coco, ofreciendo un contrapunto refrescante que resalta la piña.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470}
            ]
        },
        "caracteristica": "dulce"
    },
    "Carne cocida en limón": {
        "descripcion": "Carne cocida con limón, refrescante y cítrica.",
        "vinos": {
            "tinto": [
                {"nombre": "Santo Tomás Cabernet Sauvignon", 
                 "notas": "Un tinto robusto con aromas de cassis, grosella y un toque de cedro. Su estructura tánica firme soporta la acidez del limón, resaltando la jugosidad de la carne con un final equilibrado.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 480},
                {"nombre": "Monte Xanic Merlot", 
                 "notas": "Un Merlot sedoso con aromas de ciruela madura, mora y un toque de vainilla. Su textura aterciopelada complementa la carne, suavizando la acidez del limón con una armonía cálida.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 550},
                {"nombre": "Cuna de Tierra Cabernet Sauvignon", 
                 "notas": "Un Cabernet estructurado con notas de cassis, grosella negra y un toque de menta. Sus taninos firmes dialogan con la acidez, resaltando la carne con un final especiado.", 
                 "region": "Dolores Hidalgo, Guanajuato", "precio": 670},
                {"nombre": "Vinicola Pozo de Luna Grenache", 
                 "notas": "Un Grenache frutal con aromas de fresa, frambuesa y un toque de especias dulces. Su ligereza y acidez equilibrada realzan la acidez del limón, complementando la carne.", 
                 "region": "San Miguel de Allende, Guanajuato", "precio": 590}
            ],
            "blanco": [
                {"nombre": "L.A. Cetto Chardonnay", 
                 "notas": "Un Chardonnay cremoso con notas de piña, vainilla y un toque de mantequilla. Su textura sedosa suaviza la acidez del limón, complementando la carne con una suavidad reconfortante.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 350},
                {"nombre": "Monte Xanic Sauvignon Blanc", 
                 "notas": "Crispado y lleno de vida, con aromas de toronja, maracuyá y hierbas frescas. Su acidez chispeante resalta la acidez del limón, refrescando el paladar y complementando la carne.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 390},
                {"nombre": "Mogor Badan Sauvignon Blanc", 
                 "notas": "Un blanco vibrante con notas de lima, hierba fresca y un toque mineral. Su acidez brillante realza la acidez del limón, limpiando el paladar tras la carne.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 460},
                {"nombre": "Cava Maciel Blanco", 
                 "notas": "Un blanco fresco con notas de cítricos, flores blancas y un toque mineral. Su ligereza y acidez vibrante complementan la carne, resaltando la acidez del limón.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 420}
            ],
            "rosado": [
                {"nombre": "Cava Quintanilla Rosado", 
                 "notas": "Ligero y refrescante, con aromas de sandía, limón y un toque de menta. Su acidez viva y carácter delicado realzan la acidez del limón, complementando la carne con un contrapunto fresco.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 470},
                {"nombre": "El Cielo Rosé", 
                 "notas": "Un rosado vibrante con aromas de frambuesa, pomelo y un toque floral. Su ligereza y acidez viva refrescan el paladar, resaltando la acidez del limón y complementando la carne.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 500},
                {"nombre": "Santo Tomás Rosado", 
                 "notas": "Fresco y jugoso, con aromas de fresas maduras y cítricos. Su ligereza y acidez equilibrada realzan la carne, ofreciendo un contrapunto refrescante que resalta el limón.", 
                 "region": "Valle de Santo Tomás, Baja California", "precio": 400},
                {"nombre": "Vinicola San Juanito Rosado", 
                 "notas": "Con aromas de granada, fresa fresca y un toque de cítricos, este rosado ofrece una frescura que realza la acidez del limón. Su textura suave complementa la carne, creando un maridaje dinámico.", 
                 "region": "Valle de Guadalupe, Baja California", "precio": 450}
            ]
        },
        "caracteristica": "cítrico"
    }
}

def obtener_recomendaciones(platillos, tipo_vino_preferido):
    recomendaciones = {}
    for platillo in platillos:
        if platillo in maridajes:
            vinos_disponibles = maridajes[platillo]["vinos"].get(tipo_vino_preferido, [])
            if vinos_disponibles:
                recomendaciones[platillo] = {
                    "descripcion": maridajes[platillo]["descripcion"],
                    "vinos": vinos_disponibles
                }
            else:
                primer_tipo = next(iter(maridajes[platillo]["vinos"]))
                recomendaciones[platillo] = {
                    "descripcion": maridajes[platillo]["descripcion"],
                    "vinos": maridajes[platillo]["vinos"][primer_tipo]
                }
    return recomendaciones

@app.route('/', methods=['GET', 'POST'])
def inicio():
    recomendaciones = None
    platillos = list(maridajes.keys())
    tipos_vino = ["tinto", "blanco", "rosado"]

    if request.method == 'POST':
        platillos_seleccionados = request.form.getlist('platillos')
        tipo_vino = request.form.get('tipo_vino')
        if platillos_seleccionados and tipo_vino:
            recomendaciones = obtener_recomendaciones(platillos_seleccionados, tipo_vino)

    return render_template('index.html', 
                         platillos=platillos,
                         tipos_vino=tipos_vino,
                         recomendaciones=recomendaciones)

@app.route('/cata')
def cata():
    return render_template('cata.html')

if __name__ == '__main__':
    app.run(debug=True)