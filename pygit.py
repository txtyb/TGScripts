import os,sys
cmd=' '.join(sys.argv[1:])
while os.system('env GIT_SSL_NO_VERIFY=true git %s'%cmd):
     pass
