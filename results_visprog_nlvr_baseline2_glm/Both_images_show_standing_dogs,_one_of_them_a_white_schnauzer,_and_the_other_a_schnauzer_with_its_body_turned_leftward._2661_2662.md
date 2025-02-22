Question: Both images show standing dogs, one of them a white schnauzer, and the other a schnauzer with its body turned leftward.

Reference Answer: False

Left image URL: http://www.paws.com.au/BreedRescue/0schnauzer.jpg

Right image URL: https://i.pinimg.com/736x/2c/7c/55/2c7c55e7bc95126a6bddab6c42b18863--teacup-schnauzer-schnauzer-puppy.jpg

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

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABFAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0K/uke/v8LuaSSwdUQ7mZQ24kL1xgH2rkNe1LxJbarbstxaWdn9raXzmZcIhk8wq+epLKv6ClttVWKzWK2DfMqlycnccDknqfxrW0LTodXu3OqGNrFVzIky7hJ6L/AF/Cn7Kyuxe0V7HH6pf3up6jbNZauLUyRtH9kLl5CoyPMAxjHAHXtUl3bPKg89mdgoGT3x3rTsokn1bVZL3TkgnSZxZ3Ct96InO3bgAL0xUs0QataNnqZ1ZtOx56w+Y8dDTNjO6qAMscDPApHI8xun3j6etdboWgLqOgSm/ZordpxJCybS3C/MeThRjGSfSuLlN07ncfDaWKHwZAZZEQG7lQEnGWJAA+prbCSeZKfNIG88DHrXmq3S6bBBpkbD+z4i9xBNK43vMxGMY4xgHFek2LvNbpJJt3MAx29yea56sLM3jpG5HdxyfZpBuYnbncTjFWblpfs0quihPKwCGznke1RalIVt3xyoHSrF8R9jPP8I/9CWlTjcTkZ97YSzy30+4LGGO3HViAOvtXBePfl8KeHV6cuf8Ax0V1OseOdL0yTUbCYyiaMMwO0YYlgCB3PHfpXBeKdbtNc0jTrO1kCy2AbzjKCqliMAA+vBrphQldNIzlUVnc5DNFQLKWUEgA0VViLnonmx2FsJ5FL7jtVfU1Z0q7fWfN8mbY8e5uOMBQOBV2VY7HSo5J7X7XBMjSykMcIADgDHfua5nwNqk95o121gPLe3uwZmI+Z45FIUk+xGK6a0rszgtC5oUTf2tcPNdSSybGZkJyOoAFbc5Xd1rOjtYdNso7uBsi5iRm3HO0nOR+YqvJqIbqeTV0ttTCrq9DkrS3e9vGhR1U/M3zHHT0960xq99ZW1xo9rZKsJby7ueTJOSuNpP8JA7CuaFwY5WZTg5PIPrXW3+vW+teCDZ3V3G2oD53LrtJccAjA5OABmuSV0dtNxtqVfDbWFsgsr5/PFrMHjjJyrAnp9M4PHvXultAgAnhkRkf5lABxg+lfOFlpupLZWeqeQHjluBB5w5II7H0r1rQdR1GxtxCkhMHzEK4zt5/lSkk9yrPodhd2RuVIeXGf7qmsjxRePp2hXV1jzPs8DSFQcbsEHHtUsWvT3AwIotw64J5rM16Q6vpV3p8sscJuImi3hCduSOcZ9qVorYVmeZ2McnjLWJ54bDy0SdJ5mNwc9G+UcYIPGRTPGNhetGt8+6FQBG6ROGUrnGSeuc12nhDwzN4amuY3eO7jusEyD5fLwD275zVbxjaW96qabHtgaVlXd0AGd3U/SvKq4mvHFqN/duvuOqNCEqPN11PJlk2qFwMLxwKKZcRm3uZYc5Mblc/Q0V7KOA9GtNXvtPWb7HcPGJ02SIRuVh7g1P4Ge10SbUbaRVAvotgkb5QrA7gPQA8/TivCvt13/z9T/8Afw/40hvrs9bqb/v4a6J1IyvoQoNdT1a61jUlv7uySSJrMTMMqNwIzng0/wC0ELznI5ryX7Xc/wDPxL/32aX7ZdH/AJeZv++zUxmkDhc9W/4RfPzG5k556ClHhhc/8fMv5CupgtWNvET/AHF/kKf9lOetHsyec6zwj4c/s3wW9rcKs/nTGZC2B5eQMZ9TxmsTxVrkHhm0DWyJJM+QVkPb2xU+manf/wBkatYbnKIgMJAPGeDz9a8y1zTJ3eKR7h5S24OWJPIOM+1c8laR1Qd4nRaR46tWZRMkqOxwQi5H4ZrdvfE1hNAHhtpzxkyHC4HqB3ryjS9F1O7ufMtIWcRNyQRwa7ZfC13NZAz3RikIJZRzitIwb6EOaR3NldvfeHfP06RJpojkgg5I7jFcdqMl1eXwupNu9EIjC5wrdm61n22sXvhdVtxcYUkfMjZDDPBrrprG3v7IX9mHJI3yxnnB7ke3tXO8NSnU9pJamvtZxhyxeh53f+Hjd3slwkjR+YQWX73OOTk+vWiuwFqrDIGQe9FdipWVjlc7nz1RRRWZoFFFFAH0hEzC1i+8P3a9QfQUx5gnUgYrVhT/AESHII/dr29hSNEjdOa9Hk0OC5p+H4HTSru6uI2ihkiDRyMMbh7Vx934fuNVtLLUbKUC1kaSN/LUEhgxHOeta+ordX+niwmu7g2gGPJWQgEfz/WmLrh0+GHTI7UmzhTbFDbxnj3OR1z3rhqUZXv3OylVjb0OUS4fw/eTWxDEsAeQB+Iol8Q3Lj5dw+hq3Pp+oajdPPNbiMN0DHJA9KsQ6CU5ZF/KuiFCVrGM6sb3OTuJ5bq++0SRkknOFQAZ9cV2vhLV7+QywxwPcBVwy4AZVqaLSYlxmJT+FTppVsrbvs6hvUZB/Sh4XTRjjiNdTPuLg211NBgjy3IwRyKK1ksLdVwIEHOelFWqfmQ5nzHRRRXCdYUUUUAfV0I/0OA5/wCWScf8BFSDpkgUUV6qPObEIX+6KMD0oopkgqJwNo6d6XyYzxtFFFMSAwRj+EUnkxn+GiilcsUW6e/50UUVJR//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

