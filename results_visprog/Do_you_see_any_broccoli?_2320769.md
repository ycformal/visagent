Question: Do you see any broccoli?

Reference Answer: Yes, there is broccoli.

Image path: ./sampled_GQA/2320769.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='broccoli')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='broccoli')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADhASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwYw4GTTRE4G5RkVuJZ2ZCsTLKrSeWvAXJzjp6da3Es7eKOPy4YhvDYB+8NuBz/wB9DFc0q9uhsoXOLgm8u4UmONuxWUZXnjJ/PP4VCkbOcAZrotfMUEAj2oZH4HyjgVB4f8h5vLYATHO3OMH/AOvVqr7nPYnk96xXtYZsYijbPcj/ABrY0C1N3eSytzFGABk5Bb1/nUt55tzcjTrX5pn/ANYw6IK6fT9Mi06yjt4+ccu3qa5KtX3fNm0IagkQUdakUjOCVB9zVlIQeBXJ3cenf27qH9oSSqin5BF1ZuOK2y3AU8Y6jqzcVCN9FzPdLa67lVajppWW502V/vL+YprKgUszoAOpLCuEu5LUt/osEqIP+ejhifyHFQhWIBCnHrXoLJsvav8AWJf+C/8A7cweLkvs/j/wDsZtY02A48/zGHaIbv16VUm8SAriKxQg95mz+g/xrAjtw6/eGfT1q/YaHcX7FYInkZfv7SMD8a3WU5TTXNOvL5x/+2MniqsnaKIpdRuZ5TtEUQ9I0A/nVeZpWHMznPq1dBF4Iv2yXjA9vMGaefA19s+WLLf9dVppZHD/AJiP/JV/8kK2If2Wc5FnyhvjHuxOSad5YDkFOOuK328D6gEYrbuSMYBdeaa/g67RTutrnI/ujcK1hLJm/dxX/kq/+SIca3WJjFUV9pAYnp7U/wAlHjzgHPXnoa0G8LTooYw3PTkeWc/ypo0K3V8SmWMf7RwR+YreNLLJfDXb/wC3f/tiHzrdFPylJCqQT37U8WyBCQwHtVptBtw2A0nPTkHNRLo9vkgiXg4znGf0qvq+X/8AP6X/AIB/9sF5diBvMt3DQzYYdieaki1PUYgNl9IyDsTuH60g0dQ5Dhkx/eYcion0+BSVG/djK5YYNS8Flst6rf8A25/9sNVai2/M1YPEV8gAlit5weMkbSPfIq5B4ks2Yi4tHXHdCGH9K5xtM2svD4Zc/jV0eG3+zNK7FGClgpOc8fpXFXy3Joq86zX/AG5/9sb069d/CrnWWmpaLcDJuEIH/LMJ8x9sVvaZqBt83RiS3tIwSkG8b5G7FvQDJ4ryl9M2AFg44zg9apSpHHIBhsYz1p0OG8HiZ+zw9eTf+Bf/ACaKeNkvij+J3viDUEvI1VI4U+cs7IOSawFlj6GsiGTTtuJ4Lgn+8kg5/AilZ9L/AIYbr8XX/CuyPBrh7vNP/wAAj/8ALA+uX10+/wD4Br2/kR6rBLJGk8QzmNuh+taU2uRLC8Uem2Mb7shxED+HNctu0zH+qus/76/4U1G0/aQ8dxu7FXH8sVouEXbef/gEf/lhP1v0+/8A4B1U/iW8muDMZY/MdtzL5ShM4xgjoRjsayrrVLu7ZEumEscf3EwAqfRRwPyrFJtc8JLj3YUo+zHpHMf+BD/CrfCjSu5T/wDAF/8ALBfWfJff/wAA2Ydku9WO4GPZEHfCxHqMZ4wehHoSRyKmjtxcajZWUTQsCkaSyB22+Y3XkjIAyAcA9CeawQtvj/Uz/n/9aiUW/kjy4ZlcdWY8fyqqfCsZyUHOWvVwX/yYnibK9vx/4B0urRRaPcjypGaBwdokILIw4ZGxwcHoRwQRWYmqpK3zIuPY4qB5o7qwm3mTZGoCK2Dl+2PTv+VO0zTba5b97drCcZG4GvksZhZYWrKnWjaS6fj+R1U5cy90tG5ibojfnUTSx5+6/wCVQTKsTtHnIB9KjDHHByPXNcqiimyKzjBXSosfM5aU+3PFa0Ss10T5mf3WRkdNzt/RRWerC21KJTk+TbhEUclmA6D8Wror23j07WLm0yf9HggR2IICkRgsOenLGtZ/C3/W4o72OY1fS5Lq5jCAtMeDjoBVuPRpzYfZlgQZYHPA2++eua3IponeNBuLPyFxzj1PoK0Y4wBknAHOT2rF1pJJdi1BXuVtI0qDT4AsafOeXfqSfrVjUdQtNNj3XEmGxkRryx/CsXU/E6xE2+nkFuhmxwP93/H/APXXOvE8ztM7mWQnOWOc1tRwk6r5qmi/EznWUNImpe+ILy7BWA+RD3CH5iPc1jp80mSpLHp9asLDG3G4g46dcUsMYNxIqkMAOtfUZXRhToV1FfY/9uicFWo5NNirbCVinRupx0qUwLG+05yRtzUgj+f5VBYDO6rlnb3d1NGnllkJ2j5ck/QdT+FcdlFXZOr2Io4PMjVQnzj/AGcfiK7nwfAtvaSLIyq8spZFyMsAAOBUem+FZpF33hETcBQPmYfh0H611NvZQQeWiIg8pcJwMgd8V8xn2YQVH2UN3+h6GDw8lLnY4RjcBt4Pf0pY2heWSJHBePG8DtnpU2KgS1jS+e7GfNeMRk54wORxXxt073PVt2LAjHpxQQqjJwB6mnrLsyMZyKqahEl1E0ZO09iOxqIq7sxtO2haAVlBBBB6Ed6rXFnDckeZFG7DoXUH+dMsh9ltEhZ9zAct0BPfA7VYEmeRnA5zXRh5VKdZSp62IlHmj7xT/sqJXDC2h3A5B8sZFV59JtWyHtIiRzgLg5P0roWmUKnnN5W/gADJJ/pVkWICFlttytz1yf1r6r6z/K9TkVPucb/ZCwy5FmpGOPMJI/WoLi1HnoWtEzkDYqfr713P2cbAm0p/stVZrSNZB82056N2zWLbm7yZoklokckvhu2u5Fma0RME4KEg57Zxx+FWJtHneJECxo3JLYyPYCuljtI4UKKWAGTjdmqskT8xxqyseC5b/JqpVJSsm7iUUtUcbeeG3uYPM8xFljzzj17VwGq6fLZavHbzKN7BTx3yTXscthcxRt5Uqk/3TXmvjL5PFtsSMYjjyf8AgRr63hPETWKnDpyS/I4cZSjy83W5Q+zK6blQg9OmPpT30n5tqnBUZdzwBxU2ptss4oUA824k2KfQseT+VWNblaC1wnDMPmr5upja9VrW17gqcYnN3Vo1tdxvbymV4yDtU4IA54NdFFrGkS2sBuZPKnkB3xiIkRke/cHtXPWCSJJ5hVFG75nYgk/h1/Gp7uO2M7FV2tgh1OQF47ev9K0m+ZqMm3bqEJuOx040uaHy7q0LIGXcjp6MP8DWLpkBM+pReXGxDhdxBymCeV7du+aNC8QNYapbxzXchsVHlOrHftU/d4PTnB47Vu+GVS41bXWTa6GcFSOQQWfkV6eB9pDAYzmf2Yf+lotyjOcGvP8AIzxbTxgjIYe+BWfqqSrYHcPl3jnH1ruprdBn92oP0rm/FC7dJPGP3i/1rHIKl8zof4l+ZeIj+6l6GLplgt7c3RmJ+Qj8zmn3envbtlc4HQireggm61D/AHl/rWtIqsCGGQa6uI6jWZz9If8ApESMPH90vn+ZyhRn6lCfrij7Of7w/Ota7s440aVZFRV5O48D8azEuo2GUkiceoYV5Cbaui2rbnSaV4akTxnZaZIoeWK3invZfRiTIyj3wUWq3im5DeKNUkJEge7byoh/EQAuT7Ar0rn9I8Vajp+uT6w0zTXcuSzPznp/gPwFa+iae5X+0Lxsyvl8txjPJY1012lGxFNNs0LC1FnbvPcuPNYb5ZGPT2rn9Y1qS/Y29uxS2HXPBf6/4f5BrOrm9kMMRItUPbq59T/T0+vSmkUnVVAXpV4bC6889yK1b7MSONEBwGGTzkirip5hAQqSeuc4pyK6neY1bHtV5UV4VkUEMB24FemkcjZXhgYOycscdcdPxqbTLWBrzUvM+9HGBGqn7xJA45/H8KuR28hUFgQf9nnI/wA96f4Zt4LnxDfeaWZVUEGNsZ5A6+ld+HqxpYbETfSH/t0RKLlJJF7wxpEN5qQEsbtDGC7KwyrHOAM969It9PtI8mOBI3YBSyDBwO309qp2FsigPHhUIwEVQAAOla6DAr8rzPNa9XEOUZWS0se3Qw8YQtYhNm0Y3RASHP3S201WSyuZL1p2gKhEKJyDkE5J/QVqA9qmU45rzauOqVbe06G6pqOxlPDOgy0L4+lV2l2nBGPqK6AMTVe8SKeB0kA6Eg9wawVWN7WNEzCNyAc0hcXB2xZaUn7oHSq+m2sl9MCVPl98HGa7a10m1ijRiNpXpjjB9q9ihgefV6IipUUTmrPTHuJ/LZixB5EfUVtQaOlvgzckDOeoFadpYR2Y2pcTlc8K53fhnFWpI1dGGAxI+63evSpUVCNrHPKo2zO8pLcbtrMeuSMn606O4icZV/m7ipYknSPLKiAfwglhj61HJbw6pZyIQVLAoxXqKuL7Cb0HFQ47EVmSSRPfune3wT3zxn9OKr2s8OgD+yzI0siguGbpg1hvqkdpPqN9JGXS4fam0gbuBnr1HGKh1Fp+ILRczNt52mvFjS2leIx7hKBxn0rC1251yyhxF9nEe/8A1iL8w9iD/OuittX+26dHLaCMyN8pSRtoB79P6VWK6hf7oby0WBCRtlilDYwc9PSkp3V0TL3lZFSCU3UWZIcSBFdgDyM/56V5V8Qv3PiiNnXAECMQfTJr1Gxs9WtWvHYWzu0x7HMi9iT2OK8t+JJMviUA4LG2QEDnBy3FfW8HNvGzUv5J/kc2Lb9mr90WPscd2LAqxwk4lDD0AyRn8qo6tO01yYVdU3H5pCudo+nc/wBa09NWSy0VDIfmVFXaepYjp+lZmoXCWlqbgYZpif3g6Z9vXHrXzNO/tO/YUnoZl01raQH7Ooh3HO1j8ze59OlY8t5dXUrMkjkoP4PlAFR3Be5nxEjFm7ZyPz7VNZWphkbzsNCeCRxn6etetGEYRu9WYu7Bo2byWIT724scBq29D1u40a9lkiVWhkP7yNu+M4/HrVFbaNULtLwoyrD60223MzMPmGQTk817mV8tXBYqnJaWj/6UjObcZRaPVbK9tNWtRcWr5H8Sn7yH0Irn/GEWzRWP/TVf61zNnfXOm3a3Ns+wjqCeGHoRW/r+r2+r+FjJF8sqzJ5keeVPP6Vw5Vg5UM1w7WsedfmdMqyqUZLrYp6AD9s1E+jrn9a1p0wMiqHh1N17qvHSRf5tWu6cFfyqOJX/AMKc/SH/AKRE0w38JfP8zhfENzI0fl7iFJ5FcqRzXYeIrNgrED7p3D6VybJzWOHa5NDKotTpNE0w3syyyr/o6HJOMbz6D2rR8QaqQPsMB+VT+8x3P936Dv8AgK0ryddN04vGFVz8kS44B9foOtclGvmSBjk853E8n6+5qcNB1p88tkVVlyR5VuSIW2KFQnPqKvQiTMRlBCk/hUKRhJAQwGf4cVoovmtGx3fL94Kcg/hXrJHC2XLe2luZ1ggXe8hwFPp3rudL8OWdnbqtzEbl2PPBKr+HpWP4fjjjvSeAVjO1fTJGa7K3lIxXyWfZjXp1PYUnZW+bPSweHjKPPLUcdF04wSRrZwJvQruVBkCuL8OaV/xXet2ryZ8hByq7c8rjivQ4mDCuS8Ogf8LL8T/7g/8AQlrlyTE1nhMfzSbtS66/8vIHRXpxU6dl1/Rmpb6TexaqHkcmBTkMGxuHYfX2rUmvUgXBWRpOyqh5rSGKgulPlgrD5gBGVBwceor5eVd1ZLnR0KnyJ8pm6dPeTzyvcoEQgBFAPatbcO9ZtvqdpPO8EZZZU6o64NF3qUVshZ3AonCUp25bDg1y6O5eluFjB54rGuL0zsY1Yqh4LdKmSCe7AkkVlVj8kfdvc+grQh8Ou5Uz43McqijJ/HsK9HDYBq0pIHNIXRLTZEpbKqPuoBzXSQwL8rkEGM5wrHGff1/lVa30423RwzAYxjOPx4qZZng+WUYXqG7E17qVtDmk7l4Ebc9agmlCqcKCRVO71FYUZY2UlTg+xqks8pAcOMnlozx+tZ1MQr8qHGk7XZZmvGjIk25U4Dc9vWo0vLdTLJEfnYAMR0rO1G8jUQxk7pJJAojIOcnufTA61GpjjXaqgLnpXn4jGOi0tzohR50Zxgi1PUriZmkdQMHyxnvgD6cHOK5rU9P1OOWSIyI5VxwV5K/7I9K72GUbfKVvKXPVBjBqaXT4biHbMA4zkNjGD6j0ow9eNZe7uu5NeitpEGl2ph0i2ieKMukY3ADPzY5watDylbBDIT2auYgvb7StTeCSOQ2wc7X65WusgvIJlOWAPcGuynUUtHoZ8tloZWpbwjiGQo0mFJxnj29PrXiXimS2XxVH5CsY4hGrM3Jcg9a9o1q+t4gx++ijY2wZwW459ua8O19o4vEKuQTGuxiOpxnpX2PCK58dOEVdunM4sb/DTfdEuoXDwzJeSIw3DEahunHU+lY13cG6EanfsXOc+pqe+vxeJyzbt+duOO//ANatayvtAhgX7R9okl3q+BEMADqv3uc8V6VHJZ4XB051cHOpUbldJtWStbo97v7jjdRSk0pWRgho40AWJlQ9/WrEdza+WUMcpB6kAcGu7Tx7oqRqv2aUqONhgUhR7fN16Vk3HinSJ5Hb7JIpk+8wjUfp7/WsI4WtJ+9lVRf9xH/8iU5JbVF9xyLuX3AxYQnAOOev+FOt5xEztsJY/dOOldPPr2iSFkRLpYyhHCDOT35asbSnVbify5NqsQFZyAT1xx3PtXr4TkwuDxFXEYOVKNo7yevvLy0tuYzTlJJSuVZbpN2VR145J71Wd8ggZGeoraup3lTzI9pjKgZUZz6nms+6WQwh2GE4Cj0/GtcsxGDniqXJRabas+Zu3ysZyTSep0/g5/tM2qShdu5kbGc4zurbuI+fQ9q4DRtTl0q9E8fK9HUnAYeh/wA8da9FWWK9tUuYW3RyDI9R7H3HSvmOL6LpZrUa2923yikeng5qVJLqYOp2oubcsB8w6iuAu7CWG5ZEj3L1HtXqEi7WIPQ1i3WmbrhmRRg14dCtyaGtSFzF1+7E96YQ2Ei/dj6nlv6CqUEqRggBiD+FQOGmnyxJPUn1J5NXYk+Vi8YAAwOe9e7h6ahBROCrLmlcsWzrLIoChiB1Y/0qwsUilFKkc/KFOBim2touxXEvlnGQcVajeRU2O27tkqTu+ldPoYmxpsxt7mEhTtzkuSTx0NdzbtgDmvO7adlRjsATtnp9K7fR7sXtiko6glGGOjDg18nxLQ0hV+X+X6np5fPeJuxvxXL+HH/4uT4lJ7oP/QlroUJArl9AbHxD8Rn/AGR/6EtcGSx/2TH/APXr/wByQOuv8dP1/RnoStxxTtwqj5zZ9vSnC5x1NfKOmzqLDpEGMpChgOWwM4+tZ8egnUNVW4jbbCmCehXd6479uKuRQHUGWEkhZM9PQdTVvV7yXTvs1vYRnejDcoHUHjivZwGGdKPtqnyRjKTb5YlzRdFWzMjSNvbdwduPx9z71sxx4LN/EePwqla6rDNJHHhllfIAxnpV8ttycEV7dLkt7vQ5HdaDVj2Jjqx5JqG4RDEwlAK9wRUks6xgFmwD0qnNIZTk9OwpTmlotxxTepxupPLYavFHaQobKbEbiY8D1yT046VNfNc2Mcclq6XChCVDnBz257/1rS1JfslpLfLtkKYDIRkYJA4HfFYsXgK+cSsNR+w27OXji8suwB9eRge1ccYNtqx1uStdszbaa8vtVsLqUsAFcSKwwdwBBOPTkCobjxSFu54I7CeQwuUYo2ehxnpXRQ+GbfRCZ47y5ncAgmbb0PoAOK5jQ226trfP/Lf/ANmauGtGDnJyV7JfmezlkKbpTqTV7W8t3YcPFMikY0q7/wA/hVuDxvJGpRtJu2UjGAf5cVpSuSquGOMY61VnleMhgxAPPWsITp3uoa+rNpVMLNWdL/yZkFz48ggsUnuNGvFjjIImZuB267e9Yt58SNKmcG3tniXqRv6nueBVj4h6458B29lGFImnEUu7JIC/OCPxrm9P0/X/ALFbvH4S0a4jdFKSSRqSw28E/OOvWv0PL8ky+vlcMZjJW520v3kIKyt/MtXe58/XzCNKu4UaC078z/Jov3HjrTLq2a3ljk8tuSFfHv6VzDajo7+JorqWBp7LyiHSU5y2DjsOnFb0uj+IJ1JXwdoqbTyYwv8A8crBn0/U7fxLDBPotil0YdwtDgRsuDycN169+1e1k+V5PSdVUKu9Oaf76m9GtXpt6vRdTmxGPlVUW6UVquk/u1f/AASbxDq+mX+kxQafaCHy5VyV9MMADxXS2urfZLaOKPTmO3ruQHI/KvPr37RFPeRSQRRHzR5iR42owzgDB6da7H+0PFvX+zbXkf3h/wDF1ln+QQp4PD0KFWPKnJ+/USb5lB76J/LpZ9TbBYvDzq1J1qF9tI81la/q9fMlvtRE6MHtNjgko+Nu304H4VUj1NIIBDLFE7BD9443E9CfoaSe78USMJJNOtjtHIyCD9Rurm7m6urgjzLa2UxFiEAA25PPGfXmvAo5BUkre3pW8qsX+prWxmCpyusK/m5I2/tu/IkeFjgcBRj61lX1h9rnM5uI41B4GOBkflWZNKbyXesMKHAGyIbfxx70SzM8YgnyqoS23J+9jAyOx7V2xyDEQjKcKsHyptpSTdlq9EcrzDAN64b/AMmkXXs5bWNW85Nhb+FTgcHmkvCr2AcRkEsOf/rdqc7H+xYSp3/McnHUc5qkbn/QzBwRu3AkfN/+qujhytL6/SjJ/aX5mWc4ejTlF0Y8qlGMrXvur7sbbRtLuUICOMk9q6XwxqRtLttPmOIpWwuez9j+PT6gVztoVKyITgnGDnFODDbu53L1YHkD/PP4V6/FNFVcdVi/L/0lHmYafJZnotxH1qodv8XWptPvP7R0uKdiPN+7KB/eHX8+v41HInznpX5+04txZ7G6ujhIUyzNGMsH9e1T26StIVKnDHoehrOheTayrnLHkitm084kAYDnk7s19bBWR48ty7bRNGBbuwAI4KnFX47aGSIJuaXZ1ye9V44yhx5e5jyZAec/jVpZIgAWbaSfmGM9sZqtyCGK3aOUCT7kZxwf511Ohbo7FSp/5ayA+h+Y1gWN1bxtIrRFlJO0gZ4/wrqPD8Ky6fMY8HZO3AOeCAR/WvJzmk50lddTswcrTNbz0jA8z5Q3Q9q5nw/Kq/ELxC4YYKDHvytdHfwGTTzxypBrhNKDjxfrAViCFH8xXl5bhYww+OUetJf+lwO+pO8qd+/6M9HaUMS27n0B4/KpbGAXl15ZY7FUu2OuBXLmW64+cnHSt/wk0zXF99oIW38jDydNpzxz+dfOYfCp1FzbHTOVo6HT6dLE97LDAAzRqN5C8Kf7oPtUg0+eO5nlnkWeGT5lyvzIatWNvbxRl4RjfySD1NWmG0fI5B9xmva9ndJyOXmaZWs7G3SV7pCHdl2qQeFH+Jq7uwMk4qoWdXX96oT+6q4rlfFmu31jcRQWRKIy72kXk5z09hSdSMI7WJlpqzrpzE64kx7YrMknEjmCJgWJ2DnvWDo02oayv79mDg8tyBt9fc+wp0mtTWFr5EYt+XySyZIPr+lctSslZyVkzTmjBJnVWemQwN5swSWUfdyMhP8A69Wrlv3Z5561k6RdSXVuksksZVgTlc4z6c1aebzJDyNq88HrXTCUfZpRVrku7d2Zt2fMR0YY7V59oYxqutK5wfP/APZmr0pfPePzGiCnecBj27GvN9Pjc6zr8oYDZcncPXLPXn16NoTfp+Z7+W1P3FZeS/8ASka5mC5U9OvNVLycMgA+lRy3APB61TlkyvWuKFLW47Lc5fxvKW061TPHnE4/4DWt4a8Qm4gg01nk8yNFMZXOMbehrD8YnfaWqjqZSB+VZk2l61p1hYThlijvZMQvFNhmIwADg8Yr9OwuU080yPCYWVSMJc1Rq7167Lrbr5HzmMquniakrX0R6omp+RGEUNvO7e5GMEdv1xXH6kHv/iHbKzSLutOqdcbWNYt1ofie1gkmmu5PLibbkXZbkntzWZLp2sR6tDbSNL9seMOh8wkhME9ewxmnkvDWCw8q06eOpycqc46dLr4nrsupxzxM7xfK1ZpjtbhaDUtUjAYqlyqlief4q7e117TpogGm8s9AXU/zrgLqzuUtZbq5nLs8gBy+4ucHk/l+tdhcT6FpENhYSvho1W4ffCZDl0U8H16fyrq4pwSxmGwtPCXrOPMvcV9owTfXql95vgMb7GU5TW/+bf6muZEmQmKRJFPUowNcr4g02KKKW5VDg8OF64z0+nerlx4k0d43CBM/wkwYb9Kzr3xDDJa+XBM7Z4ZZI8gj0r5TDcP5vCaaw81/26/8jsrZjh6seWRzxnhgYMqb0Hzfdz+JqASLcgyRgQYUkkHrj60OzRgpEEKMckc8fnTZJJCC0aKrfwqOgFfYZTlONpyqudKSvTmldPdrRHi1JxurPqakmyHQrZUk3gtwwHAJzn/CqMpbaA3U4PByBU73sa6ZBESRKJMnPbr3FVTcBg0YRQWIJOOePfuK87J8LXw+aUoVoOL5k9dHuepm1WnVUHB3tCK07paomtU37l5wcZwMmpnRVOVDOpPJPapNIJDSgY5A5qe6eYJym099uCMete7xD/yMany/9JR4tPY1fCdzsnmtSSUlXKn/AGl/xX+VdDInz1wml3b2+oxTn7qyoxOMZGdp/Rq9BkT5z7V8HmFPkrX7nr4eXNA83tYQV+bIAOOnetW3BQAo+fQZrPXAuGw4X5ifwPI/nVhdu7YrESYHI44FfRQ1R5ktGb0VwGjIxuI4YnjFNMD3B3RDcSOB0GKqWxjAw/UrxubnFWYysU26MuIgu3IzWsVbYhl6COC2VDNHiQDbtUZwTXU+GriL7UYlOGnToQB8yfT2J/KuchtUUbngHIwAeWJ71s6bO8WCqYZSJEA6Kw9fr0/GubF0/aU2jWjLlmmdqIo2jO5evBrz/SNNab4h+I4YFyI1BwfTK130U8dxapNGfkkAYZ7e31HSuV8KH/i6Hif/AHF/9CWuXLaaeHxaf8n/ALfE7qkveg13/Rl57CWM4aJh+Fa+kM0FhdRheTJGwB6dcZrolUMOlRThS5iBC/Jlvcf5FfPzw6hBtHRGpdq5FA9xHGC3c9FFXC8jJsD4PvziqULJGHkZmLY2jJ4/L/PSlimRCdnzt261yQfLZNmslfUkl0+6lXDXYXPICrz9DUUen2rSbrxBI6jAWTn8aswzeWrM5beRwCM4qBzI8hICu/AwzYwM9ap8u9tRWb0Zdt7W2t7fyYE8uPJOAemfrzWBqOlIL8zvg2u8Ns53M3oAOg963zISrbl2kjkA1EJmCBgeCOhHP40VFGUUn0I5E9wtJxHAkf2bYuMAe3vVhjFEApQBevHrVSaZZY3CuI5COpHX8fSqKzMyMq3OSnDqOoP+e9Cm9lr9xXJ8hNS1xLecqoDDscn8a4jQ7u0Fz4gubtV2NOpAPuzdPWumvYLOeFRdmIyDn5SS4/KvPE1Cz0y41OVotzCX9wrcYwT/APWqOWU079T1sHaOFr27R/8ASkVNITxV4lgmuLCayEUUpjPm7UOcZ6Y9DV9/DfjcLgy6cfYOv+FZngLWTa/bLPfh5mMka9iwHP6fyrt11K9mEhMbIsa7mIH6Y7/hX0Wf5lPL8xq4ajhqPJFq16avsvPueDSnUnTUnUlf1PNfEWna5afZV1GS2bdLiPymBw3viibU7y5hsbK+eMiwvxEgVQMc/Nz35Fb3xAgMVtp1wHJ3z85GCDiuL88PfGSQ8teB2J6deea+1yCrHMMuo150oKS57csbWd7O3a637nn15SU2nJvbdnsPkQ3di1uGJnhcvkMcnOeozyMcYrjNZiZPHdoiNIj/AGIfc+991hj64qXVNbi0+5+3WeoWzERNGYlkEhkOcjpnA69fYe4xJdetbvxPb6jOfLjFuVbbk4OGx79xXwvDmV4yM679nJqVKolo92tvn0N61SLS9UX/ABhpDWeiRXjgO01zgyKvAXDbQT3OB244qbSIY5vG0K3IW4VdNRjuUN0jXsfSq3izxDpupeH7WwsriSRopVbDIw4CkdT9arWmvWdt4nhvTOWiWySEybG4YIAeOvUV9Tl+X5gsjdOVKSny1lblaevJy6W62072MJyh7W6emh0Ul1ZNKypDamIli5WBd2M8duOKqz2NhcKVtvLUBSyr5a8e/TOail8U6TNIzTSCVkk/dERMAy9sjsR7flWLdazBd3LK1x5UBAy0aNuLev8AnOa+SpZNnN/4NRfKX+Rs6lPui7eW0c0GxYY/LjGcCMAt7npXIzBop2B8ssoOSvI6d8962pdZQ/OZfMYAAfKRk9Mmsm4kiluN8apGNucKnBbnr9fWvpsiy/M6TrKrTmk6c7XT3t+Zz1JQdrPqUJmzBlJSB3YDGRToSxTLbMnuo5pskZliw3Bzk0sMRiVRnOBjFe8sBinmOFqOnK0Y07uz0sle78upPNHkav3NGzyIZiH2kYPXk9an3ysC2QznueSPwqPToUlSYyLkLjnOMdatzxRNGFR4xjlXB5rm4hf/AAo1Pl/6SiIbGcEdS2RjKPx6HGf6V6TbyCe1hlP8cat+YFectkSAEg/K3J642mu90lt2jWJP/PBf5V8Xmq+FnpYR6M4MN8kRBB3DaT6Ff/rEflV62jQS5Z0Qk570y7sxa6ldWbLwT50Xv3x+WRUsYMyL5SqF/hwf1r1sPNSiclWNmaUSmZFCREZO38PXHatOKExjCSrlAQofnGaoW0rRhYBnzOpY9KnS1mDBywIJy2TwK6DEvNBLuiAuCXz8pPGavJaSbSZJWcheAh2jNZQifcSsmTjhjngeoqaykmjnkBQs64BLHIFVZ2A6vQdQABtpiQsjZG7+B/8AA/z+tU/C52/E7xMD/cH/AKEtZrpvuY1csE+6VVfvD/PepPBlwv8AwsDXBNKTJJGFUseWIK9/XApUaCjRxU49Yf8At8TohUu4xff9D1iF+Ky766a01KRnB2MFKn1GMVbhfb3rO8SGRLWC4jBOxirccAHpXyeI1pN9j0Kfxlme5a4tikQ3SYyFOBmktowJN0zTZ7x+WV5rC0+9jnkRHJVwwB9ql1fWpEXyDORIyYWKMY289WNebo3d6nVZrRHSpcKFw0nlx9gTgmopriLcWjkw/GF7NXGSatP5Eccm1znK+uR3qWw1LMgacyO3VhnJJrPETnCJUIJs6iKdrh3aQmNf4SVIJp0shTIVmKjrWedRjuIhi3fd13N8oqldP5gZlVtw+6DIcCuZ4ine1zZUJvoaDXDRk7GyD0ANZ19cTToVEwijHMjlguB9e1YN5d6lYoXjj3DGV8s5/nXH6lPc3TtLdGViOcFTgV1UIxntsTOnKKuzotU8V29nHJb6diVwpDXGflU+3qa4LVbxmWCaT78uWYkc84Jpty8s1sxWIosYzljzVZ7S5ntYZPNaXdwE9M8V9Tl+U0p0PrNWqqcVLl1Tetr9EzKGKnGjWpxi3dJ300tJd/u0ILO8ns5jJbztEzKULKOcHrXR6F4rewvYvtV1LJbkFZN4LHHY/hVK38L3LQtJNI0IVd3EZYD2J7GhfDs0lqkjXQVn3YjKc4Hf8a+jzB8M4+rOrWq6y3tzdv8Ar2zxYOvCNkv6+81vFPiPS9Tt7JLFnJhuBIwZW4GPc1z0c63N3dBbH7UskplCoWXAyew+oplxaPFHAHnbmTYFaMjb05z0NXbXRWfW7uxi1HaI4yxnRDhxx79Of0r2cHHKsHlvLh6j5VGTTbnspq7vGMZaNraz9Vcwk5yndoktrQyO5XwvPMg7B5PlH1FNlihhYyS+GZkj2dDNIAPfOKfcX+q2UYVNenkxKI9iSnBAHB6/Sujltf7Ps5JNQ1GATbiywO5cPyewwfpjjNeDmOdzwcKdaL541LpWqV18Nr6OS79jSFPmuu3kjir62kMazJpUltGx+VgWYHPQZNUjbzCQRmJw5GduOa6+/nt7C2WeLmAEDyWYYdzzlu544rmpro3F/JcWqJECuQjuQAPTNejkvFmIrU6sVTSUIykrylJ3VtG5Nvr3M6lFKzvuVhbTFygicsvUY6VGylSdwI+tXY3eWBZbiPywQcFwMfUCobm9eORXkdZACNo2gAE+3pxUx44xbdvZR+9h9XXcjERaHevLZwR2FR8Z54x19jUU0pXYoO0buSDg0+1R3IXA3Mehr0p5tjlmGJoqp7sYyaVlo0tOhPJHlTJFUlsYJPoKlmtJIYw7Dg9farVlaFNQeGVdrIucA9On+NS3zYsmRTkBwGz1rohmWMeMoU3PSShdWWt1r06mbSs9AjhQWwhj5Yklyy4I9P8APvTztiR2BBJ45H8qdId4jLKVG0DI5Jpjvst/LXLEnGfTnrXyeJqzq1JTm7ts0iVpcKGdQ2BE/B5HTA/nXbaSwGl26H+BAv6VxGyR96Pjc5WMY9zk/wAhXTwz+WrKDxmvncz1aSPSwqsrh4hs5JEgvbdczRMBx3B/+visqBjFcEBWVGyQmOVYHDKfof6V1uxZ4WiflWGDXHXVu1nqElnM22OY74pSfut05/kfzqsvr6cr6CxNO+pfS7gguAypmQjbgnpWjBcPNdRhioRVOSRjmsSxtFZwkv30OHVs5B9Ku7o47tDC6thcc85r3VZ7HnO6N8ttZhkMoUfKBxkU61j8yRLnGyRuqZ/rVUk/Z/NJMeMDBA5FPEcpcR29wFV1yKEBfubgNKI1dTgZL5+7XP6Tuk8XakYW25xwe4yPStd7UtA+4b5M4OMZrL0XfF4u1MRgZCgYLY7ivRwSXsK6/u/+3RJb1R6ZpusMv7q7bIXA83B/8e/x/Ot5pQ8ZRsFWGCPUVwcnnxzLMsoj2j5j2I96W18TNbOY2gMkQbAVWwD7r6fTp9K+Yr4GXxUvuO6niFtMuanpc0LvKVAUfcdW6j0IrH1BjPFHMF+YDk5rrZZ4NVtCLe5CSbSPmGSM+o/rXOa5bX1tEiQWyvHtwXXlRjvx/Wvm69CcZOyPVpTTSE061fU4t+4KiMAWxyD6CtyOCK2XbGAM9T3Jrk/Ds7adfSNMxaO4wJB2B7H8P5V1zDjJxj3714+NlPn5W9DvoKO5JvBTjrVdpI9wU7txBOccVIr7eSSB3zVWVgSSvIrijHU7EKVWQ7XXI9AcVnahpiTMxiQDj0q8khB+YU25L7/MX5lHVe1bwlKMtDOpfocFrdi9tYXIdSpCEnIqlpFjcXtjD9mClkIJ3HAxmut8VSLP4fuWkixIIiA4P6GuJspp7eygktn2yBSBlsA/WvtsLOdTIH0ftf8A2w4pPWs/7i/9LidpHJexMbV7ZnkI++i4UioTcLFG/m8yH5WQdvTn0/xqs2oXlloJfVbkSTS/JCI/+WY6k5HoefSsG18RLE7LPF53ACvgEk9cDPUV4VPDyndxX3dTxXOzKniEk3ETrvCO5ILdOPSsu6uJvtsjrcMSRtLq3JGMY4/Cujv9RttUYpco2xVZ4kdsEkd+P88VylxJDHMTtAjyBhDn9a/RchxOFrZfLD1lJSpwneyTVpSi9Nd9F0tucVRNSuu5bm8oWSL5gMscm0Ec8bQT+R6fjVyBo5tbluJrmF8JjzJMZdunf+lYKzCWZyFCqOiZzUf205KC2UnjoTkY6/nWuKw2XPAUFKU7e/bSN9XG9/e+6zGnPme3Q6DVGsp7hIhPgDlnjXcPpWXORuZYiQoG0E88U6G/tJbQRCxH2o/LvMpC9Tz169vwpnlXF15a2kCgqv7xi4wT69awyyvlGBlLn9pJNOLTUUrPrpK/QJxnLsNkdpFjU/dXqPU+tQyRGSJoy3BYEEjJGPepSsiSEMqqRwYyf1z9aWAkxkyQscjIIOO+Ofau9YzhtbYef3//AG5PLV7kMkRkYHcAB7VaidlkVowdwHbmpLeBZIi5HQ9qsw2JwGXh+3fNevj8flWHxNb903Vaabvo7r/FovRXM4xm0tdB9i7tevPPG+1127sY546flSahjyWwFDFhn1PvVwwSR2EaMhYo25gnpz/jVbUI2FiJGZQrMNoA6j615GXY765jqU+Xls1FJXekdFudmPwkcM4xi780Yy/8CVyZ5ldY1BYLtySeOnoaZcPsgVwQSR37ikZ0eBIiVV1A4x1+lRCIECIs2wEs3P8ACOv59PxryazSbZzRV9CSyDtNEG6KDOwPqeF/TFXy+DwarWWRbNO33p23f8BHT+v6U/dknvXzuInz1GepTXLE6aJ+gqHV9NTUrLb0deVb+6fWmRPWhDIPWuOMnTlzI2aUlZnJWUk0kht3BW+g4K55lUdvcgdPUcVZgeM3AuFi2nr8vU/X0q9rejmcC5tjsnT7jdPwNZttcNfCRowY9RjP72Dp5v8AtD/a9u9fQ4XEqcbnm1qLTOiJRgrNzzuCnrmnQ3MpVvKRQQ20561QsrnzI980iZJwAP5U1JzBI5jIKDLEnjn+td0Vc5Wafmus5DSRjj5iwwPp71maXOi+KtWk3lQVGMDryPWrUN0t2BuUZxgFecGs3SxND4n1GIRiRiAG3dByDmvVwS/c1/8AD/7dEh7o6e6ukimi8yViHBGM46e1VZV+0SrkFYzkc44pLm0DYlmlKKcndnIBq1bGAWoSfJwuQx4zXnaJaFdQS2kgIa3ky8YyCCR9Ola1rrcqQK04ycfN2J/oaxbidvLLxNLFjkgpgfiac8j3VomGG8nnaOo9K5atCFRe8jaFWUNjorddGv5QQib+6g7Sfw/wq1exNEuYwTH/AC+tcnJCI9NB2MWzlmA5/wDrU+21y+tYwQ5liZcESEkA/jXh43JY1V7j1PSw+PcX7xptORIM+tNS8IYj19a5weJ4C+y7HlSFsDapxV9nKnjr7V81Vwc6T5aisfQUq8KivFm004ZQRxxg81G106kgDtnOf0rJS6CMBu59KmNwjjl1B9M1j7GxctiHxFKsmh3xKjd5JwRx6Vy+khv7KVkCF1ww3rkd+K3tbYtot2oOS0RAHcmuSsdUnsrYRGwkcYxnJGf0r7TKsDVxeSyo0LOSqp2corTlt9po4p1aVOpU9pezhbZvXmT6eg7UdenltZbN1244YFucjnp6VzgnlTJSQhTzjHT1rWvdO1HVbo3Vvpd2oYAHZCzg479Khbw7rJBzpl6ue5tnH9K9Khw9i4QsoxV/78P/AJI+cqVIc2j09GZ73s7MWKhmxwWwee5NQzu0tsGbqTkjPWrT6BqKuQ1tcoe48lqR9NuFj8h4pVZTzlCDXuZbk+JpRrJxV5QaXvR3vF9/IwnUi2ipbf61to2jb0qIs8LblYq55+WrcVo0I3ZYgjGSKrfZH7yKavFZNjHg6NJQu4uV9V1at1CNSPM3cSSTYckBpMhyTg5yKcJnMgmkZ2cD5SDjigWjZyZFpXtGZuJF/rXmf2Fj/wDn3+K/zL9rDuPije4jysh3KpYg55x1q1uZ3V2OS3H9KhtoDC2SAw7cVdLxuADGxPc4606eRY9Su6f4r/Ml1Y9yfTWPmhCm5SecV06WwgfzIiipjoBn8qwNHUjcwIDEkcjGPxrZkZFRYnmO1wCNuMf/AFq6s3ivr9V92ZRloipPPIluH3lSzEMQMZHPasu+laW3XYSIVIAWtG7I+yKG2kbscfjWfefLabSnJIO4DANc2QW+tw/xv8z1s6+Kl/17h/6SPlZniysgKAckrkqcdqRbdjstSSJZPmnI6oo7fX+p9qfG0dsi3JBEhA8iIDO9vXH8vWrEMRt42Mh3TyHdI3v6D2FeTjsRytpHLQpX1ZJK4AwBgDoB2FNgjMiE++Kglcc1etMLbrnqea8bZHaXY36Vehk4xWRG/Iq2kuOAazlEpM2Y5A3BAIxjHrWLq+jecwubZ/KnX7kn9G/xq5FL0xV1HDqQcEEcg0qVSVKV0OUVJWZzUFwupTra3Wyy1RCAGYYWf6nsfQ96uSBnuGtbhZIpE+9GwwwpurWEEpWO4BCH/VSjqvtUA1O5tEitdYQ3VunEF6h/eRj0z3Hsa97DYtSWh59WibdjaiFFKblYnnntWE+pW+m+KNSkuo5HVztAjGeePU1sB7k2gubWUTWgODcKpwvs4/hP6VOl45j3FTvA4I5B969rA4yFLn548ykrb26p9n2OWUGjK/4TC18kqsdwrcAfICP50h8VadtQpb3KuOuUUg/rVi5uZElyk7Flxk9ga1be4niRZJCknmYwu4fnXU6+BSv7F/8Agf8A9qRqYUvi2zuYPLmW5BznKRLj/wBCpyeKdKgjVY4bxmBzudV/Ej5q2L+RHZMKYnztzjg1PH5YtxufdngK/T6il7fA2/gP/wAD/wDtQ17mFc+M7SZQqR3KjPOVGCPpmq0fiqyWARyW00gB9APr3roJDKZNqoNij5XAwpqZ+bXgoh5Ye+PpUutgF/y4f/gf/wBqWnLucFqmoWd26G2iliAyCpA6evWo4Nau7dPLjnk8sdFYBh+tdm5hDrNIJHkJyu7BXI7fSoL6BpHVPIDxuMumMYP/ANasakcsqfHh2/8At/8A+1NoV6sPhkc0fEM5UAhc98Lj+tVpdYupG/1rImP4Bg/zrpbKxtlu5I0hVlU8MDnFXl0yJ7lkkt9y7d6kYA+lY/V8qi/92f8A4H/9qavHYhq3OcXFfJGzNunLtzuzk/zrRttZsRF/pKXJf/pmBj9TXTvZQpKojQLjtjBwa041Rw1pJGhB5X5cZq3Typ74Z/8Agf8A9qOhmWLw7bo1LXOMOvWGAF+3geny/wCNNXXbAkiU3rDPGAP8a7Q27R4MQYscg59PWmPbESSO/lyoF4XGGX8aXsso/wCgZ/8Agb/yOj+3sz/5/P7l/kcO+t22CEjnIzxux/Kmpr0YQgxy7u2DgV17WzqylpZgnOExxj69aq240+GVtiorEcvuzz6U5YfKJRt9Wf8A4G/8if7fzNP+M/w/yOdTWLLy8SLcA5OAqjA/WmjV7HY26KbfnjCjGPzrZnFx5pWI4iBYhmxgj0z3ohVZJGRfLTgDbjp7+9WsPlKX+7P/AMDf+Qv7fzP/AJ/P8P8AIwhq8G3mJs/7ox/Oozq64JEY3e6f/Xreu4I3QxIjeaDwExj60wW3lkuTiUqd8Q6MBSdHKLf7s/8AwN/5B/b+Z/8AP5/h/kZMesQ+WPMR9/oqDH86c+s22/8AdxS7cdWAzU6sm0ybi8YI3DaQR9RV64ui8CkL+7A5IznFJ0MpT/3Z/wDgb/yK/t7M3/y+f3L/ACMc6zF/cc/8B/8Ar0jazHjiJs+9WxESQNo2HkN3IpolkjbYBu+baExkt/jSdPKF/wAwz/8AA3/kNZ7mb/5fP7l/kZ8+px3EWySI8HPFVprhXhMS7woIKgjr+Par1zNFby7Qiy3J+5EnzKh/9mP6D3p9vaMj/aLpvMuG5AJyF/8Ar0Us1y7AyjOlh2rO69/r/wCAnPWeIxk/aV53fcW1gdX+13JJnI+UE52D/H+VLNJyaWWXFU5pM96+TlJ1ZubOlJRVkG7zJAo71pb9oCjsKpWUe7dKe3AqdjzUyWtgRPHJxntUyycis9XwfpU6SUnEaZpxSYwfSrsUvH+NY8co4qzHN3rKUS0zVmSO6gaJ8YPf0rAkeWxkaCYCSI8EMMgitWKbPeluoI72HY2A3ZvSlCTg7oGroyLYXNo7T6JdvCWwZLYv8r4OQMdCPY1aj1a1nYxzh9Nu8/NxmJz9P4fw4rImSW0mKNkMOhHep472KaPyb2FZY+xPVfoa9OliX1OadJPY25ytvakT2y7X+68eCjfRv8cGqQlMbId5Q56E5/Wq0MdxaMX0q9LxnrBIeo9MHg04XtnI5S9tXsZz1eFcoT6lD0/DFenRxKtqck6L6GotwZbwOX/docYU5OPatBpstiNAYwBliOc+tZdnGURjbNHdRnOWgbLD6qeR+Gaes8EqiJMjYfmDEhh+B5ro54y2MXFrcunUBGzRhhtHTYvX2qKWa5miK+WFB5DA9faswc3RUORnqB1H1FaT3sMbxptyQOdvI+taWS2JGpKjMRK7K6YAUpnA9q0lv7YImWO8DaFPJz71Rl2Ndx7iFVlOfcn+VWfsVrsZXuMMR820459aiVnuNCOY0SQsMFj0U4yT7VM10saxjzCikcHbz6VnCUAuMGQKMeZyR7GkeN3YeaQq9N2c49zT5V1FcuSATXJlUEsME5Pp3q3cNL58UkQRmxyM4qHy1tIUeNSwXrjrimW12J5hv3J224+9+NQ+4y3NeP5b7VkR8Y24zisO7uJre5k2XLkjbuJPH061pX2oPAXUYGR8jA5LeoxVe0mtriKXdCqkg7gy8txyacdFewMkS4lhjhRZ4pPM555xWfdhWvkbyl3HLfKf1NUplXYxXaqc7Qrbjx2prTi4miYs2/AwAvcVoo21JZrSopjT9xkY5A4Gcdaqi0W3QHzSWJ6scfhRLOZZQrHyiikMqnP6VmT3bLLlMIGGM44xUxTYWL19eA+XwoBPbqoqtFKROZFRzGxIA5wo+tRRxRvB5oXhjtPOc/WorhBEwCyOwYgbAdxP4daHZKw0maFzBF9nkGeGPBXqfxqsZlgKEybUHy9KqTI0WGuZhAByquct+CD+uKgbUBJJ/oFu0rj/AJbTYO36D7q/qa551oxW9zWNJsvSzsEVpGEEP8LEct/ur1P8veqBuprrdHZoUjPDzOcs31P/ALKOKRbNpnM13KZnbk8nb+fU1b3BAAOAOBjjFeZXxfRHZTo2G21tHarkfNIfvO3U/wCApJZfemSTe9VXlya4rSm7yN9ErIdJLUK7pnCLyTUTMSa0bODyk3t94/pWllFE7llAIYVQdAKiYgk80sj479agzmoSG2ME1SrOelZP2jnOacLketbOmTzG0sw9sVYjmTbktg+lYIuvepluh0zWbpjUjoY5gAKtRzgkfMK5xLz3qdLwDvWbpstSNu5hivY9j4zjhh2rnbq3ltJCrjjsw6GtGO+Gc5xUrzRXEflyAEGkk4g3cxFlKkEHBHpV1NTcp5c6LOno45/Oq13ZmAlozuj6/SqYk5reL6ol+ZqeXZSsHt5ntpewbkfnVw3WqwqvnRx30I7sN5A9iPmFYO/IqSO5liOY5GT6Gt41pLczdNM1V1TTWcl0uLOXvtPmLn6Ng/rWjFdLcCNra7tJNrZ2l/KY/g3+NYB1R3+W5giuF/2l5/OmEaVMM+TPbk90bI/KumOLfVmUqKOouRcY3pBKoAypKbgPxGRViK+gmQh9jTEYIHGDXJwwmI5stY2H0bKH9Kti58QJ0niul/2ir/8AoQrZYlNWMnROit5Z2eWJ4wi7eMdG7dqR4mEXDAkNnG7Nc8urahC6mfRomUHkxoUJ/wC+TikHiNQB52m3KnrlZ3H881oq99iHRZ0QvGjtpd0m4qMEZGeafZyxy27Ll1IO5jnBrl/+EgsCrBra9Gf+m4OfzWhfENnGmI0vQD1HnJ/8TTdVW2F7JnQpHDLKXactJ2+Y9KiuLlDPJHH8q42NzgYIrAj12xiOY7a7z6+eP6LTX1tZHJTTZnJ7vM5z+WKPbK4eyZo2628Uy+YPlXuPT3qW5u7aJ9wMZcH5eeue9Y5vrt/9VosK+7Rs3/oRoF1rODteC2X/AGQiY/IVMsUv6ZSoM3DPLJbhoIpZCQA2EI/XpWfdGIgCWaCHHZpN7fkmf51mSrLOc3eqGQ+i5f8AnSx2tvgEQySe8rbR+QrCWM5dmaLDk7ahaxjy4/PumIx/zzU/gMk/mKTzdRkXCeXYxHrt+Un/ANmP51IvyLhWWMekS4/XrQGRSSAM+p5NcdTGN7am8aKRBHp8IO6TdO3q/wAq/l1NWsqoA4wOigYA/Conm61A83HWuaU5z3NUox2LLS571A8uB1qu01QvLRGmDkSyS5qBnJNMLFm2ryav21qI8SSct2HpWtlFE7jrO2C/vJevYelW2eo2eomkrOzbHsK7H1qIsO9IXqIvz1NUkK5z4nalFw1QUV6HKjnuy0LojvTxd89apUUuRD5maQu/eplvDnrWQCRSiQiodNDUzdS9461Ol/jvXPCYinic1DolKZ0yagMcnOagmCSfMnyt6VircH1qRbojvUeytsVzFvzNpwetOEvvVMzhxz+dRmQrT5A5jQ8yniQVm+fThce9Hsx8xo7weuKNwB4JH0OKzxPz1p3n+9LkYXNIXM6/cnkH/AqeNRvF/wCXl/x5rKFx7077RRysLo1Rqd3jBmBHugo/tK5P8af9+xWV54pfPo5WF0aZ1C6PWb8kFNN7cnrcSfgcVm+fThLnrS5WF0XWmdvvSu31Y0iqGPT8TVUTKPel+0+9JxY7o0U2JyeTT/tAArKN17003PvU+yb3DmNNrj3qM3HvWcbj3qM3HvVKkLmNBp/eomm96pGemGb3q1TE5FtpveiMNM2B+dVEbceTxVtbhUUBeBTcbbCuaEKxwDI5buakMw4yayzd+9MN371Hs2x8xptMMdajMvvWaboetNN0PWmqbFzGgZeozTTIPWs43PvTTc81SpsXMVKKKK6TIKKKKACiiigAooooAcKd2oopFIevWnHpRRUdShnagUUVQDqU0UVJSDvSjpRRQAo6CgdKKKQC96XtRRSABQaKKAE7000UUxCdqSiimgYzvSd6KKolkq9PwoNFFT1GIev+fWmmiimhDO9JRRVIkSkoopiP/9k="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>12</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 12 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes
