import subprocess
import os
import shutil

dirname = os.path.dirname(__file__)

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

shutil.move(src, dst)
