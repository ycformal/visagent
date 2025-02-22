Question: A dog has its mouth open and showing its tongue in the rightmost image.

Reference Answer: False

Left image URL: http://www.domestic-executive.com/wordpress/wp-content/uploads/2013/04/Bassets-kitchen-garden2013-04-04-DSC_02274.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/5e/ac/c4/5eacc4ee37d10cac359f76dce14ecb57.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog showing its tongue?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the dog showing its tongue?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the dog showing its tongue?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

