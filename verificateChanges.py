import os
import subprocess

dirs = [d for d in os.listdir(".") if os.path.isdir(d)]

valid_keys = ["limpio", "clean"]

def verify(s):
    s = s.lower()
    for k in valid_keys:
        if k in s:
            return False
    return True

if __name__ == '__main__':
    programOutput = ""
    for d in dirs:
        if os.path.isdir(os.path.join(d, ".git")):
            subprocess.run(["git", "add", "."], cwd=d)
            output = subprocess.check_output(["git", "status"], cwd=d, text=True)
            if verify(output):
                programOutput += "\"" + d + "\" dir has changes.\n"

    if (programOutput):
        print(programOutput, end='')
    else:
        print('All ok.')