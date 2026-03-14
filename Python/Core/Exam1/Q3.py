# #Time Traveller
#
# class Timetraveler:
#
#     def __init__(self,cname,o_year,d_year):
#         self.codename=cname
#         self.origin_year=o_year
#         self.destination_year=d_year
#         Timetraveler.cname.append(cname)
#         Timetraveler.registry+=1
#
#     registry=0
#     cname=[]
#     @classmethod
#     def show_registry(cls):
#         print(f"Total Number of travellers {cls.registry}")
#         print(f"codename: {cls.cname}")
#     @staticmethod
#     def year_status(oy,dy):
#         if oy==dy:
#             print('Present')
#         elif oy>dy:
#             print("Past")
#         else:
#             print("Future")
#
# t1=Timetraveler("001",2024,2026)
# t2=Timetraveler("002",2026,2025)
#
# Timetraveler.show_registry()
# t1.year_status(t1.origin_year,t1.destination_year)

''' option -2 - Time Traveller '''
class Timetraveler:

    def __init__(self,cname,o_year,d_year):
        self.codename=cname
        self.origin_year=o_year
        self.destination_year=d_year
        Timetraveler.registry.append(cname)

    registry=[]
    @classmethod
    def show_registry(cls):
        print(f"Total Number of travellers {len(cls.registry)} ")
        for i in cls.registry:
            print(f"codename: {i}")
    @staticmethod
    def year_status(oy,dy):
        if oy==dy:
            print('Present')
        elif oy>dy:
            print("Past")
        else:
            print("Future")

t1=Timetraveler("001",2024,2026)
t2=Timetraveler("002",2026,2025)

Timetraveler.show_registry()
t1.year_status(t1.origin_year,t1.destination_year)