import time
import platform
import subprocess

REPORT_FILE_NAME = 'logfile.txt'
HOSTNAME = "google.com"
PACKETS_NUM = 1
COMMAND_INTERVAL = 5


def Main():
    # get system name
    systemName = platform.system().lower()

    command = ['ping']

    # option for the number of packets as a function of
    command.append('-n' if systemName == 'windows' else '-c')
    command.append(str(PACKETS_NUM))

    command.append(HOSTNAME)

    with open(REPORT_FILE_NAME, 'w') as f:
        command_str = ' '.join(command)
        f.write('REPORT\n')
        f.write('Command: ' + command_str + '\n')

    while True:
        is_error, output = subprocess.getstatusoutput(command)

        if is_error:
            CT = time.strftime("%H:%M:%S %d/%m/%y")
            with open(REPORT_FILE_NAME, 'a+') as f:
                f.write('\n' + CT)
                f.write('\n' + output)
                f.write('\n' + '-----------------------------------')
        time.sleep(COMMAND_INTERVAL)


if __name__ == "__main__":
    Main()
