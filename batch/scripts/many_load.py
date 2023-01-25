import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site,Category,State,Iso,Region

def run():
    fhand = open('scripts/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Site.objects.all().delete()



    for row in reader:
        print(row)

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        i, created = Iso.objects.get_or_create(name=row[10])
        r, created = Region.objects.get_or_create(name=row[9])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            l = float(row[4])
        except:
            l = None


        try:
            l = float(row[5])
        except:
            l = None
        try:
            h = float(row[6])
        except:
            h = None

        try:
            d = str(row[1])
        except:
            d = None
        try:
            j = str(row[2])
        except:
            j = None



        s=Site(name=row[0],description=d,
        justification=j,year=y,longitude=l,latitude=l,
        area_hectares=h,
        category=c,state=s,region=r,iso=i)
        s.save()
