Question: Several animals are attacking their prey in the image on the right.

Reference Answer: False

Left image URL: http://3.bp.blogspot.com/-9ueVTEWqLpk/UimcvPPgIgI/AAAAAAAAAsw/1t3PXNXkFGQ/s1600/CLOV-5.jpg

Right image URL: http://1.bp.blogspot.com/-uOCrXA5heY4/U0o2UJD51WI/AAAAAAAABDU/RWibUiADynI/s640/IMG_6333.JPG

Original program:

```
ANSWER0=VQA(image=RIGHT,question='Are several animals attacking their prey?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='Are several animals attacking their prey?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDURbpMKWXlcKRToHuSjLGwGRwCKimv1gQZPzc9e9KdatlUPJIsfqWOMH8a8tNvWx0aEok1KOQYZHQ8Yx/n3p8l1qI5QICDx1INYmva6YdJWa0uNjCQAMMEEDkqfrVHTvGcV5cpb+RM5ckRuqE8989sD1rRQk1zWA61ry7wWESnA5+Y8n2pItSuQ4MkLL8uTg5FVUvfMYxqjApycjA/CkN3sVh5qBsYAxmo17Bc0F1C6cKzQEE5wMjJpVv7hiwMJGD1BzWFPqqBin22NZPrTGu3t08+KcyAnlUXrVcr7DRvLqs7ZYW52j/awTVaTX50YK1o23ofnGQa5y68Rq6hI7OWRweQhwyn160kfiK7IkjktER843sMjHYj8apQfVDasdONeAch4JVGOCMHp+NPj1kSA4jlz67DiuWuL+/urZY9pTA5eLgH8uR+FVLG3uY2aPzpApOdhkJHHvRyLqI66TWkVsfO3HVcf1orlxbaepbzJVDE55GaKLQ7jsNur6KJPLIkQKOBI5JAPfjPH0rIuJ5oJEmnRJY5BhXVd+M9wavQsud0/kEgDLxnOfripzcNZW4kt1kYu5+7h0Ze+eK20Rm5HMa5dER2NlnEQG7k5y3c1s2morHbSW6SgRIFyqcFP8OKr6gljdX2+4iTZFbseAQM9R9DmsTVNGurO6tZLRmaO6UcZ/jC5x+I6VSaejC/U6d7i/S4bM85jDbgXbj24p8mq3sMYE5zBwAygZPsR6VbsHa+0uF0O0PGCCec8DPuDWibBJo/mXdjGNvH4Vm5pPUfMcvDp0eosWmLTKp4aM4Iz6r3rQj0W6tlP2S4DsGBCscbvUHPatxNOtI5CygRSgjJVsGpF8lQ7ucrjg/zqXV7D3MJLKWeX/SbRVlGAS68fgw59K1La2ZF8rbwAMfPuqw0VvMhTzWweQAaa0LopDpHNHxsIJ3ADv8AhUObYteoyFPs6nyxG6Zyyh8498VYhv1lhbyBDnkfK2V/LvUKSLblRs4X7pAH6EUXDwyyADZv9vlf8u9F0xCSS6eznznj8zvvCg0VA8Em7rG3u0IJ/Oip90ZWjhgUhVaNQTgk89e3SpYrWKPcscsajOCqrxTzPGgO5CSCcjIZjSR3KSwqiBV56nK4P61o2yNSGXS7NZGc5y5AJZs1NJpEBMUjO58kkxsW6cY6fiaBC5RjKxA6jCDg59RTU3QogYkJkruOWBqbsEi1Y29tZ2aJCvyJkEMBnrU5uGxNtUbhgEK3I4/wrJF0YXJfEeWI3K2R196tbvMy0kxIPOdu0mk99SrAxMrZ83YzfKVYYqvdSnS70pdbXszD8szLtw4POfUH0PpVgTRWcyXUhZo4fncqwGccgbT1z0rlY7467rk9zesXiBaRYeirntjvzWtOC3HsacWo2txc+SszCV2JWMAfOOuQOw68e1aiPdQgiRUdMZyD07Gq9vDal4bi0tbaK8n+XCFVdvUL+PGPatuLw7fC7gW94TbkqoJIHUcDnJpTh72iBGUZJWlUNHnjChVLdT04ouLG8CtJLbMkZHDbeRWvdarBpcKpbKVKHjORIhB6NwQeayGvLq8XzmZ5Hb+KQkfp+PpUuLRaSJIpZTEuJwvHTG6iqZkuMnls99pIH5ZoqeQC3I0cuY1mj4+blhxz3H+etZvmywzuXLPH0jxgN19QelODIVaORnjQrwW42n0HX9Ki22qKpkkdVxjcxGW/Hp/KqRnYuiZYt2whSTkhumfalZiqFsuqjnax3gnsfpWddS2jFIUkBH98kfiasWlg1w7FrhREx272Y4x754FIpRZEl6l8rkAMTycLyew4pzC7hkDQCSRegVME+3HrXReHvC0c7i4ZxLCxA3ZBGfb6V6JY+G7G2tEEVtE0gXIcjr6ZreNFy1BtR3PJtY8Nazb+H7i/kO5GONoUDqQP8/SvPtOs9St9TbMcjwgMS/Y8e/rX0T44V4fC0tuoRI2kjTj+71x9civIby3mSLNs8vm57KCGHfP+eacv3b5UNRUocxgW9nqk+rx3JjeGGGVGy3OEBGQMde9ehah4wnvriXyciJsYORz+VYdhdXlvaCLyUWQ5f1JJ7enHNRywO0iOzeTI2BlgAoI/n3qXK6tcVl0LapJJh2kYIc4AAbcPxq2JVVed+0DqFxwPSktAr/LDcEtF13DjH8qfcRXG9TDICg6/JnNY7uw+ZXsQS3kIYbrbJIz83UUUx47otlpYQfQjOP0oq+VD5GY042xyMuQQABg1a039/cOkvzKn3Qe1FFNCiX9BiR2YsiksXJ49DxW2lrBf2H+lRLJhT2x0x6UUVL0kdEV7preFtNtLPVXEERQSQguN5OTz6mvQ4OYhz7/rRRXZS2OStucj43lf7Lbx5G0y7cEDpXlbSOUuV3HBJzg4oorOruENiWJ2OmPIWYsrEDJ6YqaJ2aIKTkMSDn6UUVnNaGnQlLtGQqMyjbng/StAANDuPUJxRRWEuguiMa4lfziM9Paiiitlsbn/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are several animals attacking their prey?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

