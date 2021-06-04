# Usage
1) Install the `esm_tools` as instructed in the documentation first: https://esm-tools.readthedocs.io/en/latest/index.html
2) Perform a dry run before executing the command with `--dry-run` option:

    `./install_editable_tools.py --dry-run --base-dir /path/to/manual/installation`

* Under the `base_dir` you will have 
    * `esm_calendar`
    * `esm_database`
    * `esm_environment`
    * `esm_master`
    * `esm_motd`
    * `esm_parser`
    * `esm_plugin_manager`
    * `esm_profile`
    * `esm_rcfile`
    * `esm_runscripts`
    * `esm_version_checker`
* If you omit `base_dir` it will use you current working directory instead (eg. `${PWD}`).

3) Run the command: `./install_editable_tools.py --base-dir /path/to/manual/installation`
4) `esm_versions check` to verify that your tools have been installed in the editable mode.
