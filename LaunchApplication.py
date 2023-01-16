import subprocess
from subprocess import PIPE

def launch(application_path):
    subprocess.Popen(application_path, shell=True, stdout=subprocess.PIPE)
