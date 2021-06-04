#!/usr/bin/env python
import os
import sys
import argparse

tools = [
    "esm_calendar",
    "esm_database",
    "esm_environment",
    "esm_master",
    "esm_motd",
    "esm_parser",
    "esm_plugin_manager",
    "esm_profile",
    "esm_rcfile",
    "esm_runscripts",
    # omit this since it is usually already in editable mode
    # "esm_tools",     
    "esm_version_checker"
]

url_prefix = r"https://github.com/esm-tools/"
github_urls = [f"{url_prefix}{tool}" for tool in tools]

# parse the command-line arguments
argparser = argparse.ArgumentParser()
argparser.add_argument('--dry-run', action='store_true', help='print the actions without changes')
argparser.add_argument('--base-dir', action='store', type=str, help='directory where actions take place')
args = argparser.parse_args()

# initialize the command-line arguments
dry_run = False
dry_run = args.dry_run

base_dir = os.getcwd()
base_dir = args.base_dir
# correct the path string if it does not end with '/'
base_dir = os.path.abspath(base_dir)
if base_dir[-1] != os.path.sep:
    base_dir += os.path.sep

# Check before executing the commands
if not os.path.isdir(base_dir):
    print(f"ERROR: the directory: {base_dir} does not exist. Exiting")
    sys.exit(1)

if dry_run:
    print(f"NOTE: --dry-run is activated. Actions will be printed but not executed\n")

print(f"::: Installing the tools under the directory: {base_dir}\n") 

# loop over the tools and execute the commands. Use --dry-run first
for tool, url in zip(tools, github_urls):
    print(f"::: Processing the tool: {tool}")
    
    # step 1) enter the directory

    if dry_run:
        print(f"    - Entering the directory: {base_dir}")
    else: 
        os.chdir(base_dir)

    # step 2) clone the repo
    clone_command = f"git clone {url}"

    if dry_run: 
        print(f"    - Cloning: {clone_command}")
    else: 
        os.system(clone_command)

    # step 3) enter the tool's directory
    cwd = os.getcwd()
    new_path = f"{base_dir}{tool}{os.path.sep}"

    if dry_run:
        print(f"    - Entering the directory: {new_path}")
    else: 
        os.chdir(new_path)

    # step 4) install the tool here
    install_command = f"python -m pip install -e ."
    if dry_run:
        print(f"    - Installing: {install_command}")
    else:
        os.system(install_command)

    # go up
    os.chdir("..")
    print("")
