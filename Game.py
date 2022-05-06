import time, random, Q_database

def game():
    a = 1
    b = 1
    num1 = 0
    c = 1
    num2 = 0
    d = 1
    num3 = 0
    e = 1
    pet_list = ['哎唷～','哎唷不錯喔！','哎唷不錯喔～這個diao！']
    
    Q_list = Q_database.set_Qs()
    random.shuffle(Q_list)
    y = Q_list[0:10]  #取前10個[0:10]
    
    for x in y:
        print('［第',a,'題］ '+x['name']+'\n'+x['Q']+'\n',sep = '')
        while True:
            z = input("作答：")
            if z == x['ans']:
                a += 1
                e = 1  #錯誤報告_1231 每題應該都有三次的嘗試機會 故在答對題目後將e變回預設值
                print('－公告－ 作答正確 恭喜晉級')
                print()
                break
            elif z == '1':
                if b == 1:
                    print('－提示－ 注音符號的開頭分別為：'+x['hint_a']+'\n'+'繼續',end = '')
                    b += 1
                    num1 = a
                    continue
                elif b == 2:
                    if num1 == a:
                        print('－公告－ 這題已經用過注音提示囉\n繼續',end='')
                        continue
                    else:
                        print('－公告－ 注音提示已經用光了喔\n'+'只能試試自己',end = '')
                        continue
            elif z == '2':
                if c == 1:
                    print('－提示－ 一字提示為：'+random.choice([x['hint_f'],x['hint_l']])+'（注意：回答請輸入完整的詞）\n'+'繼續',end = '')
                    c += 1
                    num2 = a
                    continue
                elif c == 2:
                    if num2 == a:
                        print('－公告－ 這題已經用過一字提示囉\n繼續',end='')
                        continue
                    else:
                        print('－公告－ 一字提示已經用光了喔\n'+'只能試試自己',end = '')
                        continue
            elif z == '3':
                if d == 1:
                    d += 1
                    num3 = a
                    zz = random.choice([x['ans'],x['f_ans']])
                    print('－提示－ 小小周握了握小拳拳ʕ•̀o•́ʔ 伊伊啊啊地向你說出了提示：'+zz)
                    time.sleep(2)
                    while True:
                        zzz = input('－疑問－ 在一番深思熟慮後 你是否決定採用小小周的建議？（輸入1：是；輸入2：否）：')
                        if zzz == '1' or zzz == '2':
                            break
                        else:
                            print('－公告－ 小小周聽不懂你在說什麼 再一次要講清楚喔')
                            continue
                    if zzz == '1':
                        anstaken = zz
                        if anstaken == x['ans']:
                            a += 1
                            print('－公告－ 小小周幫你答對了 他很開薰(｡◕∀◕｡)')
                            print()
                            break
                        else:
                            print('－公告－ 小小周答錯了 \n試試重新',end = '')
                            e += 1
                            continue
                    elif zzz == '2':
                        print('－公告－ 小小周哭哭啼啼地跑走了இдஇ\n壞壞的你必須自己',end = '')
                        continue
                elif d == 2:
                    if num3 == a:
                        print('－公告－ 這題小小周已經提示過囉(๑•́₃•̀๑)\n繼續',end='')
                        continue
                    else:
                        print('－公告－ 小小周累了(◔₃◔)\n'+'只能試試自己',end = '')
                        continue
            else:
                if e <= 2:
                    e += 1
                    print('－公告－ 答案不對喔\n試試重新',end = '')
                    continue
                else:
                    print('－公告－ 答錯次數已達上限！要不要再去多聽幾遍周董的歌呢？')
                    time.sleep(2)
                    print('－公告－ 本次挑戰中 你一共答對了',a-1,'題 再重新嘗試看看吧！',sep='')#
                    time.sleep(2)
                    print('\n－挑戰即將結束－\n')
                    time.sleep(2)
                    print('-'*150)
                    print('再次',end = '')
                    return
                
    time.sleep(2)
    print('-'*150)
    print('恭喜你歷經千辛萬苦 順利完成了10題的挑戰\n接下來有請周董來到台前跟你說句話\n\n周董走近你身邊 拍了拍手 翹起食指 說了句：',random.choice(pet_list),sep = '')  #小彩蛋
    print()
    time.sleep(2)
    print('-'*150)
    print('再次',end = '')
