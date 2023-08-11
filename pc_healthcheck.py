"""
PC Health Checker
by: Benedict Z. Castro
benedict.zcastro@gmail.com
"""

# Import needed modules
import shutil
import psutil

# Create functions to check for disk usage and CPU percent usage


def check_disk_usage(disk: str) -> bool:
    """This function checks the disk usage of the PC and returns True if the free space is greater than 20%."""
    du = shutil.disk_usage(disk)
    free_percentage = du.free / du.total * 100
    return free_percentage > 20


def check_cpu_usage() -> bool:
    """This function check the CPU usage of the PC for 1s, and returns True if it is less than 75%"""
    usage = psutil.cpu_percent(1)
    return usage < 75


# Main


def main():
    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR!")
    else:
        print("Everything is OK!")


# Run script
if __name__ == "__main__":
    main()
