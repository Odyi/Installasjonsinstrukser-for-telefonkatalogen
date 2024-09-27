import sqlite3  # Import SQLite3 library to work with the SQL database in Python
import os

# Ensure the directory for the database exists
os.makedirs('/home/pi/telefonkatalog', exist_ok=True)

# Connect to the SQLite database located in the Raspberry Pi
conn = sqlite3.connect('/home/pi/telefonkatalog/telefonkatalog.db')
cursor = conn.cursor()  # Create a cursor object to interact with the database

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS personer (
               fornavn TEXT,
               etternavn TEXT,
               telefonnummer TEXT
            )''')
conn.commit()  # Save changes to the database

# Function to display all people in the database
def visAllePersoner():
    cursor.execute("SELECT * FROM personer")
    resultater = cursor.fetchall()
    if not resultater:
        print("Det er ingen registrerte personer i katalogen")
    else:
        print("**************************************************************************")
        for person in resultater:
            print("Fornavn: {:15s} Etternavn: {:15s} Telefonnummer: {:8s}"
                  .format(person[0], person[1], person[2]))
        print("**************************************************************************")
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

# Function to add a new person to the database
def legg_til_person_i_db(fornavn, etternavn, telefonnummer):
    cursor.execute("INSERT INTO personer (fornavn, etternavn, telefonnummer) VALUES (?, ?, ?)",
                   (fornavn, etternavn, telefonnummer))
    conn.commit()

# Function to delete a person from the database
def slett_person_fra_db(fornavn, etternavn, telefonnummer):
    cursor.execute("DELETE FROM personer WHERE fornavn=? AND etternavn=? AND telefonnummer=?",
                   (fornavn, etternavn, telefonnummer))
    conn.commit()

# Function to display the menu
def printMeny():
    print("------------------- Telefonkatalog -------------------")
    print("| 1. Legg til ny person                              |")
    print("| 2. Søk opp person eller telefonnummer              |")
    print("| 3. Vis alle personer                               |")
    print("| 4. Avslutt                                         |")
    print("------------------------------------------------------")
    menyvalg = input("Skriv inn tall for å velge fra menyen: ")
    utfoerMenyvalg(menyvalg)

# Function to execute the menu selection
def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        registrerPerson()
    elif valgtTall == "2":
        sokPerson()
    elif valgtTall == "3":
        visAllePersoner()
    elif valgtTall == "4":
        bekreftelse = input("Er du sikker på at du vil avslutte? J/N: ")
        if bekreftelse.lower() == "j":
            conn.close()
            exit()
        else:
            printMeny()
    else:
        print("Ugyldig valg. Velg et tall mellom 1-4.")
        printMeny()

# Function to register a new person
def registrerPerson():
    fornavn = input("Skriv inn fornavn: ")
    etternavn = input("Skriv inn etternavn: ")
    telefonnummer = input("Skriv inn telefonnummer: ")

    legg_til_person_i_db(fornavn, etternavn, telefonnummer)  # Add the person to the database

    print("{0} {1} er registrert med telefonnummer {2}".format(fornavn, etternavn, telefonnummer))
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

# Function to search for a person
def sokPerson():
    print("1. Søk på fornavn")
    print("2. Søk på etternavn")
    print("3. Søk på telefonnummer")
    print("4. Tilbake til hovedmeny")
    sokefelt = input("Velg ønsket søk 1-3, eller 4 for å gå tilbake: ")
    if sokefelt == "1":
        navn = input("Fornavn: ")
        finnPerson("fornavn", navn)
    elif sokefelt == "2":
        navn = input("Etternavn: ")
        finnPerson("etternavn", navn)
    elif sokefelt == "3":
        tlfnummer = input("Telefonnummer: ")
        finnPerson("telefonnummer", tlfnummer)
    elif sokefelt == "4":
        printMeny()
    else:
        print("Ugyldig valg. Velg et tall mellom 1-4.")
        sokPerson()

# Function to find a person based on search criteria
def finnPerson(typeSok, sokeTekst):
    kolonne = {"fornavn": "fornavn", "etternavn": "etternavn", "telefonnummer": "telefonnummer"}.get(typeSok)
    if kolonne:
        cursor.execute(f"SELECT * FROM personer WHERE {kolonne}=?", (sokeTekst,))
        resultater = cursor.fetchall()
        if not resultater:
            print("Finner ingen personer")
        else:
            for person in resultater:
                print(f"{person[0]} {person[1]} har telefonnummer {person[2]}")
    else:
        print("Ugyldig søketype")
    input("Trykk en tast for å gå tilbake til menyen")
    printMeny()

# Start the program by displaying the menu
printMeny()
