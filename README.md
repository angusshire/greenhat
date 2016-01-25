# greenhat <img src="https://github.com/4148/greenhat/blob/master/greenhat.png" alt="greenhat image" width="10%" height="10%"/>
greenhat is a quick hack for decorating your GitHub contribution calendar with commits for the past `n` days. It uses the `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environmental variables to make commits appear in the past. Be warned that greenhat will clobber your repository's commit history.

### How to Use
Place `greenhat.py` in your Git repository. Make sure your [remote repository URL is set](https://help.github.com/articles/adding-a-remote/), and that you have a [public SSH key set up](https://help.github.com/articles/generating-ssh-keys/). Then run the script with the python interpreter, with an integer specifying `n` number of days before today to generate commits for. E.g.,

	python greenhat.py <n>

It might take a while to generate all the commits. If greenhat stops before it finishes, you can resume where you last left off by specifying a date before today when you want it to resume, like so:

	python greenhat.py <n> <date>

`n` is the remaining days you want to generate commits for, and `date` is a date string in the form `yyyy-mm-dd`  (e.g., 2013-04-05).

#### An Example

The following calendar is the result of running `python greenhat.py 365`:

<img src="https://github.com/4148/greenhat/blob/master/example.png" alt="example image"/>

The run took a total of eight hours. Beautiful, isn't it?

Enjoy your decorated calendar!

### License
greenhat is distributed under the GNU General Public License v3.0 (GPLv3).
