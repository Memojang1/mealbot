import discord
from neispy import Neispy
import datetime

name = "천안청수고등학교" #학교이름변수

current_date = datetime.date.today() #오늘날짜 꺼내오기
t = str(current_date.year) + current_date.strftime("%m%d") #오늘 날짜 씨발진짜 이ㅏ개새끼 정리시키기

n = int(t)+1

neis = Neispy.sync('126594b98c6348ca93433b5abd47d1fa') #네이스코드

scinfo = neis.schoolInfo(SCHUL_NM="천안청수고등학교") #학교이름으로 코드추출
AE = scinfo[0].ATPT_OFCDC_SC_CODE  # 교육청 코드
SE = scinfo[0].SD_SCHUL_CODE  # 학교 코드

scmeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD=t) # 교육청, 학교코드 이용해서 오늘 날짜 급식정보 가져오기
meal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  #줄바꿈

nimeal = neis.mealServiceDietInfo(AE, SE, MLSV_YMD=n)
nmeal = scmeal[0].DDISH_NM.replace("<br/>", "\n")  #줄바꿈





class MyClient(discord.Client): #봇 로그인시키기
    async def on_ready(self): 
        print('Logged on as', self.user) #로그인된거 출력시키기

    async def on_message(self, message): #사용자가 보낸 메시지 감지
        if message.author == self.user:
            return

        if message.content == '$급식': 
            await message.channel.send(meal) # 저거치면 오늘 급식 사용자가 보낸 채널에 알려주기

        if message.content == '$오늘날짜':
            await message.channel.send(t) # 저거치면 오늘 날짜 사용자가 보낸 채널에 알려주기

        if message.content == '$내일급식': 
            await message.channel.send(nmeal)#내일급식 치면 내일급식 알려주기

#특정날짜 지목해서 급식 알려주기
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('MTEyNTcxMTM1MTc1NTU4MzUzOQ.GwqLU3.GKG1-Lby_9eczh_5T3c29yRT6k10bdLORee1Nc')