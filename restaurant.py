# 1.餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性：
# restaurant_name 和 cuisine_type(烹饪)。
# 创建一个名为 describe_restaurant()方法和一个名为open_restaurant ()方法,
# 其中前者打印前述两项信息，而后者打印一条消息,指出餐馆正在营业。
# 根据这个类创建一个名为的实例，分别打印其两个属性，再调用前述两个方法。

# 2.三家餐馆：根据你为完成练习1而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant()。

# 4.就餐人数：在为完成练习1而编写的程序中,添加一个名为number_served的属性,并将其默认值设置为0。
# 打印有多少人在这家餐馆就餐过,然后修改这个值并再次打印它。
# 添加一个名为set_number_served()的方法,它让你能够设置就餐人数。
# 调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法,
# 它让你能够将就餐人数递增.调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

# 6.冰淇淋小店：冰其淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，
# 让它继承你为完成练习1或练习4而编写的Restaurant类。这两个版本Restaurant类都可以，
# 挑选你更喜欢的那个即可。添加一个名为flavors的属性,用于存储一个由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。创建一IceCreamStand实例,并调用这个方法。
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=1):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def describe_restaurant(self):
        print('这个餐馆叫%s,擅长的烹饪类型是%s' % (self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print('欢迎光临,正在营业!')
    def set_number_served(self,n):
        print('目前有%d人就餐过'%n)
    def increment_number_served(self,m):
        for i in range(1,m+1):
            self.number_served+=1
        print('目前有%d人就餐过' %self.number_served)

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type,flavors, number_served=1):
        super().__init__(restaurant_name, cuisine_type, number_served=1)
        self.flavors=flavors
    def get_info(self):
    #重写父类
    # def describe_restaurant(self):
        print('这家冰激凌小店的名字是%s,它的烹饪类型是%s,冰激凌口味包含%s'%(self.restaurant_name,self.cuisine_type,self.flavors))

if __name__ == '__main__':
    Ice1=IceCreamStand('星吧乐','手工制作',['辣的','咸的','甜的','酸的','苦de'])
    # Ice1.get_info()
    #父类重写
    Ice1.describe_restaurant()







# if __name__ == '__main__':
#     # restaurant = Restaurant('桂满陇', '江浙菜')
#     # print(restaurant.restaurant_name)
#     # print(restaurant.cuisine_type)
#     # 创建三个Restaurant的实例化对象
#     restaurant1 = Restaurant('傣妹', '四川')
#     restaurant2 = Restaurant('上上签', '火锅')
#     restaurant3 = Restaurant('我家酸菜鱼', '鱼火锅')
#     # 实例化对象调用我们的类方法
#     # restaurant1.describe_restaurant()
#     # restaurant2.describe_restaurant()
#     # restaurant3.describe_restaurant()
#     # restaurant1.open_restaurant()
#     # restaurant2.open_restaurant()
#     restaurant3.open_restaurant()
#     # restaurant3.set_number_served(44)
#     restaurant3.increment_number_served(20)
