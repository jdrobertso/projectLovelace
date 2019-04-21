def logistic_map(r):
    x = [0.5]
    y = 0

    while y<=49:
        z = (r * x[y]) * (1-x[y])
        x.append(z)
        y += 1

    return x