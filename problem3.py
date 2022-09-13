# Victer Phiathep
# RUID : 179005525

# Write two function to convert between military time
# and 12 hour format


def ampm_to_military(ampm_time):
    pass



def military_to_ampm(mil_time):
    if int(mil_time[0]) <= 12:
        converted_time = f"{mil_time[0:1]}:{mil_time[2:3]}am"
        return converted_time
    else:
        hours = int(mil_time[0:1])- 12
        converted_time = f"{hours}:{mil_time[2:3]}pm"



military_to_ampm('1212')
