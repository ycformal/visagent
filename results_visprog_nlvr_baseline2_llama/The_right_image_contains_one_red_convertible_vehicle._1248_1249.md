Question: The right image contains one red convertible vehicle.

Reference Answer: False

Left image URL: https://static.cargurus.com/images/site/2009/09/11/21/54/buick_reatta-pic-3299734822194454596-1600x1200.jpeg

Right image URL: http://st.motortrend.com/uploads/sites/5/2006/08/c12_0606_01l-future_classic-buick_reatta.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is there a red convertible vehicle in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is there a red convertible vehicle in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a red convertible vehicle in the image?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

