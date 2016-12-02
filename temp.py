from subprocess import call


# cache_file = open('cachefile', 'r')
# xsan_volumes = []
#
# for line in cache_file:
#     volume_name = line.split(" - ")[0]
#     volume_mounted = line.split(" - ")[1].replace('\n', '')
#
#     if volume_mounted == "not mounted":
#         print volume_name + " is " + volume_mounted
#         xsan_volumes.append([volume_name, volume_mounted])
#     else:
#         print volume_name + " is mounted"
#         xsan_volumes.append([volume_name, "mounted"])
#
# print xsan_volumes

# ######################################

def mount_volume(self):

    f = open("cachefile", "w")
    try:
        call(["ls", "-l"]) #, stdout=f
        f.close()

    except (OSError, SyntaxError):
        print "this failed OS"

    cache_file = open('cachefile', 'r')
    for line in cache_file:
        volume_name = line.split(" - ")[0]
        volume_mounted = line.split(" - ")[1].replace('\n', '')
        mount_button_name = 'mount_btn_' + volume_name
        unmount_button_name = 'unmount_btn_' + volume_name

        if volume_mounted == "not mounted":
            print volume_name + " is not " + volume_mounted
            unmount_button_name.state = "down"
            mount_button_name.state = "normal"
        else:
            print volume_name + " is mounted"
            mount_button_name.state = "down"
            unmount_button_name.state = "normal"

mount_volume(self)

PRATT - / Volumes / PRATT
# WILLIAMS - not mounted
# LAMBERT - /Volumes/LAMBERT
#