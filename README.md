# TotsRucs Scrapper

Script per extreure (scrapejar) els enllaços de descàrrega (elinks) de https://web.totsrucs.cat.

Exemple d'URL:
https://web.totsrucs.cat/index.php?pagina=series&veure=temporada&id=8213


## Què fa
Donada la URL d'una pàgina de sèrie de totsrucs.cat (com l'exemple anterior), el script:
- Fa una petició HTTP a la pàgina.
- Parseja el HTML i cerca els enllaços que corresponen als capítols
- Exporta la llista d'enllaços trobats a la sortida estàndard o a un fitxer.

L'objectiu és obtenir fàcilment la llista d'enllaços perquè es puguin fer servir en eines de descàrrega.

## Dependències
El script utilitza biblioteques comunes per a scrapping. Si el teu repositori no conté un `requirements.txt`, instal·la-les manualment:

Recomanat: crea i activa un entorn virtual:
- Linux / macOS:
  python3 -m venv .venv
  source .venv/bin/activate

- Windows:
  python -m venv .venv
  .venv\Scripts\activate

### Instal·lar dependències:
- Via requirements.txt: 
  pip install -r requirements.txt

- Instal·lació manual:
  pip install requests beautifulsoup4 lxml

## Ús (exemples)

- Escriure la llista d'enllaços a la consola:
  python3 scrapper.py "https://web.totsrucs.cat/index.php?pagina=series&veure=temporada&id=8213"

- Guardar la sortida a un fitxer:
  python3 scrapper.py "https://web.totsrucs.cat/index.php?pagina=series&veure=temporada&id=8213" > elinks.txt


## Notes
- Evita fer peticions massives en curt temps: considera posar pauses (sleep) entre peticions si iteres sobre moltes pàgines.
- Per a automatitzacions grans, valora fer servir la cache i un User-Agent identificable.
