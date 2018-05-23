### Git

* Going back to the latest commit

		git reset --hard HEAD

* Going back to a specified commit

		# Resets index to former commit; replace '56e05fced' with your commit code
		git reset 56e05fced 

		# Moves pointer back to previous HEAD
		git reset --soft HEAD@{1}

		git commit -m "Revert to 56e05fced"

		# Updates working copy to reflect the new commit
		git reset --hard