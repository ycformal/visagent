Question: Are both the person to the right of the other people and the skateboarder that is not male standing?

Reference Answer: yes

Image path: ./sampled_GQA/n489190.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='people')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='skateboarder')
ANSWER0=VQA(image=IMAGE,question='Is the skateboarder male?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'no' and {ANSWER1} =='standing' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'ANSWER1'

