import os

# Reset the batch file
with open("thenewpoketext/export.cmd", "w"): pass

# Define the path to the folder containing the .nds files
folder_path = "./thenewpoketext/"

# Loop through all files in the folder that end with ".nds"
for file_name in os.listdir(folder_path):
    if file_name.endswith(".nds"):
        # Get the file name without the extension
        file_name_no_ext = os.path.splitext(file_name)[0]

        # Create the script file
        script_file_name = f"export_{file_name_no_ext}.txt"
        with open('thenewpoketext/' + script_file_name, "w") as script_file:
            script_file.write(f"{file_name}\n")
            script_file.write(f"getall xml/{file_name_no_ext}.xml\n")
            script_file.write("q")

        # Add the command to the batch file
        with open("thenewpoketext/export.cmd", "a") as batch_file:
            batch_file.write(f"thenewpoketext < {script_file_name}\n")

# Add the "@echo off" line to the batch file
with open("thenewpoketext/export.cmd", "r") as batch_file:
    lines = batch_file.readlines()

with open("thenewpoketext/export.cmd", "w") as batch_file:
    batch_file.write("@echo off\n")
    batch_file.writelines(lines)
