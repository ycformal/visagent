Question: There are children standing by a door.

Reference Answer: True

Left image URL: http://1.bp.blogspot.com/_afl4_CngAHU/TNYY4mWfcgI/AAAAAAAAAew/zSEGRsMNWzs/s1600/IMG_0129.JPG

Right image URL: http://2.bp.blogspot.com/_qxLIzrfZzxY/TKaWL6H-HNI/AAAAAAAAF-M/VbkX-X6tanY/s1600/DSC_0074.JPG

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are children standing by a door.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are children standing by a door.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

