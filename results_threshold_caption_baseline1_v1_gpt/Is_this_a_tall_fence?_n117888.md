Question: Is this a tall fence?

Reference Answer: yes

Image path: ./sampled_GQA/n117888.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='fence')
ANSWER0=VQA(image=IMAGE,question='How tall is the fence?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 10 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

