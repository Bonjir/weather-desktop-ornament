import utime

LOG_FILE = 'log.txt'

# def init():
#     global flog
#     flog = open(LOG_FILE, "a+")
#     info("Log Start.")

def info(inf):
    flog = open(LOG_FILE, "a+")
    y, m, d, h, mn, s, _, _ = utime.localtime()
    infostr = "{y}-{m}-{d} {h}:{mn}:{s}\tINFO\t: {inf}\n".format(y=y, m=m, d=d, h=h, mn=mn, s=s, inf=inf)
    flog.write(infostr)
    print(infostr.strip())
    flog.close()
    
def error(err):
    flog = open(LOG_FILE, "a+")
    y, m, d, h, mn, s, _, _ = utime.localtime()
    errstr = "{y}-{m}-{d} {h}:{mn}:{s}\tERROR\t: {err}\n".format(y=y, m=m, d=d, h=h, mn=mn, s=s, err=err)
    flog.write(errstr)
    print(errstr.strip())
    flog.close()
    
def critical(err):
    flog = open(LOG_FILE, "a+")
    y, m, d, h, mn, s, _, _ = utime.localtime()
    cristr = "{y}-{m}-{d} {h}:{mn}:{s}\tCRITICAL\t: {err}\n".format(y=y, m=m, d=d, h=h, mn=mn, s=s, err=err)
    flog.write(cristr)
    print(cristr.strip())
    flog.close()
    
