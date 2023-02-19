import os

# specify the parent directory to search for "tmp_" folders
parent_dir = './thenewpoketext/'

# iterate over all the directories in the parent directory
for dirname in os.listdir(parent_dir):
    if not dirname.startswith('tmp_'):
        continue

    # build the full path to the "msgdata" directory in the current directory
    msgdata_dir = os.path.join(parent_dir, dirname, 'root', 'msgdata')

    # check if the "msgdata" directory exists
    if not os.path.exists(msgdata_dir):
        continue

    # rename the "msg.narc" file to "msg1.narc"
    msg_file = os.path.join(msgdata_dir, 'msg.narc')
    msg1_file = os.path.join(msgdata_dir, 'msg1.narc')
    if os.path.exists(msg_file):
        os.rename(msg_file, msg1_file)

    # rename the "pl_msg.narc" file to "msg.narc"
    pl_msg_file = os.path.join(msgdata_dir, 'pl_msg.narc')
    if os.path.exists(pl_msg_file):
        os.rename(pl_msg_file, msg_file)
