
import subprocess


def create_process(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read()
    code = p.wait()
    return code, result



print  create_process('df -h')

#print  create_process('tfad -h')