#!/usr/bin/python
# vimcdoc-sf.py
# An index.html generator for the vimcdoc project.
# Usage: 
#   'vimcodc-sf.py' to output to stdout
#   'vimcodc-sf.py -ci' to generate the index.html 
# Author: lang2 (lang2@users.sourceforge.net)


import re
vimcdoc_ver = "" 
data_dir_prefix = "../../"
news_file = data_dir_prefix + "NEWS"
author_file = data_dir_prefix + "AUTHORS"
version_file = data_dir_prefix + "VERSION"
index_file = "./index.html"

def GetVimcdocVersion():
    global vimcdoc_ver
    f = open (version_file)
    vimcdoc_ver = vimcdoc_ver + f.readline().rstrip()
    f.close()

def PrintNewsHeader():
    print '<table class="HEADER1" width="100%" border="0" cellspacing="0" cellpadding="1">'
    print '<tbody>'
    print '<tr>'
    print '<td>'
    print '<table width="100%" border="0" cellspacing="0" cellpadding="4">'
    print '<tbody>'
    print '<tr class="ROW1">'
    print '<td class="NEWS"> <em>News</em> </td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '<p class="LEFT">'
    print '<dl class="NEWS">'

def PrintNewsFooter():
    print '</dl>'
    print '<br><br>'

def PrintNews():
    PrintNewsHeader()
    f = open( news_file )
    line = f.readline()
    while ( line ):
        print '<dt class="NEWS">'
        print line
        print '</dt>'
        print '<dd class="NEWS">'
        line = f.readline()
        while ( line != "\n" ):
            print line
            line = f.readline()
        line = f.readline()
        print '<br><br>'

    f.close()
    PrintNewsFooter()

def PrintHeader():
    print '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">'
    print '<html>'
    print '<head>'
    print '<meta content="text/html;charset=iso-8859-1" http-equiv="Content-Type">'
    print '<title>Vim Chinese Documentation</title>'
    print '<style type="text/css">'
    print 'A          {color:black; text-decoration:underline}'
    print 'H2         {color:black; align:center}'
    print 'BODY       {background-color:white}'
    print 'P          {font-family: Verdana, Helvetica, sans-serif; color:black; text-align:center; font-weight:normal; font-size:0.9em}'
    print 'P.LEFT     {font-family: Verdana, Helvetica, sans-serif; color:black; text-align:left;   font-weight:normal; font-size:0.9em}'
    print 'P.SMALL    {font-family: Verdana, Helvetica, sans-serif; color:#38506c; text-align:center; font-weight:normal; font-size:0.5em}'
    print 'UL.LEFT    {font-family: Verdana, Helvetica, sans-serif; color:#758cab; text-align:left;   font-weight:normal; font-size:0.9em}'
    print 'TD.NEWS    {font-family: Verdana, Helvetica, sans-serif; color:black; text-align:left;   font-weight:bold; font-size:1.1em}'
    print 'TD.LEFT    {font-family: Verdana, Helvetica, sans-serif; color:black; text-align:left;   font-weight:normal; font-size:0.9em}'
    print 'TD.HEADER  {font-family: Verdana, Helvetica, sans-serif; color:black; text-align:center; font-weight:bold; font-size:0.9em} '
    print 'DD.NEWS    {font-family: Verdana, Helvetica, sans-serif; color:black; text-align:left; font-weight:normal; font-size:0.9em} '
    print 'DT.NEWS    {font-family: Verdana, Helvetica, sans-serif; color:#758cab; text-align:left; font-weight:normal; font-size:0.9em} '
    print 'TR.ROW1    {background-color:#E6E6fE}'
    print 'TR.HEADER1,TABLE.HEADER1 {background-color:#657a97}'
    print '</style>'
    print '</head>'
    print '<body>'

