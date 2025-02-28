Question: An image shows five white pear shapes, and at least two are holding flowers.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/c5/21/2c/c5212c2b07836b26dd2b20f3c8d2a821--d-india-olio.jpg

Right image URL: http://mobile.vitceramics.com/var/m_7/79/79e/16943/465879-WL%20vase-group-white-brown-jade.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows five white pear shapes, and at least two are holding flowers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDYhtJbhCTcKQP9k/8A1qU6fKBg3OR/uCtjwnYw31zdQz79qorjBxznFdQfDmnf3Zf+/leaqNWa5o2sXWdWM2ovQ81ubSSC2eT7Sp2DPMf+FY0l05crndjvjAr0Pxno9nY+FrqeAOsmUXJYngsAeK8uETYB8w8/7NUqcoaT3NKHO4++z2vSMnRrE4GTAn/oIq9iquiJ/wASHT/+vaP/ANBFX+K7VsZvcYBThQRiMv8Awg4qpPqFvbqWkYgfShzS3YKLexeGMVYSB2UMMYIyDnOaz7O5ju4VmiJKN0yMV5H4sGo+HPE9xb2t1cw20x+0Q+XKyja3UcHsc007rQyqy9mrtHskt3DbttkJz7DNTxukkYdDlT0NeWeHJNR1KaKJry4kZ8Z3yE49a9SiiWCJYl+6oxTSktyKdZVL2VrElFRlsGiqNDjPBgK6lc7mzmEcYH94V1BnmzwjHnsgx+HPNcX4IuWk1eUMjJmA8Ee4ruFjZTlXA5z92uenF8iSNa7vK5HqVlaanZPY3sfmQyD5hnacjkEehFee+KfCem6J4dimtricXe8LmRx+9z147YHPFekyOEUDAJ7kDrXlHjO7ebxLcJI0nlxgIgcHA4GdvtmrqJWuwpt3sj0TR22+H9Oyefs0f/oIqdpOawodXtrXRbNJLiGOT7KpRZX27vl4/WuIk8ZXV1aXDvcNHPC0QiiTK4YE+YzY7YIGPoaiVRRE2luV/il4n8ReH/EFkunatPb2dxbhzCoUruViD1HcYrgZvHPiSZZhLqsrYYAfKvHJ9q3/ABZdr4le1F1KVuLcznPQHeQyqpP90DpXECxlurqaGzPnZYHftKheT1zSTjMqNRW0PpL4bTXN14E0y5vJWlnmRnZ26n5zj9AK5n4mTpe+I7KwQDNrbFpG93IIH5Ln8ataF4ntrDw7Y6VpdvJC1pH5TGf95uI5JGOvJPpXGeIdRlvPFE927bTcTLtI6BQoH+NaJ9EjjxFSLi0ndno3g4RWMSy8yN5XyooyzHA49M13NvJJPAJZLaW3Y/8ALOQgn68E1znh22t4TEu0FEGBXYMMocdulEJubv0NYUPYwUd2Z0mQ5oq0wBP3RRWhRyOlrFbXZffj5SPm4rft7iKaUIHVsjoDWDuWpIrj7PKsqqDt7U1orCZuzPs7ZrmPEjF4bbakZO9s7z2x2q/ca5Z4+aQqfQqc1k3V0L11KgiNM4J4JNJq6GnqYvjW6n0vTNHuLO2+03Tq8RiKB42jZPm3D0ztI+leSy3EttLJ9t/dRggBy3JXPQAZ9fwr1nWZftN4qMAUiRUQegxzUOn6FpzkPLY2bNk4YwKT/KuKTTlrsbOi5a3POZLK61y5s7LRree9Mr5uLeQCSJRgYk3/AMI2nrkf0q9daevh3UpdJ2lXiYtvP8eejflXu+m21rbWiZUxx8gLGoVcjtgV5v8AFDTjcXthfW0TPMqMkmwZJXII/ma1g7WRjVpv2bSMGzcxhDGwVg2c59MVV1KGGXXUS33qlzJ+6RuqnGf5Z/Sm6Wsk91bwMwhycb5AQqe5wM1uw6Z9g8QebqRPmrGn2Tapwdx+ZjnpxkYreTtE82lScp2ex6D4bgm8uKLzCcKBlq7WOIpHgsSa5PSrqOBAzMFOBgetdJJqdpbQJJdXEUIcfLvcDP0/MVhRstz16nZFgqaKkGCARyDRXSYnxP8A8LB8W/8AQwX/AP39pf8AhYXi7/oYb/8A7+1zNFIZ0h8f+LD11++/7+0n/Ce+Kv8AoPX3/f2ucooA+jrLzrjQdKvLh3eSW0ieSRurEqCSa1rNhGqMuSOea6Pwjo0dx4H0EvyG0+A4P+4K1F8LaXE2424J7gEgfpXO6LbN1VSRz8eoTSHZEpZz0z/X0qLUJbGG5ijuJ2lmI+ZYx90evsK6C9SK1iKWtsi4/hAxn8a4iYFtQmadDFIzhsHuPr3qZLkWm5UffeozxHpV4BDeWqB7SKLdK0ZyUY9cj0xxmtV9GPiTTrUB8TpGGUn0wP8A61bGkeZITCilwTgj2PXPtW7aaRDp0JW3zvIxuPHHoBW1J80WmcVai1WU4swNJ8P30JVL+eB406FSQ/8AhXg3iHxJf+IfELX9ySq/vEhhViBHGAwVR/MnuTX0LqmkXl3GwErgkcFTjFeRf8Kl8RpqLrDDFLb7CqSGQL14+YH6mp5baJHVGXVs9c+GurvrXgTTp5ZGkmjUwyMepKnH8sUVf8I+Hx4X8OwaYHEjqS8jgYBY9ce3aitUnbUyk027Hw9RRRTEFFFFAH254J/5EPw9/wBg23/9FitsgGiigRDJDGw5QGq/2C0kbD28bA9iM0UUmUjQgtoLZNsEKRg9dq4zUhAxRRTEGBQOtFFMQtFFFID/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows five white pear shapes, and at least two are holding flowers.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

