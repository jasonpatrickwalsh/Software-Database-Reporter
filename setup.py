from cx_Freeze import setup, Executable
	
setup(
    name = "Software Database Adjuster",
    version = "1.6",
    description = "Software Database Adjuster Tool",
	author="Jason Walsh",
    executables = [Executable("gui.py")])