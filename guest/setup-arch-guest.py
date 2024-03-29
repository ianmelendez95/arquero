from subprocess import *
import sys


def main():
    ping_arch()
    fdisk()


def ping_arch():
    try:
        check_call(['ping', '-c', '1', 'archlinux.org'], timeout=3)
    except TimeoutExpired:
        error('Unable to ping archlinux.org, network not configured')


def fdisk():
    print("Formatting /dev/vda")
    fdisk_proc = Popen(['fdisk', '/dev/vda'], stdin=PIPE, text=True)
    swap = 'n\np\n1\n\n+5G\nt\n82\n'
    root = 'n\np\n2\n\n-16.5K\nt\n83\n'
    full = swap + root + 'w\n'
    fdisk_proc.communicate(input=full, timeout=5)
    # fdisk_proc.stdin.write('n\np\n1\n\n+5G\nt\n82\n')
    # fdisk_mk_swap(fdisk_proc)
    # fdisk_mk_root(fdisk_proc)
    # fdisk_proc.stdin.write('a\n2\n')  # make MBR bootable on root partition
    # fdisk_proc.stdin.write('w\n')  # commit changes
    # fdisk_proc.stdin.flush()
    #
    # if fdisk_proc.wait() != 0:
    #     error('Error partitioning disk: ' + str(fdisk_proc.returncode))

    print("Formatted /dev/vda")


def fdisk_mk_swap(fdisk_proc):
    fdisk_proc.stdin.write('n\np\n1\n')  # new primary partition, default number
    fdisk_proc.stdin.write('\n+5G\n')  # default sector start, +5GB end partition (swap)
    fdisk_proc.stdin.write('t\n82\n')  # type to 'Linux swap'
    
    
def fdisk_mk_root(fdisk_proc):
    fdisk_proc.stdin.write('n\np\n2\n')  # new primary partition, default number
    fdisk_proc.stdin.write('\n-16.5K\n')  # default sector start, take rest of disk minus 16.5KiB at the end
    fdisk_proc.stdin.write('t\n83\n')  # type to 'Linux'
    

def write_line(popen, msg=''):
    popen.stdin.write(msg + '\n')
    popen.stdin.flush()


def error(msg):
    print(msg, file=sys.stderr)
    exit(1)


if __name__ == '__main__':
    main()

#
# set -e
#
# function error() {
#   msg="$1"
#   echo "ERROR: " msg
# }
#
# MYIP=$(dig whoami.cloudflare ch txt +short @1.1.1.1)
# if ! timeout 1 ping -c 1 archlinux.org; then
#   echo "ERROR: "
