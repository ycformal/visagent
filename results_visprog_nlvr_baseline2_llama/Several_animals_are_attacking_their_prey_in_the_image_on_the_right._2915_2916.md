Question: Several animals are attacking their prey in the image on the right.

Reference Answer: True

Left image URL: https://1.bp.blogspot.com/--hPm7XT98nk/WOU6X3pMrwI/AAAAAAAAhVg/V9UU83VID74VX2LOZepJIykGpYyuO_rwACLcB/s1600/Last_Tan_Blog_0002.JPG

Right image URL: https://3.bp.blogspot.com/-usXU5DCr4-k/VvOvnUl-SiI/AAAAAAAAFrs/V76PQz_4OiY7djFbK0EIJY4wPPQljswhQ/s1600/HYENA%2BMIMAZ.jpg

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are several animals attacking their prey?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are several animals attacking their prey?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are several animals attacking their prey?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

