Question: There is at least one paper towel holder that is visible without a roll of paper towels on it.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/b1/67/64/b167642b29888ab32d637deea722886c.jpg

Right image URL: https://www.antiquefarmhouse.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/m/o/mouse-paper-towel-holder.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is at least one paper towel holder that is visible without a roll of paper towels on it.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is at least one paper towel holder that is visible without a roll of paper towels on it.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

