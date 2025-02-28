Question: A spoon is shown with a cola bottle in one of the images.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/13/ec/95/13ec95dc935e9b6ae82a5032bcf85c7f--spoon-rest-bottle-crafts.jpg

Right image URL: https://img0.etsystatic.com/165/0/5460547/il_340x270.1093974608_flil.jpg

Original program:

```
Statement: A spoon is shown with a cola bottle in one of the images.
Program:
ANSWER0=VQA(image=LEFT,question='Is a spoon shown with a cola bottle in the image?')
ANSWER1=VQA(image=RIGHT,question='Is a spoon shown with a cola bottle in the image?')
ANSWER2=EVAL(expr='{ANSWER0} xor {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A spoon is shown with a cola bottle in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A spoon is shown with a cola bottle in one of the images.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

