import sqlite3

DB_PATH="data/metadata.db"

# Initialisaing connection with sqlite and establising it

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
            claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            type TEXT,
            flag TEXT
        )
    """)
    conn.commit()
    conn.close()

# Performing actions of getting,creating,adding and deleting from the metadata table
def get_all_metadata():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM metadata")
    rows = c.fetchall()
    conn.close()
    return rows

def add_metadata(name, type_, tags, owner_role):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO metadata (claim_id,amount,type,flag) VALUES (?, ?, ?, ?)",
              (claim_id,amount,type,flag))
    conn.commit()
    conn.close()

def update_metadata(claim_id,amount,type,flag):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("UPDATE metadata SET claim_id=?, amount=?, type=?, flag=? WHERE id=?",
              (claim_id,amount,type,flag,claim_id))
    conn.commit()
    conn.close()

def delete_metadata(id_):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM metadata WHERE id=?", (claim_id,))
    conn.commit()
    conn.close()