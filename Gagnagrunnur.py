import sqlite3

conn = sqlite3.connect('muminspurningar.db')
c = conn.cursor()


### notad til ad hlada inn spurningum i gagnagrunninn og testa.



def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Spurningar(SpID INT PRIMARY KEY,spurning TEXT, rettSvar CHAR, level INT)')
    
    c.execute('CREATE TABLE IF NOT EXISTS Svor(SvID INT PRIMARY KEY, svor TEXT, rettSvar CHAR)')
    
def data_entry():
    pass
 

    c.execute("INSERT INTO Spurningar VALUES(5, 'Fra Muminhusinu liggur litill stigur, hvert liggur hann?', 'b', 3)")
    c.execute("INSERT INTO Svor VALUES(5, '(a) I mumindal \n(b) Ad sjonum \n(c) Ad fjollunum  \n(d) Ad muminpobbnum', 'a')")
    
    c.execute("INSERT INTO Spurningar VALUES(6, 'Hvad heitir besti vinur Muminsnada?', 'a', 2)")
    c.execute("INSERT INTO Svor VALUES(6, '(a) Snork Stelpan \n(b) Sara \n(c) Muminstelpan  \n(d) Snabbi', 'a')")
    
    c.execute("INSERT INTO Spurningar VALUES(7, 'A hvad morgum tungumalum hafa sogurnar um muminalfana vera thyddar?', 'd', 3)")
    c.execute("INSERT INTO Svor VALUES(7, '(a) 2 \n(b) 27\n(c) 56 \n(d) 34', 'd')")

    c.execute("INSERT INTO Spurningar VALUES(3, 'Hvernig er husid sem Muminalfarnir bua i, a litinn?', 'b', 2)")
    c.execute("INSERT INTO Svor VALUES(3, '(a) Marglita \n(b) Blatt \n(c) Hvitt  \n(d) Rautt', 'b')")
    
    c.execute("INSERT INTO Spurningar VALUES(4, 'Hvad gera muminalfarnir a veturna?', 'a', 2)")
    c.execute("INSERT INTO Svor VALUES(4, '(a) Leggjast i dvala \n(b) Syngja \n(c) Byggja snjohus  \n(d) Flytja til utlanda', 'a')")
        
    c.execute("INSERT INTO Spurningar VALUES(1, 'Fra hvada landi er Tove Jansson, hofundur Muminalfanna?', 'c', 1)")
    c.execute("INSERT INTO Svor VALUES(1, '(a) Noregi \n(b) Hawaii \n(c) Finnlandi \n(d) Lettlandi', 'c')")
    
    c.execute("INSERT INTO Spurningar VALUES(2, 'Hvad eru mamman og pabbinn kollud i muminalfunum?', 'd', 2)")
    c.execute("INSERT INTO Svor VALUES(2, '(a) Mamma og pabbi  \n(b) snadaPabbi og Snorkmamma \n(c) Ma og Pa \n(d) MuminMamma og MuminPabbi', 'd')")

    c.execute("INSERT INTO Spurningar VALUES(9, 'Hverju safnar hemullinn?', 'b', 1)")
    c.execute("INSERT INTO Svor VALUES(9, '(a) Serviettum \n(b) Frimerkjum \n(c) Dukkum  \n(d) Skartgripum', 'b')")

    c.execute("INSERT INTO Spurningar VALUES(10, 'Hvada husgagn er thekkt med muminalfunum a?', 'a', 2)")
    c.execute("INSERT INTO Svor VALUES(10, '(a) Bolli \n(b) Bord \n(c) Klosett  \n(d) Hnifur', 'a')")
    
    c.execute("INSERT INTO Spurningar VALUES(11, 'Hvar er skemmtigardurinn Mumingardurinn?', 'b', 2)")
    c.execute("INSERT INTO Svor VALUES(11, '(a) Danmorku \n(b) Finnlandi \n(c) Kanada  \n(d) Bretlandi', 'b')")
    
    c.execute("INSERT INTO Spurningar VALUES(12, 'A hvada skepnu minna muminalfarnir?', 'd', 2)")
    c.execute("INSERT INTO Svor VALUES(12, '(a) Haenur \n(b) Zebrahest \n(c) Fil  \n(d) Flodhest', 'd')")
    
    c.execute("INSERT INTO Spurningar VALUES(13, 'A hvada islensku sjonvarspstod voru Muminalfarnir syndir?', 'b', 1)")
    c.execute("INSERT INTO Svor VALUES(13, '(a) Stod 2 \n(b) RUV \n(c) Skjar 1  \n(d) Syn', 'b')")
    
    c.execute("INSERT INTO Spurningar VALUES(14, 'Hversu margar baekur hafa komid ut um Muminalfana?', 'a', 3)")
    c.execute("INSERT INTO Svor VALUES(14, '(a) 5 \n(b) 4 \n(c) 1  \n(d) 9', 'b')")
    
    c.execute("INSERT INTO Spurningar VALUES(15, 'Hvar komu Muminalfarnir fyrst fram?', 'c', 1)")
    c.execute("INSERT INTO Svor VALUES(15, '(a) Sjonvarpsthattum \n(b) Leikriti \n(c) Bokum  \n(d) Teiknimyndasogu i dagbladi', 'c')")
    
    c.execute("INSERT INTO Spurningar VALUES(16, 'I hvada af eftirfarandi landi er ekki starfsraekt Muminkaffihus?', 'a', 3)")
    c.execute("INSERT INTO Svor VALUES(16, '(a) Svithjod \n(b) Japan \n(c) Sudur-Koreu  \n(d) Taiwan', 'a')")
    
    c.execute("INSERT INTO Spurningar VALUES(17, 'Hver af eftirfarandi islensku tonskaldum samdi lag fyrir Muminalfamynd?', 'd', 1)")
    c.execute("INSERT INTO Svor VALUES(17, '(a) Megas \n(b) Bubbi Morthens \n(c) Thorvaldur Bjarni Thorvaldsson \n(d) Bjork', 'd')")
    
    c.execute("INSERT INTO Spurningar VALUES(18, 'Hvada karakter i Muminalfunum spilar a munnhorpu?', 'b', 3)")
    c.execute("INSERT INTO Svor VALUES(18, '(a) Snabbi \n(b) Snudur \n(c) Muminmamma  \n(d) Mia litla', 'b')")
    
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