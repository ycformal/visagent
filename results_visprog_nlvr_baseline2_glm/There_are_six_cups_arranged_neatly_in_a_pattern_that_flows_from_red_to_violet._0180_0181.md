Question: There are six cups arranged neatly in a pattern that flows from red to violet.

Reference Answer: False

Left image URL: https://officedepot.scene7.com/is/image/officedepot/508527_p_1_102617?$OD%2DLarge$&wid=450&hei=450

Right image URL: http://img1.tebyan.net/Big/1390/11/13813822242282461416714717910019183227103198.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAApAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iub1zxHdaVem3is43Xyw4dpDzn2x/Wsq3+IcYvBDdWbhNm5mjGcH8Tj9a5li6TqeyT970Z2wy/EVIc8Y3XqjuaK42/+IFilluskZrpvuJMvy9eclScVzur+OdXudLuYY41tpGA2zQsQyc/WtJ1oQkoydrnDiebDO1WLTPVKK8G0PxH4ivfENhZDW7wxzXaK258krnkc+2a93LgV24jDyoNJvc58Nio4iLcVsOopu8Um8dq5zpH0hIqJplB5YVnXOqmOZ440U7O7HrXJXxtCgrzl/mKT5Vdlu/vo7G0knk5CDO3OCayR4miADPF8h7q2a47Ub57ma6SdWXdIwDk5z9M1U0OFbrxDbWKbmjixJIx9Bz/gK9/BYahXw3t07rftt/wTwY5nVq4n2MY2t/XY9YzRSqNwzRXmHu2OR8bJtuLWX+9Gy/kc/wBa4VwrbwcEYIr1jXNDj1uCKN5mhaNiQyqD1GMVwXiPw2nhy1glE8twJWYOSmAvHHT8a8uOFnHGut9n/gH0+V4ql7ONFv3jntKtFur8RKowsUrnA9EJ/pS3ELSQuiAvI+AqjqT2FbPgGNNQ8QsRE3kxwPubBxz8uM/ia6y2+HulWupR3gub1/LdXWN5AVyDkZ4zXTiqEqtRSi9jy+I6bqYqK7L9WedeA9A1tfGtlJfaJfWkEDNI0s0RVQQpwM9+SK9T1vVX0+aKNdq+aW+dugxjj681v1yfjG3+1aTOUGZYG81AOpx1H5V6dSu69RSn6HBlmFo0qsabXut/8Az9Q8V3FhGDFLHPM52pERnJx7dK5I+K9ZuP3zalMrHkBGCqPoBVPQbuS/8AElgGhYxQy+Y5xxgA9f5VW1DSru01SW0trW4ljDnySsZOVPT/AArx87o1Fy+zb87H3uHwGGozdKcVzWvd28z1DQNTuLvSLeW6YPM65Z8Y3cnms3xBceRcRSZwrAjOepq/pVhPFpdlDja0UKowI79T+pNaqab5ibZVVxnOGGa+fp5VXnVant0Z8dmUac+eNN2u/wBTiIdIn1tUniuFjUEr8yk5967jStLFnbRxDnYoG7GM+9X7eySIABQAOwFWwABxX19Cc6eHjQvpE8ShgaVKbqJe892CrhcUUtFB2hSFQwIYAg9jS0UANVFRcIoUegGKdRRQAV4p4m+Nul6L4j1HSptEvJXtLh4WdZ0AYg4yBivaz0r4p+JP/JSvEf8A2EJf/QqBp22PVF+Pmhqc/wDCO3v4XCf4VKn7QWhp08O3v/gQn+FfPtFG5TqSfU+iV/aM0denh28/7/p/hUg/aS0of8y9ef8Af9P8K+cqKCLn0d/w0npf/QvXv/f9P8KP+Gk9L/6F+9/7/p/hXzjRQB9Hf8NJ6X/0L97/AN/0/wAKK+caKAP/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

