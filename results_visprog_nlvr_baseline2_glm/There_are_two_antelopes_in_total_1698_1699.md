Question: There are two antelopes in total

Reference Answer: True

Left image URL: https://dewetswild.files.wordpress.com/2016/06/red-hartebeest-7.jpg?w=378&h=558

Right image URL: http://www.africahunting.com/hunting-pictures-videos/watermark.php?file=7118&size=1

Original program:

```
Statement: There are two antelopes in total
Program:
ANSWER0=VQA(image=LEFT,question='How many antelopes are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many antelopes are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 2')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two antelopes in total' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two antelopes in total' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