def PrintSidebar():
    print '<table width="100%" border="0" cellspacing="0" cellpadding="1" align="center">'
    print '<tbody>'
    print '<tr>'
    print '<td valign="top" align="left" width="15%">'
    print '<table class="HEADER1" border="0" cellpadding="1" cellspacing="0">'
    print '<tbody>'
    print '<tr>'
    print '<td>'
    print '<table class="HEADER1" cellpadding="4" cellspacing="0" border="0">'
    print '<tbody>'
    print '<tr class="ROW1">'
    print '<td class="left">&nbsp;</td>'
    print '</tr>'
    print '<tr class="ROW1">'
    print '<td class="HEADER">'
    print '<h2>Vimcdoc</h2>'
    print '<hr noshade="noshade" size="1">'
    print '<!-- NavBar -->'
    print '<p><a href="http://sourceforge.net/projects/vimcdoc/" onmouseover="status=\'SourceForge Page\'; return true" onmouseout="status=''; return true">Project Page</a></p>'
    print '<p><a href="images" onmouseover="status=\'Vimcdoc Screenshot\'; return true" onmouseout="status=\'\'; return true">Screenshot</a></p>'
    print '<p><a href="http://sourceforge.net/project/showfiles.php?group_id=56777" onmouseover="status=\'Download\'; return true" onmouseout="status=''; return true">Download</a></p>'
    print '<p><a href="http://vimcdoc.sf.net/doc/help.html" onmouseover="status=\'Read online\'; return true" onmouseout="status=''; return true">Read Online</a></p>'
    print '<p><a href="http://vimcdoc.sf.net/ChangeLog" onmouseover="status=\'Changelog\'; return true" onmouseout="status=''; return true">Changelog</a></p>'
    print '<p><a href="http://sourceforge.net/svn/?group_id=56777" onmouseover="status=\'Subversion\'; return true" onmouseout="status=''; return true">Subversion</a></p>'
    print '<p> <a href="http://sourceforge.net/export/rss2_projnews.php?group_id=56777" \
            onmouseover="status=\'Project News RSS Feed\'; return true" onmouseout="status=''; \
            return true">News RSS</a></p>'
    #print '<p> <a href="http://sourceforge.net/export/rss2_projnews.php?group_id=56777&rss_fulltext=1" \
            #onmouseover="status=\'Project File Release RSS Feed\'; return true" onmouseout="status=''; \
            #return true">File RSS</a></p>'
    print '<hr noshade="noshade" size="1">'
    print '<p><a href="http://vcd.gro.clinux.org"'
    print 'onmouseover="status=\'vcd\'; return true"'
    print 'onmouseout="status=\'\'; return true">gro mirror</a></p>'
    print '<p><a href="http://www.vim.org"'
    print 'onmouseover="status=\'Vim\'; return true"'
    print 'onmouseout="status=\'\'; return true">Vim home</a></p>'
    print '<p><a href="http://vimdoc.sf.net"'
    print 'onmouseover="status=\'VimDoc\'; return true"'
    print 'onmouseout="status=\'\'; return true">VimDoc</a></p>'
    print '<hr noshade="noshade" size="1">'
    print '<p><a href="mailto:lang2@users.sourceforge.net" onmouseover="status=\'Contact\'; return true" onmouseout="status=''; return true">Contact</a></p>'
    print '<!-- NavBar --> '
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '</td>'
    print '<td align="center" valign="top">'
    print '<table border="0">'
    print '<tbody>'
    print '<tr>'
    print '<td class="LEFT" width="80%">'

def BeginMainBody():
    print '<!-- Body -->'
    print '<!-- ===================================================================== -->'

def PrintWhatIs():
    print '<table class="HEADER1" width="100%" border="0" cellspacing="0" cellpadding="1">'
    print '<tbody>'
    print '<tr>'
    print '<td>'
    print '<table width="100%" border="0" cellspacing="0" cellpadding="4">'
    print '<tbody>'
    print '<tr class="ROW1">'
    print '<td class="NEWS"> <em>What is</em> </td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '<p class="LEFT">'
    print 'Vimcdoc is an attempt to translate the wonderful Vim online'
    print 'documentation into Chinese, allowing more people to get to'
    print 'know and make use of this great tool. After installing vimcdoc,'
    print 'You will be able to do <code>:help</code> and read'
    print 'documentation in Chinese.'
    print '<br><br>'
    print '</p>'

def PrintDivider():
    print '<!-- ===================================================================== -->'

