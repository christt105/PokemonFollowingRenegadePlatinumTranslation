import subprocess
import os
import shutil
import msg_name_changer

os.chdir("./thenewpoketext")

for file_name in os.listdir("./"):
    if file_name.startswith("tmp_"):
        shutil.rmtree(file_name)

if not os.path.exists('./xml'):
    os.makedirs('./xml')

unpacking = subprocess.call(["thenewpoketext_script_export.cmd"])

os.chdir("../")

msg_name_changer.rename_msg_files()

os.chdir("./thenewpoketext")

unpacking = subprocess.call(["thenewpoketext_script_export.cmd"])

os.chdir("../")

src = './thenewpoketext/xml'
dst = './xml'

# Remove the existing xml directory
if os.path.exists(dst):
    shutil.rmtree(dst)

# Move the thenewpoketext/xml directory to the xml directory
shutil.move(src, dst)
