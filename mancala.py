import time
import sys,getopt
import operator
import numpy 
level1States=[]
#////////////////////////////utilities////////////////////////////////
def gettempvaluesalphabeta(alpha,beta,v):
	if(alpha==9999999999):
		tempalpha="Infinity"
	elif(alpha==-9999999999):
		tempalpha="-Infinity"
	else:
		tempalpha=alpha
	if(beta==9999999999):
		tempbeta="Infinity"
	elif(beta==-9999999999):
		tempbeta="-Infinity"
	else:
		tempbeta=beta
	if(v==9999999999):
		tempv="Infinity"
	elif(v==-9999999999):
		tempv="-Infinity"
	else:
		tempv=v
	return tempalpha,tempbeta,tempv
def gettempvalues(v):
	if(v==9999999999):
		tempv="Infinity"
	elif(v==-9999999999):
		tempv="-Infinity"
	else:
		tempv=v
	return tempv
def evaluate(game_state):
	#print "evaluate function"
	if(player==1):
		#print game_state[len(boardPlayer1List)]-game_state[len(game_state)-1]
		return game_state[len(boardPlayer1List)]-game_state[len(game_state)-1]
	elif(player==2):
		#print game_state[len(game_state)-1]-game_state[len(boardPlayer1List)]
		return game_state[len(game_state)-1]-game_state[len(boardPlayer1List)]

def gameend(game_state):
	
	flag=1
	
		
	for i in range(0,len(boardPlayer1List)):
		if(game_state[i]!=0):
			flag=0
	
		
	for i in range(len(boardPlayer1List)+1,len(game_state)-2):
		if(game_state[i]!=0):
			flag=0

	return flag
def gameEndUtility(game_state):
	temp1=game_state
	flagEnd=0
	for z in range(0,len(boardPlayer1List)):
		if(temp1[z]!=0):
			flagEnd=1
			break
	if(flagEnd==0):
		sum1=0
		for y in range(len(boardPlayer1List)+1,len(game_state)-1):
			sum1=sum1+temp1[y]
			temp1[y]=0
		temp1[len(game_state)-1]+=sum1
	
		return temp1
	flagEnd=0
	temp2=game_state
	for z in range(len(boardPlayer1List)+1,len(game_state)-1):
		
		if(temp2[z]!=0):
			flagEnd=1
			break
			#print flagEnd
	if(flagEnd==0):
		sum1=0
		for y in range(0,len(boardPlayer1List)):
			sum1=sum1+temp2[y]
			temp2[y]=0
		temp2[len(boardPlayer1List)]+=sum1
		return temp2
	return game_state
def cutoff(game_state,depth):
	if(depth==maxDepth):
		return True
	else:
		return False

def evaluate(game_state):
	#print "evaluate function"
	if(player==1):
		#print game_state[len(boardPlayer1List)]-game_state[len(game_state)-1]
		return game_state[len(boardPlayer1List)]-game_state[len(game_state)-1]
	elif(player==2):
		#print game_state[len(game_state)-1]-game_state[len(boardPlayer1List)]
		return game_state[len(game_state)-1]-game_state[len(boardPlayer1List)]
