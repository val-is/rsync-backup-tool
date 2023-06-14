# rsync-backup-tool

python script/tool to make configurable backups with rsync easier to manage.

## usage

tool can be configured with a `.txt` file.
each line in the file is a directory that will be copied to the rsync backup host.

the tool is used at the command line like:
`python client_sync.py --path-list config.txt --remote-host user@hostname --remote-folder /home/user/backups/...`

`user` should be the user account to save under; `hostname` the hostname or IP of the remove host; `--remote-folder` points to the (existing) directory to save things under.

folders will be copied over and saved under `remote-folder/dir-sent` where `folder-sent` is the name of the local directory
