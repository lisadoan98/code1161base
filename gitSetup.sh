# edit these lines
MYNAME="Catherine Vu"
MYEMAIL="catherine.vu.97@hotmail.com"
# stop editing


# don't edit these lines
git config --global user.name $MYNAME
git config --global user.email $MYEMAIL
git config --global credential.helper 'cache --timeout=36000' #cache password for 150 minutes
git config --global color.ui auto #colour the output in git
git config --global core.editor "atom --wait"