def Actions(game_state,dummyPlayer):
	actions=[]
	capture=[]
	mancalaThere=[]
	alphabetList=[]
	if(dummyPlayer==1):
		for i in range(0,len(boardPlayer1List)):
			#print "round"
			temp=list(game_state)
			counter=temp[i]
			
			if(counter==0):
			 	continue
			flagEnd=1
			temp[i]=0
			j=i+1
			flag=0
			flagMancala=0
			flagEnd=0
			while(counter):
				
				if(j==len(temp)-1):
					j=0
				
				if(counter==1 and temp[j]==0 and j!=len(boardPlayer1List) and j<len(boardPlayer1List)):
					
					
					captureSquare=len(temp)-2-j
				
					temp[len(boardPlayer1List)]=temp[len(boardPlayer1List)]+temp[captureSquare]+1
					temp[j]=0
					temp[captureSquare]=0
					flag=1
				else:
					temp[j]=temp[j]+1
				if(counter==1 and j==len(boardPlayer1List)):
					flagMancala=1
				counter=counter-1
				j=j+1
			print "temp"
			print temp
			
			temp=gameEndUtility(temp)

			if(flag):
				capture.append("capture")
			else:
				capture.append("nocapture")
			
			if(flagMancala):
				mancalaThere.append("mancala")
			else:
				mancalaThere.append("nomancala")
			actions.append(temp)
			alphabetList.append("B"+str(i+2))
		

		print "actions"
		print actions
		
		print "capture"
		print capture
		print "mancalaThere"
		print mancalaThere
		print "alphabetList"
		print alphabetList
		#raw_input()
		return actions,capture,mancalaThere,alphabetList
	elif(dummyPlayer==2):

		for i in range(len(game_state)-2,len(boardPlayer1List),-1):
			#print i
			temp=list(game_state)
			counter=temp[i]
			#print counter
			if(counter==0):
				continue
			temp[i]=0

			j=i+1
			flag=0
			flagMancala=0
			flagEnd=0
			while(counter):
				if(j==len(temp)):
					j=0
				if(j==len(boardPlayer1List)):
					j=j+1
				if(counter==1 and temp[j]==0 and j!=len(temp)-1 and j>len(boardPlayer1List)):
					print "capture Indhu"
					print j,i,temp[j],temp[i]
					captureSquare=len(temp)-j-2
					temp[len(temp)-1]=temp[len(temp)-1]+temp[captureSquare]+1
					temp[j]=0
					temp[captureSquare]=0
					flag=1
				else:
					temp[j]=temp[j]+1
				if(counter==1 and j==len(game_state)-1):
					flagMancala=1
				counter=counter-1
				j=j+1
			print "temp"
			print temp
			temp=gameEndUtility(temp)

			if(flag):
				capture.append("capture")
			else:
				capture.append("nocapture")
			if(flagMancala):

				mancalaThere.append("mancala")
			else:
				mancalaThere.append("nomancala")
			
			
			actions.append(temp)
			alphabetList.append("A"+str(len(game_state)-i))
		print "actions"
		print actions
		
		print "capture"
		print capture
		print "mancalaThere"
		print mancalaThere
		print "alphabetList"
		print alphabetList
		#raw_input()
		return actions,capture,mancalaThere,alphabetList


#///////////////////////////////////////minimax///////////////////////////////////////
def minimax(game_state,depth):
	value=[]
	finalvalue1=[]
	v=-9999999999
	a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,player)
	filewrite.write("root"+","+str(0)+","+"-Infinity"+"\n")
	for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
		
		
		
		tempvalue,tempvalue1=(min_value(a,1,mancalaThere,capture,alphabetList))
		v=max(v,tempvalue)
		tempv=gettempvalues(v)
		filewrite.write("root"+","+str(0)+","+str(tempv)+"\n")
		
		value.append(tempvalue)
		finalvalue1.append(tempvalue1)
	print "minimax final contestants"
	print value
	print finalvalue1
	print numpy.argmax(value)
	print finalvalue1[numpy.argmax(value)]
	return finalvalue1[numpy.argmax(value)]


