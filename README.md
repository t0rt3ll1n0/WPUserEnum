# WPUserEnum v1.4
This basic python3 script check if your wordpress installation is vulnerable to user enum in /wp-json/wp/v2/users
## Usage:
````~$ python3 WP.py http://www.site.com````

## Usage with a list (WP_LIST.py):
(I know that the code i weird)
````python
#!/usr/bin/env python3

import os
import sys

try:
    filelist = sys.argv[1]
except IndexError:
    print("Usage: python3 WP_LIST.py list.txt")
    exit(0)

f = open(filelist, "r")
x = f.read().split()
for site in x:
    os.system(f"python3 WP.py {site}")
````

````~$ python3 WP_LIST.py list.txt````
Note: the format of the list must be like:
````
http://www.site.com
http://www.site2.com
http://www.site3.com
````

### To enable colors in cmd/powershell run:
````reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f````

- Fake useragents for bypass something ;)

- Username extraction with ID, username and full name

- Status code detection

~ If you found any bug/improve, message me on telegam @Davidet
