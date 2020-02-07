import git
repo = git.Repo( '/home/pknviki95/Desktop/Python' )
print (repo.git.status())
# checkout and track a remote branch
#print repo.git.checkout( 'origin/somebranch', b='somebranch' )
#add a file
print (repo.git.add( '.' ))
#commit
print (repo.git.commit( m='git operations using python scripts' ))
#now we are one commit ahead#
print (repo.git.FetchInfo())
print(dir(git))