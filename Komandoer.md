# Telefonkatalogen - Installasjonsveiledning

## Steg 3: Oppdatere og oppgradere Raspberry Pi

1. Kjør følgende kommandoer for å oppdatere systemet:
   
   ```bash
   sudo apt update
   sudo apt upgrade -y


## Steg 4: Installere nødvendig programvare
1. Installer Python3 og pip:
   
    ```bash
    sudo apt install python3 python3-pip -y
    
3. Installer git for å kunne klone GitHub-repoet:
   
    ```bash
    sudo apt install git -y

Steg 5: Klone GitHub-repoet
1. Klon repoet til Raspberry Pi:
    ```bash
    git clone https://github.com/dittbrukernavn/telefonkatalogen.git
2. Gå inn i prosjektmappen
   ```bash
   cd telefonkatalogen

Steg 6: Installere avhengigheter
1. Installer nødvendige Python-pakker ved å kjøre:
   ```bash
   pip3 install -r requirements.txt

Steg 7: Konfigurere brannmur
1. Installer ufw (Uncomplicated Firewall):
   ```bash
   sudo apt install ufw -y
2. Tillat kun SSH-trafikk:
   ```bash
   sudo ufw allow ssh
3. Aktiver brannmuren
   ```bash
   sudo ufw enable


## Steg 8: Installere og sette opp MariaDB

1. Installer MariaDB-serveren:
   ```bash
   sudo apt install mariadb-server -y
   ```

2. Sikkerhetskonfigurer MariaDB:
   ```bash
   sudo mysql_secure_installation
   ```
   Følg instruksjonene for å sette opp rotpassord og gjøre grunnleggende sikkerhetsinnstillinger.

3. Logg inn på MariaDB:
   ```bash
   sudo mysql -u root -p
   ```

4. Opprett en database for telefonkatalogen:
   ```sql
   CREATE DATABASE telefonkatalog;
   ```

5. Opprett en bruker og gi den nødvendige privilegier:
   ```sql
   CREATE USER 'brukernavn'@'localhost' IDENTIFIED BY 'passord';
   GRANT ALL PRIVILEGES ON telefonkatalog.* TO 'brukernavn'@'localhost';
   FLUSH PRIVILEGES;
   ```

6. Initialiser databasen med tabeller. Kjør SQL-skriptet som definerer strukturen (lagre SQL-skriptet som `schema.sql` i prosjektmappen):
   ```sql
   USE telefonkatalog;
   SOURCE /path/to/schema.sql;
   ```

7. Verifiser at databasen er riktig satt opp ved å kjøre:
   ```sql
   SHOW TABLES;
   ```

8. Avslutt MariaDB:
   ```sql
   EXIT;
   ```








     



