# Artikl Finder 3000
Ime Studenta: Marko Franković

 Kolegij: Raspodijeljeni sustavi

# Pokretanje
Pokretanje:

    Scraperi:
        uvicorn sraper:app --reload --port 8000
        uvicorn sraper:app --reload --port 8001
        uvicorn sraper:app --reload --port 8002

    Collector:
        uvicorn collector:app --reload --port 8003

    Main:
        uvicorn main:app --reload --port 8004

# Usage
Kako bi program radio potrebno je prvo pokrenuti sve fileove. Nakon pokretanja fileova
na početnom endpointu od main.py filea će se prikazati message da je upisano u bazu. Upisivanjem
/menu endpointa prikazati će se glavni menu sa opcijama. Moguće je prikazati sve artikle, prikazati samo artikle
iz željene trgovine, pretražiti željeni artikl u svim trgovinama te povratak na ponovni odabir iz menua.


# Greške
Internal Error Greška - nije resolvana - kod radi tj. upisuje podatke u databazu

SSL Greška - Nije dodana IP Adressa za access Clusteru
