Question: What type of device is not silver, the monitor or the keyboard?

Reference Answer: keyboard

Image path: ./sampled_GQA/n435808.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='monitor')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the monitor?')
BOX1=LOC(image=IMAGE,object='keyboard')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER1=VQA(image=IMAGE1,question='What color is the keyboard?')
ANSWER2=EVAL(expr="'monitor' if {ANSWER0} =='silver' else 'keyboard'")
ANSWER3=EVAL(expr="'{ANSWER2}' if {ANSWER1} =='silver' else '{ANSWER2}'")
FINAL_RESULT=RESULT(var=ANSWER3)
```
Answer: keyboard

