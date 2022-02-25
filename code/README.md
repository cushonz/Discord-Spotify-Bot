# To-Do

Offline Queue :

	Save list of all ackd reqs with date
	nav to latest date in ack file
	add all recursively(?)

Basically the problem is the auth token expiring and the bot going offline. To prevent gaps in the playlist a list of all acknowledged requests will be storeded in a csv which can then be used as a "checkpoint", this means on startup the bot will correct any outtages.
