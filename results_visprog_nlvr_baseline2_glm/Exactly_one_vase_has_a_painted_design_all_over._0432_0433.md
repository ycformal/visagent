Question: Exactly one vase has a painted design all over.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/0a/2d/a2/0a2da211045de2666639ed0dfccaaf47--pear-shaped-bodies-rim.jpg

Right image URL: https://i.pinimg.com/236x/c4/33/1c/c4331cd367472c8a5734516d60c314e1--pear-shaped-seals.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Exactly one vase has a painted design all over.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Exactly one vase has a painted design all over.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

