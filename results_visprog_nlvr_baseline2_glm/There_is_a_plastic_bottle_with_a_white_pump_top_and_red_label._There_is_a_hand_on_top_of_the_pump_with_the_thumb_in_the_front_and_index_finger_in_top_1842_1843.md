Question: There is a plastic bottle with a white pump top and red label. There is a hand on top of the pump with the thumb in the front and index finger in top

Reference Answer: False

Left image URL: http://farm3.static.flickr.com/2127/2519983644_6b72295ce1.jpg

Right image URL: https://i.pinimg.com/736x/37/37/2e/37372ea5de30e8b24c03aba49f100673--coca-cola-light-coca-cola-bottles.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a plastic bottle with a white pump top and red label. There is a hand on top of the pump with the thumb in the front and index finger in top' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a plastic bottle with a white pump top and red label. There is a hand on top of the pump with the thumb in the front and index finger in top' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

