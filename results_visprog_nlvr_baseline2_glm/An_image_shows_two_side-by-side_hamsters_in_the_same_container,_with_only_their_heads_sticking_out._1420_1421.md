Question: An image shows two side-by-side hamsters in the same container, with only their heads sticking out.

Reference Answer: True

Left image URL: http://fscomps.fotosearch.com/compc/UNR/UNR216/u19836436.jpg

Right image URL: http://fscomps.fotosearch.com/compc/UNR/UNR216/u25536637.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows two side-by-side hamsters in the same container, with only their heads sticking out.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows two side-by-side hamsters in the same container, with only their heads sticking out.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

