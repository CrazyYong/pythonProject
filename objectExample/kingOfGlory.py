#!/usr/bin/python3
#coding=utf-8


class KingOfGlory:
    def __init__(self,name,category,output,skill):
        self.name=name
        self.category=category
        self.output=output
        self.skill=skill

    def scene1(self):
        print ('%s偷红buff，释放%s偷到红buff消耗血量300'%(self.name,self.skill))

    def scene2(self):
        print ('solo战斗，一血，消耗血量500')
        print ('%ssolo战斗后的血量%d'%(self.name,self.output-500))

    def scene3(self):
        print ('补血加200')
        print ('%s补血后的血量%d'%(self.name,self.output+200))

kai = KingOfGlory('铠','战士',1000,'极刃风暴')
zhaogJun = KingOfGlory('王昭君','法师',1000,'凌冬将至')
ake = KingOfGlory('阿珂','刺客',1000,'瞬华')

kai.scene1()
kai.scene2()
kai.scene3()