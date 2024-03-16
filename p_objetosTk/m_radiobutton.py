from tkinter import *

off = """iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAACxAAAAsQHGLUmNAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAARdJREFUSInt1L9OQjEUBvAfxsV/q/ga7j4C8gguiLMRZ3U3mrg5GN8BHRndeQ5wxARHHFqClHsLXBNd/JKTNu055+s5bT/+8deolay10cDWink+8YonTJY5n0WnKnaaJtssIGjEcYIXDJccqI6mUHkzVpFFLybvJus7OIq2nex1Y0wvTbaRIXqPYw2XGOAt2hAXBb4LKGpRig5uk7Vd3MX5fS44VwGhLdeZ/RuL7VqL4FA4bRn2ok9lgh9jGUEfH5n9UfSpTDAW+lyGK+EXVyYgvJKO+UpGOMfDsuDcM91PSB7NLrRv/uT1dQimgcfCDx0U+Jx8mx+YyUu2XVO0VRe7VpqsTK5bgnCtKtdjQRifrSDX//hdfAGatksoVnN9XgAAAABJRU5ErkJggg=="""
on = """iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAACxAAAAsQHGLUmNAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAkVJREFUSIntVL9LHGEQfevlIOePQoucHKQSkiJpbMU/QQ8hfZqgMU0IahOE5PoQQVMEQVKmSaVXCwHbYKVF2hRySpCQC3eYnfcmxX7fed5qzs7GgYVldr/3Zr55b4DbuOlIchn3ZGID8y7OOFWSpYALIgERSgUX4SIkwk1wsu20+s8PD7aAxP9LMLHuCxA3RcIZgOI7BWcA5vkjEi4B4vzpx8db3Xh3cg2IM+GgS9wReQwj3AWQoBtAh5NABl52qepkQrEKoA8BVfLsOuo/Xo/MxXx5pTFUKGhSIIqDxf2j2v1W/Da6eLAtsgqy1Is30JuQpfFaTgJlUlk9XkmKbNBtLzHtpb9ax2Mvvy+dn+FJ7KgvQRyoLPu5snqyLNk7J4e77nwY1Pux54dLoe0sb9cgiAOVC+WVxpBkby8bqJOgrFZZ+DYos3DGcgS5GUCZWkCiUNAkL1beAQ+FjDTpk06HRIDqT9DRuRMGQ0JdBZ4pyQxyBUnnCXJXFA0kMxRLxX0nm1eBO/m7+df3FT2SXpMgA3Ic1SotirUrwEHpDb5MtdExYNqfILoUzAZ2uvFwDaZlkc3uyim9an+eWgdw0c19O7BYre7F3Onmo7WhJB13chpm03/ONB7BAYDGctxPvXGJk9kO1cyOLh5sS9aQOZpn1pHv3QF7iidf4W6gaRxhvYhqX4PA6i7NOpmIrEbJdi850IPbFWQd56PtXrz8uoYnYy8OnxlZhbGE4FC5ARSkTC1SmikrWystN+1gd+5T77q+jZuPf54eo3kDTHFnAAAAAElFTkSuQmCC"""

on1 = """iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAJpJREFUOI1jYKAhUAbiYihWJkVjDhD/x4FzCWk+DlWYhUUuEyp3gpDNfHgs4IWqycMm+R9qCwiwMGA6nwUqlw7lowBlNEFcYYAsr4JsQAkZBpRSakAJsgEqZBigyoAGQILpUDa2QGSFyqWiGQYH+VAJHmySUMADVVOAS8FJqII0LHIwm0/jsQDFJdhwISHNyECNARJVZVA2bQAAIKJOmDgTISMAAAAASUVORK5CYII="""
off1 = """iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAIZJREFUOI1jYKAhUAbiYihWJkVjDhD/x4FzCWk+DlWYhUUuEyp3gpDNfHgs4IWqycMm+R9qCyGQDlWLApSxCeIBILUqyAIlZBhQSqkBJcgCKmQYoIpNMJ0Izam4LMuHSvDg0cwDVVOAS8FJqII0PDafJuREmEuw4UJCmpGBGgMkqsqgbNoAAGvhLqcV6SMIAAAAAElFTkSuQmCC"""