def min_value(game_state,depth,mancalaThere,capture,alphabetList1):

	print "action considered"
	print alphabetList1
	print game_state

	
	if (cutoff(game_state,depth) ):
		
		if(mancalaThere=="nomancala"):
			
			tempv=gettempvalues(evaluate(game_state))
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
			return evaluate(game_state),game_state
		# elif(mancalaThere=="mancala"):
			
		# 	v = evaluate(game_state)
	if(gameend(game_state)):
			
			print "capture or game end function"
			tempv=gettempvalues(evaluate(game_state))
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
			return evaluate(game_state),game_state
	
	if(mancalaThere=="mancala"):
		v=-9999999999
		
		print "player %d" %maxPlayer
		print "mancala and min_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,maxPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempv=gettempvalues(v)
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
			value1,state1=min_value(a,depth,mancalaThere,capture,alphabetList)
			if(value1>v and depth==1):
				state=state1
					
				

			v=max(v,value1)

	else:
		v=9999999999
		
		print "player %d" %minPlayer
		print "no mancala and min_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,minPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempv=gettempvalues(v)
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
			
			value1,state1=max_value(a,depth+1,mancalaThere,capture,alphabetList)
			if(value1<v and depth==1):
					
				state=game_state
					
				

			v=min(v,value1)

	tempv=gettempvalues(v)
	filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
	

	return v,state


def max_value(game_state,depth,mancalaThere,capture,alphabetList1):
	print "action considered"
	print alphabetList1
	print game_state
	
	
	if (cutoff(game_state,depth) ):
		if(mancalaThere=="nomancala"):
				
			tempv=gettempvalues(evaluate(game_state))
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
			return evaluate(game_state),game_state
		# elif((mancalaThere=="mancala")):
			
		# 	v = evaluate(game_state)
	if(gameend(game_state)):
			
			print "capture or game end function"
			tempv=gettempvalues(evaluate(game_state))
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
			return evaluate(game_state),game_state
	
	if(mancalaThere=="mancala"):
		v=9999999999
		
		print "player %d" %minPlayer
		print "mancala and max_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,minPlayer)
		state=a0[0]
		print maxPlayer
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempv=gettempvalues(v)
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
			
				
				
			value1,state1=max_value(a,depth,mancalaThere,capture,alphabetList)
			if(value1<v and depth==1):
				state=state1
				
				# print state
			v=min(v,value1)
	elif(mancalaThere=="nomancala"):
		v=-9999999999
	
		print "player %d" %maxPlayer
		print "no mancala and max_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,maxPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempv=gettempvalues(v)
			filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")
				
				
			value1,state1=min_value(a,depth+1,mancalaThere,capture,alphabetList)
			if(value1>v and depth==1):
				state=game_state
				# print "haha max"
				# print state
			v=max(v,value1)						
	tempv=gettempvalues(v)
	filewrite.write(alphabetList1+","+str(depth)+","+str(tempv)+"\n")	
	
		
		#print "v"
		#print v
	return v,state













#////////////////////////////////alpha beta/////////////////////////////////
def alphabeta(game_state,depth):
	value=[]
	finalvalue1=[]
	v=-9999999999
	alpha=-9999999999
	beta=9999999999
	a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,player)
	filewrite.write("root"+","+str(0)+","+"-Infinity,"+"-Infinity,"+"Infinity"+"\n")
	for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
		
		
		
		tempvalue,tempvalue1=(min_value_alphabeta(a,1,mancalaThere,capture,alphabetList,alpha,beta))
		v=max(v,tempvalue)
		
		alpha=max(alpha,v)
		tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
		filewrite.write("root"+","+str(0)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
		
		value.append(tempvalue)
		finalvalue1.append(tempvalue1)
	print "alphabeta final contestants"
	print value
	print finalvalue1
	print numpy.argmax(value)
	print finalvalue1[numpy.argmax(value)]
	return finalvalue1[numpy.argmax(value)]
def min_value_alphabeta(game_state,depth,mancalaThere,capture,alphabetList1,alpha,beta):

	print "action considered"
	print alphabetList1
	print game_state

	
	if (cutoff(game_state,depth) ):
		
		if(mancalaThere=="nomancala"):
			
			tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evaluate(game_state))
			filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
			return evaluate(game_state),game_state
		# elif(mancalaThere=="mancala"):
			
		# 	v = evaluate(game_state)
	if(gameend(game_state)):
		
		print "capture or game end function"
		tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evaluate(game_state))
		filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
		return evaluate(game_state),game_state
	
	if(mancalaThere=="mancala"):
		v=-9999999999
		
		print "player %d" %maxPlayer
		print "mancala and min_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,maxPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
			filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
			value1,state1=min_value_alphabeta(a,depth,mancalaThere,capture,alphabetList,alpha,beta)
			if(value1>v and depth==1):
				state=state1
					
				

			v=max(v,value1)
			if(v>=beta):
				tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
				filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
				return v,state
			alpha=max(alpha,v)


	else:
		v=9999999999
		
		print "player %d" %minPlayer
		print "no mancala and min_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,minPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
			filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
			
			value1,state1=max_value_alphabeta(a,depth+1,mancalaThere,capture,alphabetList,alpha,beta)
			if(value1<v and depth==1):
					
				state=game_state
					
				

			v=min(v,value1)
			if(v<=alpha):
				tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
				filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
				return v,state
			beta=min(beta,v)
	tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
	filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
	
	

	return v,state


