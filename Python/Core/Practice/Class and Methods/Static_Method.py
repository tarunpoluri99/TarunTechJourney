class Movie:
    language="Telugu"
    def __init__(self,director,hero,tickect_price):
        self.dir=director
        self.hero=hero
        self.tp=tickect_price

    def collections(self,tickets):
        return self.tp*tickets

    ''' we create instance method instead of class method bcuz we want to change particular
    object not all class languages.so, using IM() instead of CM().  '''
    def dub(self,new_lang):
        self.language=new_lang

bahubali=Movie("ssr","pb",350)
bahubali.collections(1000000000)
print(bahubali.language)
bahubali.dub("Hindi")
# called dub(),its an Instance Method so it changes lang only for a particular object
print(bahubali.language) #Hindi changed from Telugu bcuz of IM()--dub()

spirit=Movie("srv","pb",500)
print(spirit.language)
# Telugu bcuz the class lang is telugu we created dub() only for particular object language.