off2 = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAdFJREFUWIXtVklOAkEU/a7ElXoQQYOIolGvpngFnIcECV4AlRWIYLyC4h7kCM7+F36lyg4UXW11jAkveZvu98eaPtEY/wxzzC1mjdlhvgg78g3/knEEXmM2mF8h2RCbX2OSWWB+BgL0mFXmmbAq30wNbHaZiajBp+ln1R/MC+Yqc2KAHt9yzLJold0tc8Y1eCIQ/ImZdbBfYrYN+yY5dqJgGN8zZ12MBbC5M/zshTXE5lFr3o4YXAGtfyS9J9bDGKnWYx1d2j4MGdJ7ojlKnCTdsrKH4Aolw2/KJtw2hDmPCSwbfvM2YU1EzzT4qEUFfHXFd90mVKJrj8EVrkgXNxSvIjqNIYET8f3+Vwkci+83myjOJbgU312bqE7xbcKO+L6xCfOkj8uKxwSyht8dmzBlCEseEygafudHiZukr+KMh+Bp6u98+GyFMcCDoR4jPCTOb7kBzBQPpB+jjbCG+6Rb1oqYBIKrboIHLsaJgDGqWHSwT5OuHMRcMOWSAICqW4YTrOM59Xf0sJEMk1CR9Jqr4JFnCmSN1gWHUpzpCvOI+jdchfQ5N4fSQ4pQ+SBg85jdGEVUvekjcBA4w7hIMDXhtkSrcVx78g3/FuIIPEZs+AZQ2740ErjcIgAAAABJRU5ErkJggg=="""
on2 = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAkVJREFUWIXtVttOU0EU3fpCERL1Q7gFEChE+QK0vwJS5VHwFwAVxYRL4QOq9Ilba/gFxPeWvlheuYjuBXtydqdzLlNoiAk7WcnJvq01lzMzRPf2n1kX4x1jm1FmnArK4kOsuxXEY4w9xt+E2JOaG1sbY55xaRFUGQXGV0FBfDoHNQuMVLPkj6l+1H8YG4xRxgNHPnxpRk5yTd0+44kvecoi/8UY8qh/xjhS9UXynIl5VXzAeOpTLIaaH6rPYtJCbB6z5kch5I8YE4ysAN8djjxM/U8K9sTzJALM1GMd7Wl/yJhk/KbGnV9jTEmOtkEK9kQxjrxbNcw5yFcdxDbWHSLWVLwnSsCsSkxbsckE5AZTVu2wis1FCdiWpGOq/9WwvjUPATWq3xPoVZHYTpQAk7Rl+V96kBu8snp8V4MLtTNJWrb8b5oQ8Nbq8UX8F3cl4LP4z6MEtHIJvom/EiVgh8I34YkHOXI7VT16lSW2GyVgTjUZsWKvPQRkrdohFXsfJaBHJa5ZMRwuuQTkm9R4EK2oeG+UAFhREnF8DjpETJN7OeDLOsj76XrnI6cURw7DhWEuI1wkrrsc65thzAgyVL/mxvCmOJRe6PkiiQDYBwpGVgoREWcgN7MJfPQpTlnFGMWAR30/BSMH8C5o9xEAw6hLqgnWEbchdnTYkwwvoRUK1tyQN/OguTKoxtTZj1L803nGEl2fcHkK/nMD1HyiJkbuMmwePRtxwKjHb4PYNvzDOEjwasJpianG71oVH2J9rSC+t5bZP7HfQiUuC8QCAAAAAElFTkSuQmCC"""

