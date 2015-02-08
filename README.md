# greenhat <img src="https://github.com/4148/greenhat/blob/master/greenhat.png" alt="greenhat image" width="10%" height="10%"/>
greenhat is a quick hack for decorating your GitHub contribution calendar with commits for the past `n` days. It uses the `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environmental variables to make commits appear in the past. Be warned that greenhat will clobber your repository's commit history.

### How to Use
Place `greenhat.py` in your Git repository. Make sure your remote repository URL is set, and that you have a [public SSH key setup](https://help.github.com/articles/generating-ssh-keys/). Then run the script with the python interpreter, with an integer specifying `n` number of days before today to generate commits for. E.g.,

	python greenhat.py <n>

It might take a while to generate all the commits. Enjoy your decorated calendar!
