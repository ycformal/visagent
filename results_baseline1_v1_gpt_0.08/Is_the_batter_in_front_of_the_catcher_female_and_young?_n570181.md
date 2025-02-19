Question: Is the batter in front of the catcher female and young?

Reference Answer: no

Image path: ./sampled_GQA/n570181.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='batter')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='catcher')
IMAGE1=CROP_FRONT(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='Is the batter female?')
ANSWER1=VQA(image=IMAGE0,question='Is the batter young?')
ANSWER2=VQA(image=IMAGE1,question='Is the catcher female?')
ANSWER3=VQA(image=IMAGE1,question='Is the catcher young?')
ANSWER4=EVAL(expr="'yes' if {ANSWER0} == 'yes' and {ANSWER1} == 'yes' and {ANSWER2} == 'yes' and {ANSWER3} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER4)
```
Answer: Runtime error: 'CROP_FRONT'

