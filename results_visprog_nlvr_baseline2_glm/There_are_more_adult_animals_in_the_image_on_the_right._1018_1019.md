Question: There are more adult animals in the image on the right.

Reference Answer: True

Left image URL: http://3.bp.blogspot.com/-fsUFCHffd30/T3JSmmycQvI/AAAAAAAAH4g/tqPztdNPx34/s640/eye.jpg

Right image URL: http://3.bp.blogspot.com/-JtNcnB4FtFw/Ug4IelpD4yI/AAAAAAAAALc/OHiK5RzOi8Y/s1600/olive+baboons.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are more adult animals in the image on the right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are more adult animals in the image on the right.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

