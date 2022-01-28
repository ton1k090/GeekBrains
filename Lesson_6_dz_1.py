def parse(file_pars):


     with open(file_pars, "r", encoding="utf-8") as f:
        for line in f:
            ip = line.split(" - - ")[0]
            rsp_and_pth = line.split('"')[1]
            rsp = rsp_and_pth.split()[0]
            pth = rsp_and_pth.split()[1]
            yield (ip, rsp, pth)

a = parse("./nginx_logs.txt")
for e in a:
    print(e)