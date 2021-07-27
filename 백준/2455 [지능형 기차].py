station1_getDown,station1_getOn = map(int,input().split())
station2_getDown,station2_getOn = map(int,input().split())
station3_getDown,station3_getOn = map(int,input().split())
station4_getDown,station4_getOn = map(int,input().split())

max_people = [] 
max_people.append(-station1_getDown + station1_getOn) 
max_people.append(-station1_getDown + station1_getOn -station2_getDown + station2_getOn) 
max_people.append(-station1_getDown + station1_getOn -station2_getDown + station2_getOn-station3_getDown + station3_getOn)
max_people.append(-station1_getDown + station1_getOn -station2_getDown + station2_getOn-station3_getDown + station3_getOn-station4_getDown + station4_getOn)

max_people.sort()
print(max_people[3])



