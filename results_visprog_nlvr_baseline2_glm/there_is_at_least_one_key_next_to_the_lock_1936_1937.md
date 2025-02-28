Question: there is at least one key next to the lock

Reference Answer: True

Left image URL: http://cdn.small.masterlock.com/product/orig/MLCOM_PRODUCT_37646_141D.jpg

Right image URL: http://cdn.small.masterlock.com/product/orig/MLCOM_PRODUCT_105.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'there is at least one key next to the lock' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'there is at least one key next to the lock' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

