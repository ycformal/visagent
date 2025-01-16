Question: Is the white bottle near the label round and large?

Reference Answer: No, the bottle is round but small.

Image path: ./sampled_GQA/n470131.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='label')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='white bottle')
IMAGE1=CROP_NEAR(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='Is the bottle round?')
ANSWER1=VQA(image=IMAGE1,question='Is the bottle large?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'yes' and {ANSWER1} == 'yes' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: no

