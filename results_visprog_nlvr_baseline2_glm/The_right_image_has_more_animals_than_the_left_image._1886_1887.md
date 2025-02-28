Question: The right image has more animals than the left image.

Reference Answer: True

Left image URL: https://www.nps.gov/common/uploads/stories/images/nri/20151203/articles/28BA1972-1DD8-B71B-0B4CF38B48048194/28BA1972-1DD8-B71B-0B4CF38B48048194.jpg

Right image URL: https://howlingforjustice.files.wordpress.com/2012/10/wolf-family1.jpg?w=470

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image has more animals than the left image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAuAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDz6yVruR4ZCj4bADYGAD2rRhh2q/zqNvQbhgD1x1NQwQQQxzzbQf33lq4Ocjvn8q0EsUvIgItzOXIDEgBsjj/JrOaV1ckoyz7cRFjxnI3cfhVYyrs6kgn8q9Cs/Ddhc+HpLC4BtpcicPMuWDdMn0HHQdjnmuan8I6pA5zZ+ah6SRyKQfTv0pqy0Hy2ObIPlbDncByfXNMUPG/PLYPyk4wa6KXw7q6WzN9gl8pMlioDbR74NY7xh3Y7QrdM+tJsDHuL1vtu18bmzu7kc11mgW2lywwXF7Gk779nl4I4OeSenFc3PZRGbzmDI3TgZFdvpOnXM+lmCyg2+XIJdzcDYTjOe/SsajXLoa0o6l2S10CMC3GlwYY9g3H1Oc9ap67YJa6VcmKPbFb27BUJyoLMMKuckDkt7nmuhsbPZc289wIFeI5jKrt3cfdcZOSDzkU/xfpUthpMhkkN35kQSb5VXB6lgAMZ9BXKpa6M6XFW2PHrlCdiwxL0+8R1+vvUC2U00e+IkkfeVTk/iK6X+yJEnEXnC4iJBikQ8YI4P4AjNSavo/2e8RrM+SJAyk55bsSPTOM/jXQqyWhyulKKu0cqIJ5izC3kODjIWitQWwiyPtj8nJwmf60Vr7RGehpW0qtcyGX5o3fgjgNjpx09P1rXgtvNjYbVXIwVU+vp+dYNtmCSZJkwyyAMOoFdTplvsh84yQyRPhsNgAHvntU1ZKNrgOtLG6gtmuJFdYyn7obshj689v8ACkOqX6TkwRyslsv7xgMqB6k0x5rrVLrfM3ThQnCgf7varlo6aXZ3VnOgxdQOvmL1BGccUlVjflGmMsfEEsGopMZCsb/LIe3+ear+KIIb24a8thHvIG5R19N3vnilihtpFNvb2zefMg5ncbcHByBj+dWZrGOHT1juVheO3CuVClz2OVbjHWlKtFe6Pfc42xjtL64eCe4WFopSojc43HqP1rtNN1qXRtsd/ZNEFyomiyykdQuPT6157eWvn6neTs4DyTvIpPTGcjFdFoF/cOVgMcsiZAxvJxU1Y+7c6KWhd1+TVb5lj0WZ1ilkDpKhxt4IKn8/xrc8UapeQaJb+bl5mKiRyO4AH6kVNYQrpzCZgkZIGY9mBjvj/wDXWb431yFrFIkBY54GOBnOK5IzcpKFtDdxUVzIqWLJMkCvDDtVN8TGYAM3PBHYZqp4pjlj1uLDKBHEDiLO0OR93Nc/p2k3OryQiN22K43EdM56112r2r2Gm2twC5uIXKu3GWyD1z9P1rRxjCWj1MqspShqciLqWPKhUTnOCAT/ACoq39supgGuLuHPRd9urHb2ycGitbrqvz/yOPQ4uXxNq00hke5BY9xEo/pTv+Er1vy/LF8wT+6EUD+VY1FdvJHsM3U8Y69EAI9QZQPSNf8AChvGWvu25tQYn1Ma/wCFYVFHJHsB0B8b+IWKk6gSVOQfKTP54p8vjzxJNGUk1IspBGPKTv17VzlFL2UOyA9Xt7e21rw5b3e4fa0iQyDAHzYGTgda0NKjXSdS8tiWjPyjJGQeorzqxv7qKGFIZWQ7VUEfhWpYyXt+ZmF26tbgyHJJyR6VjKlJ6XOmEk3ZLU9Y1yO8vtOiNn5Uk0TA+WWAEiEcjPqDgiuJu7eY3MVxrtlJHZxvyiZzjucj0+tc9BrGp2cEKW99OiuCcbs+vtW9pvxA1NZ4bW5RJUkba0ifI+Pw4zXP7GcNtfzNPaRZ11n4VtIx52i6iWt7hSI4w4LBvUE/e+nWqupaZbaXoaxazeSyhnJjkR9hyB05zz9alurKKwitNRspJbe5mDFyhGxyOQ5XoGx1I49qyp/EEuqabcafqC/aHuN4EjKOCM4PHpjgiudO8r39ROpG1miyPD9jcIk+n6nYm2kUMvnqd+e+dpweaKq22jW9naQxrNIAUDY2hvr1P40Vty9pGHuPW34n/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image has more animals than the left image.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

