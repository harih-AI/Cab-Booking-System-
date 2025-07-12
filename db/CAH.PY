from database import get_connection

def insert_sample_cabs():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM CABS")
    if cursor.fetchone()[0] == 0:
        cabs = [('Mini', 1), ('Sedan', 1), ('SUV', 1)]
        cursor.executemany("INSERT INTO CABS (CAB_TYPE, IS_AVAILABLE) VALUES (?, ?)", cabs)
        conn.commit()
        print("✅ Sample cabs inserted.")
    else:
        print("ℹ️ Cabs already present.")
    
    conn.close()
insert_sample_cabs()