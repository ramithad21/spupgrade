import os,csv

def test_fcn() :
    try:
        tabReader = csv.reader( open("popu.csv", "rb"), delimiter=',', quoting=csv.QUOTE_NONE )
        fd = open("out.csv", "wb+")
        tabWriter = csv.writer(fd, delimiter=',', quoting=csv.QUOTE_NONE)
        if tabReader != None :
            for record in tabReader:
                record.append("new_thing")
                tabWriter.writerow(record)
        fd.close()
        return

    except Exception,e :
        print "Exception : " + str(e)
        
def main():
    test_fcn()

if __name__ == '__main__':
    import sys
    main(*sys.argv[1:])
