Question: Where is the traffic light?

Reference Answer: ahead

Image path: ./sampled_GQA/557127.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='traffic light')
ANSWER0=EVAL(expr="'top' if {BOX0.y} < IMAGE.height/2 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'list' object has no attribute 'y'

