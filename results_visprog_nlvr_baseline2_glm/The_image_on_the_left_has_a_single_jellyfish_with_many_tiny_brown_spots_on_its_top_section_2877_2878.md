Question: The image on the left has a single jellyfish with many tiny brown spots on its top section

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/16/93/47/169347424a6a70d00268ac1692c4bc88--jellyfish-tattoo-deep-sea.jpg

Right image URL: http://calphotos.berkeley.edu/imgs/512x768/0000_0000/0305/0687.jpeg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The image on the left has a single jellyfish with many tiny brown spots on its top section' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The image on the left has a single jellyfish with many tiny brown spots on its top section' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

