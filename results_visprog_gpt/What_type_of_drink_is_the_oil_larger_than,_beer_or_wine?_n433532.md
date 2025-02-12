Question: What type of drink is the oil larger than, beer or wine?

Reference Answer: wine

Image path: ./sampled_GQA/n433532.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='oil')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='beer')
IMAGE1=CROP(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE,object='wine')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=SIZE(image=IMAGE0)
ANSWER1=SIZE(image=IMAGE1)
ANSWER2=SIZE(image=IMAGE2)
ANSWER3=EVAL(expr="'beer' if {ANSWER0} > {ANSWER1} else 'wine'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: Runtime error: 'SIZE'

