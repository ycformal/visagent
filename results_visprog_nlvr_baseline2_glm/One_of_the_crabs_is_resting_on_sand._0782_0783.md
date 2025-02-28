Question: One of the crabs is resting on sand.

Reference Answer: True

Left image URL: http://kenjonesfishing.com/wp-content/uploads/2012/01/Red.top_.Rock_.bottom.crab_2003.transbaby.jpg

Right image URL: https://i1.wp.com/calphotos.berkeley.edu/imgs/512x768/0000_0000/0505/2034.jpeg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One of the crabs is resting on sand.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the crabs is resting on sand.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

