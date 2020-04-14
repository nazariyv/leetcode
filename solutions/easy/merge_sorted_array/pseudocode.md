```python
while lix < m and rix < n:

    if stack.top() is not None:
        top = stack.pop()
        if top < n1[lix]:
            stack.push(n1[lix])
            n1[lix] = top
            lix += 1
            continue

        if top < n2[rix]:
            stack.push(n1[lix])
            n1[lix] = top
            lix += 1
        else:
            stack.push(n1[lix])
            n1[lix] = n2[rix]
            lix += 1
            rix += 1

    # stack top is None
    else:
        if n1[lix] <= n2[rix]: lix += 1
        # n2[rix] > n1[lix]
        else:
            stack.push(n1[lix])
            n1[lix] = n2[rix]
            lix += 1
            rix += 1

if stack.top() and n2[rix:]:
    top = stack.pop()
    if top < n2[rix]:
        n1[lix] = top
        lix += 1
    else:
        n1[lix] = n2[rix]
        lix += 1
        rix += 1

if n2[rix:]:
    n1[lix] = n2[rix]
    lix += 1
    rix += 1

if stack.top():
    n1[lix] = stack.pop()
    lix += 1
```