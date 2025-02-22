Question: The image on the right shows some of the trees surrounding the yurt.

Reference Answer: True

Left image URL: http://downwindsports.com/icefest/wp-content/uploads/2016/10/Yurt-interior.jpg

Right image URL: https://content.govdelivery.com/attachments/MIDNR/2012/12/20/file_attachments/181666/Craig%2BLake%2BYurt%2BExterior.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show some of the trees surrounding the yurt?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Does the image show some of the trees surrounding the yurt?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the image show some of the trees surrounding the yurt?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

