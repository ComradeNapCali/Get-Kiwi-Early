# Get-Kiwi-Early

This repository contains the source code to the Corporate Clash content pack installing prank program, GetKiwiEarly.exe

The program fools people into believing that they will get the at-the-time unleased Kiwi species, but instead downloads a content pack that replaces every single texture and audio file to be the União Brasileira de Vídeo (A Brazilian video union similar to the MPAA) logo.

This was a program first made in November 2018, and was made to be a parody of a exploit tool.

This program is being made open source for archival reasons, as well as to assist any other people in creating similar programs.

[Here was the original YouTube video that showcased this program.](https://www.youtube.com/watch?v=BnjZrxG_nN8)

# Usage

To build this repository, you will need to copy and paste extracted phase files from the Corporate Clash to the `og_phases` folder.

Next, install any requirements by running `python3 -m pip install -r requirements.txt`, in addition to having a copy of [Panda3D's SDK](https://www.panda3d.org/).

Run `python3 build_phases.py` to create and package the phase files. If successful, a folder called built with multifiles will be created.

To build the installer, run `build_exe.bat`, which should build the executable to a folder called `dist`

# Notes

As this program was written a while ago, there are some things that were written unoptimally.

* The manifest URL is hardcoded into the installer.
    * In addition, Windows directory names are also hardcoded.
* Before open sourcing, comments were non-existent. Comments were retrofitted as part of the open source release.
* No clean-up function are in the code that automatically delete `phases` and `built`
* Deployment tools were not developed for this program.
* Some of the code is kind of sloppy.
    * For example, a couple of values used more then once were not assigned to variables.


# Credits

This repository contains sound effects from [freesound.org:](https://freesound.org/)

* error.wav - [Jazzy Chords by NenadSimic](https://freesound.org/people/NenadSimic/sounds/150879/)

* select.wav - [UI_Correct_button11.wav by ZenithInfinitiveStudios](https://freesound.org/people/ZenithInfinitiveStudios/sounds/342997/)

* finished.wav - [sf3-sfx-menu-back.wav by broumbroum](https://freesound.org/people/broumbroum/sounds/50557/)


# License

All source code contents of this repository are licensed under The Unlicense.

For more infomation, see LICENSE.md or [unlicense.org](https://unlicense.org/)

All images contained in this repository are licensed under the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/)

error.wav and select.wav are licensed under the [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/)

finished.wav is licensed under the [CC BY 3.0 license](https://creativecommons.org/licenses/by/3.0/)