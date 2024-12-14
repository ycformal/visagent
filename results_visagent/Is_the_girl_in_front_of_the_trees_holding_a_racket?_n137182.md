Question: Is the girl in front of the trees holding a racket?

Reference Answer: No, the girl is holding a surfboard.

Image path: ./sampled_GQA/n137182.jpg

Program:

```
 Is A <spatial pos> B <attr>?
Program:
BOX0=LOC(image=IMAGE,object='trees')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='girl')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Is the girl holding a racket?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: No

