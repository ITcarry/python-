
g_var = 1

def test():
    global g_var
    l_var = 12
    g_var = 5
    
if __name__ == '__main__':
    test()
    print g_var