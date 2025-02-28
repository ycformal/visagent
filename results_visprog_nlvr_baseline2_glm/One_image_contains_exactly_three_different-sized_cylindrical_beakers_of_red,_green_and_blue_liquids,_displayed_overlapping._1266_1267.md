Question: One image contains exactly three different-sized cylindrical beakers of red, green and blue liquids, displayed overlapping.

Reference Answer: True

Left image URL: https://cdn7.bigcommerce.com/s-ufhcuzfxw9/images/stencil/500x659/products/13948/16114/ce-bei0600__22276.1503517946.jpg?c=2

Right image URL: https://cdn7.bigcommerce.com/s-ufhcuzfxw9/images/stencil/500x659/products/13948/16026/WO-BEAKHST__70023.1503517944.jpg?c=2&imbypass=on

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image contains exactly three different-sized cylindrical beakers of red, green and blue liquids, displayed overlapping.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image contains exactly three different-sized cylindrical beakers of red, green and blue liquids, displayed overlapping.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

