Question: Is the size of the picture large?

Reference Answer: no

Image path: ./sampled_GQA/n314171.jpg

Program:

```
ANSWER0=EVAL(expr="'yes' if {IMAGE.size[0]} > 500 and {IMAGE.size[1]} > 500 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if IMAGE.size[0] > 500 and IMAGE.size[1] > 500 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 434 > 500 and 640 > 500 else 'no'")=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

