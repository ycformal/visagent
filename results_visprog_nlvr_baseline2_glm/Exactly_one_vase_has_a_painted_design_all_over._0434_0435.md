Question: Exactly one vase has a painted design all over.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/13/3f/b1/133fb1f33c19ce8ea654e6999fd415c3.jpg

Right image URL: https://i.pinimg.com/736x/f8/52/13/f8521362a9583b0995660d9f59f792b7--chinese-ceramics-qing-dynasty.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Exactly one vase has a painted design all over.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Exactly one vase has a painted design all over.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

