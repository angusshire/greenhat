from datetime import date, timedelta
from random import randint
from time import sleep
import sys
import subprocess
import os

# returns a date string for the date that is N days BEFORE today
def get_date_string(n):
	d = date.today() - timedelta(days=n)
	rtn = d.strftime("%a %b %d %X %Y %z -0400")
	return rtn

# main app
def main(argv):
	if len(argv) != 1:
		print "Error: Bad input."
		sys.exit(1)
	n = int(argv[0])
	i = 0
	devnull = open(os.devnull, 'w')
	while i <= n:
		curdate = get_date_string(i)
		num_commits = randint(1, 25)
		for commit in range(0, num_commits):
			subprocess.call("echo '" + curdate + str(randint(0, 1000000)) +"' > realwork.txt; git add -A; GIT_AUTHOR_DATE='" + curdate + "' GIT_COMMITTER_DATE='" + curdate + "' git commit -m 'update'; git push;", shell=True)#, stdout=devnull, stderr=devnull)
			sleep(.5)
		i += 1

if __name__ == "__main__":
	main(sys.argv[1:])
