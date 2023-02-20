import subprocess
import os
import shutil

os.chdir("./thenewpoketext")

if not os.path.exists('./xml'):
    os.makedirs('./xml')

unpacking = subprocess.call(["batch.cmd"])

os.chdir("../")

msg_changer = subprocess.call(["python", "msg_name_changer.py"])

os.chdir("./thenewpoketext")

unpacking = subprocess.call(["batch.cmd"])

os.chdir("../")

src = './thenewpoketext/xml'
dst = './xml'

# Remove the existing xml directory
if os.path.exists(dst):
    shutil.rmtree(dst)

# Move the thenewpoketext/xml directory to the xml directory
shutil.move(src, dst)
