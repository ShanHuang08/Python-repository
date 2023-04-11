import subprocess, os
def cd(cmd):
    #cmd is expected to be something like "cd [place]"
    cmd = cmd + " && dir" # add the pwd command to run after, this will get our directory after running cd
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) # run our new command
    out = p.stdout.read()
    err = p.stderr.read()
    # read our output
    if out != "":
        # print(out)
        print(len(out))
        print(type(out))
        os.chdir(out[0:len(out) - 1]) # if we did get a directory, go to there while ignoring the newline 
    if err != "":
        print(err) # if that directory doesn't exist, bash/sh/whatever env will complain for us, so we can just use that
    return

cd("cd C:\\users")