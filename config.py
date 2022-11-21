def init():
    global temp
    global humid

    global humid_limit
    humid_limit=80
    global temp_limit

    global temp_threshold
    temp_threshold=2
    global humid_threshold
    humid_threshold=5

    global pre_temp
    global pre_humid

    global status  # 1-Idle 2-Pending 3-Spraying 4-Aborting
    status=1

    global spraying
    spraying=False

    global spray_til
    spray_til = 30

    global spray_TIMEOUT
    spray_TIMEOUT=60

    global auto_delay
    auto_delay=1800