def max_value_alphabeta(game_state,depth,mancalaThere,capture,alphabetList1,alpha,beta):
	print "action considered"
	print alphabetList1
	print game_state
	
	
	if (cutoff(game_state,depth) ):
		if(mancalaThere=="nomancala"):
				
			tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evaluate(game_state))
			filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
			return evaluate(game_state),game_state
		# elif((mancalaThere=="mancala")):
			
		# 	v = evaluate(game_state)
	if(gameend(game_state)):
		
		print "capture or game end function"
		tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,evaluate(game_state))
		filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
		return evaluate(game_state),game_state
	
	if(mancalaThere=="mancala"):
		v=9999999999
		
		print "player %d" %minPlayer
		print "mancala and max_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,minPlayer)
		state=a0[0]
		print maxPlayer
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
			filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
			
				
				
			value1,state1=max_value_alphabeta(a,depth,mancalaThere,capture,alphabetList,alpha,beta)
			if(value1<v and depth==1):
				state=state1
				
				# print state
			v=min(v,value1)
			if(v<=alpha):
				tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
				filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
				return v,state
			beta=min(beta,v)
	elif(mancalaThere=="nomancala"):
		v=-9999999999
		
		print "player %d" %maxPlayer
		print "no mancala and max_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,maxPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
			filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
				
				
			value1,state1=min_value_alphabeta(a,depth+1,mancalaThere,capture,alphabetList,alpha,beta)
			if(value1>v and depth==1):
				state=game_state
				#
				# print state
			v=max(v,value1)						
			if(v>=beta):
				tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
				filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
				return v,state
			alpha=max(alpha,v)
	tempalpha,tempbeta,tempv=gettempvaluesalphabeta(alpha,beta,v)
	filewrite.write(str(alphabetList1)+","+str(depth)+","+str(tempv)+","+str(tempalpha)+","+str(tempbeta)+"\n")
		
		#print "v"
		#print v
	return v,state
#/////////////////////////////////////////////greedy/////////////////////////////////////////////////////////

def greedy(game_state,depth):
	value=[]
	finalvalue1=[]
	v=-9999999999
	a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,player)
	
	for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
		
		
		
		tempvalue,tempvalue1=(min_value_greedy(a,1,mancalaThere,capture,alphabetList))
		v=max(v,tempvalue)
		
		
		value.append(tempvalue)
		finalvalue1.append(tempvalue1)
	print "minimax final contestants"
	print value
	print finalvalue1
	print numpy.argmax(value)
	print finalvalue1[numpy.argmax(value)]
	return finalvalue1[numpy.argmax(value)]


