'''
3 i/p:
- git url = https://github.com/pknviki95/Python_script.git
-tag name = v_1.0
-tag location/if not given HEAD

store the output value to a file
tag_name.log
'''

import subprocess

def git_log(git_url,tag_name,tag_pos):
    file_name = tag_name+'.log'
    with open (file_name,'w') as f:
        subprocess.run('git clone '+git_url ,stdout=f,stderr=f,stdin=f,shell=True)

            
        if  tag_pos == None:
            subprocess.run('git checkout master',stdout=f,stderr=f,stdin=f,shell=True)
            
        else:
            subprocess.run('git checkout '+tag_pos,stdout=f,stderr=f,stdin=f,shell=True)
            
        subprocess.run('git tag '+tag_name ,stdout=f,stderr=f,stdin=f,shell=True) 
        subprocess.run('git push origin '+tag_name,stdout=f,stderr=f,stdin=f,shell=True)  
        subprocess.run('git show '+tag_name ,stdout=f,stderr=f,stdin=f,shell=True)
        
        subprocess.run('git add .' ,stdout=f,stderr=f,stdin=f,shell=True)
        git_commit_message = input("your message: ")
        subprocess.run('git commit -m '+git_commit_message ,stdout=f,stderr=f,stdin=f,shell=True)
        
        subprocess.run('git push origin master',stdout=f,stderr=f,stdin=f,shell=True)
        subprocess.run('git log --all --oneline'  ,stdout=f,stderr=f,stdin=f,shell=True)
        





git_logging = git_log(git_url = input("enter git_url :" ),tag_name = input("tag_name : " ),tag_pos = input("tag_pos : "))
print(git_logging)
