Question: The lefthand image shows that the phone comes in at least three different colors.

Reference Answer: True

Left image URL: https://ae01.alicdn.com/kf/HTB1D7PWOpXXXXayaXXXq6xXFXXXw/Samsung-Galaxy-On7-2016-G6100-Cell-Phone-3300mAh-3G-RAM-32G-ROM-Octa-Core-5-5.jpg_640x640.jpg

Right image URL: http://www.pngall.com/wp-content/uploads/2016/06/Samsung-Mobile-Phone.png

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many different colors does the phone come in?')
ANSWER1=EVAL(expr='{ANSWER0} >= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many different colors does the phone come in?')
ANSWER1=EVAL(expr='{ANSWER0} >= 3')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many different colors does the phone come in?')=<b><span style='color: green;'>5</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 >= 3")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="5 >= 3")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

