# You come into work one day with a new device that you haven't worked with before. This device is reponsible for controling all of the
# lights in the facility. However, for some reason, when you try to export the part numbers from the device, instead of giving them to
# like a csv, it gives you two very long string.


export_string_1 = "LT47055_LT47110-1_LT47110-2_LT47415_LT47425_LT52110_LT52119.01_LT52130-1_LT52130-2_LT52208.01-1_LT52208.01-2_LT52216.01_LT52226.06_LT52258.01-1_LT52258.01-2_LT52266.01_LT52274.06_LT52304.06_LT52308.01-1_LT52308.01-2_LT52316.01_LT52354.06_LT52358.01-1_LT56106-1_LT56106-2_LT56106-3_LT56107-1_LT56107-2_LT56107-3_LT56107-4_LT56108-1_LT56108-2_LT56108-3_LT56109-1_LT56109-2_LT56109-3_LT56109-4_LT56110-1_LT56110-2_LT56110-3_LT56111-1_LT56111-2_LT56113-4_LT56114-1_LT56114-2_LT56114-3_LT56115-1_LT56115-2_LT56115-3"
export_string_2 = "LT47040_LT47050_LT52358.01-2_LT52366.01_LT52606.02_LT52626.02_LT52706.02_LT52708_LT52726.02_LT52728_LT52734_LT52805_LT52810_LT52820_LT52830_LT52910_LT52920_LT52930_LS56010-1_LS56010-2_LS56010-3_LT56002-1_LT56002-2_LT56010_LT56010-1_LT56010-2_LT56010-3_LT56010-4_LT56101-1_LT56101-2_LT56101-3_LT56101-4_LT56102-1_LT56102-2_LT56102-3_LT56103-1_LT56103-2_LT56103-3_LT56103-4_LT56104-1_LT56104-2_LT56104-3_LT56105-1_LT56105-2_LT56105-3_LT56111-3_LT56111-4_LT56112-1_LT56112-2_LT56112-3_LT56113-1_LT56113-2_LT56113-3_LT56105-4"

# The part numbers are separated by underscores. As this is an Amazon site, the part type is followed by the panel number.
# Your superior needs to know how many lights are associated with panel 47 and 56 combined.