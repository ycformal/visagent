Question: Is the person that is looking down young or old?

Reference Answer: The man is young.

Image path: ./sampled_GQA/n206358.jpg

Program:

```
 Is A <attr> or <attr>?
Program:
BOX0=LOC(image=IMAGE,object='person')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the person looking down?')
ANSWER1=VQA(image=IMAGE0,question='What is the age of the person?')
ANSWER2=EVAL(expr="'young' if {ANSWER1} < 30 else 'old'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: young

