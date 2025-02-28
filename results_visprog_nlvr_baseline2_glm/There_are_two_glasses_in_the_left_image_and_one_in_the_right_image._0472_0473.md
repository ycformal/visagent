Question: There are two glasses in the left image and one in the right image.

Reference Answer: True

Left image URL: https://images.vat19.com/covers/large/tipsy-wine-glasses-2.jpg

Right image URL: http://static.wixstatic.com/media/b5c609_a6886bb97d93a45a472fc4514433e891.jpg_256

Original program:

```
Statement: There are two glasses in the left image and one in the right image.
Program:
ANSWER0=VQA(image=LEFT,question='How many glasses are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many glasses are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == 2 and {ANSWER1} == 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two glasses in the left image and one in the right image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two glasses in the left image and one in the right image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

