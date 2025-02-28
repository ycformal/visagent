Question: In one image, a row of three green plants sits on a rectangular table, which has light-brown armchairs at its ends.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/13/58/20/1358208bae4217dc459781b0ce934bda--open-kitchens-white-kitchens.jpg

Right image URL: https://i.pinimg.com/736x/c3/37/1e/c3371e1ddd9261c3f000e089fa2f65fb--open-concept-kitchen-concept-kitchens.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In one image, a row of three green plants sits on a rectangular table, which has light-brown armchairs at its ends.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In one image, a row of three green plants sits on a rectangular table, which has light-brown armchairs at its ends.' true or false?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

