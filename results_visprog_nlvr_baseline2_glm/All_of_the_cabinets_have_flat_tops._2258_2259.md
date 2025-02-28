Question: All of the cabinets have flat tops.

Reference Answer: False

Left image URL: https://slimages.macysassets.com/is/image/MCY/products/3/optimized/1950366_fpx.tif

Right image URL: https://chairish-prod.global.ssl.fastly.net/image/product/sized/faf5e3d8-a494-487d-af85-465b943f3cbd/ethan-allen-maple-china-cabinet-1637?aspect=fit&width=320&height=320

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'All of the cabinets have flat tops.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All of the cabinets have flat tops.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

