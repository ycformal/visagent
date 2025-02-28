Question: Is the microwave oven out on a kitchen counter?

Reference Answer: yes

Image path: ./sampled_GQA/64342.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='microwave oven')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='kitchen counter')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is the microwave oven out on a kitchen counter?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD17Z+7rzPxTcRQeKPKkPzSSfl8uMn8eK9TK/u/xrzvxDah9duyWPJHYHsKzrq8TWg7SOI1JcXVwPc1ysEbcYYAduK63U123VwMk4Y8n6VxEOqRjH7lz+IrCGhvM2EgY/8ALT/x3/69Ti3YIx39BnpVGLVUwD9nf/voVc/tNfKbFs3Kkff/APrVZOoCMsoO7GaXy2/vVPbr5kKFQeRmpvIPcfrUJSZXMkU/KP8Aep1up+04POKteWB1I/MUyJcXh+gp2fUOZHQaYP3uP9k1y/iq4EOvSL/0zQ/pXW6WuZgP9k1wXj0SJ4pbGceRH29jRGOopysir9tHrRWCZmBwc0Vpyoy5z7NK/JXBa7HnWrk+4/kK9Ax8tcNrUWNau2BJ3MDgngcCtKmqIp6M891VP9Nuf9415jAvI9K9W1ZP9Ouf9815ZZ6cdSu1iafy4wOQByevPp2xWEUbtt7GrBGcgEVprBmBiPQ1mW8JguGt1cyIjYVmOTit+GPFu5/2T/KriiJOwxZba30oG5njiDRgLvONx46U0WyNGroVZWGVYHgisu80iS6iW782RiYl2JsznHYYq/pCSW2nR2867JFyWQ9VyScVStsGq1B7YcDbUyqwvbUehXOP92pnYcGm5Avrf3KD/wAdpWHzHWaOv+kqP9k1xHxAQDxMf+uEf9a7rRh/piD/AGW/lXB/EglfFAH/AE7x/wBamKCb0OMmGJDRTJDl6K0Mj7X/AIa4zWl/4m1wfcfyFdn/AA1yOsj/AIms34fyqpbEx3PPtZXbd3R9GP8AKsCPTbGDwhpt7Hbqk8+5XcE5bk/4V0+sRGS9uYwVUnJyxwO3+NZ02iTy+DdO02O7txc27sWbecEZOccZ/iFTCLszXnSaOensY3EU1uoRycOv8/xpxkUSPAssQkHy7CG9Ox710UGkzLpzxMIGmb+Lcce56Zrm9V0Ca1lgmuZI3+0S4jZOfukA/jxSSd9rEuSb1Nmwto309IWbKqcB146Y6fjV9rC3ni8p0AYjCsOo/Gs/QrgSwyLJhfLc7uOO5zTdZvHnsBFYzsszsMsvy7ADnJPYcVq7WuxR5r2RlXgawuDbXJVZB0OeGHqKIw0up2+DwgR2+mzH9ar+JLqPVbWyizulh+drjPDY4IAHqeal06TffxtwQ0CkkHODgcVl6Gt0tGdxoo/0tP8AcavPPiZcKvjJYSDk20fP516Jon/H4n+4a8z+KSxt42Id2Qi1iKkDjvSiiZnKO+5sgY+tFQySqzkiQfiKKsyPt/8Ahrk9Z/5Ckv0H8q6sn5K5DXJANVlHsv8AKnLYI7nG6vFm5upuGRMB1GcgMVx/I0WN0LfzFhlWB23Ebn255XIBPSrF9oFlqNzNNPLcZmxvRJNqnHTgU7/hHbTBHn3JyAOX7DpThNJWCcLu5tLqEt0lvD9rSTauJvLOCWx147Zrzv4hp5EkHkocI5kPU845JrtbHTLfTZHkgaXLDad7luM57niuW+IFtH/Z015yZWhKe2AR/jROd1oEI66nFaHrd3ZurJ5TIy5KOvVvXI5qbUp7vVSkU0kUMJIBit49obnjJOSazdIsLm8iDW6hhFtZstjrnp69Kt3IZXEcwMeSAcnbx7GlzRa5b6lKMk720LqaF5sJTz5FBXb17ZJ7j3qxY6aunz7lmaTzeTn2yKx7exgN0Wa7SNIjgBpT8/HXr24ragYqYUaYS4B/eDo3zGs4Skm49DSaTs7anZ6Gw+0KNoztY7u546V5t8UIo38ZbmYg/Z4gT6DmvRdCP+kr/uGvM/ia7DxvJhuPs8II9eM04kyOdOl2/wDfYj1zjNFEl4pb7vb1oq3Jmaij7SP3DXEeIiRqzf7i/wAqKKJ7BDcyQx9amVjkc0UVmjVjnJxXKePj/wASBv8Arm38xRRTewlucp4UAGkysBySAT+Bqr4xYizscHqXP60UVyr+O/66HZ/y4X9dTkWkfDjdxtrr9FZjY2JJJPln/wBCNFFdcdmccviR3ehH/SV/3DXmvxNGfGUxP/PCL/0GiikhyOPUkKOTRRRVkH//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the microwave oven out on a kitchen counter?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

