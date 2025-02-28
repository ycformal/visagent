Question: Birds are gathered around their prey in the image on the right.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/7c/7c/3a/7c7c3a3a79c787e00e758a98238a75ff--exotic-animals-exotic-birds.jpg

Right image URL: http://fs5.directupload.net/images/170104/i2k995gz.jpg

Original program:

```
Statement: Birds are gathered around their prey in the image on the right.
Program:
ANSWER0=VQA(image=RIGHT,question='Are birds gathered around their prey?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Birds are gathered around their prey in the image on the right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Birds are gathered around their prey in the image on the right.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

