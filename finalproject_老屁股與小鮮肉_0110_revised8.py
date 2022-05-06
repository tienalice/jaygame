import time, random, sys, Q_database, Game  #Q_database, Game為自定義模組

print("歡迎來到周杰倫的Top50暢銷歌曲專屬搜尋引擎\n")
print("我們提供以下四種功能:\n")  ##0107_皮耶爾更改:增加一種功能
print("1.歌詞填空遊戲\n2.歌詞片段找完整歌詞\n3.歌曲名稱找完整歌詞\n4.結束使用本引擎\n")  ##0107_皮耶爾更改:增加結束的功能

start=0
while start<1:
    
    fuc=input("輸入功能編號:")  ##0107_皮耶爾更改:修改內容
    print()
    
    if fuc=="1":

        print('－  歡迎來到杰迷的我唱你接KTV  －\n')
        time.sleep(2)
        print('在這裡你將面對來自地獄般的魔鬼挑戰')
        time.sleep(2.5)
        print('前路驚險異常 若是害怕 不如趕緊退出')
        time.sleep(2.5)
        print('若是選擇留下 那便預祝你一帆風順')
        time.sleep(2.5)
        print('挑戰即將開始 你－－敢自稱杰迷嗎？\n')
        time.sleep(4)
        print('挑戰開始_\n')
        time.sleep(2)
        print('［范特西的功能選單］\n․輸入1：注音提示（僅能使用一次）\n․輸入2：一字提示（僅能使用一次）\n'+
              '․輸入3：獲得來自小小周的提示 但小小周無法對爸爸的全部歌曲都非常熟悉 所以你可以決定是否採用（僅能使用一次）')
        print('\n［注意］\n․每題的回答機會僅限3次（不含提示）')
        print("----------------------------------------------------\n")
        time.sleep(2)
        Game.game()
        
    elif fuc=="2":

        file=open('lyrics.txt','r+', encoding='UTF-8')
        text=file.read()
        if True:
            print('－  歡迎使用以歌詞片段尋找完整歌詞的功能  －\n')  ##0107_皮耶爾更改:增加print
            find1=input('請輸入歌詞片段（注意：若欲輸入多個連貫片段 後一句請直接接續前一句 切勿輸入空格或標點符號）：')  ##0107_皮耶爾更改:增加提醒
            lyrics1=[]
            sp_ly1=text.split('\n')#把歌名跟歌詞分開
            for item in sp_ly1:
               lyrics1.append(item)
            songname=(lyrics1[0:100:2])#取出只有歌名的部分
            songlyrics=(lyrics1[1:101:2])#取出只有歌詞的部分      
            newsong=[]
            for item in range(len(songlyrics)):#把歌詞中的/去除掉，使用者查找的範圍可以更大
                newsong.append(songlyrics[item].replace('/',''))
                
            #0108_珮甄更新(開始)   
            number=[]
            for i in  range(len(newsong)):#找出使用者輸入的是哪一首
                if find1 in newsong[i]:   
                    number.append(i)      #把歌詞找到對應的歌曲號碼加到number[]
                else:                       
                     continue             #沒找到就繼續
            #print(number)
            nums =  list(range(len(songlyrics)))#建立跟歌單一樣數字的串列
            
            #print(nums)
            if len(number) !=0:          #輸入的歌詞有找到對應的歌曲
                for j in range(len(number)):      #因為使用者輸入的歌詞可能不只在一首歌裡面，用for迴圈一一檢查
                    if j in  nums:                          #如果找到的數字在歌單數字的串列印出相對應的歌名歌詞
                            print('\n這首歌是：'+songname[number[j]])
                            print("\n這首歌的完整歌詞是:\n"+songlyrics[number[j]])
            else:  #輸入的歌詞沒有找到對應的歌曲
                print('\n查詢不到結果 輸入歌詞不在周杰倫的top50歌單中')         #如果找到的數字不在歌單數字的串列印出不在歌單內
            #0108_珮甄更新(結束) 
                
        file.close()
        print("\n----------------------------------------------------")  ##0107_皮耶爾更改:增加換行
        print('再次',end = '')

    elif fuc=="3":
        print('－  歡迎使用以歌曲名稱尋找完整歌詞的功能  －\n')  ##0108_皮耶爾更改:增加print
        time.sleep(2)   
        file=open('lyrics.txt','r+', encoding='UTF-8')
        text1=file.readlines()
        songname = text1[0::2] #取出只有專輯名 歌名的部分
        lyrics = text1[1::2]  #取出歌詞
        #print(songname)
        dict1={}#等一下要放專輯和歌名
        songname_new=[]
        for i in songname:
            j=i.strip().split(',')#strip:去掉'\n',split:把字串變list
            albumname=j[0]
            songname=j[2]
            songname_new.append(songname)
            try:
                dict1[albumname].append(songname) #先假設專輯名和歌名已經存在
            except:
                dict1[albumname]=[] #如果不存在就宣告新專輯 再將歌名放入
                dict1[albumname].append(songname)
        print('［可選擇的專輯］')
        for i in dict1:
            print(i)
        while True:
            album=input('\n以上專輯名請擇一輸入 以找尋歌曲:')
            if album in dict1:
                print('\n［本張專輯裡收錄以下歌曲］')
                
                for i in dict1[album]:
                    print(i)
                while True:
                    song=input('\n請輸入要查詢歌詞的歌曲：')
                    if song in dict1[album]:
                        number=songname_new.index(song)
                        print('\n'+song+'的歌詞是:\n'+lyrics[number])
                        break
                    else:
                        print('輸入錯誤，請再重新輸入一次')
                        continue
            else:
                print('您輸入的專輯錯誤，或是不在周杰倫的TOP50歌單裡')
                continue
            print("----------------------------------------------------")
            print('再次',end = '')
            break
    elif fuc=="4":  ##0107_皮耶爾更改:增加結束的功能
        print('－本引擎即將關閉－')
        time.sleep(2)
        sys.exit()        
    else:
        print("數字輸入錯誤 請重新",end='')
        continue
