Question: All of the cabinets have flat tops.

Reference Answer: True

Left image URL: https://a.1stdibscdn.com/archivesE/upload/1121189/f_52111531470126394320/5211153_z.jpg

Right image URL: https://i.ebayimg.com/thumbs/images/g/QVEAAOSwvg9XZ~iS/s-l225.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'All of the cabinets have flat tops.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the cabinets have flat tops.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

