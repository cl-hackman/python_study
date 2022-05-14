import time, sys
indent = 0 # How many spaces to indent
indentIncreasing = True # Wether the indentations is increasing or not

try:
    while True: # The main loop
        print(" " * indent, end="")
        print("********")
        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces:
            indent += 1
            if indent == 20:
                # change direction:
                indentIncreasing = False
        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()