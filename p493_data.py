#! encoding=utf-8

# Creation Date: 2017-04-05 15:09:50
# Created By: Heyi Tang

if __name__ == "__main__":
    maxn = 10;
    dup = 10;
    with open("in2.txt", "w") as fout:
        for i in range(maxn):
            for j in range(dup):
                num = maxn -1 -i;
                fout.write("%d\n" % num)
