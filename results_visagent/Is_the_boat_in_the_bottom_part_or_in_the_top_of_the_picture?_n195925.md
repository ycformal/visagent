Question: Is the boat in the bottom part or in the top of the picture?

Reference Answer: The boat is in the bottom of the image.

Image path: ./sampled_GQA/n195925.jpg

Program:

```
 Is A <planar pos> or <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='all')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='boat')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'top' if {ANSWER0} > 0 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='all')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>IMAGE0</span></b>=<b><span style='color: red;'>CROP_ABOVE</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>BOX1</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDQMPJpRDV7yuelKIRX13OfHumUvJpfJq95XtS+V7Uc4vZlDyqDDV/yaPKo5xezM/yqTyav+TSGL2o5xezM8w0ww1pGL2ppip84eyM1oaYYa0jFTDFR7QPZGd5OKKv+V7UUc5XsjW8unCOpmKJ94gVS1S7ltLB7iIIm1kG6UZHLAZwPrXA6tlc9CNFykorqWPLpfLqLTbo3WnWs82A8sKuSBgEkA1e2ChVbkulZ2K3l0eXReXtpp8XmXc6Qr23Hk/QdTWFL400xd3lRTygck7Qo/Wk66W7HHDylsjcMdNMdc0nxF0Qh/MW5jZRwNgYN9CD/ADq3p/jTRdRk8sXBt2zgCcbQ345xT9siXQl2Nkx0wx1a6gEcg00iq9oL2Zh3kWrR3EDWnkT24b97HIdkjDHZunXnpVtAXXLRPGe6tj+lXmAAyenrVC51KwtTie7hQ+m7J/IUlO3UrkctLDvL9qKzj4l0kk7boEDuFNFHt49y/q8+xvJ/x/yfSq2u/wDIIP8A12h/9GpRRXK9mbx+NCaP/wAi3pv/AF7x/wAhWmv+oH+7RRTWxM92eS63/wAhA/Ss+b7poorml8R6MPgMF/vt9adH91/92iit+hxLc9m8If8AIqWP+5/Wto0UVotjF7nI+Nf9VB+NcGfutRRWNTc7KPwkB6L9KKKKks//2Q==">, <b><span style='color: darkorange;'>object</span></b>='boat')=<img style="vertical-align:middle" src="data:image/jpeg;base64,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"></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDQMPJpRDV7yuelKIRX13OfHumUvJpfJq95XtS+V7Uc4vZlDyqDDV/yaPKo5xezM/yqTyav+TSGL2o5xezM8w0ww1pGL2ppip84eyM1oaYYa0jFTDFR7QPZGd5OKKv+V7UUc5XsjW8unCOpmKJ94gVS1S7ltLB7iIIm1kG6UZHLAZwPrXA6tlc9CNFykorqWPLpfLqLTbo3WnWs82A8sKuSBgEkA1e2ChVbkulZ2K3l0eXReXtpp8XmXc6Qr23Hk/QdTWFL400xd3lRTygck7Qo/Wk66W7HHDylsjcMdNMdc0nxF0Qh/MW5jZRwNgYN9CD/ADq3p/jTRdRk8sXBt2zgCcbQ345xT9siXQl2Nkx0wx1a6gEcg00iq9oL2Zh3kWrR3EDWnkT24b97HIdkjDHZunXnpVtAXXLRPGe6tj+lXmAAyenrVC51KwtTie7hQ+m7J/IUlO3UrkctLDvL9qKzj4l0kk7boEDuFNFHt49y/q8+xvJ/x/yfSq2u/wDIIP8A12h/9GpRRXK9mbx+NCaP/wAi3pv/AF7x/wAhWmv+oH+7RRTWxM92eS63/wAhA/Ss+b7poorml8R6MPgMF/vt9adH91/92iit+hxLc9m8If8AIqWP+5/Wto0UVotjF7nI+Nf9VB+NcGfutRRWNTc7KPwkB6L9KKKKks//2Q==">)=<b><span style='color: green;'>0</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'top' if ANSWER0 > 0 else 'bottom'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'top' if 0 > 0 else 'bottom'")=<b><span style='color: green;'>bottom</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>bottom</span></b></div><hr>

Answer: bottom