on3 = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAOxAAADsQBlSsOGwAABL1JREFUWIXll11sU2Ucxp/nPasbAUIwRiJfUSDRAJIQJsSFsa1064gXKmRowEA3iaIGl/B1i8SYgBkgi16gYy0mRkNI9ALD6LqPKkOcgkEiXijKR4IEMBFW2NjW83jR0+6cFUo3veN/0/P+v57f+/Z/0rfAg24caUHgQGC6LS6BOBvQJIkGZILQOQndHReiJ7Ad9v8KUHOwxrp+6+YqQhtIPpMrV9I1kZ9ag8ndsXWxy/8ZoHx/5SJj2ERybj6wLpBeUe92/Nm6M9eJ5ATwhyvfArmHoC/TGOqC8CXE7iRxCQB8So63yTkAqwEsJzk+nW/L7rDRvzxeG/9nRAD+cHAriZ2uHR2DWN9ed/RULujAvsAEPWS2CthCpsAlnTH9dmns9diNvAD84coakF8QNJJEaFvb+db3RjJcFZGqBRS+IjnVgYi1n48Gh/fIAgg0BSbbljlLcgIACNrQHop+mK+wF6JiJuSLG3KKA7G5vTa6KydARXNV2BiGkKrY11YbXe+OL9i3wFeQKAyBXA1hDkAL0FVBLTZN448bj/3hzvdHqhZC6CJZIClBk3y8bW3b3+m48ez+QGA6DVY7O78yOPbOZo/4+yUzCxJFp0jzMcEyko+QmEjySUNTb0lnF+1a/Ka7pj0U7Ra5FwBIjoMK3nbHPQBJcU164gXsiq+MJzLiu0sfK7DYmet1JFlI4qNFuxe/5vbbvr4dgvpSh6rQPQEoLHOS7IGkOeCOFchuTA/U/U0fFDeUTkuv4qvj1wF97UBODzQHns4G2AYDcL6zOn3s1ZZr6VBxQ/E0AC/mJw4QHGMh+YbHaaM1/Zg0pjgLoHRWcBLJMU6LX921Fn0Bkla+AKnOXOpeJi39kgEUZmQB+PoHJqafRVz1NJPJ8+iHjMKjHp5B0zPUn+OyAAZ8Vm/GKY3xdsPtkQII6Pe0cJ0gZQ9mARRhaNcCnvA0o/3TKAA8NTaQGUoKf2UBtK5pvSVb552U4tRQpqx76ndxyb44EgBDfOZeW0Yl6eekZTLz4HkNBXQCAImHl84I+jOBlUiS3JKvuKS2Exu7Dg/zLXc+B/oHeo7fFYBGB4cKsMkdO7Gx66Ck7fcTt6WfB9X3cmo/KStvDj5PmlnO8sjxdcczA+kBaF/b2iLpNwAgUO2PVC5zx7/f1PWOzeSLtpPj2SHUa0ONfXZPycnNJ6+n/dV7qwsNtdOV6Plhy/oxKg9XrbDIQ07TKwM2Fn5bF700TI3FDc8WG2PmQSgSeIG+/m+667tvDu/nDwebSdQ6/draQ9FATgAA8EcqDxFmBQBI+N2Y5NLY2tiIhhAAKiLBBoPUVympRxyY3xHqOOfOMXcrTFhWnaQzAEBilm2bH/zhqhfyFfZH/FP8zcEjLvGkaL8yXBzIcSULNAUmyzJHQM5L+2SrU8beU3ij4GhLfcudLOH9/tmyfHWU1pMc64j3i3aoIxT7/G46OS+lJU0l44ussZ+Q5iW3X9JtAKcBXQRwB+AkAXPTNx9X3kUbWtVZ29p1L428/heUh4PPGWhHvldzSQkCjb3JxA73KzdqgLRVRCqXQKaGUBmAp9K3Xkf0MqluCYf7krcO3k94VAAeE1gWKZvgrPritfG+Ufd6oO1fIvIKbjT3gpcAAAAASUVORK5CYII="""
off3 = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAASlQTFRFAAAAIx8gJB8gIx4gIx8hIx8fKBshJCAgIh4gIyAgIh8gJCEhIiAhIx8gIx8gIx8gIx8gIx8gIx8gJB8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8hIx8fIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gIx8gJB4fIx8gIx8gIx8gIx8gIx8gIx8gIx8gJCAhIx8gIx8gIx8gIx8gIx8gIh8gIh8gIx4fJB8gIx8gIx8gIx8gIx8fIx8gIx8g////QBrA4QAAAGF0Uk5TAAAAAAAAAAAAAAAAAAEPL0lmLgEFOovI7PnrK57tA1fY+tKYbWnUUgJq7/3EXBcBARhd7vOFilYs12/01iqd/gSXw8U5+2CHEMcBn3hlbnlImQEZYcZxUAIBAgNV02gDKcPP7wUAAAABYktHRGIruR08AAAACXBIWXMAATr2AAE69gE6sVc6AAABk0lEQVQ4y62T6VLCUAyFGwFFVDZLbVlEgSIIVitFxR1lERE3QFzR8/4vYSltp9A6zjjefzf5bm5ykjDMPx5a8geCoVAw7F+ecXKzEW6FFwAhusJFWJp2u2LxBMyTiMdmJhBaTa4B66l0RhQz6ew6sLaxaiEol99EobglbbsZxrMj7xYLSORzJkGULEEpS6Rb3CTtKSjtk8cADipQDq15EXt4hOMTMm6nOCufTybFcmeo6jaK8LiQpuoi+RJ8jcYVcqjvmv+ZeTXqaGpZ0VULKXlaGDVECq0rDQjwSM/ages2+IAGBAVkbH7VfgMhqAEhQHQCRCD0G9Axvrh1Au4g3GtAOIoHsif52EY0bJSZ7dqBblYv00WaUHPTQvXqKI8Dj6Quyjap+4bUDJ2rzdpjf24WQzF7u58s7WY8tJGAwknkHt+98xKngB+Q13jge86XUOg35BffaPq7vZY6cuKrNeTbe0Ud2o/2zXB41x4NbWXwOZGUa+Grah379NeibTPYWtNYnHKNddBeX72OunpLTu4/n2/BsUs//y/9pgAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0xMS0wOVQwOTo1NDowNyswMTowMC72kzQAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMTEtMDlUMDk6NTQ6MDcrMDE6MDBfqyuIAAAARnRFWHRzb2Z0d2FyZQBJbWFnZU1hZ2ljayA2LjcuOC05IDIwMTYtMDYtMTYgUTE2IGh0dHA6Ly93d3cuaW1hZ2VtYWdpY2sub3Jn5r80tgAAABh0RVh0VGh1bWI6OkRvY3VtZW50OjpQYWdlcwAxp/+7LwAAABh0RVh0VGh1bWI6OkltYWdlOjpoZWlnaHQANTEywNBQUQAAABd0RVh0VGh1bWI6OkltYWdlOjpXaWR0aAA1MTIcfAPcAAAAGXRFWHRUaHVtYjo6TWltZXR5cGUAaW1hZ2UvcG5nP7JWTgAAABd0RVh0VGh1bWI6Ok1UaW1lADE1NDE3NTM2NDcganrbAAAAE3RFWHRUaHVtYjo6U2l6ZQAxOC41S0JCSeC45gAAAEx0RVh0VGh1bWI6OlVSSQBmaWxlOi8vLi91cGxvYWRzLzU2L003b09mb04vMTY3My9yYWRpb2J1dHRvbm9mZm91dGxpbmVfMTEwOTE0LnBuZzfP9i8AAAAASUVORK5CYII="""

