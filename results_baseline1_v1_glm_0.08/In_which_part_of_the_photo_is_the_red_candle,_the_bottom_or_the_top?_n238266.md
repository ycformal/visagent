Question: In which part of the photo is the red candle, the bottom or the top?

Reference Answer: top

Image path: ./sampled_GQA/n238266.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='candle')
IMAGE0=CROP_TOPOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='red candle')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'top' if {ANSWER0} > 0 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_TOPOF'

