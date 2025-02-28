Question: The left image contains a human wearing a heavy jacket.

Reference Answer: True

Left image URL: https://cdnd.lystit.com/photos/bloomingdales/1745841-Monarch%20Orange-1c8ca99b-.jpeg

Right image URL: https://cdnb.lystit.com/photos/2013/10/22/canada-goose-yellow-and-orange-kensington-parka-product-1-14347801-836179825.jpeg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left image contains a human wearing a heavy jacket.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image contains a human wearing a heavy jacket.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