off4 = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAADsAAAA7AF5KHG9AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAxBJREFUWIXt199rlmUYwPHP9Tz3u1kUTjup+eOsH0oHCXMQJbRwJxlukPQnSFFUEml2EKMDm0KiNAz6E6LQKQW2VMoKzJWdFEpn/uxIMwJ/bHvuDvYyNrd37W0v1IEXPPA893091/fLzX3zXA934z+OaCY5v+zRiv7IenNhhWxVvcqFyC7mMFJkw/GRcy0VyK/qymF35tkF5fN9mW2PId8tSiBvVavutV94qZ57VTiUs8Nl5ayai2DMyomwJsJm9GMZsnCg+Mu2+NhY0wJ5m+U5+SzzDG4Ie4sb9sSH/pxXeoelVWU7tuGe4ESUXohB1xYskLeq5QcczfTgcpH1x6DT84Fn1XjHE1U2jNWZk2W7jTHg9p15xVwvVw/an5MeycWi0N0sHGKXn4t2T0kuRbKhmvDBnHmzzN+zPmencDOyp2PAT83CZ9Qb0JXDSbRHWB/v+nH6/KwVyKXdksjJ3sXCIQaM5tK+es3BO+dnCORdHjO59FeL++1ZLHwKkgxKriltzLs80lBAm36JnByM1+bf7c1EvO16ToYlLNHXUCDXbJQokiOtgk+BksMSudQ7fTyZ+bS6fvdLqwXU/CrDFGNOgYfAuN9bLpBdqtNWTB+euQdKWdly9GQsVShRqhoLJFck3Kez5QJjOiUkl+cTOC+hsLblAm3W1gXONxSImhGJqmZzq/lVqU8iar5sKCAmz2okffkTS1sFzwd1RLJZQulwQ4F40Tml45LlVZvtrRKoCjslHUojscVvM5izbD/XJfsBt4QNscnoYuD5iG7ha7QpdMVzzkyfn/Uxik1GJQckSySH8hdW/mv4UavUHJQsUTN0J3xOAdDuDclxpRXanMrHdDcNH7FO6VtJp+Qb1701V17jluykZSZ8arIRvSnsc9tg9Lo+L/iEDmEnXke7cExlS/T4oykByKNqbtqLV+q51zCsMiw561a9KW230oQ1Qh/60IFKNmTcm9FjvBFjYW35aY8b977w/ELy8ZVsRzz5zw1Ncz8mZzys0i/rxSqmNuiF+jWiNBzrZh61u/G/jr8BQEvlQKGDLPYAAAAASUVORK5CYII="""
on4 = """iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAADsAAAA7AF5KHG9AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA+tJREFUWIXt19+LH9UZx/HXM9+Z2VUQd9OrmtULaROVXiiNrYIJuyZ70xR3RVn/ASsV20oqRNMLWSqxq0LwR4ii9A8wtGTX0EK6aoxflDam8coS60XB/GgvyqaRgtFk5+lFpmHXbOJ3XUEvfODAHOYz5/M+z5lz5hm+ia84YjnivN/ahvFIo1lYLV3djnI00rEMs0Waiee9/6UC5M+sy/BEcntPet7upK2x01srAsj7VM3lnhF+2mrnhOlMr3QaR1SOgTOG5sP1Ee7AOAaRwq7iv7bEi84sGyC3WJWl3yfD+FjYUXzsyXjOR5eEftiVTWMrtuCyYH903BVTTvYMkPep8lv2JSM4UaTxmPIOnHnAaNGYENZjqH3kKLpN2l0971XIX7mxSTO4Jul2+myKSZ/2BDD/qF3S/ThWNG6J7Y7nL62Zb7wUbLhkBjjQafwknvVBThpq5v0Zq7Gz85iffy5A/trNmf6C05Fui0mH8yEbmsK0c2vbS5wsGIundHPSugxd9EW4OR7114XC4gKAjieUIks7YtLh3GZN029abVBNj22wqU3nI74Tkw5lx9PtmFOf9VsEkI+7TmlEaa64wpOQ/V6I2mDULLOtysv8ForSlNJJHZvycWsunoHauJIs7Ylf+Ci3G1UZUfEF24bcbmM84lSWZpToN3bxDFQ2KSlKe6Hpd88y0r5ka/pMtFl4RUl2jC70LC3uXdNevQdRuc0K4/yuqfxNwnmPJQG+Dc76F6itXimA/58V6XjrtmjMxQCdlvFs26++BHsacKXC6QX9JQFK/8QVKlfh72rHsXaFAMfBGVe1bicW3ly8C0ofKlG4AbLWXelLmLU3Qe0GZetxMYCozCppKndA0efllQIUld3QdIwpicqfFnku7ORua7NwBHPRuDYmnMq9XhO91QEXRDgQmw3nHgM57x8YCNbE3T5YOgMT3tfxutKqprYV1O5V+/cXmP2cjnuhKWxTGtAxu9D8ggxA/sE66SA+EdbHZofyDesxjVU9zn0O4zGsm3v9QDiAWmFd/Mi7C4UXfIxis0NKu5T6labzj4ZiWFe/W9Te6OH43a/2wxjWzX2uVtmj1K+y87PmS2YAcr/SvH3O1YAnhDtjo4OQB20UJrCetihtCxKFl+P7XoecdZMw7dzJ96Y5ozHRY0EC2TVo3u9aiNPC0z41FaNOXeyZFn5A2IYH0Se8pnF3jPjPUvpLF6WHVE7bgQda7UnMaMwoHfFJW5T2GTLvemEMYxhAI+101kMxcv5sXR7AeZB3fM9ZvxF+3Iser0oPx60Of55weT8m7/quxrg06tz6LyxKj2JWx0zctHirfRNf6/gf4uU+sY57lqYAAAAASUVORK5CYII="""

on5 = """iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAACxAAAAsQHGLUmNAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAtRJREFUSInV1V9olmUYx/HP9bzv876bDk9qWepOwtFJZlRKVC6MdRTVax73Z4wgo5MSCTppHvQHKuhIRUKROhKkiQWBIsrCZFDgqJO1oyzLedAfkEq25+rAbe5lG5udecMFD/dz3b/vdf/u+7kebvURyyXkK+6YDs9EZUuEdZDpUjJaCyfigMn/BcjXrKsKezGAGi7j55nXG7AWU9Lhoubt+NivKwbkbn0Vx9Al7Cs4HB/6vi3ndZuqwgBeFf4qws74wMiygHxTXxVO4seCVrxvInd5vKIVbIRkomA49jube/RWNcPYWIT+eK8d0gbIIeuqaRdwubjmUdd0JZ8m25fY/ukoPS9crRrOobuouS+G/DabU8xfUNXtjYauoqalrqtq+iabtmuyWGTTE1XhvLS66LQjGtZUNUPzNecA+Y61UfdSlvbFkIksfaZDjw6WiZ5c5Ui8ZTxLB6I0mO/qXmBRfuTl5GCEe/3j9gxnFrNlqRGpT+nPLFwIBmO3Q207qBoe0nA53vBD1am1gsrbourUij3GNExWTVtndetzFZTW4yJEp155M/UTqRc0XIy8/kG2AZRSzFjWuFl5mFlTV8w9zwdk6VKwBbLDxLI9ZKH6xEyhGzKMzs7PnUFRGtWwNo/aVHQYvtkzKFYZzqPu19Bd1J1fANB0QmmqKgzEc85G0+lossI4GS0jVWFAaUrNl7OybU5MH3cwwgsRNmm6qu681LOMOz8pPex3azKMZTpUe9auRQH5lbtwAVfUPKLTahxB/xLiJ1VeNO1v/zqH20zbHE/daBULm90p24RTmJB2RL/x/NY2qWX2KoZx4Xg8aCRPu0f6HHer9MeTvp6vt3i7PmObwjGswX4cjj5jbTkjNmNA2oU/FHbGY+3iSwIgR92pMiQNun6dJ9344fSgG1P4RM3e2HrDlhUB5kDf6cbTKluE9dcn/SKMCl/EA64sp3Frj/8A/d7e5JF2d4YAAAAASUVORK5CYII="""
off5 = """iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAACxAAAAsQHGLUmNAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAkhJREFUSInV1c9rnFUUxvHPue+8bxRKFWSMpnEjrV3Vitgu/JGVgiAtlfwFwY2KG5Xi0mShTrGFrtoi0uwLBdMoCIoKlSBZCC260l21NenGurI2c28XaaaZpnHiuOqze8857/M958K5l3tdMaigvO7hbjgY2b4IY1CKy4XFKszHKctDAcpbxnIygylUWMJvt9LjGMWKYjZV3o/jrmwZUN41kTmLbcKJxGwc9VNfzdv25GQKbwp/pTAZHzs/EFDeM5HDV/glcSg6ft1sSiiH7cqVz7AzhRfjo35IH6BMG8tdF7CU/vFcHHHt38zXNfVAbiygnSpPxrQ/1nJpfWFumYnGtlQ5tFVziCOupfu9Go3tuTJ99y4+MJo7bnQ7jm3V+E51O47njhvlQ+2NE9znoForNU4PC0iV02otIw5sAOTGMxpL8Y6fhwXEYRc1lvOI/WuxVi9Z24FLw5r31LgUZXUh+wBqRQze7IFqSShrn70jKrXLWsb/N6A2XprbW90DpNqixmg5Y8+w3uWMpzTaqeWHDQAj5tVWbq3/UMrJlNqKyhd3LejO+SSf83eZt+u/mpc5u/M517tzTq6P918VX3oUF3BV5dl4aYtXxbcedN0CHtK1N17Z5KqIl13RMqm2U7JQvvbEQPNv7JYtqD2uMrnefMMEvZ++84LkLLbjJGZjwsW+mvP2YkrxBv6UTMbzvr/Ta/MHZ9EjsmnFa1b3ZdntB+cxtLGCT1VmYn9/5wMBPdCP2jgg2yfsWA36XVgUPo+nXR3kcW/rJg03qVuZwiiIAAAAAElFTkSuQmCC"""
def printarnome(event=None,name=""):
    print(name)
class Btn(Button):
    def __init__(self,master,var,value,calback,icon="icon6",**kwargs):
        super(Btn,self).__init__(master,**kwargs)
        self.estado = var
        self.value = value
        self.calback = calback
        self.icon = icon
        self.dict_icon = {
            "icon1":(on,off),   #24x24
            "icon2":(on1,off1), #24x24
            "icon3":(on2,off2), #24x24
            "icon4":(on3,off3), #24x24
            "icon5":(on4,off4), #32x32
            "icon6":(on5,off5), #24x24
            }
        self.on = PhotoImage(data=self.dict_icon[self.icon][0])
        self.off = PhotoImage(data=self.dict_icon[self.icon][1])
        self.configure(
            relief=SOLID,
            image=self.off
            )
        self.pack()
        func = lambda *args:self.inicializa(args)
        self.estado.trace_add("write",lambda a,b,c: func(a,b,c,value,var.get()) )
        self.bind("<Button-1>",lambda e: self.valida(value))
        self.bind("<Button-1>",lambda e: calback(e,value),add="+")
        self.inicializa()
    def inicializa(self,*args):
        if self.estado.get() == self.value:
            self.configure(image=self.on)
            self.invoke()
            return
        return self.configure(image=self.off)
    def desativar(self):
        self.configure(image=self.off)
    def ativar(self):
        self.configure(image=self.on)
        self.estado.set(value=self.value)
    def valida(self,value):
        if self.estado.get() != value:
            self.estado.set(value)
class FrmRadioBtn(Frame):
    def __init__(self,master,cor="",**kwargs):
        super(FrmRadioBtn,self).__init__(master,**kwargs)
        self.widthbtn = 0
        self.listabtns = []
        self.cor = cor
        if cor:
            self.configure(bg=cor)
        else:
            self.cor = "SystemButtonFace"
    def add_btn(self,value,var,calbak,text):
        #print(f"ANTES DO PARANDO - {value,var.get(),calbak,text}")
        self.btn = Btn(self,var,value,calbak,compound=LEFT,text=text,bg=self.cor)
        self.btn.pack(side=LEFT,padx=("4px","4px"),pady=("4px","4px"))
        self.listabtns.append(self.btn)
        self.reconfigure()    
    def reconfigure(self):
        for widget in self.winfo_children():
            tamho = len(widget.cget("text"))
            if tamho > self.widthbtn:
                self.widthbtn = tamho + 145
        for widget in self.winfo_children():
            widget.configure(bd=1,relief=SOLID,width=self.widthbtn)
if __name__ == "__main__":
    root = Tk()

    frm = FrmRadioBtn(root)
    frm.pack()

    # def desativar_rbds(self,event):
    #     event.widget.ativar()
    #     for w in self.winfo_children():
    #         if event.widget != w:
    #             w.desativar()

    str_ = StringVar(master=frm,value="")

    frm.add_btn("btn1",str_,printarnome,"Pagamento Extra")
    frm.add_btn("btn2",str_,printarnome,"Pagamento Parcela")
    frm.add_btn("btn3",str_,printarnome,"Pagamento Entrada")
    frm.add_btn("btn4",str_,printarnome,"")
    frm.add_btn("btn5",str_,printarnome,"")
    frm.add_btn("btn6",str_,printarnome,"")

    root.mainloop()
        
