Question: There is a smartphone in the right image.

Reference Answer: True

Left image URL: http://nerdtechy.com/wp-content/uploads/2016/03/ASUS-MB-MB169B-USB-monitor-1.jpg

Right image URL: https://static1.squarespace.com/static/54791cf3e4b01fb132fd0e4f/t/55d51a93e4b0f5881c80faa9/1440029336261/Dashboard-Text+Alert+-+Placeit+-+iPhone-Laptop.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Is there a smartphone in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Is there a smartphone in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a smartphone in the image?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

