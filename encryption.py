import random

def seed_to_int(seed=r"D0G$0ILN'Y08ZxNovYPbVF5M%dqClx#&>8ETZMb2mNZd2q.IF0OMfv/AF;}i;x;4{:I>v=gdY3q[.;>A>B5x'ub2T(*:xMKYacK5b\9m*'=YK6sk\"li_KN;q{/5C)Cx-F;+{XO',w]!A0P|~gKQpu+7Z]?jg7\"AC%.7gj'9x6-t^FPDppk<ld9b&Hr--pl#C(fz5+*ku)&x$YuawqDEm}/6q]NaU[f<+P'O|pJ+`q~ZCz#|/dG^!u]x,$lTrC_JhhKI/}e6aB!p5]2x)Dp#^T=3'26;R6Gu94BGv~)Ix_sVLWb!14^,X{![J`-:cVP,$ZzaUQs/[]u1Pq|wsWi~x`G/s>1L=_@J1?b8Fb.F\"}!|d*;nEdcN?Bg,.S^*FojW7:@[5n'M=-W]n6t/[v_R_pWq&{S<5_@#0&#4#}eOMkNNG5}rNeP(\Itn\j%}D8DJfCMpm^/mWLx-}HS\H.Yo<j.q}&^3[/-uQm\+9//8j!\"&^+fwn|sMH/-+>$U%i\")pB"):
    if seed == r"D0G$0ILN'Y08ZxNovYPbVF5M%dqClx#&>8ETZMb2mNZd2q.IF0OMfv/AF;}i;x;4{:I>v=gdY3q[.;>A>B5x'ub2T(*:xMKYacK5b\9m*'=YK6sk\"li_KN;q{/5C)Cx-F;+{XO',w]!A0P|~gKQpu+7Z]?jg7\"AC%.7gj'9x6-t^FPDppk<ld9b&Hr--pl#C(fz5+*ku)&x$YuawqDEm}/6q]NaU[f<+P'O|pJ+`q~ZCz#|/dG^!u]x,$lTrC_JhhKI/}e6aB!p5]2x)Dp#^T=3'26;R6Gu94BGv~)Ix_sVLWb!14^,X{![J`-:cVP,$ZzaUQs/[]u1Pq|wsWi~x`G/s>1L=_@J1?b8Fb.F\"}!|d*;nEdcN?Bg,.S^*FojW7:@[5n'M=-W]n6t/[v_R_pWq&{S<5_@#0&#4#}eOMkNNG5}rNeP(\Itn\j%}D8DJfCMpm^/mWLx-}HS\H.Yo<j.q}&^3[/-uQm\+9//8j!\"&^+fwn|sMH/-+>$U%i\")pB":
        seed1 = "68487136487376783989485690120781111188980988670537737100113671081203538625669849077985010978901005011346737048797710211847657059125105591205952123587362118611031008951113914659626562665312039117985084404258120777589979975539892571094239618975541151079234108105957578591131234753674167120457059431238879394411993336548801241261037581112117435590936310610355923465673746551031063957120544511694708068112112107601081005798387211445451121083567401021225343421071174138120368911797119113686910912547541139378978591102604380397912411274439611312690671223512447100719433117931204436108841146795741041047573471251015497663311253935012041681123594846151395054598254711175752667111812641731209511586768798334952944488123339174964558998680443690122978581115479193117498011312411911587105126120967147115624976619564744963985670984670923412533124100425911069100997863661034446839442701111068755586491531103977614587931105411647911189582951128711338123836053956435483835523512510179771077878715312511478101804092731161109210637125685668741026777112109944710987761204512572839272468911160106461131253894519147451178110992435747475610633923438944310211911012411577724745436236853710592344111266"
        return seed1
    seed1 = ""
    for i in seed:
        seed1 += str(ord(i))
    return seed1

def encode(message,seed):
    temp = ""
    for i in range(len(message)):
        if (i+1) % 2 == 0:
            temp += random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ ")
            temp += message[i]
        temp += message[i]
    output = ""
    if seed == "":
        seed = seed_to_int()
    else:
        seed = seed_to_int(seed)
    for i in range(len(temp)):
        output += str( chr( ( ord(temp[i]) + int(seed[i]) ) ) )
    return output

def decode(message,seed):
    if seed == "":
        seed = seed_to_int()
    else:
        seed = seed_to_int(seed)
    temp = ""
    for i in range(len(message)):
        temp += str( chr( ( ord(message[i]) - int(seed[i]) ) ) )
    output = ""
    for i in range(len(message)):
        if (i+1) % 2 != 0:
            output += temp[i]
    return output

while True:
    opt = input("Enter e to encode, d to decode and q to quit:\n")
    if opt[0].lower() == "q":
        break
    message = input("Enter the Message:\n")
    user_seed = input("Press enter to use default seed(recommended) or write your own seed:\n")
    if opt[0].lower() == "e":
        print(encode(message,user_seed))
    elif opt[0].lower() == "d":
        print(decode(message,user_seed))
