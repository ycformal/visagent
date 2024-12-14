Question: Is this a tall fence?

Reference Answer: Yes, this is a tall fence.

Image path: ./sampled_GQA/n117888.jpg

Program:

```
 Is this A <attr>?
Program:
BOX0=LOC(image=IMAGE,object='fence')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What is the height of the fence?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 6 feet else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Yes

