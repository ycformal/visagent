Question: The right image features a dog with its front paws on a table top, and the left image features a dog lying down with another dog figure next to it.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/56/b5/8e/56b58e72556544d5ed2751b19e4e6915--hungarian-vizsla-wake-up.jpg

Right image URL: https://i.pinimg.com/736x/9b/06/c7/9b06c7caeedb7fae287a9eb6b8ff551c--butterfly-wings-training-center.jpg

Original program:

```
Statement: The right image features a dog with its front paws on a table top, and the left image features a dog lying down with another dog figure next to it.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image features a dog with its front paws on a table top, and the left image features a dog lying down with another dog figure next to it.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA+AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0QODyDTZZI4wDI6qCcDccZNYNjq5lgWRNrruKfeHJA5Az+FbtpcNLu3LsAQsCSDng9we1fCYbL6tWpGMk1F9bHtVKsYRbW5Va8tAcfaIs+m4VQ1Wx03UrRpLm2guPLGVLqCVPam3nizTLa4WPzGd2O1CsZIY+x+tVtR1l5LaWVbaVxtAd1wcDP1/zmu95R7NqVObun+HUyWIb0lE5DWtFmvzOsJtAs2wlpUJddueAe3WtjRNJie+tLG4VXid1BBGQcc4P5VKkyuS2CB6kVd0Jw/iKxA/564/Q16SqTfLFvREckVdpbmrB4P0a3P2kWUPmE+YGTKFT7YrpNP1Gzs7aCIRyBUQIDwcisya78uLGenFc/c6kY9oDHgjqa9ySUY6HlKTb1PV7TULW7+WCUMwHIwQast901wfhPVrZNTS1ubuCOeeFpYomkAZ1yOQPwNcPrl/rvhv4sXGpx3k0+lzv/q1uNwZCoJCpk8Ke+Ki5Z2usX2s3Gt3sFlqMdraW7rGP9HV2LbQWOT7tWdJpes3EqtJ4iu9ydNkMSgZ/4DVDR/G/h57dp7/VIYLi4nkeRZlZQCWOBkjB4xV5vFujvBfzRaxYyLHC7Rosy5JAOMDr2rohCLWpjOTTsZ+keMNLg0qGPUdTea7G7zHeNiT8xxyBjpiiuItorxIF2Qw3iEArKJgB0HHIzxRXC03qejy01pZ/f/wDGtPHWoWunR2n7lEXcMhcNyck5Hf3rsPDniG61nQdTlcoFiMcICZHDdSf8968zbSLxnVBbsWPYEV2vhGRNO0LVtPmYC4kBlI9AF4P5ionyWtFji5dYkOsxXbBQZkcRnMe47Sp9mrFtLxluHTU4rp4t3zjzSQO+cDtU8uqQXdsVuG2jdtBzyvoTS2l0Y7srcqCyYUkDhh2P0rnhdbm9SzWh0+mXUVzBugk3opPOetbvh8hPEFg3YS5/Q1kfZbWxtbae0VEjnzuUcZbqf0qykk0O2S2KiYfNGXBIz7gVhUhyVEKMuaJ0V/Md0gB/jb+Zrm9U1+3060CG1hN70VnXcuP7xHr+hqld/2/qRKteRW8JJyLbgnn+8efyrmNU0O8i1CG2tYmlMiFwxfl2zzyep6V6k580EkcNOPLN3LwmMmLqV2lYDALc8eg9Bz0qAzyXFsf3UihjlAqnIq78O7Z9Rn1G1Y7khCuM/3iSCM/hXYQWVplsvuZTjb6YrhnGUWdsakXojziTQtYlTfBKnlEfLDN/CPTkEVRn2QRfZbyaK3a0UNvhtlaQNjIAYYyOnXvXoGo3qWMM0zYCRgnk4ryTUbhry8uZA4ZZ5Acjv8AhXZRlKW5yVoxjsX7t71LuRZLqWSTOXZ5Ocnntx3oqleafDayrHcXcsExUM8IQnYT2PPXGPzorayMrtHs2nafp1vp8NxeSCPfkSP6Mei/TrWJr2kXExaK1+eJfnW4RQCQRyMjqPWp/E2ntLpc4gEzW00ayE5+6QcnjpkY9vf1rI0bQL8R212jzSwSIZYJN2SgXjkdvwzXney3cWeiquyZyF9pdzaSIjksJTleCdw9q7Tw/wCHmkhhlvmwUTamOq/X86ng0559as7vUFkktdpETSE7ST2wenNdc2YV2osanGQNoXI6V1whdXkctapaVonHXWhan9qjiiZWtYW8yNh0Hc8dumMe9aFncssTFmUEDgsMgfhV67uwN27APcK2a4PXbjytL1OBXzmPK/TIrCpTi2ioTlZ3O8jmXylwwIUYBA4/Cmzr9pRVGA6OroSOhB/wyPxr5+86QdJH/wC+jR50v/PR/wDvo118hzXPcNDtpNC8a3w06OMafLEhmjkY7o85IK/Q9vQ1xmt6/f6L4juZbZ22mdzsfO11LE/5NcF50uc+Y+f9401mZjlmJPuaORbMfM9z1631uy8U6bLChCXJX54pOo/xHuK5FYF0nWc3qSxCLLwnb1btz0x71x4YqcgkH1FK0jt95mP1NTCm4N2ehU58y1Wp0OoiK8vGuoLrd5w3v5rchz1HuPSiucorQzPfvGN7ZT+ExeW8wX7QpCqrcMSOp+nIxWx4NvIrLTbGOd1Tybddm7owZQSM9uQD+dea2MX9r6LLpO4xvC3nLITkBTwRj15zXo/hq4g1Dw5ZTSWsIlWPy3IjByU+XP44rhm5UdY7pnT7tRWex01xeaZcRMk1rCVPzj/SBj6/d4rmdY1axtCyxRW6hVKjfIzf0+lZut6+2mLK40+B4EHzfPhiPptrzzWvEh1cuVg8pPTOa1jXqTWxn7GEepr3+txzSE+eiDOMIMVzOs3sU1nMEkydhH15FUPIKNkkGobiP/Q5XP8Ad4/OnbXVl6W0MWiiiuk5wooooAKKKKACiiigD//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image features a dog with its front paws on a table top, and the left image features a dog lying down with another dog figure next to it.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

