import sqlite3

conn = sqlite3.connect('spurningar.db')
c = conn.cursor()

### notad til ad hlada inn spurningum i gagnagrunninn og testa.

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Spurningar(SpID INT PRIMARY KEY,spurning TEXT, rettSvar CHAR, level INT)')
    c.execute('CREATE TABLE IF NOT EXISTS Svor(SvID INT PRIMARY KEY, svor TEXT, rettSvar CHAR)')

def data_entry():
    pass

    c.execute("INSERT INTO Spurningar VALUES(1, 'Hvaða jólasveinn kemur fyrstur til byggða?', 'a', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Stekkjastaur\n(b) Stúfur\n(c) Giljagaur\n(d) Kertasníkir, 'a')")

    c.execute("INSERT INTO Spurningar VALUES(2, 'Hvað heitir kærasti Mínu músar?', 'c', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Mikki refur\n(b) Jenni\n(c) Mikki mús\n(d) Stuart litli, 'c')")

    c.execute("INSERT INTO Spurningar VALUES(3, 'Hvað heitir snjókarlinn í Frozen?', 'c', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Guðmundur\n(b) Ingólfur\n(c) Ólafur\n(d) Snæfinnur, 'c')")

    c.execute("INSERT INTO Spurningar VALUES(4, 'Hvað heitir höfuðborg Danmerkur?', 'b', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Árhús\n(b) Kaupmannahöfn\n(c) Stokkhólmur\n(d) Álaborg, 'b')")

    c.execute("INSERT INTO Spurningar VALUES(5, 'Hvaða dýr er merki hjá verslunarkeðjunni Bónus?', 'd', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Köttur\n(b) Mús\n(c) Villisvín\n(d) Grís, 'd')")

    c.execute("INSERT INTO Spurningar VALUES(6, 'Í hvaða heimsálfu er Egyptaland?', 'b', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Evrópa\n(b) Afríka\n(c) Asía\n(d) Eyjaálfa, 'b')")

    c.execute("INSERT INTO Spurningar VALUES(7, 'Hvað eru margar hliðar á trapissu?', 'b', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Fimm\n(b) Fjórar\n(c) Þrjár\n(d) Núll, 'b')")

    c.execute("INSERT INTO Spurningar VALUES(8, 'Hvað heitir asninn í Shrek?', 'a', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Asni\n(b) Eyrnaslapi\n(c) Fáviti\n(d) Fíóna, 'a')")

    c.execute("INSERT INTO Spurningar VALUES(9, 'Hvernig eru buxurnar hans bangsímon á litinn?', 'd', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Rauðar\n(b) Bláar\n(c) Grænar\n(d) Hann er ekki í buxum, 'd')")

    c.execute("INSERT INTO Spurningar VALUES(10, 'Hvenær er þjóðhátíðardagur Íslendinga?', 'c', 1)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) Fyrsta sunnudag í ágúst\n(b) 1.maí\n(c) 17.júní\n(d) 4.júlí, 'c')")

    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM Spurningar ')
    for row in c.fetchall():
        print(row)

    c.execute('SELECT * FROM Svor ')
    for row in c.fetchall():
        print(row)

    conn.commit()
    c.close()
    conn.close()

#create_table()
#data_entry()
read_from_db()
