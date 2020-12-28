class cat(object):
    def __init__(self, name,hunger = 0,boredom = 0):
        print("Появилась кошка")
        self.name= name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

    def talk(self):
        print("меня зовут", self.name,"\n","Самочувствие : ",self.feel)
        self.__pass_time()
    def __yeah(self):
        print("yeah")
    def neyeah(self):
        print("neyeah")
        self.__yeah()
    def eat(self,food = 4,boredom = 4):
        print("Спасибо")
        self.boredom -= food
        if self.boredom < 0:
            self.boredom = 0
        self.hunger-=food
        if self.hunger < 0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun =4):
        print("ОГО")
        self.__pass_time()
    def golos(self):
        print("мяу мур")
        self.__pass_time()
    @property
    def feel(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m="Как обычно все клубнично"
        elif 5<= unhappiness <=10:
            m="норм"
        elif 10<=unhappiness<15:
            m="Могло быть и лучше"
        else:
            m="все плохо"
        return m

class dog(object):
    def __init__(self, name,hunger = 0,boredom = 0):
        print("Появилась собака")
        self.name= name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

    def talk(self):
        print("меня зовут", self.name,"\n","Самочувствие : ",self.feel)
        self.__pass_time()
    def __yeah(self):
        print("yeah")
    def neyeah(self):
        print("neyeah")
        self.__yeah()
    def eat(self,food = 4,boredom = 4):
        print("Спасибо")
        self.boredom -= food
        if self.boredom < 0:
            self.boredom = 0
        self.hunger-=food
        if self.hunger < 0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun =4):
        print("ОГО")
        self.__pass_time()
    def golos(self):
        print("гав гав")
        self.__pass_time()
    @property
    def feel(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m="Как обычно все клубнично"
        elif 5<= unhappiness <=10:
            m="норм"
        elif 10<=unhappiness<15:
            m="могло быть и лучше"
        else:
            m="все плохо"
        return m

class rabbit(object):
    def __init__(self, name,hunger = 0,boredom = 0):
        print("Появился кролик")
        self.name= name
        self.hunger=hunger
        self.boredom=boredom
    def __pass_time(self):
        self.hunger +=1
        self.boredom +=1

    def talk(self):
        print("меня зовут", self.name,"\n","самочувствие : ",self.feel)
        self.__pass_time()
    def __yeah(self):
        print("yeah")
    def neyeah(self):
        print("neyeah")
        self.__yeah()
    def eat(self,food = 4,boredom = 4):
        print("Спасибо")
        self.boredom -= food
        if self.boredom < 0:
            self.boredom = 0
        self.hunger-=food
        if self.hunger < 0:
            self.hunger=0
        self.__pass_time()
    def play(self,fun =4):
        print("ОГО!")
        self.__pass_time()
    def golos(self):
        print("фырк фырк")
        self.__pass_time()
    @property
    def feel(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness <5:
            m="Как обычно все клубнично"
        elif 5<= unhappiness <=10:
            m="норм"
        elif 10<=unhappiness<15:
            m="могло быть и лучше"
        else:
            m="все плохо"
        return m

def main():
    f = None
    while f != 0:
        x = int(input("Напишите цифру чтобы выбрать животного: 1 - Кролик,2 - Кошка, 3 - Собака "))
        if x == 1:
            crit_name = input("Имя Кролика ")
            crit1 = rabbit(crit_name)
        elif x == 2:
            crit_name = input("Имя Кошки ")
            crit1 = cat(crit_name)
        elif x == 3:
            crit_name = input("Имя Собаки ")
            crit1 = dog(crit_name)
        else:
            f = 0
        if f !=0:
            zapusk(crit1)
def zapusk(u):
    choice = None
    while choice != 0:
        print("""
          Моя зверюшка
          0 - Выйти
          1 - узнать о самочувствии зверюшки
          2 - покормить зверюшку
          3 - поиграть со зверюшкой
          4 - попросить голос  
     """   )
        choice=int(input("Выбирайте "))
        if choice==0:
            print("Пока")
        elif choice ==1:
            u.talk()
        elif choice == 2:
            u.eat()
        elif choice==3:
            u.play()
        elif choice==5:
            print(u.name)
            print(u.boredom)
            print(u.hunger)
        elif choice == 4:
            u.golos()
        else:
            print("Такого пункта нет")
main()

input("Enter,чтобы выйти")
