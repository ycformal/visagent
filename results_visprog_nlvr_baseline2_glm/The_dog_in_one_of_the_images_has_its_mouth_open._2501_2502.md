Question: The dog in one of the images has its mouth open.

Reference Answer: False

Left image URL: https://dogbreedinfo.com/images/afghanmilky.jpg

Right image URL: http://www.doggies.com/imageuploads/1243277652_afghan4.jpg

Original program:

```
Statement: The dog in one of the images has its mouth open.
Program:
ANSWER0=VQA(image=LEFT,question='Is the dog in the image opening its mouth?')
ANSWER1=VQA(image=RIGHT,question='Is the dog in the image opening its mouth?')
ANSWER2=EVAL(expr='{ANSWER0} xor {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The dog in one of the images has its mouth open.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The dog in one of the images has its mouth open.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

