import os
import time

# Path to the file/directory
path = r"C:\Program Files (x86)\Google\pivpT.png"

# Both the variables would contain time
# elapsed since EPOCH in float
ti_c = os.path.getctime(path)
ti_m = os.path.getmtime(path)

# Converting the time in seconds to a timestamp
c_ti = time.ctime(ti_c)
m_ti = time.ctime(ti_m)
print( f"The file located at the path {path} was created at {c_ti} and was last modified at {m_ti}")