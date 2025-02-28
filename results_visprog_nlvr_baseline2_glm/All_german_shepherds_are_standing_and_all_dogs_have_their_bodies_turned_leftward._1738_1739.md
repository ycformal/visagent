Question: All german shepherds are standing and all dogs have their bodies turned leftward.

Reference Answer: False

Left image URL: http://www.allbigdogbreeds.com/wp-content/gallery/belgian-malinois/Belgian-Malinois-2.jpg

Right image URL: https://woodsmanwannabe.files.wordpress.com/2015/02/bmalinios.jpg?w=676

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'All german shepherds are standing and all dogs have their bodies turned leftward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA+AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDj9d1K31nS2WSKSK4j/wBUXUBh69+mO1Jb3XlWMMMGAhiwseB8xPViPr/SudXw94iZgJ9F1J40I5+zuDz74rVhstcg09LqPRr62uQ5j2pbu2U2jBII+tQpLdshu63IJFAkAVxH6MDjn2rQhcW6He+cD77DOKxpLDW5t4l06/3E7vmhfnJ+lXBp+pSQ+XLZXpAHAMLDH6Vn7Z38jJyexsWF3byNIBxJtwp7E+mO1au+4vrsW0MZEkY5ToRwB3/GuYt9I1OaSP7PZXO5Rkb42AUds8YJrqo7DVYVZY7ORpHOWdwc4FZwxLgmqjM4zcdJsrm9gsbj7PJHIjDkjeMEZ5+nFUtVZbC2SF5gzfbHxuYHCjAGfTr39ayJrO5XxFfX96AkNrmAq/UsRkbQepB5P/16rWXhrVbuK4e0Y3MW4OXDYBZhk5z0bjkVs/djzyehvZJXb0Oj0+UXGu6bLHdFo1uUQxJwM7vXuB6969QdsJuaRAo5JPFeQ6DBcwa3pMU0DrscEhgcN8/LA457V6NrWoG3gdY7JpWxtjHXLnpgZ57/AI1z1feaaZpRSasi7/aen5P+mQcHB/eVzN74kkXxhFpFrdqyztCy7VyVAJ3rnvuH5YpV8LvLZRiSQJctzKoGQD6bs1JpXh0DxFJrE6rvii8hAOob+I5+nH41nFpXubyULe6zqfMz06fWiq7QqTw5PHoaKzuZjzqsqZCyLjpkZqM6pMcncGPqSagWzfgKGP0IqQaezn7hBPYNmvnOes9meLqP/tS6ZlRNxYnhUBYmrrz6nbx7pNxz0UNkmo/sf9mzoZZDHLJwUJ6/5xXLza3d/wBpP5RbyVPKHtXtYfApJe2k+b8j1KOAUoKUnub9xrlxAB5uU54L/L+pqe2uNWuZ8LHs+XeS7YwPWsyPU4rmyjafLq4GAeQPetGXW4tM1q4nLYhjdUZRj5l2jH45/nXRHLqTd+eVgeAinuzxvxxqc0/jK8gnjUIjkAEnDjPXHY9PyrovDes/2fpt0mmCOZrmZGYKC+07RkE4xuzziuM8eeIX17xLPdfZ4Lba/wAqwr93B657mvZPDVjFp3hiwg8rZIYhJIOuXbkk+/NdONr+yockluRjHFRtHqZX/CVmC1kmutOudsCFpJVhPyqBzjP/AOqsSX4m+HpGDH7buBB5gHGP+BV1PisRnwfrOCci0k4z7V85Vy5dCFSEmu5GEdos9mHxQ0ADk3xPfEC//FUkXxS0SJmAF4ULFiDAOp/4FXjVFeh9Xgddz2w/FnQRgCO76d4B/wDFUV4nRR9XgF2fS+o3Oo29sJNMtre5lz80ck2z5fbtn64rN/4SHxDNiO08PGByceddzqFT6YJz+Va6yg7cK2fbtT87uu4H618vSruktIq/fqeXTrcmyQ2YTjTLGa9uY7maIfvpFG0d/X0FcNoPiSXWPEdxo9nBBJbNuea6kUkqg4GOeuf50nxG8SPFp40azZi0rbpHTrjoF981t+CfCDeGNHY3DL/aFzh5sHhAOiA98dT7mvaqz9lQVSXxNHp1sTKFFLqY00Os6fqoguos28h/dzxnKAZ6E/w/jSfEjWv7PsHs4l23T4jaUfxAAciuu1+6az8PXcoY/dCjB5JYgf1rL0fSrLX0OrapZQ3DM5WFZV3BFXrge5z+VRQxjVP2k1psRDFN0nKe+x4ro9lca5rlrYJl5bqVUJ6nBPJ/LJr6WMbJGsSDEcaBV+boAABXmWh6dFb/ABb1VliWOOFpGjVF2gBkGMAdODXoEm8ru2Mq+/f3rnzOp7RxS7X+848TO7XoUfFyZ8HaweB/oknH4V84V9B+KWH/AAimrqFJ/wBEk5LZ7V8+V05Qv3cvU1wr91hRRRXrnUFFFFAH0xvXacv+BFJHOqtuLHAGDTdquFTB3ZJ3FqaYFc4Yt1wec+1fH8iZ4tzhWs7b+29Fa4y4OoSySFumFUFBn0ziu3l1S3zueZiepOahWys7d2KwJvc7jlcg0rRxySACFAuOABXViq0a0k+xrWq+0d0Y3jHUfN8OlLbMzPcIp+XAHU/0rb066srDTbW0+0/6mMK209Tjn9c1HLYWV4Ak0RZY/mxn1FNSygKkbM5ORnr+dKU4+xjTXdsl1PcUUZMc8P8AwsG6u0b91NbqS5P3mCgf0/Suha4jc5VyePulwcn2qidLsmlEpgHmAbQwJGOtWktY9oARAOcYFTWnGpyvskgnPnt6GX4mdD4W1YksCbV8c+1eC1714kUHwtquCQRayZGfavBa9TKVanL1OzB/Cwooor1TrCiiigD/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All german shepherds are standing and all dogs have their bodies turned leftward.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

