Question: Does the appliance underneath the counter top look old or new?

Reference Answer: new

Image path: ./sampled_GQA/n35676.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='counter top')
IMAGE0=CROP_UNDER(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='appliance')
ANSWER0=VQA(image=IMAGE0,question='Does the appliance look old or new?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_UNDER'

