Question: Is the motorcycle on the right part?

Reference Answer: No, the motorcycle is on the left of the image.

Image path: ./sampled_GQA/n9181.jpg

Program:

```
 Is A <planar pos>?
Program:
BOX0=LOC(image=IMAGE,object='motorcycle')
IMAGE0=CROP_RIGHT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the motorcycle on the right part?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