def min_value_greedy(game_state,depth,mancalaThere,capture,alphabetList1):

	print "action considered"
	print alphabetList1
	print game_state

	
	if (cutoff(game_state,depth) ):
		
		if(mancalaThere=="nomancala"):
			
			
			return evaluate(game_state),game_state
		# elif(mancalaThere=="mancala"):
			
		# 	v = evaluate(game_state)
	if(gameend(game_state)):
			
			print "capture or game end function"
			
			return evaluate(game_state),game_state
	
	if(mancalaThere=="mancala"):
		v=-9999999999
		
		print "player %d" %maxPlayer
		print "mancala and min_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,maxPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			
			value1,state1=min_value_greedy(a,depth,mancalaThere,capture,alphabetList)
			if(value1>v and depth==1):
				state=state1
					
				

			v=max(v,value1)

	else:
		v=9999999999
		
		print "player %d" %minPlayer
		print "no mancala and min_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,minPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			
			
			value1,state1=max_value_greedy(a,depth+1,mancalaThere,capture,alphabetList)
			if(value1<v and depth==1):
					
				state=game_state
					
				

			v=min(v,value1)


	

	return v,state


def max_value_greedy(game_state,depth,mancalaThere,capture,alphabetList1):
	print "action considered"
	print alphabetList1
	print game_state
	
	
	if (cutoff(game_state,depth) ):
		if(mancalaThere=="nomancala"):
				
			
			return evaluate(game_state),game_state
		# elif((mancalaThere=="mancala")):
			
		# 	v = evaluate(game_state)
	if(gameend(game_state)):
			
			print "capture or game end function"
			
			return evaluate(game_state),game_state
	
	if(mancalaThere=="mancala"):
		v=9999999999
		
		print "player %d" %minPlayer
		print "mancala and max_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,minPlayer)
		state=a0[0]
		print maxPlayer
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			value1,state1=max_value_greedy(a,depth,mancalaThere,capture,alphabetList)
			if(value1<v and depth==1):
				state=state1
				
				# print state
			v=min(v,value1)
	elif(mancalaThere=="nomancala"):
		v=-9999999999
	
		print "player %d" %maxPlayer
		print "no mancala and max_value function"
		a0,capture0,mancalaThere0,alphabetList0=Actions(game_state,maxPlayer)
		state=a0[0]
		for a,capture,mancalaThere,alphabetList in zip(a0,capture0,mancalaThere0,alphabetList0):
			
			
				
				
			value1,state1=min_value_greedy(a,depth+1,mancalaThere,capture,alphabetList)
			if(value1>v and depth==1):
				state=game_state
				# 
				# print state
			v=max(v,value1)						
	
	
		
		#print "v"
		#print v
	return v,state











#//////////////////////////////////////////////main////////////////////////////////////////
start_time = time.time()

nextstate_filewrite=open('next_state.txt','w+')
argv=sys.argv[1:]
try:
	opts, args = getopt.getopt(argv,"i")
except getopt.GetoptError:
	print 'usage is: python mancala.py -i <inputfile>'
print args
f=open(args[0], 'r') 
playerStates=[]
taskNumber = int(f.readline().strip())
player=int(f.readline().strip())
depth=int(f.readline().strip())
boardPlayer2=f.readline().strip()
boardPlayer1=f.readline().strip()
boardPlayer2List=[]
boardPlayer1List=[]
boardPlayer2List=boardPlayer2.split(" ")
boardPlayer2List = [int(i) for i in boardPlayer2List]
boardPlayer1List=boardPlayer1.split(" ")
boardPlayer1List = [int(i) for i in boardPlayer1List]
mancalaPlayer2=int(f.readline().strip())
mancalaPlayer1=int(f.readline().strip())
maxPlayer=player
lastDepth=depth-1
maxDepth=depth
if(maxPlayer==1):
	minPlayer=2
else:
	minPlayer=1
if((depth%2)==0):
	lastPlayer=minPlayer
else:
	lastPlayer=maxPlayer


print "maxPlayer"
print maxPlayer
print "lastPlayer"
print lastPlayer
for i in range(0,len(boardPlayer1List)):
	
	playerStates.append(boardPlayer1List[i])

playerStates.append(mancalaPlayer1)
i=len(boardPlayer2List)-1
while(i>=0):
	
	playerStates.append(boardPlayer2List[i])
	i=i-1