def PrintGetVimcdoc():
    print '<table class="HEADER1" width="100%" border="0" cellspacing="0" cellpadding="1">'
    print '<tbody>'
    print '<tr>'
    print '<td>'
    print '<table width="100%" border="0" cellspacing="0" cellpadding="4">'
    print '<tbody>'
    print '<tr class="ROW1">'
    print '<td class="NEWS"> <em>Get Vimcdoc</em> </td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '<p class="LEFT">'
    print 'The latest version is <font color="red">' + vimcdoc_ver + '!</font><br>'
    print 'Vimcdoc is hosted by sourceforge. So you should be able to'
    print 'get it from any sourceforge mirror. See the links below:'
    print '<br><br>'
    print '</p>'
    print '<ul class="LEFT">'
    exe_address = 'http://prdownloads.sourceforge.net/vimcdoc/vimcdoc-' + vimcdoc_ver
    exe_address = exe_address + '-setup.exe?download'
    tarball_address = 'http://prdownloads.sourceforge.net/vimcdoc/vimcdoc-' + vimcdoc_ver
    tarball_address = tarball_address + '.tar.gz?download'

    print '<li> Latest <a href=' + exe_address + '>win32 installation program</a>'
    print '</li>'
    print '<li> Latest platform independant <a href=' + tarball_address + '> tarball</a>, including an Linux/BSD installation script'
    print '</li>'
    print '<li> If you are a BSD user, you might want to check out this\
            <a href="http://www.freshports.org/chinese/vim-scdoc">port</a>.\
            Thanks for hamigua. '
    print '<li> There is package for Debian systems too available at\
            <a href="http://chinese.alioth.debian.org/vimcdoc">here</a>.\
            Thanks for Carlos Liu. '
    print '<li> Latest <a href=vim_user_manual_603.0.pdf>PDF</a> version of the translated Vim user manual. '
    print 'Thanks slimzhao for permission to host this file.'
    print '</li>'
    print '<li> For more please use the \'Download\' link on the left.</li>'
    print '</ul>'
    print '<p class="LEFT">'
    print '<a href="http://gro.clinux.org">gro</a> has a '
    print '<a href="http://vcd.gro.clinux.org">mirror</a>, where you can get the latest for'
    print 'Linux and windows platform.'
    print '<br><br>'
    print '</p>'

def PrintAuthors():
    print '<table class="HEADER1" width="100%" border="0" cellspacing="0" cellpadding="1">'
    print '<tbody>'
    print '<tr>'
    print '<td>'
    print '<table width="100%" border="0" cellspacing="0" cellpadding="4">'
    print '<tbody>'
    print '<tr class="ROW1">'
    print '<td class="NEWS"> <em>Authors</em> </td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '<p class="LEFT">'
    print 'Vimcdoc was started by Ken in 2002.6. lang2 started a similiar'
    print 'project from <a href="http://www.linuxforum.net">linuxforum</a> soon after. At the end of 2002 they merged and the'
    print 'current vimcdoc took form. We have 19 '
    print '<a href="http://sourceforge.net/project/memberlist.php?group_id=56777">members</a>, among'
    print 'whom the following has contributed a lot to this project:'
    print '<ul class="LEFT">'
    f = open( author_file )
    auth = re.compile( "^(\w+)\s+\(\s*(\w.*)\s*\)" ) 

    line = f.readline()
    while ( line ):
        mobj = auth.match(line)
	if mobj is not None:
		print '<li>' + mobj.group(1) + ' - ' + mobj.group(2)
        line = f.readline()
    f.close()

    print '</ul>'
    print '<br><br>'
    print '</p>'

def EndMainBody():
    print '<p class="SMALL">'
    print 'Vimcdoc is &copy; 2005 by the vimcdoc team.'
    print 'All rights reserved.'
    print '<br><br>'
    print '<a href="http://sourceforge.net">'
    print '<img src="http://sourceforge.net/sflogo.php?group_id=56777&amp;type=3" width="125" height="37" border="0" alt="SourceForge.net Logo" /></a>'
    print '</p>'
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'
    print '</td>'
    print '</tr>'
    print '</tbody>'
    print '</table>'

def PrintFooter():
    print '</body></html>'

#####
# Main program
#####
import sys
import os
from sys import argv

if len(argv) == 2:
    if argv[1] == '-ci':
        os.remove ( index_file )
        save_out = sys.stdout
        sys.stdout = open( index_file, 'w' )

GetVimcdocVersion()
PrintHeader()
BeginMainBody()
PrintSidebar()
PrintWhatIs()
PrintGetVimcdoc()
PrintNews()
PrintAuthors()
EndMainBody()
PrintFooter()

if len(argv) == 2:
    if argv[1] == '-ci':
        sys.stdout.close()
        sys.stdout = save_out
