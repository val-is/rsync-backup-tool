import argparse
import pathlib
import subprocess

def parse_dir_sync_list(filename):
    paths_out = []
    with open(filename, 'r') as f:
        paths = f.readlines()
        for path in paths:
            paths_out.append(pathlib.Path(path).resolve())
    return paths_out

def sync_files(dir_paths, remote_host, remote_host_folder):
    for path in dir_paths:
        subprocess.Popen(["rsync", "-av",
                        "--delete", "-e", "ssh",
                        str(path),
                        f"{remote_host}:{remote_host_folder}/{path.name}"])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path-list", dest="path_file", required=True)
    parser.add_argument("--remote-host", dest="remote", required=True)
    parser.add_argument("--remote-folder", dest="remote_folder", required=True)
    args = parser.parse_args()

    sync_list = parse_dir_sync_list(args.path_file)
    sync_files(sync_list, args.remote, args.remote_folder)