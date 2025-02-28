Question: A solid-color yurt with contrasting roof and one visible door is sitting in a snowy landscape with trees in the background.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/3b/c9/ed/3bc9ed7c2338a4a861e77b525638d831--luxury-yurt-luxury-camping.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/02/68/c7/1c/the-yurt.jpg

Original program:

```
Statement: A solid-color yurt with contrasting roof and one visible door is sitting in a snowy landscape with trees in the background.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A solid-color yurt with contrasting roof and one visible door is sitting in a snowy landscape with trees in the background.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A solid-color yurt with contrasting roof and one visible door is sitting in a snowy landscape with trees in the background.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

