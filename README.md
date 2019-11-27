# ERICA_gamesimulator
## 1.선수 능력치
- 로밍능력 (구현 랜덤) roamingstat
- cs수급률 (구현 쉬운 정보) csstat
- 스킬능력 (구현 랜덤) skillstat
- 오더 (구현 랜덤) orderstat

###1-1. 변수
-itemstat : cs수급에 따른 추가 능력치 (일시적)

## 2.턴수
- 2분당 1턴
- 총 15+-5

## 3. 판단
- cs수급
	cs스탯/5 +- rand 0~2
- 딜교
	- (스킬능력 + cs추가스탯) 자신과 상대 비교
	- 50:50기준, 스탯 따라 유불리
	- 승패에 따라 dmg변화
- 오브젝트 시도
	- (오더 + 스킬능력 + cs추가스탯) 각자 능력치+ / 시도 선수 수
	- 오브젝트 턴 유효 - 턴마다 시간이 걸림.
- 로밍
	- 로밍스탯 + 스킬능력 + cs추가스탯
	- 로밍턴 유효
##4. 확률

- cs수급 
	itemstat = csstat / 5 +- rand(0~2)

- 딜교
	battlepower += skillstat + itemstat
	winlose = 0.5 + (this.battlestat -other.battlestat)
	dmg = itemstat only

- 오브젝트 시도
	tryobject += orderstat + skillstat + itemstat
	tryplayer += 1
	objectturn = objectpower / tryobject + 1

- 로밍시도
	tryroaming += roamingstat + skillstat
	roamingturn = roamingtime / tryroaming 
