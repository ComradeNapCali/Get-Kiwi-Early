import shutil
import glob
import os
import sys
import subprocess

print("Building GetKiwiEarly...")

# If the phases folder does not exist, create it.
if not os.path.isdir("phases"):
    os.mkdir("phases")

# Get a list of the phase folders in og_phases.
original_phases_list = glob.glob("og_phases/*")

# Copy the folders in og_phases into the phases folder, this is so that we have a backup of the phases.
for phases in original_phases_list:
    print("Copying: {}".format(phases.split(os.sep)[1]))
    shutil.copytree(os.path.abspath(phases), os.path.abspath("{}/{}".format("phases", phases.split(os.sep)[1])))

replacement_files = ["ubv_logo.jpg", "ubv_logo.rgb", "ubv_logo.png", "ubv_music.ogg", "ubv_sound_effects.ogg"]

# Get the files in the phases we are going to replace.
file_replace_list = glob.glob("phases/**", recursive=True)

for file in file_replace_list:
    for replacements in replacement_files:
        if file.endswith(replacements.split(".")[1]):
            # If the directory has bgm and is an audio file, make sure that it's replaced with ubv_music.ogg.
            if ('bgm' in file) and (replacements.split(".")[1] == 'ogg'):
                replacements = 'ubv_music.ogg'
            print("Replacing: {}".format(file))
            # Overwrite the files themselves.
            shutil.copyfile(os.path.abspath(replacements), file)

phase_numbers_list = glob.glob("phases/*")

if not os.path.isdir("built"):
    os.mkdir("built")

# Build the multifiles with multify.
for phase_numbers in phase_numbers_list:
    phase_name = phase_numbers.split(os.sep)[1]
    print("Packing: {}".format(phase_name))
    subprocess.Popen("multify -C {} -cf {} {}".format(os.path.abspath("phases"), "built/{}.mf".format(phase_name), os.path.basename(phase_numbers)), shell=True)

print("All done!")