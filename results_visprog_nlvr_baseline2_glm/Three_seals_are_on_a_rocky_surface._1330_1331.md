Question: Three seals are on a rocky surface.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/08/23/00/a0/pepe-s-dive-center.jpg

Right image URL: http://media.npr.org/assets/img/2015/03/20/_mg_6678_custom-be213d2390780e70a6b9b384c53a730cb8b0d635-s900-c85.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Three seals are on a rocky surface.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAkAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCrb3AgQFo2ZjgkdB+frWrb3CTr8uRnsT/KsVXSOUL9oxH6M3O70qtrN28MQS2YBpOMxnn2AqWB1y+Uihp5Y494wodgMn6//qrJuLqWORoDG8ZDBm3AEOnf8/UVi65PeJcLbXKM3kImJB/E2AMYHeid7+6+zyyQP5SqUTYpI256/X2rNSb1LcbFyeQLcsCQYw2UC8NjqParNpdmHU0dYQkRy2GOcgg9aqKybY2uGBIAXaw2mtU3sV3eWyPGiEqsRx2Cjvj6Vpe5Bet3mIkuTBI7HIBZcKo9SabKLaZ0lkmgOBjapJ59sdea1vtcl4Db2ys/y43vxt/DoK5i/urTS71gsMtzdAHM0r/KhPoB/hVXJbHT/vJXMU0EaLjJGd3vkdqqyqpTYtxK5OWY8BQPSs661xbIKY/mlkB2hhkgfTsPwzUaiXUIS99eNCp7KoIpBysrGOaG5kczRG3YEdBlhUL33lxLEdzKg+UBAv8AL1rSn0WK4RT/AGi2RwSY+o7d6IYNL0r5jtlkxgtMd2foKOW5XkZY1S72jyrWQr6iPNFbEnihY2AS2kZccFRgUU7eYtDi9atNcsCZL7/SYgcedE28DHqR0/Gk0bWZYpF1B4wYbMh90nIZs/Ko9T/hXW23iHSFWRX1e1iGDzuDAZHYd+exonTwfq8KDVtYsJJEziSFvJzn/ZBqX2Gu4S3tvqim8bdJLMRIQj9R26dKmhvLiEQrEjxpGu0AE4zkk/XsM1VdvDS3m+18QWlvGuMbGU7vbB6VoLrGgrGE/wCElgk95SCc/hiuZ0nayOlVFuzes53voB9qCsMfLvXcaSDToodc094ER4nkKSp2VtpI/P8ApWMniDRrdC0Wu2ErDopkCfrzVvwtf6JN4igEGrxz3M8hOwSZLHB7fSnThKLJnKMkdvd3H2aIwW8OCw+8K5PxRY3EWlRXSwK7mdEYEYO1ic/5967rdCrli65xjkdBXHeORqU9nENL/eEHLI54610swSOBmjihmkvbpsKnsTVe41AX8UjwLIsfBVMAbh6mtafQNT1lolnsmtYl+8xfr+FdPpnhCythErQiU+kn3fyqNXsXojzhZrgp5RlITuFJ4qRrG78nzFgkeNgQHMZ2n8RXtSaRaRwLIIIwp+VflHXviqU+nQ+YCUAx0wOlUkQ9TyOCzv4oyuyWLnO3dj+dFervDGXO1QB70UybHzFRRRTKCiiigArrvhfz8SNFz/z1b/0BqKKAPpC5UIJGHXFVzGrW5zzu5P50UUhksMMZKAqCCR+ppvlJ5wxkc9jRRQIknc4VcDamQoqGSNfs8XGdwJJP1xRRQMpzKBIQMiiiigD/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Three seals are on a rocky surface.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

