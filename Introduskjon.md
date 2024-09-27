## Telefonkatalogen - Installasjonsveiledning

Introduksjon
Dette prosjektet er en enkel telefonkatalog-applikasjon som kjører på en Raspberry Pi. Prosjektet inkluderer installasjon av operativsystem, oppsett av SSH, brannmur, database, og telefonkatalogens Python-kode. 

Denne veiledningen gir en trinn-for-trinn instruksjon for å sette opp prosjektet fra bunnen av.

**Krav**
**Før du starter, sørg for at du har følgende:**
- En Raspberry Pi (modell 3 eller nyere)
- MicroSD-kort (minst 16 GB)
- Raspberry Pi-strøm kabel
- Ethernet-kabel eller Wi-Fi 
- En annen datamaskin for SSH-tilkobling
- Ubuntu som operativ system



## Steg 1: Installere Ubuntu

1. Last ned **Raspberry Pi Imager** fra den offisielle [Raspberry Pi-nettsiden](https://www.raspberrypi.com/software/).
2. Sett inn MicroSD-kortet i datamaskinen og åpne Raspberry Pi Imager.
3. Velg `Ubuntu` som operativsystem.
4. Velg MicroSD-kortet som mål.
5. Gå til de avanserte innstillingene (gear-ikonet) og:
   - Aktiver SSH.
   - Sett opp Wi-Fi (om nødvendig).
   - Angi lokal bruker og passord for Pi (standard bruker er `pi` og passord `raspberry`).
6. Klikk **Skriv** for å installere OS på MicroSD-kortet.
7. Når prosessen er ferdig, sett MicroSD-kortet inn i Raspberry Pi og start den opp.



## Steg 2: Koble til Raspberry Pi via SSH

1. Åpne terminalen på datamaskinen din.
2. Koble til Raspberry Pi ved å bruke kommandoen:
   ```bash
   ssh pi@raspberrypi.local
