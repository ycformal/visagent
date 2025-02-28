Question: There is exactly three cups of hot chocolate.

Reference Answer: True

Left image URL: http://2.bp.blogspot.com/_Dwex9AQ8IuA/Sx-uOFsoYdI/AAAAAAAAP5U/E_mgqa1wJSw/s400/two-cups-of-cocoa-7.jpg

Right image URL: http://karainthekitchen.com/wp-content/uploads/2011/02/IMG_8247.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is exactly three cups of hot chocolate.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is exactly three cups of hot chocolate.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