playerStates.append(mancalaPlayer2)
states=[]

evalValues=[]
print taskNumber
print player
print depth
print boardPlayer2List
print boardPlayer1List
print playerStates
print mancalaPlayer1
print mancalaPlayer2
print "////////////////input/////////////////////"
if(taskNumber==1):
	print "greedy"
	maxDepth=1
	greedysolution=greedy(playerStates,1)
	print greedysolution
	print "player 2 states"
	plyr2States=greedysolution[len(boardPlayer1List)+1:len(greedysolution)-1]
	plyr2States.reverse()
	print plyr2States
	for x in range(0,len(plyr2States)):
		nextstate_filewrite.write(str(plyr2States[x])+" ")
	nextstate_filewrite.write("\n")
	print "player 1 states"
	print greedysolution[0:len(boardPlayer1List)]
	for x in range(0,len(boardPlayer1List)):
		nextstate_filewrite.write(str(greedysolution[x])+" ")
	nextstate_filewrite.write("\n")
	print "player 2 mancala"
	print greedysolution[len(greedysolution)-1]
	nextstate_filewrite.write(str(greedysolution[len(greedysolution)-1])+"\n")
	print "player 1 mancala"
	print greedysolution[len(boardPlayer1List)]
	nextstate_filewrite.write(str(greedysolution[len(boardPlayer1List)])+"\n")




elif(taskNumber==2):
	filewrite = open('traverse_log.txt', 'w+')
	print "minimax"
	filewrite.write("Node"+","+"Depth"+","+"Value"+"\n")
	minimaxsolution= minimax(playerStates,depth)
	print "player 2 states"
	plyr2States=minimaxsolution[len(boardPlayer1List)+1:len(minimaxsolution)-1]
	plyr2States.reverse()
	print plyr2States
	for x in range(0,len(plyr2States)):
		nextstate_filewrite.write(str(plyr2States[x])+" ")
	nextstate_filewrite.write("\n")
	print "player 1 states"
	print minimaxsolution[0:len(boardPlayer1List)]
	for x in range(0,len(boardPlayer1List)):
		nextstate_filewrite.write(str(minimaxsolution[x])+" ")
	nextstate_filewrite.write("\n")
	print "player 2 mancala"
	print minimaxsolution[len(minimaxsolution)-1]
	nextstate_filewrite.write(str(minimaxsolution[len(minimaxsolution)-1])+"\n")
	print "player 1 mancala"
	print minimaxsolution[len(boardPlayer1List)]
	nextstate_filewrite.write(str(minimaxsolution[len(boardPlayer1List)])+"\n")


elif(taskNumber==3):
	filewrite = open('traverse_log.txt', 'w+')
	print "alpha beta"
	filewrite.write("Node"+","+"Depth"+","+"Value"+","+"Alpha,"+"Beta"+"\n")
	alphabetasolution= alphabeta(playerStates,depth)
	print "player 2 states"
	plyr2States=alphabetasolution[len(boardPlayer1List)+1:len(alphabetasolution)-1]
	plyr2States.reverse()
	print plyr2States
	for x in range(0,len(plyr2States)):
		nextstate_filewrite.write(str(plyr2States[x])+" ")
	nextstate_filewrite.write("\n")
	print "player 1 states"
	print alphabetasolution[0:len(boardPlayer1List)]
	for x in range(0,len(boardPlayer1List)):
		nextstate_filewrite.write(str(alphabetasolution[x])+" ")
	nextstate_filewrite.write("\n")
	print "player 2 mancala"
	print alphabetasolution[len(alphabetasolution)-1]
	nextstate_filewrite.write(str(alphabetasolution[len(alphabetasolution)-1])+"\n")
	
	print "player 1 mancala"
	print alphabetasolution[len(boardPlayer1List)]
	nextstate_filewrite.write(str(alphabetasolution[len(boardPlayer1List)])+"\n")


elif(taskNumber==4):
	print "competition"
