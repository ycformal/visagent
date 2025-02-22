Question: There are exactly four bottles, one in one image and three in the other.

Reference Answer: False

Left image URL: https://ssli.ebayimg.com/images/g/wX8AAOSw42JWEWBs/s-l640.jpg

Right image URL: https://sc02.alicdn.com/kf/HTB1Syt_mdbJ8KJjy1zjq6yqapXad/Aluminum-Alu-Metal-Magic-Sport-Water-Bottle.jpg_640x640xz.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many bottles are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many bottles are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 4')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: can only concatenate str (not "int") to str

