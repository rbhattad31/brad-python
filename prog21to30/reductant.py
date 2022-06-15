def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

a="calvin klein design dress calvin klein"
a=' '.join(unique_list(a.split()))