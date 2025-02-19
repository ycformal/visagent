Question: What are the trees behind of, pigs or cows?

Reference Answer: cows

Image path: ./sampled_GQA/n164272.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='pigs')
IMAGE0=CROP_BEHIND(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='cows')
IMAGE1=CROP_BEHIND(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What are the trees behind of?')
ANSWER1=VQA(image=IMAGE1,question='What are the trees behind of?')
ANSWER2=EVAL(expr="'pigs' if {ANSWER0} > 0 else 'cows'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: Runtime error: '>' not supported between instances of 'str' and 'int'

