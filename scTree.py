
from optparse import OptionParser
from Readfile import *
from Edmonds import *
import os

def getPath(path):
    path1=path.split("/")
    if path1[0] == ".":
        if (len(path1)==1):
            newpath=os.getcwd()
        else:
            newpath=os.getcwd()
            for ele in path1:
                if ele !=".":
                    newpath=newpath+"/"+ele
    elif path1[0]=="..":
        i = 0
        for ele in path1:
            if ele == "..":
                i=i+1
        path2=os.getcwd()
        path2=path2.split("/")
        newpath="/"+path2[0]
        if len(path2)-i > 1:
            for j in range(1,len(path2)-i):
                newpath=newpath+"/"+path2[j]
        for j in range(i,len(path1)):
            newpath=newpath+"/"+path1[j]
    else:
        newpath=path
    return newpath


def main():
    usage = "usage: python %prog <-P path> <-I input> <-O output>"
    description = "Input integer copy number profile. Columns correspond to chromosomal position. Rows correspond to cell or clonal ID"
    op = OptionParser(version="%prog 1.0",description=description,usage=usage,add_help_option=False)
    op.add_option("-h","--help",action="help",
                  help="Show this help message and exit.")
    op.add_option("-P","--Path",dest="Path",type="str",
                  help="Path to script")
    op.add_option("-I","--Input",dest="Input",type="str",
                  help="Input file")
    op.add_option("-O","--Output",dest="Output",type="str",
                  help="Output path")
    op.add_option("-D","--Datatype",dest="Datatype",type="str",
                  help="Output path")
    op.add_option("-W","--Windows",dest="Windows",type="str",
                  help="the number of genes you want to merge when you input copy number profile inferred from scRNA-seq")

    (options,args) = op.parse_args()
    if not options.Path or not options.Input or not options.Datatype:
        op.print_help()
        sys.exit(1)
    currentPath=os.getcwd()
    scTreepath=options.Path
    scTreepath=getPath(scTreepath)
    filename=options.Input
    filename=getPath(filename)
    if not options.Output:
    	outpath=currentPath
    else:
    	outpath=options.Output
        outpath=getPath(outpath)
    os.system("mkdir -p "+outpath)
    os.chdir(outpath)
    datatype=options.Datatype
    os.system("mkdir temp")
    writename=outpath+"/CNV.tree.txt"
    os.chdir(outpath+"/temp")
    print "Transfer data to segmental level"
    if datatype == "D":
        os.system("Rscript "+scTreepath+"dataTransfer.R "+filename+" "+datatype)
    elif datatype == "R":
        if not options.Windows:
            print "Please the number of genes which are merger into the bin is default value 20. If you want change it please specify the value through -W"
            delt = str(20)
        else:
            delt=options.Windows
        os.system("Rscript "+scTreepath+"dataTransfer.R "+filename+" "+datatype+" "+scTreepath+" "+delt)
    else:
        print "Please provide the correct inputfile type through -D either 'D' or 'R'."
    CNVfile=filename+".CNV.txt"
    print "Inferring RDMST."
    (nodes,root) = read(CNVfile)
    node_name_list = nodes.keys()
    g = create_tree(nodes, node_name_list)
    result = compute_rdmst(g, root)
    write=open(writename,'w')
    tree=result[0]
    out1="from"+"\t"+"to"+"\t"+"dist"
    print >> write, out1
    for ele in tree.keys():
        out=ele
        for value in tree[ele].keys():
            out1=out+"\t"+value+"\t"+str(tree[ele][value])
            print >> write,out1
    write.close()
    print "RDMST inferrence finished."
    print "Identififying lineage specific CNAs."
    os.system("Rscript "+scTreepath+"LSA.tree.R "+scTreepath+" "+filename+" "+writename+" "+CNVfile+" "+outpath+" "+datatype)
    os.chdir(outpath)
    os.system("rm -r temp")
    os.system("rm "+CNVfile)




if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("User interrupt me, see you!\n")
        sys.exit(0)
