# To-Do

Offline Queue :

	Save list of all ackd reqs with date
	nav to latest date in ack file
	add all recursively(?)

Basically the problem is the auth token expiring and the bot going offline. To prevent gaps in the playlist a list of all acknowledged requests will be storeded in a csv which can then be used as a "checkpoint", this means on startup the bot will correct any outtages.

# Update 2/25/22

Opted to change song look up into a try catch loop, if an error is caught the program will reboot itself in order to refresh the auth token received from spotify, if this doesn't work I think a 25 minute chronjob might do the trick.

Overall this was a more simple idea and prevents manual reboots, consider passing in the song that caused the error as a parameter so the bot doesn't drop any requests.
