#!/usr/bin/python
# Rewrite by youstar
# Modified from: PHP Vulnerabilities Fuzzer By c4 (http://www.0x50sec.org)
import sys,os
psatlist = ['include||require||require_once||include_once||file_get_contents','exec||system||popen||passthru||proc_open||pcntl_exec||shell_exec','eval||preg_replace||assert||call_user_func||call_user_func_array||create_function','_GET||_POST||_COOKIE||_SERVER||_REQUEST||_ENV||php://input||getenv','session||cookie','extract||parse_str||mb_parse_str||import_request_variables||unserialize','copy||rmdir||chmod||delete||fwrite||fopen||readfile||fpassthru||move_uploaded_file||file_put_contents||unlink||upload||opendir||fgetc||fgets||ftruncate||fputs||fputcs','select||insert||update||delete||order by||group by||limit||in(||stripslashes||urldecode','confirm_phpdoc_compiled||mssql_pconnect||mssql_connect||crack_opendict||snmpget||ibase_connect','echo||print||printf||vprintf||document.write||document.innerHTML||document.innerHtmlText','phpinfo||highlight_file||show_source','iconv||mb_convert_encoding']

def print_version():
    print "\n|---------------------------------------------------------------|"
    print "|      youstar[@]foxmail[dot]com  v1.0                          |"
    print "|      6/2012      psat.py                                      |"
    print "|      --Php Source Audit Tool--                                |"
    print "|      --Environment:Linux--                                    |"
    print "| Usage:    psat.py  filepath                                   |"
    print "| Example:  psat.py  /home/root/discuz                          |"
    print "| or                                                            |"
    print "| Usage:    psat.py  filepath report(y/n)                       |"
    print "| Example:  psat.py  home/root/discuz  y                        |"
    print "|---------------------------------------------------------------|\n"
    
def print_choice():
    global psatlist
    inum = 0
    print "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
    for ipast in psatlist:
        print inum,":",ipast
        inum = inum + 1
    print "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

def Psatscan(path, itype, report='n'):
    global psatlist
    reportpath = path
    keylist = psatlist[itype]
    keylist = keylist.split('||')
    if report.lower() == 'y':
	reportpath = reportpath + '/report'
	if os.path.exists(reportpath) == False:
	    os.mkdir(reportpath)
	reportpath = reportpath + '/report.php' 
	print 'Please see you report file:%s'%(reportpath)
    for ikey in keylist:
	if report.lower() == 'y':
	    cmd = "grep -in '%s' -r '%s' | grep -v psat.py | grep -v .css | grep -v .js | grep -v report.php |grep '%s' --color >>'%s'"%(ikey,path,ikey,reportpath)
	else:
	    cmd = "grep -in '%s' -r '%s' | grep -v psat.py | grep -v .css | grep -v .js | grep -v report.php | grep '%s' --color"%(ikey,path,ikey)
	os.system(cmd)
	
def Choose():
    print_choice()
    print "Choose Number:#"
    id = raw_input()
    id = int(id)
    return id

if __name__=='__main__':
    report = 'n'
    if len(sys.argv) < 2:
        print_version()
        sys.exit()
    if len(sys.argv) == 3:
	report = sys.argv[2]
    codepath = sys.argv[1]
    itype = Choose()
    Psatscan(codepath,itype,report)