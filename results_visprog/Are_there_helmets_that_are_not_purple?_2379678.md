Question: Are there helmets that are not purple?

Reference Answer: Yes, there is a black helmet.

Image path: ./sampled_GQA/2379678.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='helmet')
ANSWER0=VQA(image=IMAGE,question='What color is the helmet?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} != 'purple' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDG0nWBBr3iPV4ofNjKqVweoHetHR/FctxMbm+YbZMrFEvb3NcFYX8ltIGtmIVvvjH86toUGomRi2CMkkdDXDKbLvdnp+la/Hqd/MlrAzRxjazsdozXK/D6OVPiLqhdNqOGwQeD8xrNt9ReDTpI7Jtsjvjrjn1rofAFvHBrcckjhrlgQzZpKp0KjK7sefeMFKa/rS8fLdMf5V0fgu3FzoTSdTvNaOvaXZy/EKaKSFGSTLyKRwT6muisLG0tIXWCOOKJeTtwAPU1Nad4qJvTjaXMcJ4qul0y9t9isZQm7I7VkWmtT6jrlldTIyEK6jHORg16tK2grtkv3XcQCuIQ5I9eSOKghmsnuJZdBe2llUASRsgEkQGTu2gngjjIzz2rqw9GrGHLJWi/62Oav7OU1UWslovn5nAa3FNZaloDGNyPsIbBXjOa67wbpbyQXN/clGkeQpAAOEj7/mf5Vd1i9u4bISX6q1tcFUKvt3hXJw2w8/L8uehznjjNb2gQJHpUEabSI12ZHtxU1mlG0JXQU4NzvUjZrb/NGpLEVtNOMZIaP5jjvziuT1iC5n1qMvvKR3Q2ccAYJ/ma7RXUGKNiM+WSPzrPu9XsY7iSAspkT7wAyR9a43G7OprQpfY2KJhu39TRTX1+wV2VnAZTgg9qKl0YMVmfP8F3IfkG3f2C967GDRNZ1PSmVotjuFaIk/eXFZFhprPo9xpYiW2voLhfNZlG9wDyAa7+G5vdR1XT7ayO2ytkWOUoRl5Mcj6CuyUOxhGk77nE3uharp0cRMDLI+BtDZrX8Oi5g1iznuYJUVX+dhxXaeI7K4hlX915hU5DZ46VzWleMr611NLIaPC+6IZecAFG7888cURop3TdiXB6NXZR8V2ZvvGF+LSaVjIqsGjOSvA6V0Oh+FpT4Nnt5L91inO9pXIdmUEZUAsOuMVz13q6Razfapp9rGLSSEltvY4wSo/OnaH8RY5k+zf2A9yiqoVvkDKue24Y+np25rWlSjzc1SWi6efmaSnNx5IR1fX/ACG+ItO828NtJ4v+x3TkNGs0QjhfIBUblJIJGDk5H0rlo9b1rwb4jCX6w3UsBxuOC20jqr4zgj1yKs/EXWotWvrdU0q401oS2I7hBkqeg47D5vzrNMo1Pwo0l4vnXtsY7W2n3cqmchW+gBxntXTUqX1XUwhSavGW6O9Ou3Pii/msY7GxEVpH9s8xC+ZkABwgfB75I/2O4rtvC11ay2t1a20srPbTMHEwAYZYkYx1HUA+mK8s1GG7i/sGa1dEnSaCxGfvhgAc/TkjntXW21zeW0+u3lp4elRrVpVaeOYiKXYxydrcluv3TjmuWVJSX7rbr6nZTkrS9t8XT/gnoM0iAQPvXoRnPvXHC7jPjbUIPKfau0vIV+Vs9s965nWNe8vSbZoZ5I5mbcYEfcyAjnJ/GrOk67Jd6cbqIlxEo3ggnBzj5jjjNQ8NLYcakGrpr5/1uaOv6v4YtNYmS4nvPObDt5MIZeRxg/QCisdPDsF4v2i20+6Mbsx3LJuVjk5IJ7UVLwEm7qT/AK+Q44inb3lqcl4H1lJfFNp/aV0wVI3VC3O5zjH416Tq1hc2AunhhIkiiFxvt48YXPz7h+ua8k/sBtP0+C/Mv+kiUYC9F9PxzXr+i218LeC81S4klvTEY8MeEQ87T6n613U6TqaQt89jgqVuSN5N/LczfEXg/wAR+IWt7zStQaSyVVDo8+wFeuR61P4c8IXGhXV3q13LbX0T5ijinQvEJMdW5GSO1eqf2pZ/2VDYrHGJkUbyWHAAyT6nNcHqLRPKbe0lZ4t2doOBn1rpjh18NuvUydaVnNsoabZtpupXAmurN7a5QM8a2uFhOei8nAqnD4RtrOXz7eCOWY7lRmdvuNn+H1ANdfo1v9ktGlvY0DE5jidecD+Ig/pVf7RLIC6DcwbDM3fv/WnXw0ZqxWGxvs56L5/5HnnifRtE0/TvOEJiknkWOSaV2dgM5bG7kdDxXMTQxRyw3MkDRw3mfLhBwdgyNxxn5uRxg4zXqWtRRXlldSXIiSSIFYGYZ2uwxx7npXnGlre6trVlaebJBqFqwWB4VwMjBIJB+XGDyPWuKGHlTk0nd9DpxGLjUSlpbr5HT6SLC81O1gTTru7udPn85oJcBtwPUkkZK5HBHOBVrX/EF/JqF9Z3gDC2kZUhJKxjnqwX7/54q5BpWuaR4ludW1RkuBd5BkhfeI8tlUPAIGOhxW7d6RpuuNG19AzSIMLNG20j29xVTwk5UlKOkuxGCzmhRxbhXV4tWTW6/r7zhZ/CS2vh5NauL24uIJcPsjh27d3bJOMZ4yKTT9RXS9Qh0XTZ/OtdSiS4kt7e4DKxIPyuezDHSuo8WTSeEfBksZnku7RHEdtHJgFC7FiDjqK868ODTnDT2dqIbxi3kuz/AHSffsOa1UJVVHW2mqJqOFKpLlV1fR+RrWXie8ja6jglEEKTsI49v3RgcdaK5+5sLCx8pLq2vYZpE8xvKmVlfJPzD24/SipSsi3Wlfc6fwvb2usz23SSG2YSMp4+YdB+fP4V6QPs6AmaP5ME8dc15p4StbNNHku5IHS6eTcbeKYIq8bQyHn0JwfWvSljkvtOiESBpWjByOMn3rowtmvdMcQlTdqm5SinY/bbo8kQEZPYkgVr6NYxaVZJcSRZu3+bLDlF9B71NpulNEoFwFlOBwq/KMHue+K0p7AzMQbhRx1x/wDXrr5kn7x5VRymrUznry6M+oXMokVyAPk3YKgDr9OafpMcctpKSAcyk/oKqXunXek6jJKifaopFyziIlVyen1GKl0yZIredN2NjZOV2YyPTtWcPjbHiF/s6XY47xU819cyWFqwj8mZmkPoSdqfpzSeGdFbSdV/tGXDvNGY055DZAbg89uvvWhJLIb251C2tFMl9hVuCMiFFwFJBHU4rB17Vp9O8a2QjglY/ZUEjMykkAnk4AAUAHmuVSarc7+G50VKMnhHTgvea/U9RiOYGRsFWBDZ6HPXNYEd2sbtDvXcrFR8w5rjPGevahFe2s1jqnlWTwfdFs0oY55Kjbj05zXntzqWqapqEGZb2VVlBUMMAc8HAGBTq4tqTUVohUMnUqcJVJO77W09d3p6I7r4i6vqLxy6VdFZrGfbPASuGQqeQCOvcc+orjtEnOnRIboMEuGAiAwdy5wTXZeLrmC6sooZirypJmMt97pyAfy/KuQ0S0F/4gSzupVjtIWDkMOCo5Cj65pTmoVbLRnThoyq4SNZu6ba+aNy10O4v4TKLWKWJWZImkbLbAeM4OPUcUV3lvHbrCq2tu3kj7vlp8v6UVSigvI5PQYYo7W1VIo0y8KkqoBIIXPP4n869x0K3hj0O2KxgEoOetFFFHS9jPFttRuWn5cZ7cirECKx5UHkDkUUVvLYxgloPvIIoogY0CH/AGeK4vxMok1XS7dv9Vc+akyjjeAo4JHNFFZQbcPmaVIr2m3Qu67awW+lTrDEsaqAAq8DoO1cRc2VvdeG9VuJ4lklWJVDNzxk8UUVhL+C/U7Lv2i9Bnw6nkm8I25kcuVUqM+gYgfpVjxK5FlG4wGBfBAx2zRRXqR/hxPmsQrc683+Z5Bqs0supoHdmCksAT0OcV0ejxRvblmQFhKwBI7cUUV5C/3l+n+R9ZRSWVRt/MvyZvxllQBXcD0DEUUUV1HCf//Z">, <b><span style='color: darkorange;'>object</span></b>='helmet')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADIASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCr8RP+QI4HtXLfDmMf2pIfYCtrx/fF9LCL/EQKx/ALiC6kfucVz3sjVnr+Qq5NVrjUIYFOXGRXN6v4mFqhTJBrjLzWprmfb5jFc9AaiU+xLkkehrrIubkRxHI9q2xnyhnrXnmgeZDJ9olBAJzjNdouqwtHjcKIvuOLNBlBi6VBAFDkYHWoJtThigLFxWTZ67G9wxz8uaJSSaKXY6x0BgbjtXifjhANYf8A3a9cj1ZZoW2ITxXj3ji4d9VZtuPlxRJptWNYQaTbKXgdtuu4r6G03m1H+7Xzl4Jc/wDCQDNfR2k82q/7tOoZQPI/ikoW8t2J/iIriUAKCu7+LEf723b0fFcHE2ExjNFPYJbmbcELcDtzV21kTz0571Qvf9dk8c1asAHuY8HvWsrWIW56Pp8e61Uip2g9qm0qH/Q1q00XJ4ryJbnoplNYcoeK5vU02z9O9dksQCmuP1+eOCXk96cNWO9tWLpl59hmZznaw2kjtzW++pGa3wD0HauBl1VQh29Pao4/Ed8SIYp/IgRRnaqgt65Y/wAq9zA4hwp8kltsfL5xln1msqtJ6ve/kO8R3UDaxI8DMzEAShlwA4GDj1HFdboM4bQY/wDdNcNfXZvpWuJ/KaVwNzRDCscYzxxn1x3FdboTAaNGAeNprnrNOTfmephoOnTjB9Ei/wCEBmO+I/57n+Vcj4quMeI7iP8A2x/Ku58EwFrG7b1mNcH4xRU8U3PQEMv8qmHxGk/hN3QbeF7fLZLZ7HFS3t3ZabOFnmeLzOVYIWXj1I6Vk6bPsiUetQ619sa9hMNn9oRo9i7ck7jnsO44IranJwnzHFWoxrwdN9To9M0u48RXheGaE2kBVvMOWWQnsMda9AeEbeB0qh4M0CPRvD8KeWVu5gJLli2SXP04wM44raaM88Vy4is6s79DrweEhhqfKty9oEWXYYq1rjyQowT0pfDyhbhgas65GrvgVh0Osy/D904jMUjE4Pem6lqH9nXBc/dPBqOxQw3P1qn4qGYQahq8BSMLVbtbrz7hF+VuelZnhD90HOOrGrgTOmdOqmmeGo8rx60l2JOihz9s31De5e5J9qvWtvunx9TUNzCVnINRKknLmGeR6xfvqq7Odq+tavgaBRLLvJzuxx6VzIjdZCua1dLvl0+QkE88nBrvUrI5Yu+5seMbXylEiFixOOa56xjxMhl65FdVFqlrdZknIO3kF+cVh6rKJrgyxjCAcHGKzcruxUoJ6o1brVI1gWOPAPQ1JY3hkQln+melckjSTz4BNbVsgjTlznGKmV0xRTvcbq2ozmXYkhKk9K3/AAzpzXCCWbJPeufS2E0+8ndgV1emXgtYhEPTOKd9UCjrc7GD7NHblQFyBivKvGMK3WqcYKjjiuhvtbNqD86gkEkVx1zePe3WSck05zvsKVVrREfhyxjttdjYHBNe/aNzbL9K8S0bTJV1SOZicele2aJ/x7qPaqTutWaU00tTzD4trtjgb/ppXncP3QT0r1/4kaR/aNsBj7rhhXlUtqbeXyjV02rWHJO9zD1NgWGKk0piLmLP94V19p4RS/jDyCtK28F29vIrheVOaUq8ErDjSle50Ojj/Q1+lXmi3HpTLO28mIIKuCM157R1lOZNkLH2rzDxMXmvioPAr1xrfzFKnpWbN4ctppNzopP0q6cuV3InHmVjxeSMrFwCT7CorK2WTUbcXMbNF5ihwPQnmvbF8LWXeNfyqUeGLLp5ajPGQK6ViLdDJ0dTxa9t3guJbfDARnagbqF7CtrS9VgtLBYZXbcFxwua3tB01Lvx1c2l0BJthIIYZ+YbR3r0ma10DSYYY7mGxtkz8hlVAzt64wSf8K+u+o4GEIe0hJ3jGV+ZLVq+i5X+Z5VfFulKy1fY8+8J+KtG0nTZIbyaUSNIWwsRYYri/E9xDqfiCe8tGLQuQQWGD+Ve5C80eYFUgtz8oO9rDCg5/vbOeP8ADNQRPpsIkVtPsLyxL/MpiQhD6ggZU1Cw2W2coQk/+31/8iYyx8k0qisvQ8XtLmCJFDyMCD2Wun0cC8v4Ghy0ca7icdyMD+tbnjnQ9Lj0SW/04Qx4ALQnAZfmAJX1GT0PP1o8A2Kpo6SyKBJMxc/QcL+gz+NceNoYV4JYihFxfM4tNp7K/ZHfSuqm+6O1s8rbIParGAeopYowFAqURivnDvLmkAC5OBT7/JvAO1JpuEnJNPuQGvQRT6AUhFtmBqprdqbmAKBzWw0Y30skQZRUJaWHJXOJ/s2UWXl7ecGotDsJbUgOuOTXbG3THQVXa2QHIUU1BbmZThBSZWpbiISTFj+lWjEBTDHzT5AueAoySruzz71DMdh4P5VTSVogFq2gEuC2cVs1Y5rPcuW9wGAXHcdK0ZIxNFzgD0FZUcRTDDsavBJ2g3AHb7Vlu7oiMncqFBHJtU4JPBFbttFG9tgnJI6e/rWEltM5De9XBP5UY556c1U2ap8u5e8xYZcD7uccVqNOqwF179MDtXKST5YEHitcXqta+WO9RfqKMk9EZ2pXD3chCLxRpllKZQXFXLeNAcsOp71c87y+gA9KTldaERav7xsWEYR0r0nROYV+leVWN55kynPGa9P8Pzo0K/MOlXDRWOlTUtih4uTNu9eN6gv/ABMSBXs/i9lWzkYnFeLXjh9TOD3q6fxFS2O70Vf9GX6VqlRisnSJo0tl3MBxWi13Bj74rmktTZGd4i1W40XTVubZY2ctghxkdKyLbXPGN3bR3Fvo8MkMi7kYLwR/31Vnxwwbw+hH98/yrU0nUbXSPAtjfXjhIo7dfqxJOFHqTXuYT2NHLvbypRnJz5db7cqfRrqXXbSpqLteLb0X8zXVMyV1Txz20OL/AL5/+yqwl14/kj8xNAgK+vy//F1uWt295YJe3KeVaygNFB0aRfVj2HtVC71yRAYolCxjgJH0FehQdGS5p4aC/wDA/wD5I86eKknaMvwj/kZ/9o+PAf8AkBwfp/8AF0+C/wDHtzJ5UOiWryf3QyZ/LfVZ9VmY5y4HuKo32o2Kobi5ijMv3VZkzz2OBzj15HFbt4O2mHh/5N/8kZrEV+sl9y/yM+W68RaF4w1K6n0+O31MQGSeJgMRKQpLDn0wep61qXOq+MdBuUuLjSIbd5YmmAeJWZkAyzk5Le+Saybe+tvFWuS51tdMvLuMWhhZGdHQIo2+ZnBBxjB9q2L/AMFavpfh++u49fMmICtzbgMCVUAlCScYAOfQ49q9h1suxUaUZ8lrRjZqpo9raaadPzMoTqwm5RWut9I/5FnR/EMfiHUoJvFesXWl6eYiIprbdEjSg8gvyAcY49xU8F9NfprUVjONXg0whor4KFe4XG7y9wGHOAevPIFZfhHw9rGq+HHe18QtZ2jysjWxQsrHA5I6d6vXGm61YxMJ/GktukQJIMbKo/I4zXhYujg6VSVKGIjFxk7aT0s3p8L9Hq7ndVpzqu84OzSutOy13+ZS1LXbDU/B9+kJSVCEaJtuXibcOD3wRwfQgetbvgsn+ybQf9M1/lXmSaXC95bxWd6JPtDKkjGNoyoJXsfvY3KeK9P8O2zaQ97pjziZtOuhbs4GMhkDKcemdwp5hUw7wKpUqilLm5nZNfZS6pdjhwtCVF8stlt/kdtGPlqUDNR253xAjvU4HtXyh6pJagiWkkfF2Bmn2/ElUbydotSTA+U0+guppsckU2V9o60nmh8EVjeINU/s6HzD0qUrobepom5Ucbqha5X+9XHQ6/Jd3CxxnljxVqS7ukcKec9CKvmityeVs6F7pR/EKPtKnuK5XUb6ezhWV+hqqmtSMoI6U+ZByM8tiEcg3d6kXbv4zgcVjJK6DqcVcgZmjJzzWsotI4k7bmibo/dB4rcttRiFkI2AzjpXIeaU4NWUuCQAFOaj2ZMZWdzr4ViazJBAzyCK5e8uNrlQCMnvXQaIrzWrA7tvPQVj6jpk6TPL5TbB3NKKSdmbS96NyGMM8eRwKcs7xyHOcU+zLOu1VJ464p9xASpYLjjmoe9mZxqOnJSW49dQzIBnj+VXluDKgAP0rlxIwmxxn0rStrhhg5qnDlWhnUnKcuZmpultyCGx716B4QuLp9rFiymvO3mDBcnpXovgu5hRFUOM981Cb6mtCVmTfEOeaHQ5mUk4HWvIoi8rq3Via9z8YQx3ekSqcEFa8UjQJfGNegatqUldo6pp7lbUNZvLJQsbN1qra+IdRluI13OQWGau3dq93qotUYLlN3PTpV+18LXoYGO8jjPrtNerPA4alThKvXhBzSkk+a9n6RY6dOtUb5ItpadP1Zu+JGZ/CcTN1Lf0rFur3+0ZPDmnYL2tlAkkidmcnPP4cfiateItF1qx0OOe81b7RbMxCx4I7deaz7Cz0lbeC5fxWLW62jdF9ilYxn03Dg/hXt5fk8cRl/JRqqVp3ulP+VK3w3/Cxnja8oqmpRa91rp/M+zO21bX7SytkbVr+K3OPlijXLlewCD0GBnpxXG3fj6wUlbDSJZh2kuptgP/AAFf8aryWOjPK7P4kikZs7nawclvqSM0xNA8MykmXxLEhz30+U/yrrlkOK6TX/gM/wD5E8pSp9UUG8ZXxvWuVsdOGV2iNtxUD1wX68VYi8bK3F5o1s6nqbaZoz+pYVk3tlbW93JHbPFdwqflmQMgYfRgCKrGEf8APqP++hWS4fxK2n/5LP8A+RNXOD6fidjBH4S8RAJHqBsLpukOooArH2lXgfjiu8vLiay8DXmnap5skws3iEpOfMABMbZHUj7ue4/GvE0hQnDW4Ueuc1s6R4k1Ow0i60e5QXWnzRssaSPzbsejIew9V6H2PNJ5JiqNSnNR5k2r2UtLNb3SEproz1D4cWEtx4WMsTAZmZT68YPoa29V0ayvdKKX0KlbcmV2x83y5Oc15dZa54m8P+GobvT4wmkvKY2ndMr53XbnPB2gGoJPHfiLU4TaC6RVn/duYk+Yqc5A/DPSvlMyoVJY6tJfzy/9KZ7s68IqKf8ALH/0lGsLVtWmbWZbfyxIy+Q2P9VtwSD+aj3x2xXQW94sXxe1iwkO2HUh5P0kCK6H8wR+NYi6fNpeniGe4nklGSY5OBEScsoH19fSu2v4fDV7rBW4+yQ6vE0ciyuTHIDgMp3cZ4x6+lZ4acYqV3dPQ5qtOc5cqWq1Oisvlt1DdRwas7hTI13byCDk5yOhzQc81yyVpNFrVXJ4mG+q94qtKCRU9t8z1FfDEg5pdA6iRuMisTxeiS2BVsYI71rwnLgH1rM8VqosGZgDjHWhSUFzMuNN1ZKCe5yGnwrBcRuCpx1rrIkjuTHhegrhdL1KO41JoMqdpIGOhrvNLYNIBwPb0qZVIzqWt0Klh5U4Xv1Kviy1QaO3A4WuZtIo/sycdq9LeO3e4iFwqMuDtD9Ce1c3rraRZaj5TSQQMUDMgwME5rGriY058jQQpSqK6Z8+B0C4JzSRysHwucU2xtHvbxIs4BPJr0vTfDOnWdgZZEUuFzljXq2Wx5vI3scRBB5qh2P0rufDXhqC/tfMdc57VwUuop/bJiT/AI9xLg4HavavCEOdPVgBjHUCs5q2goQ11KiaRHp/yIuB3ArR/sq3uYcMgOR3qt4h1e204FpHAINVtG1xtQwY1by8/erNQ5jotylseHbSGMhY1H4Vh6vpcMcDAKOR2rspHzFn2rDv4vNiYmnNWiJRTZw1voEcilwijnqeKsJ4fGc5jH/AqsaxHt8NXnHQD/0IVk6bpvhaa0ha91GSOZkBkUPjB7/wmvdy3J4YvDfWJzktbWjHm6J913MK9SNOXLymqNDXu8X/AH1WzpEcenSqd6gHr8wrmNa0nwjb6HPPpmqyTXylfLiL53AkZ/hHb3rttL+Fnhu80qxuZrq+WWe3jkbEqgbmUE4+X1NdVbh/C0qaqVK0opu2tPXT/t7zM44hdIfj/wAAm8Qa7A2luokU5GAAa81tI/tF+X9TW54/8D6f4Wsbe5sprh/Nm8siVg3YnIwB6VzGmXlxbzQx21ss0jLkKT9al8OJ0FXwlTn5m1qlG1r3d3JmkMTd2mjYi02T/hL4rc/eNvvGOexrsfDUUN5qUiMBKsB5BOF78k+mQR05IPtXENfar/wlcDSWZt7yaEQIq8lQwIDj6Zz+FdzoF1aWqyLpwhZ7qMtJuYyyqkQ2qoI4RR1JPUtgZrDM8sar4f29nanFb3V7y+TNPrsoU5RpPdv9DS8crp4g0/8AeRPN9qAmjznCgDqKva1D4Svz9ls4rCK8f5YwkKjJ644HH41h+J7OyEVo9lctJdNdKshbJ8ssuQD6810Wr2Hh61vL7yr1ItSiwPInj2IkjsB5g45UZJwOK56NR069RRbW35G+KjzZfhm/7/8A6Ujn5rbSr/wLdX8Vjarc2KAzmKFC29eM9PusP1wfWvO9R1gwW4MGnxYADmby1Hlkc4ORz6Y5BzXr2o6Za+H7iCaKKR9N1AfYL8CIx5DZHmAezDIP1ryr4oaQmk39yIZN0Uphk2gYVSV5wOwyCfxrdYucovlkzzJUuVq5N4c+JGmRSRQ6votqqoSftMUCMwPY7SOevTnNdH4o0e01LQI9R0uKyFsIvtEklvAMbMnLx4Odo/iU8r1HAIHicRt/s83m+Z53Hl7Tx75ru/h344OgLPpl7ua0bM1u2N3kyjrx3VxwR7A+tc0sRUmkpNu3mzeC5HePU5JJY3upFjfeMnDEEZHrVEFw6N5hKlux6V1fiHQ7Sw1aS/0yRTpt0Fmt0B5RXGdn/ATkfQCsDUrRrTXJbZk2+WVBGMcYHP49fxr1HXl9Tw7Un8U+v+EJU2pNvy/U6KDSdVvfDz3EHnTWEch8yMPlUbHB2/TvWfZQD7UNzvEqEYeMfN0zkfhXoXgKTdoUlqeY5ZXEi+oIArlryw8nXriztpTKkLs5O0EsM4HA9Av613YvNcV9bqUYStabW0drvyOevBU/fe3Kvvsjo/EnhCODwbD4psPEVzqKSuFnSbh1J99xzz/MVm6iDI1pJIxd3sbdmLHJP7ta5/TNXe30/W9FllJiZcwgnuHHH5fyrv5fCOoalpGlalYmKTdp8CtEW2twgHGeD+leTmdaticsU6uslUa2S05V2SPbyKrTpYq83ZOPX1Rt/DvVM2M1jMf9Q/y/7rdP/Hs/nXZs6EEjGBXlWkQ3uja0kV3bzWouUaDdIhADH7hz04YLXetcNDaush2zAYdfRu4r5tLmin12OvMqSp4hyjtLX/P+vM0re+hE5XIo1C6iTa+etcQs1xbyvPKrqhPB9Kn1jVMaS8yndtH51ahrY4pRSSdzpUv4lkBJFYvjhmvNGeO2bMjYxzXHJ4tDWwzES/8Ad9K2LC+Oo2QdjjDYAPrWkYRT0JlB2VjlPC3hzULG+kkuVBjZgeD716RZv9kDMvrWfHfK4UbACDjIq3HMshZV5Yg1m4+0qq3UUlKnC0uhX13X4LnSJkEmHAI68g15DcCa4uHkmkeRyfvOxJre1vR9ak1iUqjC13bsqc5qjLaTI+DC/wCArWrRcOmo8NUUpPsYWmzLa3AcnHNeh6fMt/pjhCWZl7Vg+N/DkGnzQNZgZfAIWneHpm0Rc3OSr8gZ/SipFS23JoycXqtDLstCMGpzPOpChsgEV65oF6lr4f8AM6AA1zLpHqsgMcTMOvHB+lV9U1MW1sunwkxMcKVb+GqdNy95MmU1GPJYwNYnvdc1N2KN5Ibj0rvvDUEUdvFAijdj8qq2FjBHaxoAp75PUmuq8Pafb20m9iM9eayUHKSitjoUlCDbWpauLV0hyRxisC+lEUDDHNd/MsM8BCkdK5O706GUurHgVpiKXLHQ44Suzz/W59/hq6CjhiM/99CsvR20NNIaS9igeYA/eHPFdRq2mR3Gm3NhFJHHJJjYXPAwQe1cVL4WuYdxe5twF5zk/wCFfTZRUw7y50auIdJ8zel7tWS6GdaE5VrxjfQx572K4kkEVqsSk8EDoK9C03xhqc1nZW1tbfu4o0RnJ7AAVwdtplxdyukIDBT97sa0k8L3bRF/tMAwMkEt/hXpVqeAr4eNB427i27tNvVJW38jn5KkHzOG51nxC1N7zw7YxSHLJcZ/8dNefpO1vNBKpIKp2/GnwafNc3Lwqwypxk5wfpXT2mmxxBIypIUYGRzSq5hhMvwcMPTl7bWV7Xjo0/XuVTpOrPX3TE/tUSa5DeeZIoVNhYryBtIOB+NbC+PPs8rm3l+ygwJCotlSMIFJ74YkckYPTP0rE8VxPJqLpbIWYRKcAc4HWuVgs7i6k2RoxbBJ9h615mcYiMvYSjHlXs46N3tq+ugey5ZSje+p6JbeJoL5WWOOAulw128mGLknAwTxlRjgdq6zT/i/Yw3ks7yaegmCh1Fq/QDgeteV+Gois9yhVc7NpHvnpW5DpGlsi+fpqBgCCY5CQT+Qr5iWJjCrPm62PqI5XiMXgMP7FXtz/iz0DxB8U9L17Sns/ttipdlbzArqfl6da4Hx7rlv4ruluIDHGwCgpHLvBIXBOOOvJ9s1RvvDts3FvZiLjq0zfyxWY/hliAY7iJG93J/pV08ZTjHlucdTIMfe/szDa3dTjIP40sMkttcJIAVdCGGa2f8AhGrsD/j6gIPqT/hU0Wg3aLtae2ZO6tkj+VP6zR/mI/sTMP8An0/w/wAzZk1H7T4Ia28to9l2jlCMAEq2dvtXPa7ObnxDeTD1QfkAK3tQKLo8u9i08kyMdvKjCleD16YrPh0mWOSae5kgl3Hcy89s/wCI/KvWVSmsFhnf7c//AGwh5bjJTnT9m7pJvbT4rHWeE7o2WgTXCuAysxVffjH64rL1zSZ4NJtdasXeO+2tJMynnYThR/3yAfxp2mtt8N2yIpMs92yDHXGB/IkGut17UbaXwfL5CKoWLbkD04rlzmrKGYVeX+eX5sinQjUheW3Kv/SUeN2SlpWcnJxkk16TqXijWtCm0eLT754oG0m1cwsodM7SCcEe1cBpCRSi63OQyQllAHU5H+Nd3rOg6hrl/wCH4dNtzLJ/YlsXJOFRfmGWPYV6kLf2Yub/AJ+P/wBJR5uvPp2N/SvikskYi1fTg47yWxHP1Rv6GqPiTxmhu2vLTcbKRgYyylSRgdj75H4V0eh/DHTtOEc+qyi9mB4iUbYQfp1b8cD2qH4oaLDe6bZSpsjZf3IUYHA+ZcD0HzD2zXkzdJyXItTpip8klLt/wfyuZmleJE1iOOMQSKGO3celX9Sslsrc7yNjjBHYYrmtOuodHs449v7xemKh13xHc3yLFtKJ6jvWlSn7RWehz0qvs5XWplfb4Ip2UqMAnitjR9VMgaOIgZ7elclJbEN5hzjrTLK9ms70TJkKK5YUFz67Ha8bJK8dz0q3MqSBHH3j1rG17UNTsNbgtrCfyjLHnBUEZyfUH0ra8O2Gu+JIvtNhYGWNOrlgo/Wsnxbo2r2msxXMoFtLEm0FuccnnuO9etlMKFDEuVVxtZ25tVe2l1r18icXi/rVNJK0jPvda8TadEJZr+LnAwsSE/8AoNb0l5A+x2UksikkDjOOa5yLTdW8RXiWUmoQsTyC6kD9FrvbjwiUZESQYWNQfrjmu7MatGpRp8rg5Xd+RWVtLdF5nFGEoNrU8u0/xI98xOoPvYdMiqmr6ubieNUGArAgVgQzeUc1PAy3N9CpOAzgE/jXzapxUuY6XVk48p7n4agFvYwy7MqV6H3p91oOl315JeTqplAwGc9PoK1tOSKLSIVBH3QBVG48Pvcq8okYHnHPSnTuo6F1LOVmZB0+dGJtpfkHTPSmR61LDJ5TuVZTyM1a0eV0uXsLhvnxwD/EKw9UgS213ZneHII9RWkMHCo9JWMMRmFShC6hc6yDxA9vAfMY8jgmvN9d8d6lBqkyQyDyz0r0+5s4GsUDRYBwAa808XeDp5Zzc2MLuP4ggzWHs5Rnyt3RvOrCdNSSszmk8QajeXgd5myTnirGo6jdNBjeeRyaq6NYSw6mIpreQueibDn8q7S68E6hqUAaCEQDH/LY7c/hXTCF1axyudne5zXh/V5lMdlGvzysEBPua+gLH4W6OukLNdXN1POyZdvM2qT6ADtXnHhTwKdMnea/kt5Jv4dhJCj8hzXU63Bqd3Yi3ttZlt4hwNiFj/6EKFhpLWOjY5Yjn0k7pHL+KNFsfDl6Xs3cgjOx2zir3gS7stUaUzn50bG2oofALXUZkuNYuZmI5Lxg/wDs1Zlv4MbSdWMsGsSAngqIcfqGrdQlblMuZJ3ZP4on03S/iR5sz+XbCyAyFLfMVOOBXDmW2S/uRBOiQnescojOSpIIHrx0/CvaLfw3Z3KCa5jhuZAMbpEBJ/OsTVPDES6n58OnQ+UYQjKkSkBg2QcAehP5V3V8ZgK8IRrU5uUYqOjSWnqmdMKE4vmurM8hliBuWeKdUDEknDA8+uK7RdU0QeFYtKGoyJcI3mCfyWJD5J3fjnn2rqotOsls5UbTrUSEbRugXIz+FZcGk3N15Mf2axiMWQ2bRT5g7fTP515sqmUyX8Opp/ej/wDInqQhXpv4lr5P/M881K/vtSuXluL2eZ3QRs7yFsqDkDnoMjOKj07T9PNwft1wEhHTahYt+lez2mm6fAnlyWVlKGXO426fK3cdKqXWmaeISTZ2ud3CrEoP8qTxWV25VTqf+BR/+RHLD15vmlKL+T/zPKNaFrc6lC9rIzwqBlmyMY6DFSBdPfYkjnAGS4Tq2MdPQH+daun2tvqXiXU5GiX7PEywRoqfKSTzx64B/OqGt3cV1dppGjwwsq/K04QBs9wD6D171tCrld1Dkqf+BR/+ROGpTnaVRtau235amZbYtkvIFAMUrIUY9flz/jV69tYrHT7ArZyx3BVnmunbckrMc4H8JwMcg85NX10yy0m0lSZ/NuoojOzNyB2VfxNJ4a129gtEsre2kuMDJSNN+VBzyuMHBPv1rrqY/DKFOnSi4xg2/ea1vbsl2OFxk+t35EOl6isbW0N1A1zbROziJUBJGP1+bafwrQ1bVv7Q0mSwhs7uGNskHb1J9fauqbW7B2trnVtH1G1WygMay28DRiKNie2NuCc9RViWbQtUjUaf4yMPHENzE0J+m7oajFY3BYms67w3M273VR7+ljpoSlCHs5T5fkeZaPZPZWuoebZ3Ms1xCIoWSM7U+YEk/gMV7z4ZurG18OaZ58kEFz/Z8JlMhCsUXIGc84BLfnWB4f8AGVjaXEujPqUFzND8rPEzbSfYkDd9RWP45bzLywcHdm3Yg/8AbRv8a5sdmNOWGVClS5EpX+JvW1ux0Zfg1Xr8rluje1vx4I90elwgr2uZh/JT/M/lWPb6NqurSNqWrXJtbbbk3V22PoFB7fkPrWVpOsXOnxPLEltKVUBRcQiTB9R6VU168vtcaObULqSbAO1d21UPso4z79a8Sk4zmnUlY+jxFCph6ThhaSd1q76/j/XkYepXpjn2nAdWwR6GnyXJkhUFccV0+jfD+28S2YvjczRzco/ORvHfH5Vtp8ObaysGN9cNI46Mh2gV7kYyautj4mfuS5GmmjzeU74gicseMClk0e6SBT5fLdOK7OeXRdHQJCsZk9EG5j9TV20XUPEmnSPplizpD94tgDPtWVapSoQ56skl3ZVOM6krQVy54O8cv4O0EWklstw46Ddtz/jUmqX9z4pWS8ntxCDwkYOa4A6tbm6kjukKXETbSj9VI9K6PS/EIjVJGQ+QDgsO1YVZQcvd6o6sPSl13T2CaCLSXFwGMc6DrnGK63RNSTUdLiuJpwznIyDjNeX+MdRg1O5MqsyqiYXn8zW34OtfN8OQOlwRktkE9DmnRcfhXQ1ryqRbulrqeQ0qkqwYHBByKSpEhkZSwU7R3pHIeo+EPFNzquoW9kx+VFyx/SvY4YGEGO2K+ZPDt1Jp98tzE2JFP516zpvxAlMcazREZGCQc/jVwcErMp8zdy5NpcV74kjh85oppHCbwfuj6VX+I/hKLRo7TVLO4lZg4R1c5J9/zxWTe/a9a8SxT2KtuTBaTOAg9Sa7wyNLDGbqY3EyDh3HQ+3pXLWwWLnjaVWjO1NL3l3/AK/AmliaSoThPdX/AOB+JU0Ca71DTEW9szBwOXH3h6gdR+NdlYWNpCgjePI9McmrHhLT0ntzcSxgqpwue5rqJ7SKcDeoyOhHUV6c5whNo5oxlOCOM1C106AlkhjXPcDGfrXKXt4huDHbYx03DoK7W+ji824t3ALRnHSuKnsjC7yKOM5wBXRG25nbS1jsJ9GsoND8xfvhAxkzyxriftQUFWx1p0mq3RtRb+c/lDomelZEm6R+9ceBwlalGSrT5rs6K+Ig7ciNoaj5UZC4/CshlmubgyKCeafbKu/5zxW7aCAlY1x8xwMDJNdknybIxilU+J2Rki9nt1EeSD9a0bYymFhIJBIcOoK/w9z9K6GHRrGzmE7R+dOOQXwQp9h6+9Zst9NJq9xDHGZfMwpw2DgD6H1pcml7C+tqc1COqRSlnYBUCB2J6Gom09JrUjzXt2J4aFRgH6HINWYEVJH8zA2sV56jFPimjz90cH865akE1Zo9ClPW9zGa1v4ZyJZEuUflWRdjDrnK5OfwqlqMhitZJEDZ2lgcjt/KulutvDnHyHIIrn9f0tfEETaeskttLIpDyx9GGclW9iK454S/vROqGN5U4fceNwarfGwbT7NXV5pWnmeMne5I6cdAB1/Gt3whpsGwvJE7TNwcrlcdcfT1rotV06y0HT/7Ms4REzcSyHl3wMncf8is7w/qOlppqJHcCOSQHaCOSe4Ge/tSo/vXZaHLjH9XgpS106Gf40ZLTXlWBUaKVIZZY2GVcqTwfYnnFZ2kw6teXkOk6Q86y3Ew+SORljV25XOOB06n0qTxWpGuWpZSC0YDZPP3jjNXPCfjLVvDt7Fb2rKbZ71ZJYiq7nOQpAYg4zx2OO1aV4OLta/qc2EqKpTU1pcteItIvvCd5ZGLV7y5mns0uZz86eXuOADyRjtz6VU0YC4vLWCPO6abEjliTJuPAK9BgZ6dc16F8RPiFdaZ4huNJsYYWjSLbcLcxK672XORjk4B6Nx7V594TXbqVhMeB9oDD6ZAqMGr2b8te5pi5csJOPZnrP8Awifhu6uoLq40i3MsR4aPKbhjGGA4b8eazPiLpACWd3pVoUsbe3Mcqqd3lMWzkj0966C2uVYjnOOo+lWYp2Xbg8kZPuT1r08Rh4VoNbHkZVmtXBVYzWqXRnjNtJsyp+63X6066kWLZGf4jkCuz8TeCpLiVrvQ40TdzJbggbD6rnsfTt9K5RtAvNMl33drcCTgb5VP8+lfOVqE6MmpI/U8HmFHGU1Kk1r06rysdZ8Oorq+urzTLe4EMzReZEWHBZSAR+R/Su9u9Ln8o2t+wMuBkY4Irybw9rTeHvFFlqIz5Ucg83HdDw36E163q+vW+p+J0gsmMkVvB80qj5WJORg98D+dell1ZzSpM+Y4gwypV/arr+e3+R4l4g0xtL1G4iETNGnzFgv3R71reDfijp/hrSLnTryFywZniZBkHPY1sa8omlv1lXBYkKT2GMV5Be+H7mK/CIreW4ypapzHLaeMp+xq6q55mHxPsnzW+8i1XUxqmu3V+F2efIW2+leoeC9NguPD8gkUFcdz94VxVn4KaZAzMc11Vg82h6NJaAhW+Ybvr0rrp4b2UbNWSRDxLnU5r6tnGeIxbpcSW0bfcfA9a6nwpfRW2iiIseHP8hXGXejajfXrPbQtMx5ODyfepLK6awie3uw8UyOQyOCCOlZpaalufvaO5n6bo815Iu4YXNdpd6RBbaTtRBvx2pLFUFwVjAwK073m0ZT6Vhe47HnaxGGXpXV+G9KutWu1hj+RAN0j9kHr9fQVhLG8+opbwoXkkfYijuSeK9j0PTI9H02O1TDSH5pZB/G/+A6Ct6NJ1Ja7EVKnIi9BaQWNqsEC4UdSerH1J7mpBxSv0zTQelevBJRsjx6rbmdn4d1QafCIpwRC+Dux90/4V0N5rVnaWxl8wS8cLHyTXFS3gtLFSykjA6VROvQ9PLauWrh1OXMdtOq4xsbMVzLfNNdyoUaZycEdB0FU9SijghUEjDHFS3eoCLR/MVSOM1yt5qj3UYVm6VNSE+aKjsjoozp8kubdjdRiS3ZWU5DGqHzMcgUea0rhXJOOma0ra0kuCI4Imkf0Ufz9K6krLU4ZPXQxnZlfqRXc6DpxsbNbm4B+0yDKqf8Almp/qf0qtY+FJRdQ3F48SqjhjD94t6c9OtXptTL3XlpBvUtje0mPxwBSclv0MXzT9yBNNP1646nFc9ExhuJridRlycDPI5746VelnuLlG8oIqgE5KH8uvWsO6UtGTIzN8xGCAFz9PxqfaRn7qLpYeVH3mXJZjMPMxjdyMenrVffKrZXn6VeihVrC2ZRgCMDimiBc5BXFZzhKL0WhvSxNKS96VmZ89xciB2wBxyT3p2nx4jWUFvMJyzA9fXNO1MKtv1BJIHWprYGKEFiERRyx61LUnG1rFvEUacua90c943sHvdImlhT/AE1IyqAdWTuv1xkj8q8jjhAtJYUPyPhwh7MO4/CvUL7W5dSv2jtiI4Ym+QclmP8AeI/xriPENoltqpjgRfLuQJkUDIUHqPwYEVxWindHV7SU1qrC6VPY6rALfW45WuI1Cw3STbWwOitnIPscZraXww9rf2eqaFqUMtwsqSRw3S7WLg5xkZDfkK4xYET5SoLd+Oley+ANDisNNi1CaBVuZ1yOMFIz0A9z3/Ct6dNVVyyRyYiusMlJddkcfrPhvxfrmvXN/q2jyK8mGLIAIQoHA35PAA9zWZZyR2Wq2sKSQztFKu+4jL7SpI+QKQBlSOuOc17+Zlt08+eQKfU/w/SsrXdHtPFFiYZ7a4jkDeZFdLtV1YDg7f4hz0NL6m4Ncj0XQx/tBVIuM1q+piQz4M8m75T8qn3xj+ta0LYd5G5VBgD1PpXOjTruw1fy7xiIQNxb+BxnII9DnHFawlknVQuYoc8cfM3+H413nzlNyjpLc0VvEtggkYF2OWHU/lWhBPFNjkqT0Vhgn8DWVCqQ9F5PVj1P41aRx5iMQuVOQSOlY1qSqRsetg8VOjO99Oo3VPD+l6kn+k2URb/nog2P+YqnplpLo9y1thpIUiBimJ5ZemD7iugJDLVW+ytjKwHzIpIrhw1ozufSYmpOdLlvdLU8O8W+K2uLu6iQ7fLlI69cGqI8Qi9WEbcMvJJ9a5TUHd9SumbO4zOSPxNPslfeGzxWsK1pHNKF42PTtO1ABFyaZ4klaXT/ADLcZkHYd6wbOZmCqDzXTaNewWkzSXf3QnBIzg121HzwdjkguWaOd8Pa4dNJe5tjKOjgfeHvVrU9T0rUbv7QYIZAVAVnAyR71vaRaaXrM93c+Uvl84UHB4rzrVkhi1a6jt2HlLIQp9a81XSuzt0bsdNpUYCM55Y1fuXDQsvrVLT9hXKyBsnpmrzkPnbyegHrWMoSg7SRompbD/AmhNLqE+rTJ8sRMUBx/EfvH8Bx+Jr0X7MRzVTTLYafp0FqAMovzH1bqf1rTV+K9KnFwgkc8kpSbEFsskeM81H/AGfKgDn7tBZ0kBB4zzWvdXSR6f2zitlNrQn6tGScpdDFvboiNY+q/WspVWa7jHZmAqZmDMS1Nsk36nCF5G7NVsc9+hu+IWSHTEiB5Ncbg7+ea6PxNN++hj9BmqOi6X/auoCN3VYU+aT5sEj0X3pRel2KdkzR0Tw0bwJeXJAgxkKTjefT6V11qLeCARwRLEq8FFHQ0jSpFGsUYURqAqBemPSqEk/lXAb+FuDQouW5w1ql3dFnU7vybGWQfwqSPrXJWkxeVzn7kLH8Thf61s6u5k06RB1LKP1rHtoJbe/NqVV1kwHbkZUEEkVFVpRsdWDjf3vMnUAQSnd8rgK3yHI5zxzWXfELDAB3Zm/X/wCtV6a6kVJSmGCSFD87DAHtmqN0TJHC7BVIyFVTnjrk+/P8qwp35rv+tDtqWasjo7e38uzhAPSNeD9KY1rGxyUA+lW4zlEH+yBipCAOK7rnztru5zWqwqr20KABnk5+grP8R3y6ZpMsjMTNINkSehPf8Bmr3iK6FvrejJn/AFsroPc4/wDr1x/jG4WfXILJzIY4IsgRkZaVumc9B0/CuTETsmzvw9LnlCHz/E5eS7a0hf58ySfwj+VR3fmS6VDO53ywMYgcchWG4D8w351cbw9qIl+a2eU9NyEMPwI9a0IvDd9PaXMc4itEyh8ydwApU+nXoa89Tgtbnt8k9rHN6Rprahq1tARxLKqN36kFv0/nXvFuUj2DgIozj0A/yK8y8PQ2w8Q2wt4VjW3jKyESbhJIu7LL6A8ce1d6LkFcDnoMA8n2r08JrTcu585m9TlxEYdl+b/4Bpx/vpzcznJH3FPRB/jV6OXnPb/Pes6FcqDJjI6elWlJ6qMerHj+dbtHLTmLqkAvbBgEHnR/PETzyOo/KudtzyDkk9ST1ro9xzlVB/2mbP5CuZugYL2aNc4DHH061I66Wky8H5qRXwfrVFJCcZKj8c1IZGLYB6VLFBk2p+J7TRBaG+ScRTZQSxpuUMOxAOehz36GrNp4g0jWsw217DIXBVkVvmAI7qcH9K5/X7T+09DubQDdKAJYf+ui8gfiMj8a8heYiUOjFGVshgcEf4Vg8PGV2tGfQYXEuVNJ9DI1eznttavraYZmhndHx6gkVVt5zE+G6Dsa1tUupbi8a+nPmSToA7nqzAAEn3OAfesV+W3YPJrilFqTTO1NWOt0WYMpbtW4zb4XHqK5zQsC1LOQMVu2Go232pTI42L1r0ackoJHFOL5jP0+aWO5lsw6wg87jnOD7d6judBHnHEmaXxM0M9xHcaa7CU9Ch6itnw/YNd6Ws18z+cWORuxxXHy62Om+lzjYr2WEB0YgjmvQvC7xXjQXVwQEjHmOT7dP1xXHat4bksbE3VpfWuoWg+9Jb7lZPTcrAEfhmug8MRyN4aiByDNIR9VXj+ZP5UpVVKzvexrKhOnLlmmj021u7a7A8iUOevFXFGBXCxw6jogjmdJxZkjIZCB9Qa73TnivYI5VPyuoIrop1edak1IKLTTuhjDiqVxK4Gwsdta1za7PuHNYd0zh8OuPrW0Fd3IrVFyWK7ZZwB0NX9HhB1HPZVzUVjNBHIyTAZJ64rSs0jjvCIAXeToo605S6HIoq1zM18tPqYSNGdgOijJrptG0lNOsQzFXnlAZm9PamWekJHMbq6lYTOclFPAAOQCR15wa0JXPJz9SOc/WrS6HHXrX0RBM2AeMjuO9Upm3oRnPFWJJPz9fWqcpAyw/EVpY4mzP1a5K6Y2T825Qfzqtb69OYvJKqzMBuZgOv4cioNbkIgUjs4OOxqnaN9ruobdRtLsEG84ABPXNYVYqS1R6OCbjHRm7eixt3iWwnXAG2UDJy4/iBPrzWRI/mSud24DGDmuqvYle3lmltEaPYzBmRTgAHHP5GuZuI7eIJ5LgsR8wzn8a5aM1I9KtT5TrLU5QN2CipN2cmq9u+bSIL/dH8qdI5xtHeu5nzi0OS8eq6aZbalEMvY3SS59Fzgn+VcpZT2Wq+JNQuLiFJkc7rcSHCj5gATz0C5P4V3nioRnw1epIMiSMqB/L9f5Vx3grw9Obu1ubu1MlnubLumVY4I6e1cOKly6pXPVy9cy1/q4iWdi2qXohub9lMx8p4ACm3tx69R6VqWmnx2uvQ3guJpEWNg7XCbQh29SegPTn8a3dS1jS9HvHh+1wW0gAKx+SSQCODgD/PrUWl65ZvBdQI08ySIRlLdgoJByWz07dfSvNeIk1yxg9f67Hr8q3b2ItZ1vT71tPWG9t7i5DvtEbh2RChByR0BOOO+M03SELBJn5OMRr6k9T+VebWshttWt7h2CLlRtPUqTtz+td74cvRJbmJj+8jcpz2FevgdKXL5ny2c028WpvsvzZ1cfBB6tVlRkgsM+g6/pVSJ1AAzx+ZNedav8RYY9We1vGuoLfGVNr94jJxk57j0rTE4hUUtLt9DXLMuli3KTlyxja7332SXV6P7tz064uordS1xLDGB/z0bFctquo6fd3yzRXkbZTawSJm5HTjHpXI/8Jx4URd8dncSy/wB6Ybj+prPvPiLGv/HrZMufuh+mK8ueMxM37sUvx/y/I+gjluXQjafNP5qK+5Xf4nZrqIXAjtbuUj1jCf1qa11zTrqUQ20m2fOGWSVHBb0yvQ8dCK8e1PxpquoRmMTeRGe0XynH161Q8O3DW+uWzKxXJwcd+4/UCpVbER9+cr26WRrHBZfWtQhR5XLRPmldN7PVtP7j6BDu0vCJkDk46V5V400oabrsskf/AB73amZPRTn5l/Pn6GvRoL+aQkNZxBj8xC3Qzj6VneKNPstb0JnjkDT2jeb5YfJC4w2CPbnHtXq1JcsHM+cy5uWIVK9m9Ne//DnkUv72zcd0IYf1qzo1jb6lfIko+VBnbuxmny2DRykRtuB4Knrj2qGMx6WBIrAynsa5qajiJc0Xotz6DEUKuG92otXsWtfMdkxggO1eRkHqO1UNIlgXUYBdt/o5PzA8j8akXVVmaR50y54BC/pVvwzp8ep6uIShKKMmsqvvTtFmcPdjqbWnrp1z4mzbInllR91NoJHfFdwLWBRgJx7VXs/D1pZSiSGMBvXFaRhJranHkjYxm+Z3PFfD95KtxLbFyY5U5TscV7zEmn3Gnx/2dp0cElvGBGi4+8Pf65rxrSD4bfVYJ4jd27xkuUYh1IAyRyPb1rudC1+xtQRDqAk5JAmTBUnr0NefSlGNXmlome7Xw9Spho04NScb7NPR2+fc3JPG+ogy6Xd6XG8eNpcN1/CtbQmDacuwbdpwB6VzU0vnymUtG2T1j6Vv+Hm/cSrnoa9Wm7yufP1E4rlas0bDlic5rI1PIIJx+FbSRPM+1Bk/oKvw2dvblXdRJMOjMOn0rpXkc05qO5zWn6HdXiLMdsMR6M4JJ+gH/wBaugstNt9NYyRF5JCMb2PQewq4UuJTkIfqxxSrZPnLyAeyjNGnU5ZTqS0Ww4SpIzx/aYxJHCJmj5LBCcA4HqeBTnsU8uSRpJAEhSXcqAbt+cDk9eO9OFtagysIUaWSJYpJNx3FVOQODxyP51YklMsbxskZRwoZdgwQvQfhWDdVv3dEdMYUEveTbM02tq7Tp5s5aG3jmb5VABf7q9eD7/Wll0WJFlDvMGSKNvvJtZnJAUH8OvTFXmlZvM3BD5oAfKAhgPXjmnPcu6MsnlspxuDRqQcdM8dqlqt/MUlhv5P6+85zVPB3nRNN9vKeVLHEY3iB3O2DgENjqwGa5PUIfsurPZs4kNs5jZwOGIPOPavTjcK0rgpGXLrOxXIy38LZBHp+Nc5c+FIJ7qW4S6lWSVy7B1DDJOfanT9p9plydKKtFWOWtFeS48lZGQS8MFbGR6fpVx7C0hspX+1RtOpGEQg45+7weat3PhTUI/mt3hlPsxQ/rVO80W+s4hNNLu2Y3DZ0B4yD3oaae5pGUWu5tabMGsIm77cflxUztlhWXo86i1bcc7XP+NSahqC2VjNdN/APlX1PYfnWzfU8WSfO4LuYPii5k1DUIdMgjMqgguqnv2/LrVV9fm8MoLazmKykErDLyAPXafel0ESyXhuTJiUku8hGcDGTWne+HpNbhFzeW/mwoMxjftdVx2xxn65rz61dR36n0OFwjULJ2t+Zzxe81x7aW+ig3wAgSeXtZwTn5vWuwsPEK6ba/Z47G3Rj2hUIpJ4yRWJHYJpkywIuUADL/DvHvj9a2hHGYGli2JExBMyEJj168/hWypw5UrEuU1Jnhmu6vf6rrVzd3U2+WJvvdgQeOPQYGBXSeH/EKPcQXAIBkYRyKOz9B+ef1rl760mnvL6KwgnuSJX3mOMsB8x646VtWthpng6ygv8AWEkudRmAeO1SXaEGcgnHWuaniFQepVXLZY5aaW6vZer/ACPY7dioG8gMeK8S1zwtq+parJLZ2U8vCr9wqvfJ3HA7frXeaPquoa9CLiO6htInHCxRb2HOPvNWN4s0DxLc3Lf2de3d7b+u/kcdCB/Qc1WK9vV5ZxhZLu+9uiv2KytYHCxqYedbmcrPRWV430vK3ft0OVj8FS2rB9U1bT7JV5KmTzG+mF4/WqOrXlkLn7NFtvoEdSJuY9wwMgAdO4p9x4P8Qo2ZrGfPq6t/UVXHhfWM4Fq+fxrljKUX70vwPSq0lONqNJrzvf8AKyM68uIZ5AYLSO2RRgKrFs+5J6mpdHGdXtf+ugq6PCmqlsNEqn0JOf5VraH4UvIb9J59qqn5DPGef6USfPFxjq2ZU4fV6kalf3Yppu7S2/rY9IZf9Hil2I7qi4OOQcdj1BqvvhuUkijZLaeRGjweNxIIx6ZqOecqCVPAHY9q53Wr5YYhLkjY4fPsOf8A61ezNJQsz4bD1JzxKnDvf8bmJISCrfgayNbTy7mOYD5ZE7eo/wAitGLUItRR2EbRMWLEdRyc8VDqcBmsHVRuMbBl/lXztJuE7H6tjYxxGGc4+qMmDFwyw7sFjXq3gvw8mk2rTyHMsvOT2HpXmGmWTx3sU0iHahzivTLTxAzxKoUgAV6VNa3Z8rN6WR1jSIKYZ0B6isW3vHu5hGpxnvWyukF1B+0kfhW9zJRbPK/DmnWUVjdajPbvMigIYo2Jbax+Y/kOg611llaaai+ZYx5il5KuucE/UUUVzqKUrHTKbkrss6Whu7j7Ba28hkUH5tuFwHwMsfrjJrsvDGmXLvOHjZVD7CcZyQcHHr0oorow8VDRGGNrSqfvJb6I7eCwEMQT7i+g5J+pqQRJH91QD696KK1UmzzbIax6knH1qJijqVJ3AjBA70UVaLjFPUbBEkMKRJvZUUKvmOWIA6DNS4A5bv0Vf1oopPTRGttbkiQq4JwRgjIPvVhbeF+DEh+mRRRWUmy1FPcRNKtI1Plr5I77SMfr/jUUlmiZ2XduxH8LOFP86KKxdacdjf2EJasrEFWIOMj0OaXIIwRxRRXbF3SZ58opSaON8XXS6LHFcW9pbyGVjmMMUZwODjAxnJA71k3thqPiTT1ks7aVPs7ES20xAfePQ9GH+NFFZRvLmTZtOnCElNLU7GPw/Z6XozLJCMx26webF8kksrDc53/3QOOh6cU57G6t4HtbV0uGhVVb+F0yOMjoT24PXPFFFcEopu7PTjJpHMa0jRX0CsSXWH5ievWsqOZ5vKtizCIfOwGM4B7UUV6FL+GmcVX4xdM8My6mksRaSKAeYBHGiKmGbOSMnJ4HPWud8aaLGZJEvmeR3URwkOoEZHQgd/fmiivKaXOehGclTcU9Gc18P9XFnfvpty20Fi6Z7ED5h+mfwr2OxkV/mjwQT8uf50UV7OEk3T16HzOOpxjiHbqrl9pAnV2Le2f6VCbxVf70gPuSP50UV2MwSRk+JGJt47oZLA+Wxz+Iz+tcleTi2jEpYKCRk+mf/r0UVzt6M5MRTj7ePnYwdQvnbeqxsT9OK5nVr57i3gsuQVJeTj8h/M/jRRXDiZNRZ7uV0YOolYhsAY3wOlaUsrQTQyr03BSPXJ6flmiivGf8RH6BTVsFNdkdH/ZsSMQq8e9TxWoXoKKK9yyPjCzHEy8qSD65q0slwowJnH/AjRRQGx//2Q=="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color is the helmet?')=<b><span style='color: green;'>black</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 != 'purple' else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 'black' != 'purple' else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
