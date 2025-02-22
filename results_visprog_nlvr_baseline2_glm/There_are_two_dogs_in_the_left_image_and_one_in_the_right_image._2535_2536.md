Question: There are two dogs in the left image and one in the right image.

Reference Answer: True

Left image URL: https://i.pinimg.com/236x/6e/ff/b7/6effb7856592d6cbca767a5a8c20a414--justine-vizsla.jpg

Right image URL: http://2.bp.blogspot.com/-jaLW0Oso050/TwUDvdyfOoI/AAAAAAAAD6w/dmgtygVs7kY/s1600/DSC_4569.JPG

Original program:

```
Statement: There are two dogs in the left image and one in the right image.
Program:
ANSWER0=VQA(image=LEFT,question='How many dogs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many dogs are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == 2 and {ANSWER1} == 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

