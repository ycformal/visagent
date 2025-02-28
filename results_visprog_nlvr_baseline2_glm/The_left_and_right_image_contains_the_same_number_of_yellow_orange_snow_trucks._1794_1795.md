Question: The left and right image contains the same number of yellow orange snow trucks.

Reference Answer: False

Left image URL: https://www.goodnewsnetwork.org/wp-content/uploads/2016/01/Snow-Plow-Wheelchair-screenshot-WOWT.jpg

Right image URL: https://i.ytimg.com/vi/_Rsq55kodRo/maxresdefault.jpg

Original program:

```
Statement: The left and right image contains the same number of yellow orange snow trucks.
Program:
ANSWER0=VQA(image=LEFT,question='How many yellow orange snow trucks are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many yellow orange snow trucks are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of yellow orange snow trucks.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of yellow orange snow trucks.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

