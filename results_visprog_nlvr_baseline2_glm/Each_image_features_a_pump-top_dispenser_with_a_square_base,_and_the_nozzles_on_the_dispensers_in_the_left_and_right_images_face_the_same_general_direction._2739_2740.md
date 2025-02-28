Question: Each image features a pump-top dispenser with a square base, and the nozzles on the dispensers in the left and right images face the same general direction.

Reference Answer: False

Left image URL: http://cdn8.bigcommerce.com/s-i17pk3h6/products/229/images/1410/glass_foam_soap_dispenser_large_chrome-metal-pump_clear_rail19_8882__84389.1481344444.800.800.jpg?c=2

Right image URL: https://www.thebathoutlet.com/static/330/images/nameeks/NNBL0048.jpg

Original program:

```
The provided program does not include a statement for this question.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image features a pump-top dispenser with a square base, and the nozzles on the dispensers in the left and right images face the same general direction.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image features a pump-top dispenser with a square base, and the nozzles on the dispensers in the left and right images face the same general direction.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

