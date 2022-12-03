
# Merge


### Setup

	git config merge.tool vimdiff
	git config merge.conflictstyle diff3
	git config mergetool.prompt false

### Start

	git mergetool



### Choose

- Remote
  
		:diffg RE

- Base
		
		:diffg BA

- Local
	
		:diffg LO


### Finish

	:xa
	git commit -m 'message'
	git clean
