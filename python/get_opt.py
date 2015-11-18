import sys;
import getopt;

def usage():
    print("Usage:%s " \
           "\t-t|--type \t define the type of file parameter is relative path of file or the absolute path of file, 0 means use default path /tmp/cm_zb_sb, 1 means absolute path"\
           "\t-f|--file \t file name of absolute or relative path, determined by --type;"\
           "\t-k|--key  \t the key to get the value;"\
           "\t-h|--help \t help information;" %Dsys.argv[0]);

if __name__ == "__main__":
    # use default path
    file_type = 0;
    file_path = "/tmp/cm_zb_sb";
    file_name = "";
    key = "";
    seperator = "\t";
    metric = dict();
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t:f:k:s:h", ["type=", "file=", "key=", "help",])
        for opt,arg in opts:
            if opt in ("-t", "--type"):
                file_type = int(arg);
            elif opt in ("-f", "--file"):
                file_name = arg;
            elif opt in ("-k", "--key"):
                key = arg;
            elif opt in ("-s", "--seperator"):
                seperator = arg;
            else:
                usage();
    except getopt.GetoptError:
        # print help information and exit:
        print("getopt error!");
        usage();
        sys.exit(1);
    if file_type == 0:
        file_name = "%s/%s"%(file_path,file_name);
    #print ("type: %d, path: %s, key: %s"%(file_type, file_name, key));
    metric_file = open(file_name, 'r');
    for line in metric_file:
        pieces = line.split(seperator);
        print pieces
        metric[pieces[0]] = pieces[1];
    print metric[key];

