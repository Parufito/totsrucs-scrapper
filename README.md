# Totsrucs Scrapper

Script de Python per descarregar elinks de sèries de la web Tots Rucs de manera ràpida i automatitzada.

## 📋 Descripció

Aquest scraper permet extreure tots els enllaços de descàrrega (elinks) d'una sèrie de la plataforma Tots Rucs de forma automàtica, sense haver de fer clic un a un a cada capítol. Simplement proporcionant la URL inicial de la sèrie, l'script mostrarà tots els enllaços disponibles de cop.

## ✨ Característiques

- 🚀 Descàrrega ràpida i automatitzada d'elinks
- 📺 Suport per a sèries completes
- 🔗 Extracció d'enllaços sense interacció manual
- 💾 Generació de llista d'enllaços en format text
- ⚡ Procés molt més ràpid que la navegació manual

## 🔧 Requisits

- Python 3.7 o superior
- Llibreries Python necessàries:
  - `requests` - Per fer peticions HTTP
  - `beautifulsoup4` - Per parsejar HTML
  - `lxml` - Parser HTML/XML

## 📦 Instal·lació

1. Clona aquest repositori:
```bash
git clone https://github.com/Parufito/totsrucs-scrapper.git
cd totsrucs-scrapper
```

2. Instal·la les dependències:
```bash
pip install -r requirements.txt
```

O instal·la les llibreries manualment:
```bash
pip install requests beautifulsoup4 lxml
```

## 🚀 Ús

### Ús bàsic

```bash
python totsrucs_scraper.py <URL_DE_LA_SERIE>
```

### Exemple

```bash
python totsrucs_scraper.py https://www.totsrucs.com/series/nom-de-la-serie
```

### Opcions

El script pot acceptar diverses opcions (segons la implementació):

- Especificar l'arxiu de sortida on guardar els enllaços
- Filtrar per temporada o capítol específic
- Exportar en diferents formats (TXT, CSV, JSON)

## 📂 Estructura de sortida

Els enllaços es guarden en un arxiu de text pla, un enllaç per línia, que pots utilitzar amb gestors de descàrregues com JDownloader, wget o similars.

Exemple de sortida:
```
https://elink.example.com/serie-S01E01
https://elink.example.com/serie-S01E02
https://elink.example.com/serie-S01E03
...
```

## ⚠️ Notes importants

- Aquest scraper està dissenyat exclusivament per a ús personal i educatiu
- Respecta els termes i condicions de la plataforma Tots Rucs
- No abuses del servei fent massa peticions seguides
- Assegura't de tenir els permisos adequats per descarregar el contingut

## 🤝 Contribucions

Les contribucions són benvingudes! Si tens suggeriments o millores:

1. Fes un fork del projecte
2. Crea una branca per la teva funcionalitat (`git checkout -b feature/nova-funcio`)
3. Fes commit dels teus canvis (`git commit -m 'Afegeix nova funcionalitat'`)
4. Puja la branca (`git push origin feature/nova-funcio`)
5. Obre un Pull Request

## 📝 Llicència

Aquest projecte és de codi obert i està disponible sota la llicència que especifiquis.

## 🐛 Problemes coneguts / Solució de problemes

Si et trobes amb errors:

- Verifica que tens totes les dependències instal·lades
- Comprova que la URL de la sèrie és correcta i accessible
- Assegura't que tens connexió a Internet
- Si el web ha canviat la seva estructura, pot ser necessari actualitzar el scraper

## 📧 Contacte

Per a preguntes o suggeriments, obre un issue en aquest repositori.

---

**Disclaimer**: Aquest projecte no està afiliat amb Tots Rucs i és només per a propòsits educatius.
