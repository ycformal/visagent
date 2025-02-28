Question: There are seven or less water bottles total.

Reference Answer: False

Left image URL: https://waterbottles.com/media/catalog/product/cache/1/image/512x/81def17d0db1ecd775be2286b34b6b68/2/4/24-oz-contigo-chug-water-bottles_group.jpg

Right image URL: http://clipart-library.com/images/di9rxknAT.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are seven or less water bottles total.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are seven or less water bottles total.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

