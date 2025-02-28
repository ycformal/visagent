Question: Each image includes an adult schnauzer with light beard standing on grass with its body turned rightward.

Reference Answer: False

Left image URL: http://www.zwerg-schnauzer.info/showphoto.php?id=1672&n=0

Right image URL: https://st2.depositphotos.com/2543399/7873/i/950/depositphotos_78732034-stock-photo-two-black-and-silver-miniature.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image includes an adult schnauzer with light beard standing on grass with its body turned rightward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image includes an adult schnauzer with light beard standing on grass with its body turned rightward.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

