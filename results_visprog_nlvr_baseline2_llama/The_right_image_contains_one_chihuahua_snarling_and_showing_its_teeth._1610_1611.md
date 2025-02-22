Question: The right image contains one chihuahua snarling and showing its teeth.

Reference Answer: True

Left image URL: http://ww4.hdnux.com/photos/43/07/23/9204939/3/920x920.jpg

Right image URL: https://quillerink.files.wordpress.com/2014/07/angrydog.jpg?w=800

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is there a chihuahua snarling and showing its teeth?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is there a chihuahua snarling and showing its teeth?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a chihuahua snarling and showing its teeth?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

