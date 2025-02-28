Question: A single dog is lying down in the image on the left.

Reference Answer: True

Left image URL: http://www.warrenphotographic.co.uk/photography/bigs/20332-Tricolour-Cavalier-King-Charles-Spaniel-pup-white-background.jpg

Right image URL: https://www.warrenphotographic.co.uk/photography/bigs/37977-Tricolour-Cavalier-pup-white-background.jpg

Original program:

```
Statement: A single dog is lying down in the image on the left.
Program:
ANSWER0=VQA(image=LEFT,question='How many dogs are lying down?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A single dog is lying down in the image on the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A single dog is lying down in the image on the left.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

