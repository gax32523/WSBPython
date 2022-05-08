#
#  Framewrok peewee
#
# http://docs.peewee-orm.com/en/latest/peewee/installation.html
#
#
# https://www.sqlalchemy.org/

from peewee import*
import os

def clrscr():
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')

def main():
    #sprawdzenie czy plik istnieje i ew. usunięcie
    if os.path.exists('auta.db'):
        os.remove('auta.db')

    myDB=SqliteDatabase('auta.db')

    class ModelBase(Model):
        class Meta:
            database =myDB

    class Cars(ModelBase):
        name = CharField(null=False)
        year = IntegerField(null=False)
        mileage=IntegerField()

    # towrzenie bazy danych

    myDB.connect()
    myDB.create_tables([Cars])

    do_zaladowania=[ {'name':'Audi TT', 'year':1999,'mileage':120000},
        {'name':'Ford Mustang', 'year':2010,'mileage':13000},
        {'name':'Kia Ceed', 'year':2021,'mileage':1},
        {'name':'Ferrari Testarossa', 'year':1999,'mileage':23000}
                    ]
    Cars.insert_many(do_zaladowania).execute()

    def AddCar(nazwa, rok_prod, licznik):
        auto = Cars(name=nazwa, year=rok_prod, mileage=licznik)
        auto.save()

    def ShowData():
        print("\nLista aut w bazie")
        print("="*43)
        for s in Cars.select():
            print(str(s.id)+(" "*(5-len(str(s.id)))),s.name+(" "*(20-len(s.name))),s.year, (" "*(10-len(str(s.mileage))))+str(s.mileage))
        print("\n")

    def DelCar(id):
        Cars.select().where(Cars.id==id).get().delete_instance()

    def UpdateCarMileage(pojid, licznik):
        row=Cars.select().where(Cars.id==pojid).get()
        row.mileage=licznik
        row.save()

    print("\n *** Aplikacja do ewidencji pojazdow ***")

    while True:
        print("="*43)
        print("Dostępne opcje programu:")
        print("""
        1. wyświetl samochody w bazie
        2. dodaj samochod do bazy
        3. skasuj smochod z bazy
        4. zmień stan licznika
        5. wyjdź z aplikacji""")
        x=input("wybierz opcję: """)

        if(x=="1"):
            ShowData()

        elif x=="2":
            nazwa=input("Podaj markę auta:")
            rok=int(input("Podaj rok produkcji:"))
            licznik=int(input("Podaj stan licznika:"))
            AddCar(nazwa,rok,licznik)
            ShowData()

        elif x=="3":
            ShowData()
            carId=int(input("Podaj id pojazdu do usunięcia:"))
            DelCar(carId)
            print("")

        elif x=="4":
            ShowData()
            carId=int(input("Podaj id pojazdu, który chcesz zmienić:"))
            stanLicznik=int(input("Podaj nowy stan licznika pojazdu:"))
            UpdateCarMileage(carId, stanLicznik)
            ShowData()
        else:
            break


if __name__ == '__main__':
    main()

