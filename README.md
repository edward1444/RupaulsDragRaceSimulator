Rupaul's Drag Race Simulator:


Ultimate Goals:

	1) Complete the mini Python program
	
	2) Make a mini-website to host the game
	

Overview of Classes:

	Queen(self, name, sewStat, danceStat, singStat, actStat, humorStat, minWinCt = 0, winCt = 0, lipsyncCt = 0)
	
	Challenge(self,name,challengeType, isElim)
	
	TeamChallenge extends Challenge(..., teamCount, countIndiv)
	
	# Note: teamCount could be considered redundant, perhaps get rid of the attribute
	

Overview of "Big Data" to use:

	contest_obj # a list full of Queen objects, all already initialized
	
	challenge_obj # a list full of Challenge/TeamChallenge objects, all already initialized
	

Overview of Functions:

	printRemaining(contest_obj) # Takes in a Queen object list, prints out all the Queen objects' names
	
	countRemaining(contest_obj) # Takes in a Queen object list, returns the amount of Queen objects in the list
	
	miniChallenge(contest_obj)  # Takes in a Queen object list, randomly assigns a Winner (because the Mini-Challenge
	
				    	# winner on the show most likely doesn't affect the Queen's overall performance)
				    	
	sortIntoTeams(contest_obj, numTeams) # Takes in a Queen object list AND a list of the teams' counts (Ex: if numTeams = [6,5],
	
					     	# then there are 2 teams with one team having 6 Queens, and another having 5 Queens,
					     	
					     	# hence is why I believe that TeamChallenge.teamCount is redundant because we are
					     	
					     	# accessing the countIndiv attribute instead
					     	
