#/usr/bin/python

def yuesefu(m, n):
        i       = 0;
        arr     = range(1, m+1);
        ret     = [];
        while True:
                i=i+1;
                first = arr[0];
                del arr[0];
                if i%n==0:
                        ret.append(first);
                else:
                        arr.append(first);

                if len(arr)==0:
                        arr.append(first);
                        break;

        return ret;

print yuesefu(50,3);