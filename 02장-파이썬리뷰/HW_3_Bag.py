# Bag.

class Bag :
    def __init__(self):
        self.bag = []

    def contains(self, e) :
        return e in self.bag  # True /False

    def insert(self, e) :
        self.bag.append(e)

    def remove(self,e) :
       self.bag.remove(e)

    def count(self):
        return len(self.bag)

    def numOf(self, item):
        return self.bag.count(item)    
  


#=================================================
myBag = Bag()

myBag.insert('휴대폰'); myBag.insert('지갑')
myBag.insert('아이패드'); myBag.insert('에어팟')
myBag.insert('립밤'); myBag.insert('맥북')
myBag.insert('신분증'); myBag.insert('사자')
print('내 가방속의 물건:', myBag.bag)
 
myBag.insert('수표'); myBag.insert('사자')
myBag.remove('지갑')
print('내 가방속의 물건: ', myBag.bag)
print('사자의 개수: ', myBag.numOf('사자'))