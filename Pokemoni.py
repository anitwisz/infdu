#slovnik slovnikov

import json

def attack_number(power:str)->float:
    if power == "super effective":
        return 2
    if power == "normal effective":
        return 1
    if power == "not very effective":
        return 0.5
    if power == "no effect":
        return 0


def attack(p1,p2):
    atk = {}
    fr = open("effectiveness.json")
    data = json.load(fr)
    for effective in data:
        for attacker in data[effective]:
            if attacker in atk.keys():
                temp = atk[attacker]
            else:
                temp = {}
            for defender in data[effective][attacker]:
                temp[defender] = attack_number(effective)
            atk[attacker] = temp
    return atk[p1][p2]

def pok_to_pok(attk,deff):
    if ' ' in attk and  ' ' in deff:
        attk = attk.split()
        deff = deff.split()
        u1 = attack(attk[0], deff[0])
        u2 = attack(attk[1], deff[1])
        u3 = attack(attk[0], deff[1])
        u4 = attack(attk[1], deff[0])
        return max(u1, u2, u3, u4)

    if ' ' in attk:
        attk = attk.split()
        u1 = attack(attk[0],deff)
        u2= attack(attk[1],deff)
        return max(u1,u2)

    if ' ' in deff:
        deff = deff.split()
        u1 = attack(attk, deff[0])
        u2 = attack(attk, deff[1])
        return max(u1,u2)


    else:
        return attack(attk,deff)


def battle(n1,n2,list_pok):

    list_pok = list_pok.split(',')
    team_1 = list_pok[:n1]
    team_2 = list_pok[n1:]
    p1 = 0
    p2 = 0
    s1= " "

    for i in team_1:
        for j in team_2:
           me =  pok_to_pok(i,j)
           p1 += me
           oponent = pok_to_pok(j,i)
           p2 += oponent


    if p1 > p2:
        s1 = "ME"
    if p2 > p1:
        s1 = "OPPONENT"
    if p2 == p1:
        s1 = "EQUAL"
    print(p1,p2,s1)



